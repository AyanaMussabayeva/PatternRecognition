a=input().split()
for i in range(len(a)):
	a[i]=int(a[i])
t = int(input())
a.sort()
b = list(reversed(a))
print(b)
sum = 0
if len(b) < t:
	for i in range(len(b)): 
		sum = sum + int(b[i])
else:
	for i in range(t):
		sum = sum + int(b[i])

print(sum)