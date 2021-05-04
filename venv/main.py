import sys
import csv
import data as dataimport
import statistics
import pandas


if __name__ == '__main__':
    path ="./dpc-covid19-ita-regioni_sample.csv" # help arg[1]= path doesnt work
     #  > or >= in lines 88 , 96 , 102 not sure!!!!




    tempdata = dataimport.data1(path)
    data =tempdata.get_data()
    #print(tempdata.get_all_districts()) # no need to useany where to my knowldege

    #tempdata.set_districts_data(["Sardegna"])
    #print(tempdata.get_all_districts())
    districts_in_D=[]
    len_data = len(data["region_code"]) # doesnt matter what coloum
    indexx=0
    while (indexx< len_data):
        tempchar=data["denominazione_region"][indexx][0] # fisrt letter of the district
        tempcode=data["region_code"][indexx]
        if (tempchar=='S' ):
            if (tempcode in districts_in_D): # no duplacites
                pass
            else:
                districts_in_D.append(tempcode)
        if (tempchar=='L' ):
            if (tempcode in districts_in_D):
                pass
            else:
                districts_in_D.append(tempcode)
        indexx+=1
    hospitalized_with_symptoms=[]
    intensive_care=[]
    total_hospitalized=[]
    home_insulation=[]
    indexx=0
    while (indexx< len_data): # build sub lists od needs values
        tempcode=data["region_code"][indexx]
        if (tempcode in districts_in_D ):
            hospitalized_with_symptoms.append(data["hospitalized_with_symptoms"][indexx])
            intensive_care.append(data["intensive_care"][indexx])
            total_hospitalized.append(data["total_hospitalized"][indexx])
            home_insulation.append(data["home_insulation"][indexx])
        indexx+=1
    print("Question 1:")
    print("hospitalized_with_symptoms: " + str(statistics.mean(hospitalized_with_symptoms)) + ", " + str(round(statistics.median(hospitalized_with_symptoms))))
    print("intensive_care: " + str(statistics.mean(intensive_care)) + ", " + str(round(statistics.median(intensive_care))))
    print("total_hospitalized: " + str(statistics.mean(total_hospitalized)) + ", " + str(round(statistics.median(total_hospitalized))))
    print("home_insulation: " + str(statistics.mean(home_insulation)) + ", " + str(round(statistics.median(home_insulation))))
    list_districts=[]
    indexx = 0
    while (indexx < len_data):
        tempcode = int(data["region_code"][indexx])
        if (tempcode in list_districts):  # no duplacites
            pass
        else:
            list_districts.append(tempcode)
        indexx+=1
    num_district= len(list_districts)
    greed_days=[]
    indexx=0
    while (indexx<num_district):
        indexx+=1
        greed_days.append(0)
    list_districts.sort()
    code_inedxable = (1==list_districts[0])and(num_district==list_districts[num_district-1])  # are codes and in complete order , no jumps (empty cells ) can cuase a index error crash
    indexx = 0
    while (indexx < len_data):  # counts green days
        if(code_inedxable):
            tempcode=int(data["region_code"][indexx])
        else:
            tempcode = list_districts.index(int(data["region_code"][indexx]))
        if (data["resigned_healed"][indexx] - data["new_positives"][indexx] > 0):  # >( has 9 ) or >=( has 15) !!!!!!!!!!!!!!!
            try:
                greed_days[tempcode] += 1 # always use protection kiddos
            except:
                greed_days[tempcode] = 0
        indexx += 1
    count_green=0
    for X in greed_days:
        if X>=340: # > or >=
            count_green+=1
    print("")
    print("Question 2:")
    print("Number of districts: "+str(num_district))
    print("Number of not green districts: "+str(num_district-count_green))
    if (10<num_district-count_green): #  > or >=
        print("Will a lockdown be forced on whole of Italy?: Yes")
    else:
        print("Will a lockdown be forced on whole of Italy?: Yes")


