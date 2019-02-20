havingfun  = False
if havingfun:
    print("i love my life")
    
userinput = input("are you having fun?: ")
while userinput == "yes":
    print("i love my life")
    userinput = input("Are you dumb?: ")
    
#example of range input list 
for i in range(10):
    print(" i love my life")
print(range(10))
print("i",i)


for i in ["dog", "cat", "mouse", "bird"]:
    print("i",i)
print(range(0,5,2))
#this will print 0-5 in two numbers so it will print 3 times including zero as in 0, 2, 4.

for i in range(3):
    print("i",i)
    
    for a in range(3):
        print("\ta,i",a,i)
for i in range(2):
    for a in range(2):
        for z in range(2):
            for k in range(2):
                print("i, a, z, k",i, a, z, k)
# print out multiplaication table with loops

for i in range(1,11):
    for j in range(1,11):
        print(i*j," ",end="")
    print("\n")
    
#find the common divisor!

n1 = int(input("Enter the first integer"))
n2 = int(input("Enter the second integer"))
gcd = 1
K = 2
while k <= (n1/2) and k <= (n2/2):
    if n1 % k == 0 and n2 % k == 0:
        gcd = k
    k += 1
print("The greatest common divisor",n1, "and", n2, "is",gcd)
