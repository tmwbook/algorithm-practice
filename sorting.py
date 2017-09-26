from copy import deepcopy

from util import get_unique_unordered

base = get_unique_unordered(11)

def acending(to_comp, comp_against):
    return to_comp < comp_against


def decending(to_comp, comp_against):
    return to_comp > comp_against


def verify(array, comp_func):
    for i in range(len(array)-1):
        if not comp_func(array[i], array[i+1]):
            return False
    return True

def bubble_sort(copy, comp_func):
    while not verify(copy, comp_func):
        #i = 0
        for i in range(len(copy)-1):
            if not comp_func(copy[i], copy[i+1]):
                temp = copy[i]
                copy[i] = copy[i+1]
                copy[i+1] = temp
           # i += 1
    return copy


def selection_sort(copy, comp_func):
    for i in range(len(copy)):
        leader = copy[i]
        lead_loc = i
        for j in range(i, len(copy)):
            if not comp_func(leader, copy[j]):
                leader = copy[j]
                lead_loc = j
        
        temp = copy[i]
        copy[i] = leader
        copy[lead_loc] = temp
            
    return copy

 
def insertion_sort(copy, comp_func):
    for i in range(1, len(copy)):
        if not comp_func(copy[0], copy[i]) or not comp_func(copy[i-1], copy[i]):
            insertion_point = 0
            for j in range(i):
                if comp_func(copy[j], copy[i]):
                    insertion_point += 1
                else:
                    break
            to_insert = copy[i]
            for j in range(i, insertion_point, -1):
                copy[j] = copy[j-1]
            copy[insertion_point] = to_insert
    return copy

def merge_sort(copy, comp_func):
    pass


if __name__ == '__main__':
    copy = deepcopy(base)
    print(bubble_sort(copy, acending))

    copy = deepcopy(base)
    print(selection_sort(copy, acending))

    copy = deepcopy(base)
    print(insertion_sort(copy, decending))
    
    print("Original: ", base)