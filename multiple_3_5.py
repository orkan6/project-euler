#Find the sum of all the multiples of or below 1000.

numb3 = 0
numb5 = 0
numb15 = 0

for i in range(0,1000,3):
    numb3 += i

for j in range(0,1000,5):
    numb5 += j

for k in range(0,1000,15):
    numb15 += k

print((numb3+numb5)-numb15)
