#Challenge 1
w = input("Give me a word.")

for i in range(0, len(w)):
    print(w[len(w)-i-1])

#Challenge 2
l = ["Bob", "Joe", "Dan", "Jordan", "Felix"]
o = input("Give me a name to add to the list.")
l.append(o)
print(str(o) + " was added into the list.")
print (l)

#Challenge 3
if "Bob" in l:
    print("Bob exists")
if "Bob" not in l:
    print("Bib des not exist")

#Challenge 4
n=int(input("Give me a number, 1-5"))
print(l[n])

#Challenge 5
l[0], l[1] = l[1], l[0]

#Challenge 6
number=[76,29,83,41,86,9,43,74,4,8,12]
print("The largest number in the list is " + str(max(number)))
print("The smallest number in the list is " + str(min(number)))

#Challenge 7
print("The sum of the numbers in the list is " + str(sum(number)))

#Challenge 8
n = input("Give me a name")
if n in l:
    print(l.index(n))
elif n not in l:
    print(str(n) + " is not in the list")
