'''
how to calculate "e"
e = 1 / i! + 1 / 2i ... + 1 / i!

i! = 1 * 2 * ... * i-1 * i
'''

calc_e = 1
end_point = 200 

for i in range(1, end_point + 1):
    denom = 1 
    for x in range(1, i + 1):
        denom *= x 
    calc_e += 1 / denom
print(" we calculated e to be:", calc_e)

#assignment 5.26 
sum = 0 
for i in range(1,98):
    sum += i / (i + 2)
print("The sum of the series :",sum)

#assignment 5.27
