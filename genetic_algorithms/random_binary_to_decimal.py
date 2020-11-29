
import random


def random_binary(n):
    a=[random.randint(0,1) for i in range(n)]
    print(a)

    prepare_conversion(a)
    

def prepare_conversion(a):
    g=''
    for i in range(0,len(a)):
            g=g+str(a[i])
            print(f'{g}----->{i}')
    print(g)

    convert(g)

    

def convert(g):
    d=int(g,2)

    print(f'Decimal: {d}')

    decision_variables(d)

    


def decision_variables(d,xmin=0,xmax=30):

    x=xmin+((xmax-xmin)/((2**n)-1))*d

    print(f'Scaled Decision Variable: {x}')


# ----------MAIN----------MAIN

n=4  #number of bits
random_binary(n)
