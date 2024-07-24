def find_first_duplicate(num_list):
    eleCount = dict()

    for num in num_list:
        eleCount[num] = eleCount.get(num, 0) + 1
        value ={i for i in eleCount if eleCount[i] == 2}
        if value:
            return (list(eleCount.keys())[list(eleCount.values()).index(2)])
        else:
            continue
        
    return -1

    


# num_list = []
# num_list = [4]
# num_list = [1, 2, 3, 4]
# num_list = [1, 2, 3, 2, 1]
# num_list = [2, 1, 3, 3, 2]
num_list = [1, 2, 3, 3, 2, 1]
print(find_first_duplicate(num_list))
