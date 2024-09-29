def unique_el_in_2_list(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    res = set1 - set2 | set2 - set1
    return list(res)




if __name__ == '__main__':
    list1 = ['a','pig','c','d','rr','r']

    list2 = ['dog','a','ac','cat','b','c','rr','r']

    print(unique_el_in_2_list(list1,list2))