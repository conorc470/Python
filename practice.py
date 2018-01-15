# Create a program that displays the first 50 prime numbers
numberOfPrimes = 0
number = 2

while numberOfPrimes < 50:
    isPrime = True   
    for i in range(2, number):
        if number % i == 0:
            isPrime = False
    
    if isPrime == True:
        print number
        numberOfPrimes += 1
        
    number += 1
    
    