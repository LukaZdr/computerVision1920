number = int(input("deine zahl"))

odd_list = list(range(1,(number+1),2))

result = 1

for number in odd_list:
  result = result * number

print(result)
