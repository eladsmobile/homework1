
import pandas


def load_data(path, features):
    """
    loads data from source
    :param path:
    :param features:
    :return:
    """
    df = pandas.read_csv(path)
    data = df.to_dict(orient="list")
    my_data = {}
    for feat in features.split(", "):
        my_data[feat] = data[feat]
    return my_data


def filter_by_feature(data, feature, values):
    """
    filters data
    :param data:
    :param feature:
    :param values:
    :return: two dictionarie- the first with the filter stated and the second without
    """
    data1 = {}
    data2 = {}
    for feat in data.keys():
        data1[feat] = []
        data2[feat] = []
        for i in range(0, len(data[feat])):
            if data[feature][i] in values:
                data1[feat].append(data[feat][i])
            else:
                data2[feat].append(data[feat][i])
    return data1, data2


def print_details(data, features, statistic_functions):
    """
    prints statistical data on the features listed
    :param data:
    :param features:
    :param statistic_functions:
    :return:
    """
    for feat in features:
        a = []
        for func in statistic_functions:
            a.append(func(data[feat]))
        print(feat + ": " + ", ".join(str(i) for i in a))