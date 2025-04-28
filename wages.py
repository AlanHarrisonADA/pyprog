from colored import Fore, Back, Style

hours = float(input("hours worked? "))
target = input("target met (y/n)? ")

double_time, overtime_hours = 0,0
if hours > 60:
    double_time = hours - 60
elif hours > 40:
    overtime_hours = hours - 40 - double_time 
else:
    overtime_hours = 0

base_hours = hours - overtime_hours
wages = base_hours * 12 + overtime_hours * 12 * 1.5
if target == "y":
    wages += 50

wages = max(wages, 20) 
wages = min(wages, 100) 

print(f'{Fore.white}{Back.green}wages = {wages}{Style.reset}')