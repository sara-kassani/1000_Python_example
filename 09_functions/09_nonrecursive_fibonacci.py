# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 09:15:35 2021

@author: sarak
"""

# Non-recursive Fibonacci

def main():
    def fib(n):
        if n == 1:
            return [1]

        if n == 2:
            return [1, 1]

        fibs = [1, 1]

        for i in range(2, n):
            fibs.append(fibs[-1] + fibs[-2])

        return fibs

    print(fib(30))

                    # [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040]

if __name__ == '__main__':
    main()