from re import S


print("Enter a value varName")
varName = int(input("enter a number"))

print("Enter Some Variable -:")

l1 = []
cnt = 0

while(cnt < varName):
    l1.append(eval(input()))
    cnt+=1

print("Before Sort list is -:")
print(l1)

print("After Sort list is -:")
S=sorted(l1)
print(S)