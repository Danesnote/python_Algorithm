import sys

n = int(sys.stdin.readline())  
result = 1

for i in range(1,n+1):
  if i <= n :
    result = result * i

print(result)