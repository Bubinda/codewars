# Background:

# sample linear regression, curtesy of wikipedia

# A linear regression line has an equation in the form 
# Y
# =
# a
# +
# b
# X
# Y=a+bX, where 
# X
# X is the explanatory variable and 
# Y
# Y is the dependent variable. The parameter 
# b
# b represents the slope of the line, while 
# a
# a is called the intercept (the value of 
# y
# y when 
# x
# =
# 0
# x=0).

# For more details visit the related wikipedia page.

# Task:

# The function that you have to write accepts two list/array, 
# x
# x and 
# y
# y, representing the coordinates of the points to regress (so that, for example, the first point has coordinates (x[0], y[0])).

# Your function should return a tuple (in Python) or an array (any other language) of two elements: a (intercept) and b (slope) in this order.

# You must round your result to the first 4 decimal digits

# Formula:

# x
# i
# x 
# i
# ​	
#   and 
# y
# i
# y 
# i
# ​	
#   is 
# x
# x and 
# y
# y co-ordinate of 
# i
# i-th point;
# n
# n is length of input.

# a
# =
# ∑
# x
# i
# 2
# ⋅
# ∑
# y
# i
# −
# ∑
# x
# i
# ⋅
# ∑
# x
# i
# y
# i
# n
# ∑
# x
# i
# 2
# −
# (
# ∑
# x
# i
# )
# 2
# a= 
# n∑x 
# i
# 2
# ​	
#  −(∑x 
# i
# ​	
#  ) 
# 2
 
# ∑x 
# i
# 2
# ​	
#  ⋅∑y 
# i
# ​	
#  −∑x 
# i
# ​	
#  ⋅∑x 
# i
# ​	
#  y 
# i
# ​	
 
# ​	
 

# b
# =
# n
# ∑
# x
# i
# y
# i
# −
# ∑
# x
# i
# ⋅
# ∑
# y
# i
# n
# ∑
# x
# i
# 2
# −
# (
# ∑
# x
# i
# )
# 2
# b= 
# n∑x 
# i
# 2
# ​	
#  −(∑x 
# i
# ​	
#  ) 
# 2
 
# n∑x 
# i
# ​	
#  y 
# i
# ​	
#  −∑x 
# i
# ​	
#  ⋅∑y 
# i
# ​	
 
# ​	
 

# Examples:

# regressionLine([25,30,35,40,45,50], [78,70,65,58,48,42]) == (114.381, -1.4457)

# regressionLine([56,42,72,36,63,47,55,49,38,42,68,60], [147,125,160,118,149,128,150,145,115,140,152,155]) == (80.7777, 1.138)


def regressionLine(x, y):
    n = len(x)
    sum_x = sum(x)
    sum_y = sum(y)
    sum_x_squared = sum(xi ** 2 for xi in x)
    sum_xy = sum(xi * yi for xi, yi in zip(x, y))

    a = (sum_x_squared * sum_y - sum_x * sum_xy) / (n * sum_x_squared - sum_x ** 2)
    b = (n * sum_xy - sum_x * sum_y) / (n * sum_x_squared - sum_x ** 2)

    return round(a, 4), round(b, 4)


# way shorter:

import numpy as np

def regressionLine(x, y):
    """ Return the a (intercept)
        and b (slope) of Regression Line 
        (Y on X).
    """
    a,b = np.polyfit(x,y,1)
    return round(b,4),round(a,4)