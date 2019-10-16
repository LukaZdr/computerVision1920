list_1 = [0]*5
list_2 = [1]*6
list_3 = [2]*4

list_1.extend(list_2)
list_1.extend(list_3)

print(list_1)

no_dup = set(list_1)

print(no_dup)

one_to_10 = list(range(1,11))

new_set = no_dup.union(one_to_10)
print(new_set)