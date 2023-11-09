# Is the string uppercase?

# Task

# Create a method to see whether the string is ALL CAPS.

# Examples (input -> output)

# "c" -> False
# "C" -> True
# "hello I AM DONALD" -> False
# "HELLO I AM DONALD" -> True
# "ACSKLDFJSgSKLDFJSKLDFJ" -> False
# "ACSKLDFJSGSKLDFJSKLDFJ" -> True
# In this Kata, a string is said to be in ALL CAPS whenever it does not contain any lowercase letter so any string containing no letters at all is trivially considered to be in ALL CAPS.



def is_uppercase(inp):
    truth_list = []
    for i in inp.strip():
        if not i.isalpha():
            truth_list.append(1)
        elif i.isupper():
            truth_list.append(1)
        else:
            truth_list.append(0)
    if sum(truth_list) != len(inp.strip()):
        return False
    else:
        return True
    

# way shorter:
    return inp.upper() == inp