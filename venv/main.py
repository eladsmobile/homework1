import sys

import data
import statistics


def main(argv):
    """
    main function
    """
    #retrieve data from file
    my_data = data.load_data(argv[1], argv[2])

    #Question 1
    statistic_functions = [statistics.sum,statistics.mean, statistics.median]
    attr = ['hum','t1','cnt']
    print("Question 1:\nSummer:")
    crnt_data, _ = data.filter_by_feature(my_data, 'season', [1])
    data.print_details(crnt_data, attr, statistic_functions)
    print("Holiday:")
    crnt_data, _ = data.filter_by_feature(my_data, 'is_holiday', [1])
    data.print_details(crnt_data, attr, statistic_functions)
    print("All:")
    data.print_details(my_data, attr, statistic_functions)
    print("")

    #Question 2
    statistic_functions = [statistics.mean, statistics.median]
    my_data1, _ = data.filter_by_feature(my_data, 'season', [3])
    print("Question 2:\nIf t1<=13.0, then:")
    crnt_data, _ = data.filter_by_feature(my_data1, 'is_holiday', [1])
    statistics.population_statistics("Winter holiday records", crnt_data, 't1', 'cnt', 13, 0, statistic_functions)
    crnt_data, _ = data.filter_by_feature(my_data1, 'is_holiday', [0])
    statistics.population_statistics("Winter weekday records", crnt_data, 't1', 'cnt', 13, 0, statistic_functions)
    print("If t1>13.0, then:")
    crnt_data, _ = data.filter_by_feature(my_data1, 'is_holiday', [1])
    statistics.population_statistics("Winter holiday records", crnt_data, 't1', 'cnt', 13, 1, statistic_functions)
    crnt_data, _ = data.filter_by_feature(my_data1, 'is_holiday', [0])
    statistics.population_statistics("Winter weekday records", crnt_data, 't1', 'cnt', 13, 1, statistic_functions)

if __name__ == '__main__':
    main(sys.argv)
