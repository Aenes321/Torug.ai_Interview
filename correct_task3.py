# Write your corrected implementation for Task 3 here.
# Do not modify `task3.py`.
def average_valid_measurements(values):
    total = 0.0
    count = 0

    for v in values:
        if not isinstance(v,bool) and isinstance(v,(int,float)):
            total += float(v)
            count += 1

    if(count != 0):
        return total / count
    return 0
