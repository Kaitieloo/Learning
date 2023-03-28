#Fizz Buzz#

def FizzBuzz(Salad):
    if Salad % 3 == 0 and Salad % 5 == 0:
        return "FIZZ BUZZ"
    elif Salad % 3 == 0:
        return "FIZZ"
    elif Salad % 5 == 0:
        return "BUZZ"
    else: 
        return "NOPE"