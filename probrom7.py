def counter_num(list1):
    counter = 0

    for i in  list1 :
        x = list1.count(i)
        if (x> counter):
            num = i
    return num
list1 = [1,8,7,4,1,2,2,2,]
print(counter_num(list1))
    
