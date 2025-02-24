months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
month_num = int(input("Enter the month (1-12): "))
if 1 <= month_num <= 12:
    print(f"Month {month_num} is {months[month_num - 1]}")
else:
    print("Invalid month. Please enter a number between 1 and 12.")