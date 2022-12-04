a = [1,2,3,4,5,6,7,8,9,10]
def replace(list):
    max1 = list.index(max(list))
    min1 = list.index(min(list))
    list[max1], list[min1] = list[min1], list[max1]
    print(list)
replace(a)
