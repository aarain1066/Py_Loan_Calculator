import argparse
import math
import sys

parser = argparse.ArgumentParser()
parser.add_argument("--type",)
parser.add_argument("--payment", type=int)
parser.add_argument("--principal", type=int)
parser.add_argument("--periods", type=int)
parser.add_argument("--interest", type=float)
args = parser.parse_args()

options = [args.type,
           args.payment,
           args.principal,
           args.periods,
           args.interest
           ]


def diff_payment_calc(principal, adj_interest, payment_periods, curr_repay):
    diff_payment = math.ceil((principal / payment_periods) + adj_interest * (principal - ((principal * (curr_repay - 1)) / payment_periods)))
    return diff_payment


def number_payments_calc(payment, adj_interest, principal):
    n_payments = math.ceil(math.log((payment / (payment - (adj_interest * principal))), (1 + adj_interest)))
    return math.ceil(n_payments)


def principal_calc(adj_interest, payment, n_payments):
    principal = math.ceil(payment/((adj_interest * math.pow((1 + adj_interest), n_payments)) / (math.pow((1 + adj_interest), n_payments) - 1)))
    return principal


def annuity_payment_calc(principal, adj_interest, n_payments):
    payments = math.ceil(principal * ((adj_interest * math.pow((1 + adj_interest), n_payments)) / (math.pow((1 + adj_interest), n_payments) - 1)))
    return payments


if args.interest is None:
    print("Incorrect parameters")
    sys.exit()
elif args.type == "annuity":
    interest = float(args.interest) / 12 / 100
    if args.payment is None:
        annuity_payment = annuity_payment_calc(args.principal, interest, args.periods)
        overpayment = math.ceil(annuity_payment * args.periods - args.principal)
        print(f'Your annuity payment = {round(overpayment)}!\n'
              f'Overpayment = {int(annuity_payment)}')
    if args.principal is None:
        principal = principal_calc(interest, args.payment, args.periods)
        overpayment = args.payment * args.periods - principal
        print(f'Your loan principal = {principal}!'
              f'\nOverpayment = {overpayment}')
    if args.periods is None:
        number_payments = number_payments_calc(args.payment, interest, args.principal)
        years = int(number_payments / 12)
        overpayment = args.payment * number_payments - args.principal
        print(f'It will take {years} years to repay this loan!'
              f'\nOverpayment = {overpayment}')

elif args.type == "diff":
    interest = float(args.interest) / 12 / 100
    diff_payments_total = 0
    for each_period in range(1, args.periods + 1):
        each_payment = diff_payment_calc(principal=args.principal,
                                         adj_interest=interest,
                                         payment_periods=args.periods,
                                         curr_repay=each_period
                                         )
        print(f"Month {each_period}: payment is {round(each_payment)}")
        diff_payments_total += round(each_payment)
    overpayment = diff_payments_total - args.principal
    print(f'Overpayment = {overpayment}')
