def calculateAbsolute():
    # This first line is provided for you
    absolute = 21
    in_num  = int(input("Enter a number: "))
    if in_num > absolute:
        result = (in_num - absolute) * 2
    else:
        result = absolute - in_num

    print('Result:',result)
        
    # end assignment

## If you want to test locally run > python payCalculator.py

if __name__ == "__main__":
    calculateAbsolute()
