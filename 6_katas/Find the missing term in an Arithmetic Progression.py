# An Arithmetic Progression is defined as one in which there is a constant difference between the consecutive terms of a given series of numbers. You are provided with consecutive elements of an Arithmetic Progression. There is however one hitch: exactly one term from the original series is missing from the set of numbers which have been given to you. The rest of the given series is the same as the original AP. Find the missing term.

# You have to write a function that receives a list, list size will always be at least 3 numbers. The missing term will never be the first or last one.

# Example

# find_missing([1, 3, 5, 9, 11]) == 7
# PS: This is a sample question of the facebook engineer challenge on interviewstreet. I found it quite fun to solve on paper using math, derive the algo that way. Have fun!


def find_missing(sequence):
    n = len(sequence)
    difference = (sequence[n - 1] - sequence[0]) // n
    low = 0
    high = n - 1
    while low < high:
        mid = low + high // 2

        if sequence[mid + 1] - sequence[mid] != difference:
            return sequence[mid] + difference

        if mid > 0 and sequence[mid] - sequence[mid - 1] != difference:
            return sequence[mid - 1] + difference

        if sequence[mid] == sequence[0] + mid * difference:
            low = mid + 1

        else:
            high = mid - 1


#takes too much time but works
def find_missing(sequence):
    return [i for i in [i for i in range(sequence[0],sequence[-1],(sequence[len(sequence) - 1] - sequence[0]) // len(sequence))] if i not in sequence][0]
 