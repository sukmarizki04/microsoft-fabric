#Comment this single 
"""
multi line strings can be written using there "s and are often used as documentation 
"""
'''
Multiline stings can be written using there 's and are often use as documentation.
'''
#Example Generator on python 
def double_numbers(iterable):
    for i in iterable:
        yield i + i
#Generator to list 
values = (-x, for x in [1,2,3,4,5])
gen_to_list = list(values)
print(gen_to_list)
#Handle Exeption 
try:
    raise IndexError("This is an index error")
except IndexError as e:
    pass
except (TypeError, NameError):
    pass
else:
    print("All Good!")
finally:
    print("we can clean up resource here!")