#Delete Element
a =[1,2,3,4,5,6,7,8,9]
print(a)

index = int(input("Enter index of element to delete: "))

if index < 0 or index > len(a):
  print("Out of range")

print(a) 

for i in range(index, len(a) -1):
  print(i)
  a[i] = a[i+1]

a.pop() #Gets rid of duplicate end element
print(a)
