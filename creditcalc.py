from math import log
from math import ceil
import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Program calculates loan interest and such.")
    parser.add_argument("-t", "--type")
    parser.add_argument("-pay", "--payment", type=int)
    parser.add_argument("-pri", "--principal", type=int)
    parser.add_argument("-per", "--periods", type=int)
    parser.add_argument("-i", "--interest", type=float)
    args = parser.parse_args()
    if argument_are_valid(args):
        args.rate = args.interest / 1200
        if not args.payment:
            calc_payment(args)
        elif not args.principal:
            calc_principal(args)
        elif not args.periods:
            calc_periods(args)
        else:
            print("Incorrect parameters.")
    else:
        print("Incorrect parameters.")


def argument_are_valid(args) -> bool:
    if not args.type or (args.type != "annuity" and args.type != "diff"):
        return False
    if args.type == "diff" and args.payment:
        return False
    if not args.interest:
        return False
    return True


def calc_payment(args):
    if args.type == "diff":
        payment_sum = 0
        for i in range(args.periods):
            payment = (args.principal / args.periods + args.rate
                       * (args.principal - args.principal * i / args.periods))
            payment = ceil(payment)
            payment_sum += payment
            print(f"Month {i}: payment is {payment}")
        print("Overpayment = " + str(payment_sum - args.principal))
    else:
        args.payment = (args.principal * (args.rate * pow(1 + args.rate, args.periods))
                        / (pow(1 + args.rate, args.periods) - 1))
        args.payment = ceil(args.payment)
        print(f"Your annuity payment = {args.payment}!")
        print("Overpayment = " + str(args.payment * args.periods - args.principal))


def calc_principal(args):
    args.principal = (args.payment
                      / ((args.rate * pow(1 + args.rate, args.periods))
                         / (pow(1 + args.rate, args.periods) - 1)))
    args.principal = ceil(args.principal - 0.99)
    print(f"Your loan principal = {args.principal}!")
    print("Overpayment = " + str(args.payment * args.periods - args.principal))


def calc_periods(args):
    args.periods = ceil(log(args.payment / (args.payment - args.rate * args.principal), 1 + args.rate))

    if args.periods < 12:
        print(f"It will take {args.periods} months to repay this loan!")
    elif args.periods % 12 == 0:
        print(f"It will take {int(args.periods / 12)} years to repay this loan!")
    else:
        print(f"It will take {str(args.periods // 12) + ' years and '} {args.periods % 12} months to repay this loan!")
    print("Overpayment = " + str(args.payment * args.periods - args.principal))


main()
