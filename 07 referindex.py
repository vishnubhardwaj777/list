
print("Enter a value varName")
varName = int(input("enter a number"))

print("Enter Some Variable -:")

l1 = []
cnt = 0

while(cnt < varName):
    l1.append(eval(input()))
    cnt+=1

count=0

for e in l1:
    print(count,e,end=",")
    count+=1
