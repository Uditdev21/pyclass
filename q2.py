var1 = 42
var2 = 42
print(f'id of var1: {id(var1)}')
print(f'id of var2: {id(var2)}')
if id(var1) == id(var2):
    print("var1 and var2 have the same memory address")
else:
    print("var1 and var2 have different memory addresses")
