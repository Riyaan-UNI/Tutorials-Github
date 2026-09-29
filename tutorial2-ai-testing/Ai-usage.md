# Ai-usage

## 1) Which requirement did AI help you clarify?

AI helped clarify the invalid-input rule:
- If either mark is outside the allowed range, print Invalid.

This was the missing decision that was not fully specified at the start of the task. The original requirements had the valid range and the formula, but the behaviour for invalid marks was still unresolved.

## 2) Why can 100 / 39 expose a bug that 80 / 80 misses?

Because the bug is about the exam minimum boundary, not the weighted total alone.

For the example:
- 100 / 39 gives a weighted total of:
  0.6 * 100 + 0.4 * 39 = 60 + 15.6 = 75.6
- This is above the weighted pass threshold of 50.

So if the code incorrectly checks only the weighted total and ignores the exam minimum, it will wrongly print Pass.

By contrast, 80 / 80 gives:
- 0.6 * 80 + 0.4 * 80 = 80
- It is above 50 and the exam is also above the minimum.

So even a buggy rule can still produce the correct result for that case, which is why 100 / 39 is a better bug-revealing test than 80 / 80.

## 3) Which actual output shows that your repair worked?

The repaired rule was:
- pass only if total >= 50 and exam >= 45

The relevant proof cases were:
- 100, 44 -> Fail
- 100, 45 -> Pass
- 100, 40 -> Fail

Actual output after the repair:

```text
Fail
Pass
Fail
```

This shows the exam boundary is working correctly:
- 44 is below the minimum and fails
- 45 meets the minimum and passes
- 40 is below the minimum and fails

## 4) Can you explain the final code without asking AI?

Yes. The final code is simple beginner-level Python.

```python
# Course result checker
# Rules:
# 1. Coursework and exam marks must be whole numbers from 0 to 100.
# 2. If either mark is outside that range, print Invalid.
# 3. Calculate total = 0.6 * coursework + 0.4 * exam.
# 4. Pass only if total >= 50 and exam >= 45.
# 5. Otherwise print Fail.

coursework = int(input())
exam = int(input())

if coursework < 0 or coursework > 100 or exam < 0 or exam > 100:
    print("Invalid")
else:
    total = 0.6 * coursework + 0.4 * exam

    if total >= 50 and exam >= 45:
        print("Pass")
    else:
        print("Fail")
```

What it does:
1. Reads two numbers from input.
2. Checks whether either number is outside 0 to 100.
3. If invalid, prints Invalid.
4. Otherwise calculates the weighted total.
5. Prints Pass only if both conditions are true:
   - weighted total is at least 50
   - exam mark is at least 45
6. Otherwise prints Fail.

## Chat history summary

We started by clarifying unclear requirements, then fixed the exam minimum boundary, then updated the CSV and verified the results. The main learning point was that boundary cases are more valuable than ordinary examples because they detect logic bugs that simpler cases may hide.

---

## Original conversation themes

- Clarify missing requirements
- Decide invalid-input behaviour
- Confirm the pass formula
- Identify the exam minimum boundary bug
- Add boundary test cases
- Update the CSV with verified actual outputs and verdicts
- Keep expected results consistent with the rule
