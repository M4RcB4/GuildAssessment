__author__ = 'Marcus'

class Shelter:

    def __init__(self, leftOver=0):
        self.maxCapacity = 30

    def orderAmount(self, small, medium, large, leftOver):
        # Check for type
        if isinstance(small, bool) or isinstance(medium, bool) or isinstance(large, bool) or isinstance(leftOver, bool):
            raise TypeError("Inputs cannot be of boolean type")
        if not isinstance(small, int) or not isinstance(medium, int) or not isinstance(large, int):
            raise TypeError("Dog count must be of int type")
        
        if not isinstance(leftOver, float) and not isinstance(leftOver, int):
            raise TypeError("Leftover amount must be a int or a float")

        # Cast to int and float
        small = int(small)
        medium = int(medium)
        large = int(large)
        leftOver = float(leftOver)

        # Check for parameter boundary conditions
        if small<0 or medium<0 or large<0: raise Exception("Dog count must be a positive whole number")
        if leftOver<0: raise Exception("leftover food must be a positive number")
        if small+medium+large>self.maxCapacity: raise Exception("Total Dog count cannot exceed {}".format(self.maxCapacity))
        
        # Calculate food need; add 20% extra; subtract leftover; return result
        foodNeeded = (small*10 + medium*20 + large*30) * 1.2 - leftOver
        
        # If food needed is less than what is left over, then return 0
        if foodNeeded<0:
            foodNeeded = 0
        return foodNeeded

# provide information and inputs when running as a program
if __name__ == '__main__':
    myShelter = Shelter()
    print("\n\n\n================================================")
    print("FOOD ORDER v1.0 \n  All dog counts should be whole positive numbers.\n  Leftover food must be a whole positive floating point number.\n  ")
    print("================================================")
    smallInput = input("How many small dogs?")
    meduiumInput = input("How many medium dogs?")
    largeInput = input("How many large dogs?")
    leftOverInput = input("How much food is left over from last order?")

    print(myShelter.orderAmount(smallInput, meduiumInput, largeInput, leftOverInput))