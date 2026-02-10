# AI Code Review Assignment (Python)

## Candidate
- Name: Ahmet Enes Salman
- Approximate time spent: 2.5 hour

---

# Task 1 — Average Order Value

## 1) Code Review Findings
### Critical bugs
- Zero division

### Edge cases & risks
- Key Error, Type Error

### Code quality / design issues
- It does not exclude "cancelled" orders from the calculation of count(denominator)

## 2) Proposed Fixes / Improvements
### Summary of changes
- Check count before dividing by zero
- Add try-except block for dictionary key error or type errors such as total += "195" -> int + string

### Corrected code
See `correct_task1.py`

> Note: The original AI-generated code is preserved in `task1.py`.

 ### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?
To test edge cases, I would test empty dictionary,all "cancelled" orders,wrong key names, NONE as dictionary value.

## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function calculates average order value by summing the amounts of all non-cancelled orders and dividing by the number of orders. It correctly excludes cancelled orders from the calculation.

### Issues in original explanation
- This function excludes cancelled orders when summing the amounts. However, it uses number of both cancelled and not cancelled orders when dividing.

### Rewritten explanation
- This function calculates average order value by summing the amounts of all non-cancelled orders and dividing by the number of not cancelled orders. If an order is excluded from the sum (because it was cancelled), it must also be excluded from the count.

## 4) Final Judgment
- Decision: Approve / Request Changes / Reject -> Request Changes
- Justification: Since division by zero is a critical bug and likely to happen change is required.
- Confidence & unknowns: Type of values in dictionary is unknown

---

# Task 2 — Count Valid Emails

## 1) Code Review Findings
### Critical bugs
- 

### Edge cases & risks
- 

### Code quality / design issues
- Poor for checking valid emails

## 2) Proposed Fixes / Improvements
### Summary of changes
- Write a more complex valid email checker function and call it in "count_valid_emails" function

### Corrected code
See `correct_task2.py`

> Note: The original AI-generated code is preserved in `task2.py`. 


### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?
I would check non-Engilsh characters, use invalid email examples that specifically designed for it from internet.
## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function counts the number of valid email addresses in the input list. It safely ignores invalid entries and handles empty input correctly.

### Issues in original explanation
- No issue in explanation

### Rewritten explanation
- 

## 4) Final Judgment
- Decision: Approve / Request Changes / Reject : Request Changes
- Justification: It needs to be improved in validating emails
- Confidence & unknowns:

---

# Task 3 — Aggregate Valid Measurements

## 1) Code Review Findings
### Critical bugs
- Zero divison, Value Error

### Edge cases & risks
- Different data types may not be converted like total += float("Jack") -> Value Error

### Code quality / design issues
- The function does not exclude invalid values when calculating number of values as denominator

## 2) Proposed Fixes / Improvements
### Summary of changes
- Accept just float and int values and count just these valid ones.

### Corrected code
See `correct_task3.py`

> Note: The original AI-generated code is preserved in `task3.py`.

### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?
I would use different types of data that may crash or mislead the program such as list,string,bool

## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function calculates the average of valid measurements by ignoring missing values (None) and averaging the remaining values. It safely handles mixed input types and ensures an accurate average

### Issues in original explanation
- It does not hande mixed input types correctly

### Rewritten explanation
- This function calculates the average of valid measurements by ignoring missing values (None) and invalid data types(other than int and float) and averaging the remaining values. It safely handles mixed input types and ensures an accurate average

## 4) Final Judgment
- Decision: Approve / Request Changes / Reject -> Request Changes
- Justification: Original function does not handle mixed types,risk of zero division. It does not calculate avarage correctly.
- Confidence & unknowns: I am not sure whether the function should accept strings that can be converted to numeric types. Example : total += float("1.58"), I chose to discard them.
