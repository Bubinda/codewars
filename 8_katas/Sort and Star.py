# You will be given a list of strings. You must sort it alphabetically (case-sensitive, and based on the ASCII values of the chars) and then return the first value.

# The returned value must be a string, and have "***" between each of its letters.

# You should not remove or add elements from/to the array.


def two_sort(array):
    return '***'.join([i for i in sorted(array)[0]])

print(two_sort(["bitcoin", "take", "over", "the", "world", "maybe", "who", "knows", "perhaps"]))
print(two_sort(["Lets", "all", "go", "on", "holiday", "somewhere", "very", "cold"]))


#shorter

    #return '***'.join(min(lst))