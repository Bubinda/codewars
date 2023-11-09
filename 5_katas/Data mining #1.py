# Your task is to build a model1 which can predict y-coordinate.
# You can pass tests if predicted y-coordinates are inside error margin.


# You will receive train set which should be used to build a model. 
# After you build a model tests will call function predict and pass x to it. 


# Error is going to be calculated with RMSE.




# Blocked libraries: sklearn, pandas, tensorflow, numpy, scipy 

# Explanation
# [1] A mining model is created by applying an algorithm to data, but it is more than an algorithm or a metadata container: it is a set of data, statistics, and patterns that can be applied to new data to generate predictions and make inferences about relationships.

    
class Datamining:
    def __init__(self, train_data):
        self.b0 = 0
        self.b1 = 0
        self.fit(train_data)

    def fit(self, train_data):
        X = [i[0] for i in train_data]
        y = [i[1] for i in train_data]
        mean_x = sum(X) / len(X)
        mean_y = sum(y) / len(y)

        self.b1 = sum((xi - mean_x) * (yi - mean_y) for xi, yi in zip(X, y)) / sum((xi - mean_x) ** 2 for xi in X)
        self.b0 = mean_y - self.b1 * mean_x

    def predict(self, X):
        if isinstance(X, int):
            return self.b0 + self.b1 * X
        else:
            return [self.b0 + self.b1 * xi for xi in X]

    def rmse(self, y_true, y_pred):
        return (sum((yi - ypi) ** 2 for yi, ypi in zip(y_true, y_pred)) / len(y_true)) ** 0.5
   

example_train_set = [(0, 1),
    (2, 2),
    (4, 3),
    (9, 8),
    (3, 5)
]

lr = Datamining(example_train_set)
predicted = [lr.predict(point[0]) for point in example_train_set]
print(predicted)


#smaller model

from statistics import variance, mean

class Datamining:
    def __init__(self, train_set):
        # This is a simple linear regression model.
        # Notice we're computing the covariance but from Python 3.10
        # the statistics module includes a function for that.
        avg_x = mean(x for x, _ in train_set)
        avg_y = mean(y for _, y in train_set)
        cov = sum((x - avg_x) * (y - avg_y) for x, y in train_set) / (len(train_set) - 1)
        self.b1 = cov / variance(x for x, _ in train_set)
        self.b0 = avg_y - self.b1 * avg_x


    def predict(self, x):
        return self.b0 + self.b1 * x