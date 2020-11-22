from itertools import permutations
def can_create(list_of_strings,input_string):
    perm = permutations(list_of_strings)    #fetching all combinations using permutation method
    s=''    #creating empty string
    for i in perm:
        if input_string in s.join(i): #verifying if the joined elements contains input string
            return True
    return False
print(can_create(['back','end','front','tree'],'frontend'))