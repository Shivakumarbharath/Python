list1 = ['Bharath', 'tom', 'Jerry', 'Likith', 'Yathish', 'Bhargav']
list2 = [1, 2, 3, 4, 5, 6]


def merge(L1, L2):
    comb = {}
    for i in range(0, len(L1)):
        comb[L2[i]] = L1[i]
    return comb


convert = merge(list1, list2)
print(convert)
# codecadamy
