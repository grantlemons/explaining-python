# Lists
# -----------------------------
# Lists are ordered, changeable, and allow duplicate values
# Lists are created with square brackets

my_list = ['lists', 'tuples', 'sets', 'dictionaries']

# Tuples
# -----------------------------
# Tuples are ordered, unchangeable, and allow duplicate values
# Once a tuple is created no values can be changed, removed, or added
# Tuples are created with round brackets

my_tuple = ('lists', 'tuples', 'sets', 'dictionaries')

# Sets
# -----------------------------
# Sets are unordered, unindexed, and don't allow duplicate values
# One cannot reference something by index as they don't have and order
# Sets are created with curly brackets

my_set = {'no', 'one', 'uses', 'these'}

# Dictionaries
# -----------------------------
# Dictionaries are ordered, changeable, and don't allow duplicates
# Dictionaries use key:value pairs
# Dictionaries are created with curly brackets

my_dictionary = {
    'mitochondria': 'powerhouse of the cell',
    'quarks': 'really small',
    'data types': {
        'list': 'ordered, changeable, and allow duplicate values',
        'tuple': 'ordered, unchangeable, and allow duplicate values',
        'set': 'unordered, unindexed, and don\'t allow duplicate values',
        'dictionary': 'ordered, changeable, and don\'t allow duplicates'
    }
}

# Here are some examples of using these
# ----------------------------------------------------------
# List
print('-----------------------------')
print( 'List' )
print('-----------------------------')
for i in my_list:
    print( i )


# Tuple
print('-----------------------------')
print( 'Tuple' )
print('-----------------------------')
try:
    my_tuple.append( 'thing' )
except:
    print( 'this doesn\'t work' )
    
    
# Set
print('-----------------------------')
print( 'Set' )
print('-----------------------------')
for i in my_set:
    print( i )


# Dictionary
print('-----------------------------')
print( 'Dictionary' )
print('-----------------------------')
for i in my_dictionary:
    pass

    if type( my_dictionary[i] ) == dict:
        pass
        for j in my_dictionary[i]:
            print( f'      Key:\'{j}\' Value:\'{my_dictionary[i][j]}\'' )
    else:
        print( f'Key:\'{i}\' Value:\'{my_dictionary[i]}\'' )