annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
r = input("Enter the expected annual rate of return [0.04]: ") or 0.04
total_cost = float(input("Enter the cost of your dream home: "))
portion_down_payment = input("Enter the percent of your home's cost to save as a down payment [0.25]: ") or 0.25
monthly_salary = annual_salary / 12
monthly_savings = monthly_salary * portion_saved
current_savings = 0.0
months = 0
monthly_r = float(r) / 12

while current_savings < (total_cost * float(portion_down_payment)):
    current_savings = current_savings + (current_savings * monthly_r) + monthly_savings
    months = months + 1

print("Number of months: " + str(months))