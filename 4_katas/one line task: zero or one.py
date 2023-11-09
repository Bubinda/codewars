# You are given an odd integer n and a two-dimensional array s, which contains n equal-sized arrays of 0s and 1s.

# Return an array of the same length as the elements of n, such that its ith element is the one that appears most frequently at the ith position of s' elements.

# Code Limit

# Less than 55 characters.

# Example

# For n = 3, s = [[1,1,0], [1,0,0], [0,1,1]],

# the output should be [1,1,0]

# 1st  2nd  3rd
#  1    1    0
#  1    0    0
#  0    1    1
 

# At the 1st position 
# there're two 1s and one 0, 
# so in the 1st element of the resulting array is 1.

# At the 2nd position
# there're two 1s and one 0,
# so in the 2nd element of the resulting array is 1.

# At the 3rd position 
# there're two 0s and one 1, 
# so in the 3rd element of the resulting array is 0.


def zero_or_one(n,s):
    return [max(i, key=lambda x: i.count(x)) for i in zip(*s)]


zero_or_one_l = lambda n,s:[max(zip(*s)[i],key=sum)for i in range(n)]


# both too long for the required 55 chars