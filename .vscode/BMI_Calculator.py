# Code file containing the BMI Calculation program


def CheckHeightFt(input):
    if input.isdigit():
        return 1
    return 0

def CheckHeightIn(input):
    if input.isdigit():
        if (int(input) > 11):
            return 0
        else:
            return 1
    return 0

def CheckWeight(input):
    if input.isdigit():
        return 1
    return 0

def CalculateBMI(heightFt, heightIn, weight): # FUNCTION IS STUB
    # Convert all height to inches
    tempHeight = heightIn + (heightFt * 12)
    # Metric conversion
    tempWeight = weight * 0.45
    tempHeight = tempHeight * 0.025
    # Square height value
    tempHeight = tempHeight * tempHeight
    # Calculate BMI
    return round((tempWeight / tempHeight), 1)

def giveBMIRange(BMI): # FUNCTION IS STUB
    if BMI < 18.5:
        return 1
    elif (BMI >= 18.5) and (BMI < 25):
        return 2
    elif (BMI >= 25) and (BMI < 30):
        return 3
    elif BMI >= 30:
        return 4


# Start program
# Declare variables
usrInput1 = "null"
usrInput2 = "null"
usrInput3 = "null"

# i variables used for loops
i1 = 1
i2 = 1
i3 = 1

usrHeightFt = 0
usrHeightIn = 0
usrWeight = 0
# usrBMI calculated from user inputs
usrBMI = 0
# BMI range of usrBMI
usrBMIRange = 0


# Begin prompts
print("Welcome to the very basic but still very nice and not buggy at all BMI Calculator System (patents pending).\n")
# Get and check height (feet) input
while (i1 == 1):
    usrInput1 = input("Enter your height (in feet): ")
    if (CheckHeightFt(usrInput1) == 1):
        usrHeightFt = int(usrInput1)
        i1 = 0
    # If input invalid, display error and retry
    else:
        print("Error: Input must be a non-negative integer (zero is allowed).")

while (i2 == 1):
    usrInput2 = input("Enter your height (in inches): ")
    if (CheckHeightIn(usrInput2) == 1):
        usrHeightIn = int(usrInput2)
        i2 = 0
    # If input invalid, display error and retry
    else:
        print("Error: Input must be a non-negative integer that is no greater than 11 (zero is allowed).")

while (i3 == 1):
    usrInput3 = input("Enter your weight (in pounds): ")
    if (CheckWeight(usrInput3) == 1):
        usrWeight = int(usrInput3)
        i3 = 0
    # If input invalid, display error and retry
    else:
        print("Error: Input must be a non-negative integer (zero is allowed).")

print("Calculating your BMI...")
usrBMI = CalculateBMI(usrHeightFt, usrHeightIn, usrWeight)
print("Your BMI is: %f" % usrBMI)

print("Determining BMI Range...")
if giveBMIRange(usrBMI) == 1:
    print("Your BMI is considered underweight.")
elif giveBMIRange(usrBMI) == 2:
    print("Your BMI is considered normal.")
elif giveBMIRange(usrBMI) == 3:
    print("Your BMI is considered overweight.")
elif giveBMIRange(usrBMI) == 4:
    print("Your BMI is considered obese.")

# TEST OUTPUT
print("Phase 1 test: the entered value was: %d" % usrHeightFt)
print("Phase 2 test: the entered value was: %d" % usrHeightIn)
print("Phase 3 test: the entered value was: %d" % usrWeight)