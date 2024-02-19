
# Input annual_salary, portion_saved, and total_cost
annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter semi-annual raise as a decimal: "))


portion_down_payment = 0.25 * total_cost
current_savings = 0
monthly_salary = annual_salary/12
number_of_months = 0

# How many months to save up enough money for a down payment
while current_savings < portion_down_payment:
    current_savings += (monthly_salary * portion_saved) + (current_savings * (0.04/12))
    number_of_months+=1
    if number_of_months % 6 == 0:
        annual_salary += annual_salary * semi_annual_raise
        monthly_salary = annual_salary / 12


print("Number of months:", number_of_months)
years = number_of_months // 12
print("Number of years:", years)