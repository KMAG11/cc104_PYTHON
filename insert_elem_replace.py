#Insert element, replaces 
a = [1,2,3,4]
print(a)
index = int(input("Enter index to insert: "))
element = int(input("Enter element to insert: "))

if index < 0 or index >= len(a):
    print("Index out of range") 
a[index] = element
print(a)
