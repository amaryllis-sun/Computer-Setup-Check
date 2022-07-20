hours = input("Enter a number of hours:")

def compute_minutes(Hours):
    m = int(Hours) * 60
    return m

#Minutes = compute_minutes(Hours)

print(hours, "hours is", compute_minutes(hours), "minutes!")