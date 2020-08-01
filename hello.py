#!/bin/python3

def hello():
    print("please tell me your name")
    print("nothing")

    place='dhaka'
    a = 0
    if place != 'dhaka':
        a = 1
        print(str(a))
    else:
        print('is it {}'.format(a))


def Human(name='joy', phn_num=0):

    if name == '':
        print('boo')
    else:
        print(name)

    return name.upper()

hello()

Human()
