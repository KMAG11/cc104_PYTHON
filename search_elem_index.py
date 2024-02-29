#Search element's index and index's element
a =[1,2,3,4,5,6,7,8,9]
print(a)

s_ele = int(input("Enter element you want to search: "))

for i in range(len(a)):
  if a[i] == s_ele:
    print("The index is", i)

s_index = int(input("Enter index: "))
print("The element is", a[s_index])
