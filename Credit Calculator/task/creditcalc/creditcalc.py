from math import ceil, log, floor
from sys import argv

# print("""What do you want to calculate?
# type "n" - for count of months,
# type "a" - for annuity monthly payment,
# type "d" - for differentiated payment,
# type "p" - for credit principal: """)

principal = 0
payment = 0
periods = 0
interest = 0
answer = "Error"

if len(argv) < 5:
    print("Incorrect parameters.")

elif "--type=diff" in argv:
    answer = 'd'
    for element in argv:
        if "--principal=" in element:
            principal = int(element[12:])
        elif "--periods=" in element:
            periods = int(element[10:])
        elif "--interest=" in element:
            interest = float(element[11:])
        elif element in ["--type=diff", "creditcalc/creditcalc.py"]:
            pass
        else:
            print("Incorrect parameters.")
            answer = "Error"

elif "--type=annuity" in argv:
    if "--principal=" not in [x[:12] for x in argv]:
        answer = 'p'
        for element in argv:
            if "--payment=" in element:
                payment = int(element[10:])
            elif "--periods=" in element:
                periods = int(element[10:])
            elif "--interest=" in element:
                interest = float(element[11:])
            elif element in ["--type=annuity", "--principal=", "creditcalc/creditcalc.py"]:
                pass
            else:
                print("Incorrect parameters.")
                answer = "Error"
    elif "--periods=" not in [x[:10] for x in argv]:
        answer = 'n'
        for element in argv:
            if "--principal=" in element:
                principal = int(element[12:])
            elif "--payment=" in element:
                payment = int(element[10:])
            elif "--interest=" in element:
                interest = float(element[11:])
            elif element in ["--type=annuity", "--periods=", "creditcalc/creditcalc.py"]:
                pass
            else:
                print("Incorrect parameters.")
                answer = "Error"
    elif "--payment=" not in [x[:10] for x in argv]:
        answer = 'a'
        for element in argv:
            if "--principal=" in element:
                principal = int(element[12:])
            elif "--periods=" in element:
                periods = int(element[10:])
            elif "--interest=" in element:
                interest = float(element[11:])
            elif element in ["--type=annuity", "--payment=", "creditcalc/creditcalc.py"]:
                pass
            else:
                print("Incorrect parameters.")
                answer = "Error"
    else:
        print("Incorrect parameters.")
else:
    print("Incorrect parameters.")

if answer == 'n':
    # print("Enter credit principal: ")
    # principal = int(input())
    # print("Enter monthly payment: ")
    # payment = float(input())
    # print("Enter credit interest: ")
    # interest = float(input())

    i = interest/(12 * 100)
    n = ceil(log(payment / (payment - i * principal), 1 + i))
    years = n // 12
    month = n % 12
    if month == 0:
        print(f"You need {ceil(years)} years to repay this credit!")
    elif years == 0:
        print(f"You need {ceil(month)} month to repay this credit!")
    else:
        print(f"You need {ceil(years)} years and {ceil(month)} months to repay this credit!")
    print(f"Overpayment = {ceil(payment * n - principal)}")

elif answer == "a":
    # print("Enter credit principal: ")
    # principal = int(input())
    # print("Enter count of periods: ")
    # periods = int(input())
    # print("Enter credit interest: ")
    # interest = float(input())

    i = interest/(12 * 100)
    a = ceil((principal * i * (1 + i)**periods) / ((1 + i)**periods - 1))
    print(f"Your annuity payment = {a}!")
    print(f"Overpayment = {ceil(a * periods - principal)}")

elif answer == "p":
    # print("Enter monthly payment: ")
    # payment = float(input())
    # print("Enter count of periods: ")
    # periods = int(input())
    # print("Enter credit interest: ")
    # interest = float(input())

    i = interest/(12 * 100)

    p = floor((payment * ((1 + i)**periods - 1)) / (i * (1 + i)**periods))
    print(f"Your credit principal = {p}!")
    print(f"Overpayment = {ceil(payment * periods - p)}")

elif answer == "d":
    print(argv)
    # print("Enter credit principal: ")
    # principal = int(input())
    # print("Enter count of periods: ")
    # periods = int(input())
    # print("Enter credit interest: ")
    # interest = float(input())

    i = interest / (12 * 100)
    pay_sum = 0
    for month_count in range(periods):
        month_pay = ceil(principal/periods + i * (principal - (principal * month_count) / periods))
        pay_sum += month_pay
        print(f"Month {month_count + 1}: paid out {month_pay}")
    print(f"\nOverpayment = {pay_sum - principal}")
