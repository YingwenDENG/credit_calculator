import math
import argparse


parser = argparse.ArgumentParser(description="calculator")
parser.add_argument("--type", type=str, help='the type of calculation', choices=["annuity", "diff"])
parser.add_argument("--principal", type=float, help="principal credit")
parser.add_argument("--periods", type=int, help="number of periods")
parser.add_argument("--payment", type=float, help="monthly payment")
parser.add_argument("--interest", type=float, help="nominal interest rate")
args = parser.parse_args()


def error_msg():
    print("Incorrect parameters")
    exit(1)


if len(vars(args)) < 5 or args.interest is None:
    error_msg()

par = args.type
# P stands for principal; n stands for periods(number of periods); i stands for nominal interest rate
P = args.principal
n = args.periods
i = args.interest / 100 / 12
m_p = args.payment
# if len(args) != 5:
#     print("Incorrect parameters ")
types = ["annuity", "diff"]
if par not in types:
    error_msg()

# calculation
# m stands for current period(first month, m = 0 ); D stands for differentiated payment
total_payment = 0
if par == "diff":
    if P > 0 and n > 0 and i > 0:
        for m in range(n):
            D = math.ceil(P / n + i * (P - P * m / n))
            print(f"Month {m + 1}: paid out {D}")
            total_payment += D
        over_p = int(total_payment - P)
        print("")
        print(f"Overpayment = {over_p}")
    else:
        error_msg()

if par == "annuity":
    if m_p is None:
        if P > 0 and n > 0 and i > 0:
            A = math.ceil(P * i * pow((1 + i), n) / (pow((1 + i), n) - 1))
            over_p = int(A * n - P)
            print(f"Your annuity payment = {A}!")
            print(f"Overpayment = {over_p}")
        else:
            error_msg()
    elif P is None:
        if m_p > 0 and n > 0 and i > 0:
            P = math.floor(m_p * (pow(1 + i, n) - 1) / (i * pow(1 + i, n)))
            over_p = int(m_p * n - P)
            print(f"Your credit principal = {P}!")
            print(f"Overpayment = {over_p}")
    elif n is None:
        if m_p > 0 and P > 0 and i > 0:
            n = math.ceil(math.log(m_p / (m_p - i * P), 1 + i))
            over_p = int(m_p * n - P)
            number_year = math.floor(n / 12)
            number_month = n - number_year * 12
            if number_month == 0:
                print(f"You need {number_year} years to repay this credit!")
            elif number_year == 0:
                print(f"You need {number_month} months to repay this credit!")
            else:
                print(f"You need {number_year} years and {number_month} months to repay this credit!")
            print(f"Overpayment = {over_p}")
    else:
        error_msg()
