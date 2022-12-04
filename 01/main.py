import os

os.chdir('01')

data = []
with open("input.txt",'r') as file:
    for line in file:
        element = line.strip().split()
        data.append(element)

##PART 1
current_max = 0
current_sum = 0
for element in data:
  
  if element == []:
    current_sum = 0
    continue
  current_sum += int(element[0])
  if current_sum > current_max:
    current_max = current_sum
  
print(current_max)
###PART 2
sums = []
current_sum2 = 0
for element in data:
  if element == []:
    sums.append(current_sum2)
    current_sum2 = 0
    continue

  current_sum2 += int(element[0])

sums.sort()

print(sum(sums[-3:]))