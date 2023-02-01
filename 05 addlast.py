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

#append element in the list
l1.append('VISNU')
l1.append('BHARDWAJ')
print(l1)
