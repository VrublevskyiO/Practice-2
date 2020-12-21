from exp_root import exponentiation
from exp_root import root
from factorial import factorial
from logarithm import logarithm

def main():
    print("1 - x^2")
    print("2 - x^3")
    print("3 - x^(1/2)")
    print("4 - x(1/3)")
    print("5 - x!")
    print("6 - lg(x)")
    print("7 - ln(x)")
    print("8 - log(x) (base=a)")
    numb=int(input())
    x=float(input("input x"))

    if numb==1:
        print(exponentiation.exp2(x))

    elif numb==2:
        print(exponentiation.exp3(x))

    elif numb==3:
        if x<=0:
            print("Unintended value")
            exit()
        print(root.root2(x))

    elif numb==4:
        print(root.root3(x))

    elif numb==5:
        if (not x.is_integer()) and (x>0):
            print("Unintended value")
            exit()
        print(factorial.fact(x))

    elif numb==6:
        if x<=0:
            print("Unintended value")
            exit()
        print(logarithm.lg(x))

    elif numb==7:
        if x<=0:
            print("Unintended value")
            exit()
        print(logarithm.ln(x))

    elif numb==8:
        a = float(input("input base of logarithm"))
        if not (a>0 or а!=1 or x>0):
            print("Unintended value")
            exit()
        print(logarithm.log(a,x))


if __name__ == '__main__':
    main()