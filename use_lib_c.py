import ctypes

# load the shared C library
clib = ctypes.CDLL('./lib.so')

# define arguments types and return type for the add function
clib.add.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int)]
clib.add.restype = ctypes.POINTER(ctypes.c_int)

# create int pointer variables
a = ctypes.c_int(10)
b = ctypes.c_int(20)

# call the C function
result_ptr = clib.add(ctypes.byref(a), ctypes.byref(b))

# dereference the resultant pointer
result = result_ptr.contents.value

print(f"The Sum is {result}")