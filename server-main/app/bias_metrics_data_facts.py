import numpy as np

def correlation(x, y):
    if len(x) != len(y):
        print("Both inputs must have the same length")
        return None
    else:
        return np.corrcoef(x, y)[0, 1]

def find_outliers(data, threshold=3):
    mean = np.mean(data)
    std = np.std(data)
    outliers = []
    for x in data:
        z = (x - mean) / std
        if abs(z) > threshold:
            outliers.append(x)
    return outliers


def extreme_values(data):
    min_val = min(data)
    max_val = max(data)
    return min_val, max_val

def relative_values(data,value):
    relative_data = []
    for val in data:
        relative_val = val/value
        relative_data.append(relative_val)
    return relative_data


def derived_values(data, operation):
    derived_data = []
    if operation == "log":
        for val in data:
            derived_val = np.log(val)
            derived_data.append(derived_val)
    elif operation == "sqrt":
        for val in data:
            derived_val = np.sqrt(val)
            derived_data.append(derived_val)
    else:
        return "Invalid operation"
    return derived_data


def category_correlation(data1, data2):
    unique_categories = list(set(data1) | set(data2))
    category_correlation = {}
    for category in unique_categories:
        category_correlation[category] = {"data1_count": data1.count(category), "data2_count": data2.count(category)}
    return category_correlation


from collections import defaultdict

def quadrant_distribution(data, x_axis, y_axis):
    """
    Calculates the quadrant distribution of data points in a scatter plot.
    :param data: list of dictionaries, where each dictionary represents a data point and has keys for x_axis and y_axis
    :param x_axis: string, name of the key in the dictionaries representing the x-axis
    :param y_axis: string, name of the key in the dictionaries representing the y-axis
    :return: dictionary, where keys are the quadrant labels (NW, NE, SW, SE) and values are the number of data points in each quadrant
    """
    quadrants = defaultdict(int)
    for point in data:
        x = point[x_axis]
        y = point[y_axis]
        if x > 0 and y > 0:
            quadrants["NE"] += 1
        elif x < 0 and y > 0:
            quadrants["NW"] += 1
        elif x < 0 and y < 0:
            quadrants["SW"] += 1
        elif x > 0 and y < 0:
            quadrants["SE"] += 1
    return dict(quadrants)


def range_distribution(bias_metric_data):
    min_val = min(bias_metric_data)
    max_val = max(bias_metric_data)
    range_val = max_val - min_val
    range_distribution = {}
    for data in bias_metric_data:
        range_distribution[data] = (data - min_val) / range_val
    return range_distribution



# x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 100]
# y = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
# print(correlation(x, y))
# print(find_outliers(x))
