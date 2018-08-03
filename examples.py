# Method Definition and call
def sum (number1, number2) :
    return (number1 + number2)

print("Sum = {0}".format(sum(40,1)))


# if, elif, else (python's version of switch statement)
inputVariable = int(input("Please enter an integer: "))
if inputVariable < 0:
    inputVariable = 0;
    print('Negative Number has been changed to zero.')
elif inputVariable == 0:
    print('Number is zero.')
else:
    print('The number entered was {0}.'.format(inputVariable))


#for loops

    # python's version of 'for each'
physicsBranches = ["Astro", "Classical", "Quantum"]

for branch in physicsBranches:
    print('{0} Physics is hard.'.format(branch))


    # for with 'in range'
for i in range(8):
    print(i)

#specifying the range
for i in range(4, 8):
    print(i)




