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
    PrintOutput(updated)

def FindWordCount(initial_list, substring):
    count = 0
    comb_string = ''
    for i in initial_list:
        comb_string += ' '
        comb_string += i
    for i in comb_string.split():
        if substring.lower() in i.lower():
            count += 1
            
    return count

def ScoreFinder(list1, list2, name):
    index = ''
    for i in list1:
        if name.lower() == i.lower():
            index = list1.index(i)
    if index == '':
        PrintOutput('player not found')
    else:
        final = str(list1[index]) + ' got a score of ' + str(list2[index])
        PrintOutput(final)

def Union(list1, list2):
    for i in list2:
        for y in list1:
            if y == i:
                list1.remove(y)
    return list1 + list2

def Intersection(list1, list2):
    list_final = []
    for i in list2:
        for y in list1:
            if y == i:
                list_final.append(y)

    return list_final

def NotIn(list1, list2):
    list_final = []
    for i in list2:
        for y in list1:
            if y == i:
                list1.remove(y)
    return list1
    
    







        
