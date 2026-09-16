from itertools import permutations
my_list=[1,2,3]

list_of_permutations=permutations(my_list)
count=0

for permutation in list_of_permutations:
    print(permutation)
    count+=1

print("Length of the list: ",len(my_list))
print("Permutation Count :",count)

