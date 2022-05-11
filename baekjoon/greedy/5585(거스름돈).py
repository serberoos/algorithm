cost = int(input())
re_cost = 1000 - cost
cnt = 0

while(re_cost > 0):
  if re_cost >= 500:
    fivehundNum = re_cost // 500
    re_cost -= fivehundNum * 500
    cnt += fivehundNum
  elif re_cost >= 100:
    onehundNum = re_cost // 100
    re_cost -= onehundNum * 100
    cnt += onehundNum
  elif re_cost >= 50:
    fivetenNum = re_cost // 50
    re_cost -= fivetenNum * 50
    cnt += fivetenNum
  elif re_cost >= 10:
    tenNum = re_cost // 10
    re_cost -= tenNum * 10
    cnt += tenNum
  elif re_cost >= 5:
    fiveNum = re_cost // 5
    re_cost -= fiveNum * 5
    cnt += fiveNum
  elif re_cost >= 1:
    oneNum = re_cost // 1
    re_cost -= oneNum * 1
    cnt += oneNum
  
print(cnt)