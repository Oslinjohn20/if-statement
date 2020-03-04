# Ask the user for input
raw_input_1 = input("Enter number 1:")
raw_input_2 = input("Enter number 2:")
raw_input_3 = input( "Enter number 3:" )
# Here we are converting our raw input to an interger

n1 = int(raw_input_1)
n2 = int(raw_input_2)
n3 = int(raw_input_3)
# checks and print the biggest value between n1, n2 and n3

if n1 > n2:
    if n1 > n3:
        print(n1)
    else: print(n3)
else: print(n2)

if n2 > n3:
     print(n2)
