# Let there be k different types of weather, where we denote each type of weather by a positive integer. For example, sunny = 0, rainy = 1, ..., cloudy = k.

# Task

# Find the probability of having weather j in n days from now given weather i today and conditional on some daily weather transition probabilities, a k*k matrix, where i and j are integers less than or equal to k.

# Example

# There are two types of weather 0 and 1. Transition probabilities:

# [[0.6, 0.4],
#  [0.3, 0.7]]
# The probability of weather 0 tomorrow if weather 0 today: 60%
# The probability of weather 1 tomorrow if weather 0 today: 40%
# The probability of weather 0 tomorrow if weather 1 today: 30%
# The probability of weather 1 tomorrow if weather 1 today: 70%
# The probability of weather 0 two days from now if we start in weather 0 becomes: 60% * 60% + 40% * 30% = 48%. Because either we stay in 0 for two days or we go from 0 to 1 and then from 1 to 0.

# Note

# We will have k ≤ 10 and n ≤ 50.

# We will have k ≤ 10 and n ≤ 50.

import numpy as np

def weather_prediction(days, weather_today, final_weather, transition_matrix):
    transition_matrix = np.array(transition_matrix)
    transition_matrix_power = np.linalg.matrix_power(transition_matrix, days)
    return transition_matrix_power[weather_today][final_weather]

print(weather_prediction(2, 0, 0,[[0.6, 0.4],[0.3, 0.7]]))



# To calculate the probability of having weather j in n days from now given weather i today, we can raise the transition matrix to the power of n and look at the (i, j) entry of the resulting matrix. This entry represents the probability of transitioning from weather i to weather j in n days.
# In this implementation, n represents the number of days in the future, i represents the current weather type, j represents the desired weather type, and transition_matrix is a 2D array representing the transition probabilities.