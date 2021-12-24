# -*- coding: utf-8 -*-
"""
Created on Sun Dec 19 02:42:43 2021

@author: sarak
"""
def main():
    scores = {
        'jane': 30,
        'Joe': 20,
        'George': 30,
        'Hellena': 90,
        }

    for name in scores.keys():
        print(f"{name:8} {scores[name]}")
                        # jane 30
                        # Joe 20
                        # George 30
                        # Hellena 90
    print('')

    for name in sorted(scores.keys()):
        print(f"{name:8} {scores[name]}")

                        # George   30
                        # Hellena  90
                        # Joe      20
                        # jane     30

    print('')

    for val in sorted(scores.values()):
        print(f"{val:8}")

                        # 20
                        # 30
                        # 30
                        # 90


    print('')
    for name in sorted(scores.keys(), key= lambda x: scores[x]):
        print(f"{name:8} {scores[name]}")

                        # Joe      20
                        # jane     30
                        # George   30
                        # Hellena  90

if __name__ == '__main__':
    main()