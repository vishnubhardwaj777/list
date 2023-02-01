print("Enter a variable Number enter in List -:")
varNum1 = int(input("enter a varNumber 1 -: "))

print("Some variable are -:")

# we dont take element this type becaue it can take only 1 time
#element = int(input("enter a number"))

l1 = []
l2 = []
cnt = 0
count = 0

while(cnt < varNum1):
    # take element this type
    l1.append(eval(input()))
    cnt += 1
print(l1)

varNum2 = int(input("enter a varNumber 2 -: "))

while(count < varNum2):
    # take element this type
    l2.append(eval(input()))
    count += 1
print(l2)

# l1.append(l2)  in this case whole l2 list append in l1
l1.extend(l2)  # in this case one by one element append

print(l1)