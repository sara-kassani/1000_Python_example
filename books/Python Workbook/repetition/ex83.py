# exercise 83: Maximum Integer

import random


# if using randrange() the second argument would be excluded
random_value = random.randint(1, 100)
# first number that is extracted will start as maximum value
maximum = random_value
print(maximum)
# number of times I get a new maximum number
updates = 0

# start looping from 1 since I already got a random value (100 is excluded in the range)
for i in range(1, 100):
    random_value = random.randint(1,100)
    if random_value > maximum:
        maximum = random_value
        updates += 1
        print(maximum, '---> UPDATE')
    else:
        print(random_value)

print('the maximum value encountered was {}'.format(maximum))
print('the maximum was updated {} times'.format(updates))
