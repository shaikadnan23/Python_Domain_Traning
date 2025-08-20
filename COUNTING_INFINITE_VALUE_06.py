# a="123"
# sum=0
# for i in a:
#     x=ord(i)-ord('0')
#     sum=sum*10+x
# print(sum)


a="123"
b=[int(i) for i in a]
sum=0
for i in b:
    sum=sum*10+i
print(sum)

# n = 1
# total = 0
# while n != 0:
#     n = int(input("Enter the number: "))
#     if n == 0:
#         break
#     if n < 40 or n > 100:   
#         continue
#     total += n   
# print( total)