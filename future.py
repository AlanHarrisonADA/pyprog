age = int(input("what's your age? ")) 
# number_of_years = int(input("how many years... ?")) 
# future_age = age + number_of_years
birthday = input("have you had your birthday this year (y/n)?")
if  birthday == "y":
    birth_year = 2025 - age 
else:
    birth_year = 2025 - age -1
# print(f"in {number_of_years} years you will be {future_age} years old")
print(f"you were born in {birth_year}")
