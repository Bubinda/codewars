# ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet. ROT13 is an example of the Caesar cipher.

# Create a function that takes a string and returns the string ciphered with Rot13. If there are numbers or special characters included in the string, they should be returned as they are. Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".

# Please note that using encode is considered cheating.


def rot13(message):
    alphabet = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
    encoded = ''
    for i in message:
        if not i.isalpha():
            encoded += (i)
        else:
            encoded += (alphabet[alphabet.index(i)+13])
    return encoded

print(rot13('aA bB zZ 1234 *!?%'))


# alternatvie

    # encoded = ''
    # for char in message:
    #     if char.isalpha():
    #         if char.islower():
    #             encoded += chr((ord(char) - ord('a') + 13) % 26 + ord('a'))
    #         else:
    #             encoded += chr((ord(char) - ord('A') + 13) % 26 + ord('A'))
    #     else:
    #         encoded += char
    # return encoded

# also another solution

    # return message.translate(message.maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz','NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'))
