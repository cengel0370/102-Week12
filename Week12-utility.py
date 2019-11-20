# Chris Engel
# CSCI 102 - Section L
# Week 12

#Functions
def PrintOutput(print_str):
    print('OUTPUT %s' % str(print_str))

def LoadFile(file_name):
    with open(file_name, 'r') as open_file:
        read_file = open_file.readlines()
        temp_list = []
        for i in read_file:
            if i.endswith('\n'):
                i = i[:-1]
                temp_list.append(i)
            else:
                temp_list.append(i)
        return temp_list

def UpdateString(string1, string2, index):
    updated = string1[:index] + string2 + string1[index + 1:]
    print('OUTPUT', updated)
