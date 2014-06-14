def list_intersection(list1, list2):
    length = len(list1)
    index = 0
    answer = []
    for element in list1:
        if list2.__contains__(element):
            answer.append(element)
    return answer

print list_intersection([1, 3, 5], [5, 3, 1])
print list_intersection([1, 3, 6, 9], [10, 14, 3, 72, 9])
print list_intersection([2, 3], [3, 3, 3, 2, 10])
print list_intersection([2, 4, 6], [1, 3, 5])
