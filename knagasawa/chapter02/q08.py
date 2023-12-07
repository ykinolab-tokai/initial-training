math = 100
for p in range(2,math+1):
  for k in range(2, p):
    if p % k == 0:
      break
  else:
     print(p, end=' ')