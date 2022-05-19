count = 0
data = []
num = int(input())
for i in range(1, num + 1):
  x, y = input().split()
  x = int(x)
  y = int(y)
  data.append([x,y])
data.sort(key=lambda x:x[1])

start = data[0][0]
end = data[0][1]
count += 1

for d in data:
  
  start = d[0]
  if start >= end:
    count += 1
    end = d[1]
  else:
    continue

print(count)