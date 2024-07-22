def find_first_duplicate(num_list):
    eleCount = dict()

    for num in num_list:
        eleCount[num] = eleCount.get(num, 0) + 1
        value ={i for i in eleCount if eleCount[i] == 2}
        # k = list(eleCount.keys())
        # v = list(eleCount.values())
        breakpoint()
        if value == 2:
            return (list(eleCount.keys())[list(eleCount.values()).index(2)])
            # return (k[v.index(v)])
        else:
            return -1

    


num_list = [2, 1, 3, 3, 2]
print(find_first_duplicate(num_list))
