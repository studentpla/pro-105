import csv 
import math

with open ("data.csv", newline = "")as f:
    reader = csv.reader(f)
    file_data = list(reader)

data = file_data[0]

#finding the mean
def mean(data):
    n = len(data)
    total = 0
    
    for x in data:
        total = total+int(x)
    
    mean = total/n

    return mean

#calculating the power 2 and getting the value
square_list = []
for number in data:
    a = int(number)-mean(data)
    a = a**2
    square_list.append(a)

#getting the sum
sum = 0
for i in square_list:
    sum = sum+i
#dividing the sum by total values
result = sum/(len(data)-1)
# getting the standard deviation by square root of the remaining value
sd = math.sqrt(result)

print ("standard deviation of given data is ", sd)
