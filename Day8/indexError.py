def access_list_element(lst, ind):
    try:
        value = lst[ind]
        print("Value at index: ", ind, "is: ", value)
    except IndexError:
        print("Error: Index out of range")

access_list_element([1,2,3,4,5], 6)