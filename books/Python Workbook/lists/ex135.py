# exercise 135: The Sieve of Eratosthenes

limit = int(input('enter a limit: '))
nums = []
for i in range(0, limit + 1):
    nums.append(i)

nums[1] = 0

#print(nums)

p = 2
while p < limit:
    # making all multiple of p except p equal to zero, because I already know they are not prime numbers
    # using p itself as third parameter of the range, so that I find all multiples until the limit
    for i in range(p*2, limit + 1, p):
        nums[i] = 0

    # incrementing p by 1 and keeping incrementing it until I find a number which is not already zeroed
    p = p + 1
    while p < limit and nums[p] == 0:
        p = p + 1


if __name__ == '__main__':
    for n in nums:
        if n != 0:
            print(n)
