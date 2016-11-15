def find_missing(list1, list2):
    missing=[]
    if len(list1)==0 & len(list2)==0:
        return 0
    elif list1==list2:
        return 0
    else:
        if len(list1)>len(list2):
            [missing.append(integer) for integer in list1 if integer not in list2]
        elif len(list2)>len(list1):
            [missing.append(integer) for integer in list2 if integer not in list1]

        return missing[0]