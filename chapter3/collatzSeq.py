def collatz(number):
    number = int(number)
    if number % 2 == 0: 
        number = number //2
        print(number)
        return number
    else:
        number = number*3 + 1
        print(number)
        return number


x = input("give a number: ")
while(x!=1):
    x = collatz(x)