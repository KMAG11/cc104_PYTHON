#Insert an element without replacing 
a =[1,2,3,4,5,6,7,8,9]
print(a)

index = int(input("Enter index of element to insert: "))
element= int(input("Enter element: "))

if index < 0 or index > len(a):
  print("Out of range")

a.append(None)


for i in range(len(a) -1, index, -1):
  a[i] = a[i-1]
a[index] = element

print(a)
