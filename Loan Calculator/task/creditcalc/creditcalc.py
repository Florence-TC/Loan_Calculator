import math
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--type", choices=["annuity", "diff"])
parser.add_argument("-mp", "--payment")
parser.add_argument("-pp", "--principal")
parser.add_argument("-n", "--periods")
parser.add_argument("--interest")

args = parser.parse_args()

# dealing with the arguments and some error cases
everything_valid = True
valid_args = []

if not args.type:
    everything_valid = False
    calc_type = ""
else:
    calc_type = args.type
    valid_args.append(calc_type)
    if calc_type not in ("annuity", "diff"):
        everything_valid = False

if args.principal:
    pp = int(args.principal)
    if pp >= 0:
        valid_args.append(pp)
else:
    pp = 0

if args.payment:
    mp = int(args.payment)
    if mp >= 0:
        valid_args.append(mp)
    if calc_type == "diff":
        everything_valid = False
else:
    mp = 0

if args.periods:
    n = int(args.periods)
    if n >= 0:
        valid_args.append(n)
else:
    n = 0

if args.interest:
    i = float(args.interest) / (12 * 100)  # convert the annual % rate to a monthly float value
    if i >= 0:
        valid_args.append(i)
else:
    everything_valid = False

if len(valid_args) < 4:
    everything_valid = False


# calculating the number of months, requires "annuity", principal, monthly payment, interest
def calc_n():
    global n
    n = math.ceil(math.log(mp / (mp - i * pp), 1 + i))

    if n == 1:
        print(f'It will take {n} month to repay the loan')
    elif n < 12:
        print(f'It will take {n} months to repay the loan')
    elif n == 12:
        print(f'It will take {n // 12} year to repay the loan')
    elif n % 12 == 0:
        print(f'It will take {n // 12} years to repay the loan')
    elif n % 12 == 1:
        print(f'It will take {n // 12} years and {n % 12} month to repay the loan')
    else:
        print(f'It will take {n // 12} years and {n % 12} months to repay the loan')

    # calculating overpayment
    overpayment = math.ceil(n * mp - pp)
    print(f'Overpayment = {overpayment}')


# calculating the annuity payment, requires "annuity", principal, number of months, interest
def calc_mp():
    global mp
    mp = math.ceil(pp * (i * (1 + i) ** n) / ((1 + i) ** n - 1))

    print(f'Your monthly payment = {mp}!')

    # calculating overpayment
    overpayment = math.ceil(n * mp - pp)
    print(f'Overpayment = {overpayment}')


# calculating the principal, requires "annuity", monthly payment, number of months, interest
def calc_pp():
    global pp
    pp = mp / ((i * (1 + i) ** n) / ((1 + i) ** n - 1))

    print(f'Your loan principal = {math.floor(pp)}!')

    # calculating overpayment
    overpayment = math.ceil(n * mp - pp)
    print(f'Overpayment = {overpayment}')


# calculating differentiated payments, requires "diff", principal, number of months, interest
def calc_diff():
    total = 0
    for m in range(1, n + 1):
        diff_pay = math.ceil(pp / n + i * (pp - (pp * (m - 1)) / n))
        print(f'Month {m}: payment is {diff_pay}')
        total += diff_pay

    # calculating overpayment
    overpayment = math.ceil(total - pp)
    print(f'Overpayment = {overpayment}')


# invoking the appropriate function
if everything_valid:
    if calc_type == "diff":
        calc_diff()
    elif calc_type == "annuity":
        if not mp:
            calc_mp()
        elif not pp:
            calc_pp()
        elif not n:
            calc_n()
else:
    print("Incorrect parameters.")
