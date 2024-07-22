def find_first_duplicate(num_list):
    eleCount = dict()

    for num in num_list:
        eleCount[num_list[num]] = eleCount.get(num_list[num], 1) + 1
        k = list(eleCount.keys())
        v = list(eleCount.values())
        if 2 in v:
            return (k[v.index(v)])
        else:
            return -1

print(find_first_duplicate([2, 1, 3, 3, 2]))
