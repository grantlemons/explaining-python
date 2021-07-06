# Functions are a predefinded list of instructions

def function_template():
    pass


# Passing values
def uses_values(input):
    print(input)


# Functions can make changes to this input and return an output
def returns_input(input):
    output = f'imagine thinking this would be \'{input}\''
    return output


# These inputs and outputs can be almost anything
def append_value(list, value):
    internal_list = list.copy()
    internal_list.append(value)
    return internal_list

my_list = ['thing 1', 'thing 2']
print( append_value(my_list, 'thing 3') )