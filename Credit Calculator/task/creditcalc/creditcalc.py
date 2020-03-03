import math

print("""What do you want to calculate?
type "n" - for count of months,
type "a" - for annuity monthly payment,
type "p" - for credit principal: """)

answer = input()
if answer == 'n':
    print("Enter credit principal: ")
    principal = int(input())
    print("Enter monthly payment: ")
    payment = float(input())
    print("Enter credit interest: ")
    interest = float(input())

    i = interest/(12 * 100)
    n = math.ceil(math.log(payment / (payment - i * principal), 1 + i))
    years = n // 12
    month = n % 12
    if month == 0:
        print(f"You need {math.ceil(years)} years to repay this credit!")
    elif years == 0:
        print(f"You need {math.ceil(month)} month to repay this credit!")
    else:
        print(f"You need {math.ceil(years)} years and {math.ceil(month)} months to repay this credit!")
    print(f"Overpayment = {math.ceil(payment * n - principal)}")

elif answer == "a":
    print("Enter credit principal: ")
    principal = int(input())
    print("Enter count of periods: ")
    periods = int(input())
    print("Enter credit interest: ")
    interest = float(input())

    i = interest/(12 * 100)
    a = math.ceil((principal * i * (1 + i)**periods) / ((1 + i)**periods - 1))
    print(f"Your annuity payment = {a}!")
    print(f"Overpayment = {math.ceil(a * periods - principal)}")

elif answer == "p":
    print("Enter monthly payment: ")
    payment = float(input())
    print("Enter count of periods: ")
    periods = int(input())
    print("Enter credit interest: ")
    interest = float(input())

    i = interest/(12 * 100)

    p = math.floor((payment * ((1 + i)**periods - 1)) / (i * (1 + i)**periods))
    print(f"Your credit principal = {p}!")
    print(f"Overpayment = {math.ceil(payment * periods - p)}")

elif answer == "d":
    print("Enter credit principal: ")
    principal = int(input())
    print("Enter count of periods: ")
    periods = int(input())
    print("Enter credit interest: ")
    interest = float(input())

    i = interest / (12 * 100)
    pay_sum = 0
    for month_count in range(periods):
        month_pay = math.ceil(principal/periods + i * (principal - (principal * month_count) / periods))
        pay_sum += month_pay
        print(f"Month {month_count + 1}: paid out " + str(month_pay))
    print(f"\nOverpayment = {pay_sum - principal}")
