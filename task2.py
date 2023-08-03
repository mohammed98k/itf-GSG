name = input("Please enter your Full Name: ")
mobile_number = input("Please enter your mobile_number (05x-xxxx-xxx): ")
dob = int(input("Please enter your date of birth: "))

current_year = 2023
current_age=current_year-dob
mobile_number = mobile_number.split()

print("Name:", name)
print("current_age:", current_age)
print("mobile_number:", mobile_number)
