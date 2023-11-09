# Consider X as the aleatory variable that count the number of letters in a word. Write a function that, give in input an array of words (strings), calculate the variance of X. Max decimal of the variance : 4.

# Some wiki: Variance , Aleatory variable

# Example:

# Consider "Hello" and "World":

# X is { 5 } with P(X = 5) = 1 because the two words have the same length.
# So E[X] = 5 x 1 = 5 and the standard formula for variance is E[(X - u)^2] so 1 x (5-5)^2 = 0 or you can calculate with the other formula E[X^2] - E[X]^2 = 5^2 x 1 - 5^2 = 0

# Consider "Hi" and "World":

# X is { 2, 5 } with P(X = 5) = 1/2 and P(X = 2) = 1/2.
# So E[X] = 5 x 1/2 + 2 x 1/2 = 3.5 and the standard formula for variance is E[(X - u)^2] so 1/2 x (2-3.5)^2 + 1/2 x (5 - 3.5)^2 = 2.25 or you can calculate with the other formula E[X^2] - E[X]^2 = (5^2 x 1/2 + 2^2 x 1/2) - 3.5^2 = 2.25


def calculate_variance(words):
    # Calculate the mean (expected value) of X
    mean = sum(len(word) for word in words) / len(words)
    
    # Calculate E[X^2]
    mean_squared = sum(len(word) ** 2 for word in words) / len(words)
    
    # Calculate the variance using the formula: Var(X) = E[X^2] - E[X]^2
    variance = mean_squared - mean ** 2
    
    # Return the variance rounded to 4 decimal places
    return round(variance, 4)

# Test cases
words1 = ["Hello", "World"]
words2 = ["Hi", "World"]

print("Variance 1:", calculate_variance(words1))
print("Variance 2:", calculate_variance(words2))


#shorter version
# from statistics import pvariance

# def variance(words):
#     return round(pvariance(map(len, words)), 4)