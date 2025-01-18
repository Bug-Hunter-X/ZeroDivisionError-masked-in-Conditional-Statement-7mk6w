def function_with_uncommon_error(a, b):
    if a == 0:
        return float('inf') # or handle it appropriately as needed. 
    else:
        return a + b