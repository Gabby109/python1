Given a list containing integers,
floats and one character strings,
write a function that takes a list
and returns a dictionary with
keys evens, odds, and chars.
The value for evens is a list of
sorted even numbers, the value for
odds is a list of sorted odd numbers
and chars is a list of sorted character
strings.

list_sort([2,0,6,5,1,7,'z','a'])
# returns
{'evens': [0,2,6],
 'odds': [1,5,7],
 'chars':['a','z']
}

"""


def list_sort(jumbled_list):
    sorted_dict = {}
    evens = []
    odds = []
    characters = []

    for item in jumbled_list:
        if type(item) == int:
            # these are numbers
            if item % 2 == 0:
                # this is even
                evens.append(item)
            else:
                # this is odd
                odds.append(item)
        if type(item) == str:
            # these are characters
            characters.append(item)
        if type(item) == float:
            # these are floats, just skip them
            # continue
            odds.append(item)
    # end of for loop

    # now do the sorting
    sorted_evens = sorted(evens)
    sorted_odds = sorted(odds)
    sorted_chars = sorted(characters)

    sorted_dict = {
        'evens': sorted_evens,
        'odds': sorted_odds,
        'chars': sorted_chars
    }
    return sorted_dict

unsorted_list = [8.0,'f', 9.0,'o', 2, 76, 0, 'i', 44.7, 'x', 'e',0.9, 5, 33, 0,'g',3.1]
print("before sorting")
print(unsorted_list)
result = list_sort(unsorted_list)
print("after sorting")
print(result)
