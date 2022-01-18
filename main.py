
def armstrongFunction(userInput):
    sum = 0
    order = len(str(userInput))
    while userInput > 0:
        digit = userInput % 10
        sum += digit**order
        userInput = userInput//10
    return sum


if __name__ == "__main__":

    userInput = int(input("Enter your number : "))
    check = armstrongFunction(userInput)

    if(userInput == check):
        print(f"This is armstrong number {check} ")
    else:
        print(f"This is not a armstrong number {check} ")
