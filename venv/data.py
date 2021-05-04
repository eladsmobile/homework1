
import pandas
class data1():
    def __init__(self, path):
        self.df = pandas.read_csv(path)
        self.data = self.df.to_dict(orient="list")

    def get_data(self):
        return self.data

    def get_all_districts(self):
        return self.data["denominazione_region"]

    def set_districts_data(self, districts):
        tempdata=self.get_all_districts()
        lendist = len(tempdata)
        removedd =[]
        indexx=0
        while (indexx <lendist):
            if tempdata[indexx] not in districts:
                print( "hi")
                removedd.append(indexx)
            indexx+=1
        self.df=self.df.drop(removedd)
        self.data = self.df.to_dict(orient="list")






def load_data( path):
    df = pandas.read_csv(path)
    self.data = df.to_dict(orient="list")
    return data

def get_all_districts(self):
    self.data

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