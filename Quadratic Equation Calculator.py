# do it by factoring

import math


a = 1

print ("a = " + str(a))

b = int(input("Give a whole number value for b in the quadratic formula"))

c = int(input("Give a whole number value for c in the quadratic formula"))


# firstPara is num in first parenthesis

# secondPara is num in second parenthesis


firstPara = 0

if b > -1 and c > -1:

    for i in range(0, int(b)):

        secondPara = float(b - firstPara)

    #   print(firstPara)

    #   print(secondPara)

    # use the two lines above for 'print' debugging / demonstrating the flow of code 
   
#        while i == int(b):
#            if firstPara + secondPara == b and firstPara * secondPara == c:
#               print("Invalid quadratic equation. No whole number solution")
#               break
        
        if firstPara + secondPara == b and firstPara * secondPara == c:
            break

        else:
            firstPara += 1

# if b < 0 and c < 0:

# if b > -1 and c < 0:

# if b < -1 and c > 0:
    




if firstPara > -1:

    firstPara = ("+ " + str(firstPara))

if secondPara > -1:

    secondPara = ("+ " + str(secondPara))


print("(x " + str(firstPara + ")") + "(x " + str(secondPara) + ")")






