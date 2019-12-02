
# convert string to int with specified radix
def str2int(x_str, radix):
    x_int = int(x_str,radix)
    return x_int

# convert int to base 10 string
def int2str(x_int):
   x_str = str(x_int)
   return(x_str)

# convert int to base 16 (string)
def int2hex(x_int):
    return hex(x_int)

# convert int to binary string
def int2bin(x_int):
    return bin(x_int)

print("number:")
x = 231
print(x)

print("number in base 10 (string)")
x_str = int2str(x)
print(x_str)

print("number in binary (string)")
x_str2 = int2bin(x)
print(x_str2)

print("number in base 16 (hex) (string)")
x_str16 = int2hex(x)
print(x_str16)

print("number reconstructed (base 10)")
xr1 = str2int(x_str,10)
print(xr1)

print("number reconstructed (base 16)")
xr2 = str2int(x_str16,16)
print(xr2)

print("number reconstructed (base 2)")
xr3 = str2int(x_str2,2)
print(xr3)


