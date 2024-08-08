# CinPy
Try to use C library inside Python code

## creating C library
Create or use a C library.
Compile c code into a shared library in linux distro using
`gcc -shared -o lib.so -fPIC lib.c`

## creating python code
Import ctypes in python to use C shared libraries

## Key Points
we can't just run any c function inside a shared library using ctypes.function_nme(param1,...)

for example, if the c function requires pointer arguments and returns a pointer.

Then we have to preprocess and prepare ctypes so that it knows function 'func_name' has these type parameters and this type of return value.

This tells add function signature is type of (*int,*int):
- `clib.add.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int)]`

This tells add function returns a *int:
- `clib.add.restype = ctypes.POINTER(ctypes.c_int)`

Also if we want to give pointers to a c function inside python:
- `a = ctypes.c_int(10)`

Calling the function by giving pointers:
- `result_ptr = clib.add(ctypes.byref(a), ctypes.byref(b))`

At the end we again need to retrieve pointer value from the returned data.
This retrieves value of the returned pointer:

- `result = result_ptr.contents.value`

>Also this *.so type is for linux pltform shared libraries.

>for windows we have to create *.dll type shared library
