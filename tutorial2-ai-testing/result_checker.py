# Course result checker
# Rules:
# 1. Coursework and exam marks must be whole numbers from 0 to 100.
# 2. If either mark is outside that range, print Invalid.
# 3. Calculate total = 0.6 * coursework + 0.4 * exam.
# 4. Pass only if total >= 50 and exam >= 45.
# 5. Otherwise print Fail.


# Get the two marks from the input stream.
# This works both for typed input and for automated test input.
coursework = int(input())
exam = int(input())

# Check marks are valid
if coursework < 0 or coursework > 100 or exam < 0 or exam > 100:
    print("Invalid")
else:
    total = 0.6 * coursework + 0.4 * exam

    # Decide pass or fail.
    # The exam minimum is 45, so 44 must fail even if the weighted total is high.
    if total >= 50 and exam >= 45:
        print("Pass")
    else:
        print("Fail")
