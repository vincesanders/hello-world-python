### list
l = [2, 'four', 6.3, '8', [5, 7]]
### dictionary
eng2ja = {'one': 'ichi', 'two': 'ni', 'three': 'san'}
### tuple
t = ('l', 'a', 'm', 'b', 'd', 'a')
### set
s = {'tree', 'building', 'sky'} # like dictionary, but no keys
'''
If the order of your data matters, then use a LIST.

If you want to store an immutable (unchangeable) list of data, then use a TUPLE.

If you need to associate values with keys so you can look up data efficiently, then you should use a DICTIONARY.

If you just need to know if you already have a particular piece of data, order doesn’t matter, and you need not keep duplicates, then use a SET.
'''
### dir() ### dir() will print out all available properties and methods on an object.
print(dir(list))
### help() ### help() will print out the man page for whatever function you pass to it. 
help(list.pop)