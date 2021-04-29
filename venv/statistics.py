def median(list_of_values):
    sorted_list = sorted(list_of_values)
    center_index = int(len(list_of_values)/2) # round to int required because division always produces float

    # Median value depends on length on list
    if len(list_of_values)%2 == 0:
        result = (sorted_list[center_index] + sorted_list[center_index-1])/2
    else:
        # Now we need only 1 index for exact value
        result = sorted_list[center_index]
    #return round(result,2) # this is it?
    return result

def mean(list_of_values):
    return sum(list_of_values)/len(list_of_values)


def variance(list_of_values):
    average = mean(list_of_values)
    squared_sum = sum([(x - average)**2 for x in list_of_values])
    return squared_sum/(len(list_of_values)-1)

def covariance(first_list_of_values, second_list_of_values):
    meanfirst = mean(first_list_of_values)
    meansecond = mean(second_list_of_values)
    sum=0
    for i in range(0,len(first_list_of_values)):
        sum=sum+ (first_list_of_values[i]-meanfirst)*(second_list_of_values[i]-meansecond)
    return sum/(len(first_list_of_values)-1)

def standarddev(list_of_values):
    return variance(list_of_values)**0.5

def correlation(first_list_of_values, second_list_of_values):
    result = covariance(first_list_of_values, second_list_of_values) / (standarddev(first_list_of_values) * standarddev(second_list_of_values)) # google says this is the correct formula
    return result