"""
The classic FizzBuzz problem.  When the number is divisible by 3 we print 'Fizz' when it's divisible by 5 we print 'Buzz'.  When it's both we print 'FizzBuzz'.
"""


def main():
    userInput = 0
    while userInput < 1 or userInput > 10000:
        print("Enter a number 1-10000:")
        try:
            userInput = int(input())
        except:
            print("Please enter an integer!")
            userInput = 0
        if userInput < 1 or userInput > 10000:
            print("Not a valid number.  Please choose one from 1 to 10000")

    # Now let's do the printing
    for x in range(1, userInput + 1):
        printStr = ""
        if x % 3 == 0:
            printStr += "Fizz"
        if x % 5 == 0:
            printStr += "Buzz"
        if x % 3 != 0 and x % 5 != 0:
            printStr += "{}".format(x)
        print(printStr)


if __name__ == "__main__":
    main()
