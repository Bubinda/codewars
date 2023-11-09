# Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

# Examples

# pig_it('Pig latin is cool') # igPay atinlay siay oolcay
# pig_it('Hello world !')     # elloHay orldway !


def pig_it(text):
    pig_list = []
  
    for i in text.split():
        if i.isalpha():
            pig_list.append(i[1:]+i[0]+'ay')
        else:
            pig_list.append(i)
    return ' '.join(pig_list)
    


# more pythonic

def pig_it(text):
  return ' '.join(i[1:]+i[0]+'ay' if i.isalpha() else i for i in text.split())