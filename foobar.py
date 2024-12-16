# 1. Replace numbers divisible by 3 with "Foo".
# 2. Replace numbers divisible by 5 with "Bar".
# 3. Replace numbers divisible by both 3 and 5 with "FooBar".
# Example:
#
# Input: 15
# Output: [1, 2, 'Foo', 4, 'Bar', 'Foo', 7, 8, 'Foo', 'Bar', 11, 'Foo', 13, 14, 'FooBar']

import os
import time

def quitCheck(x):
    if x.lower() == 'q':
        quit()

def notPositiveCheck(x):
    if x < 1:
        return True

result = []

active = True

while active:

    result.clear()
    n = 0
    os.system('cls')
    print('Welcome to FooBar!')
    print('Type "Q" to quit at any time.')
    n = input('\nPlease enter a positive integer: ')
    quitCheck(n)
    try:
        n = int(n)
    except ValueError:
        print('ERROR: Input must be an integer.')
        time.sleep(3)
        continue
    if notPositiveCheck(n):
        print('ERROR: Input must be positive.')
        time.sleep(3)
        continue

    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            result.append('FooBar')
        elif i % 3 == 0:
            result.append('Foo')
        elif i % 5 == 0:
            result.append('Bar')
        else:
            result.append(i)

    print(f'\nResult:'
          f'\n{result}')
    n = input('\nType anything to continue or "Q" to quit... ')
    quitCheck(n)