# In a factory a printer prints labels for boxes. The printer uses colors which, for the sake of simplicity, are named with letters from a to z (except letters u, w, x or z that are for errors).

# The colors used by the printer are recorded in a control string. For example a control string would be aaabbbbhaijjjm meaning that the printer used three times color a, four times color b, one time color h then one time color a... and so on.

# Sometimes there are problems: lack of colors, technical malfunction and a control string is produced e.g. uuaaaxbbbbyyhwawiwjjjwwxym where errors are reported with letters u, w, x or z.

# You have to write a function hist which given a string will output the errors as a string representing a histogram of the encountered errors.

# Format of the output string:

# letter (error letters are sorted in alphabetical order) in a field of 2 characters, a white space, number of error for that letter in a field of 6, as many "*" as the number of errors for that letter and "\r" (or "\n" depending on the langauge).

# The string has a length greater or equal to one and contains only letters from a to z.

# Examples

# s="uuaaaxbbbbyyhwawiwjjjwwxym"
# hist(s) => "u  2     **\rw  5     *****\rx  2     **"
# or with dots to see white spaces:

# hist(s) => "u..2.....**\rw..5.....*****\rx..2.....**"
# s="uuaaaxbbbbyyhwawiwjjjwwxymzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz"
# hist(s) => "u..2.....**\rw..5.....*****\rx..2.....**\rz..31....*******************************"
# Notes

# Unfortunately most often Codewars compresses all white spaces into one.
# See other examples in the "Sample tests".


def hist(s):
    errors = 'uwxz'
    output = ''
    error_dict = {i: s.count(i) for i in sorted(s) if i in errors}
    for i in error_dict:
        count_star = '*' * error_dict[i]
        space = ' ' * (6 - len(str(error_dict[i])))
        output += f'{i}  {error_dict[i]}{space}{count_star}\r'
    return output.rstrip('\r')


print(hist("uuaaaxbbbbyyhwawiwjjjwwxym"))


# other solution

# from collections import Counter

# ERRORS = 'uwxz'

# def hist(s):
#     cnts = Counter(s)
#     return '\r'.join(f'{c}  {cnts[c]: <6}{"*"*cnts[c]}' for c in ERRORS if cnts[c])