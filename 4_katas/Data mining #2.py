# Your task is to build a model1 which can predict y-coordinate.
# You can pass tests if predicted y-coordinates are inside error margin.


# You will receive train set which should be used to build a model. 
# After you build a model tests will call function predict and pass x to it. 


# Error is going to be calculated with RMSE. 


# Side note: Points in test cases are from different polynomials (up to 5th degree).




# Easier version: Data mining #1




# Blocked libraries: sklearn, pandas, tensorflow, numpy, scipy 

# Explanation
# [1] A mining model is created by applying an algorithm to data, but it is more than an algorithm or a metadata container: it is a set of data, statistics, and patterns that can be applied to new data to generate predictions and make inferences about relationships.


class Datamining:
    def __init__(self, train_set):
        self.train_set = train_set
        self.intercept = None
        self.slope = None
        self.rmse = None
        self.fit()

    def predict(self, x):
        # should return predicted y
        y_pred = self.intercept + self.slope * x
        return y_pred

    def calculate_rmse(self):
        # Calculate the root mean squared error (RMSE) between the predicted y-coordinates and the actual y-coordinates in the train set
        n = len(self.train_set)
        squared_errors = [(self.predict(x) - y) ** 2 for x, y in self.train_set]
        mean_squared_error = sum(squared_errors) / n
        rmse = mean_squared_error ** 0.5
        return rmse

    def fit(self):
        # Fit the linear regression model to the train set
        n = len(self.train_set)
        sum_x = sum(x for x, _ in self.train_set)
        sum_y = sum(y for _, y in self.train_set)
        sum_xy = sum(x * y for x, y in self.train_set)
        sum_x_squared = sum(x ** 2 for x, _ in self.train_set)

        self.slope = (n * sum_xy - sum_x * sum_y) / (n * sum_x_squared - sum_x ** 2)
        self.intercept = (sum_y - self.slope * sum_x) / n
        self.rmse = self.calculate_rmse()

# Example usage
train_set = [(1, -100000000), (4, 4), (2, 2), (3, 2), (5, 2)]
model = Datamining(train_set)
#model.fit()
print(model.predict(1))  # Output: 3.2

# does not work for larger datasets