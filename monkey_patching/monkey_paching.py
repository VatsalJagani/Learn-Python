# In Python, the term monkey patch refers to dynamic (or run-time) modifications of a class or module. 

import os
print("Original join func: " + os.path.join("c", "d"))

def patched_func(a, b):
    return "Hello World !!!"

# replacing address of "func" with "monkey_f" 
os.path.join = patched_func

print("Updated join func: " + os.path.join("c", "d"))