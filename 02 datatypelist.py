print("Enter a variable Number enter in List -:")
varNum = int(input("enter a number"))
print("Some variable are -:")

# we dont take element this type becaue it can take only 1 time
#element = int(input("enter a number"))

l1 = []
cnt = 0

while(cnt < varNum):
    # take element this type
    l1.append(eval(input()))
    cnt += 1
print(l1)
i=0
for e in l1:
    print(type(l1[i]))
    i+=1
