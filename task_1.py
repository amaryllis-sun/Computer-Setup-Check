hours = input("Enter a number of hours:")

def compute_minutes(Hours):
    m = int(Hours) * 60
    return m

print(hours, "hours is", compute_minutes(hours), "minutes!")
