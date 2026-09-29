# Course result checker

## Goal
Decide a course result from coursework and exam marks.

## Questions to resolve with AI and the tutor
- What inputs and ranges are allowed?
input 1 = corusework (int, [0, 100]); input 2 = exammarks (int, [0, 100])
- What weights and pass rules apply?
Compute: 0.6 * coursework + 0.4 * exam = total; if total >= 50 and exam >= 45
- What happens if either mark is invalid?
If either mark is outside the allowed range, print Invalid.
- What exact output is required?

## Reviewed requirements
- input 1 = coursework (int, [0, 100]); input 2 = exammarks (int, [0, 100])
- Compute: 0.6 * coursework + 0.4 * exam = total; if total >= 50 and exam >= 45
- If either mark is outside the allowed range, print Invalid.

## Review checkpoint
- [ ] We checked all rules against the tutor's rule card.
- [ ] We can explain the result for coursework 100 and exam 44.
- [ ] We reviewed our expected test results before implementation.

These are fictional classroom rules, not COMP1117 grading rules.
