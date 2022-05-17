

def isPrime(number):
    if number>1:
        for i in range(2,number):
            if number % i == 0:
                return False
        return True

def minNumber(arr,N):
    sum_ = 0
    count = 0
    for value in arr:
        sum_ += value
    if isPrime(sum_):
        return 0
    else:
        while(isPrime(sum_)==False):
            sum_ += 1
            count += 1
    return count



