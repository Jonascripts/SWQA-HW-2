# Code file containing the BMI Calculation program


def CheckHeightFt(input):
    if input.isdigit():
            return 1
    return 0

def CheckHeightIn(input): # FUNCTION IS STUB
    print("placeholder\n")

def CheckWeight(input): # FUNCTION IS STUB
    print("placeholder\n")

def CalculateBMI(heightFt, heightIn, weight): # FUNCTION IS STUB
    print("placeholder\n")


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
        print("Error: Input must be a non-negative integer (zero is allowed).\n")

# TEST OUTPUT
print("Phase 1 test: the entered value was: %d" % usrHeightFt)