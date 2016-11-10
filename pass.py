import sys
import random as r

lower='abcdefghijklmnopqrstuvwxyz'
upper='ABCDEFGHIJKLMNOPQRSTUVMXYZ'
numb='0123456789'
symb='!@#$%^&*()-_=+'
ambig=r"~`\|';:/?><.,[]{}"

low=1
upp=1
num=1
sym=1
amb=1

def main():
    r.seed()
    get()
    return 0

def get():
    while True:
        try:
            print 'Length:'
            length = int(raw_input())
        except ValueError:
            continue
        except KeyboardInterrupt:
            print '\n(exiting)'
            sys.exit(1)
        except EOFError:
            continue
        break

    concat(length)

def concat(length):
    pool=''
    if low:
        pool += lower
    if upp:
        pool += upper
    if num:
        pool += numb
    if sym:
        pool += symb
    if amb:
        pool += ambig
    calc(pool,length)

def calc(p,length):
    x = len(p)
    pool = list(p)
    passwd=''

    for i in range(length):
        passwd += p[r.randint(0,x)]

    print passwd

main()
