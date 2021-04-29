import csv
import sys

# import pandas doesnt work , does an error no moudle something



def main(argv):
    argv[0] = r'/home/student/C:\Users\elad\PycharmProjects\homework1\venv\main.py'
    #argv[1] = r'/home/student/C:\Users\elad\PycharmProjects\homework1\venv\london.csv' # error argv not definde / out of index
    #argv[2] = "hum, t1, cnt, season, is_holiday "
    # filename = r'C:\Users\elad\PycharmProjects\homework1\venv\london_sample.csv' #sample
    filename = r'C:\Users\elad\PycharmProjects\homework1\venv\london.csv'
    count1 = 0
    sumcnt = 0
    listcnt = []
    sumt1 = 0
    listt1 = []
    sumhum = 0
    listhum = []

    listt1 = []
    with open(filename) as csvfile:
        table = csv.reader(csvfile)
        next(table)
        for line in table:
            if (int(line[9]) == 1):
                # if(int(line[7])==1):
                count1 += 1
                sumcnt += float(line[1])
                listcnt.append(float(line[1]))
                sumt1 += float(line[2])
                listt1.append(float(line[2]))
                sumhum += float(line[4])
                listhum.append(float(line[4]))

        print("Question 1:")
        print("Summer:")
        temp1 = int((count1 / 2) + 0.5)
        listhum.sort()
        if (count1 % 2 == 1):
            mid = listhum[temp1 - 1]
        else:
            mid = (listhum[int(count1 / 2) - 1] + listhum[int(count1 / 2)]) / 2
        print("hum: " + str(sumhum) + ", " + str(sumhum / count1) + ", " + str(mid))
        listt1.sort()
        if (count1 % 2 == 1):
            mid = listt1[temp1 - 1]
        else:
            mid = (listt1[int(count1 / 2 - 1)] + listt1[int(count1 / 2)]) / 2
        print("t1: " + str(sumt1) + ", " + str(sumt1 / count1) + ", " + str(mid))
        listcnt.sort()
        if (count1 % 2 == 1):
            mid = listcnt[temp1 - 1]
        else:
            mid = (listcnt[int(count1 / 2 - 1)] + listcnt[int(count1 / 2)]) / 2
        print("cnt: " + str(sumcnt) + ", " + str(sumcnt / count1) + ", " + str(mid))
    count1 = 0
    sumcnt = 0
    listcnt = []
    sumt1 = 0
    listt1 = []
    sumhum = 0
    listhum = []

    listt1 = []
    with open(filename) as csvfile:
        table = csv.reader(csvfile)
        next(table)
        for line in table:
            if (int(line[7]) == 1):
                count1 += 1
                sumcnt += float(line[1])
                listcnt.append(float(line[1]))
                sumt1 += float(line[2])
                listt1.append(float(line[2]))
                sumhum += float(line[4])
                listhum.append(float(line[4]))
        print("holiday:")
        temp1 = int((count1 / 2) + 0.5)
        listhum.sort()
        if (count1 % 2 == 1):
            mid = listhum[temp1 - 1]
        else:
            mid = (listhum[int(count1 / 2)] + listhum[int(count1 / 2) - 1]) / 2
        print("hum: " + str(sumhum) + ", " + str(sumhum / count1) + ", " + str(mid))
        listt1.sort()
        if (count1 % 2 == 1):
            mid = listt1[temp1 - 1]
        else:
            mid = (listt1[int(count1 / 2)] + listt1[int(count1 / 2 - 1)]) / 2
        print("t1: " + str(sumt1) + ", " + str(sumt1 / count1) + ", " + str(mid))
        listcnt.sort()
        if (count1 % 2 == 1):
            mid = listcnt[temp1 - 1]
        else:
            mid = (listcnt[int(count1 / 2)] + listcnt[int(count1 / 2 - 1)]) / 2
        print("cnt: " + str(sumcnt) + ", " + str(sumcnt / count1) + ", " + str(mid))
    count1 = 0
    sumcnt = 0
    listcnt = []
    sumt1 = 0
    listt1 = []
    sumhum = 0
    listhum = []
    listt1 = []
    with open(filename) as csvfile:
        table = csv.reader(csvfile)
        next(table)
        for line in table:
            if (1 == 1):
                count1 += 1
                sumcnt += float(line[1])
                listcnt.append(float(line[1]))
                sumt1 += float(line[2])
                listt1.append(float(line[2]))
                sumhum += float(line[4])
                listhum.append(float(line[4]))
        print("all:")
        temp1 = int((count1 / 2) + 0.5)
        listhum.sort()
        if (count1 % 2 == 1):
            mid = listhum[temp1 - 1]
        else:
            mid = (listhum[int(count1 / 2)] + listhum[int(count1 / 2) - 1]) / 2
        print("hum: " + str(sumhum) + ", " + str(sumhum / count1) + ", " + str(mid))
        listt1.sort()
        if (count1 % 2 == 1):
            mid = listt1[temp1 - 1]
        else:
            mid = (listt1[int(count1 / 2)] + listt1[int(count1 / 2 - 1)]) / 2
        print("t1: " + str(sumt1) + ", " + str(sumt1 / count1) + ", " + str(mid))
        listcnt.sort()
        if (count1 % 2 == 1):
            mid = listcnt[temp1 - 1]
        else:
            mid = (listcnt[int(count1 / 2)] + listcnt[int(count1 / 2 - 1)]) / 2
        print("cnt: " + str(sumcnt) + ", " + str(sumcnt / count1) + ", " + str(mid))

    # question1 over , start of question2 !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    sumholilow = 0
    listholilow = []
    sumweeklow = 0
    listweeklow = []
    sumholihigh = 0
    listholihigh = []
    sumweekhigh = 0
    listweekhigh = []
    with open(filename) as csvfile:
        table = csv.reader(csvfile)
        next(table)
        for line in table:
            if (int(line[9]) == 3):  # winter
                if (int(line[7]) == 1):  # is holiday
                    if (float(line[2]) <= 13):  # temp below 13
                        sumholilow += float(line[1])
                        listholilow.append(float(line[1]))
                    else:  # than temp is above 13
                        sumholihigh += float(line[1])
                        listholihigh.append(float(line[1]))
                else:
                    if (float(line[2]) <= 13):  # temp below 13
                        sumweeklow += float(line[1])
                        listweeklow.append(float(line[1]))
                    else:  # than temp is above 13
                        sumweekhigh += float(line[1])
                        listweekhigh.append(float(line[1]))
    print("Question 2:")
    print("If t1<=13.0, then:")
    print("Winter holiday records:")
    count1 = listholilow.__len__()
    temp1 = int((count1 / 2) + 0.5)
    listholilow.sort()
    if (count1 % 2 == 1):
        mid = listholilow[temp1 - 1]
    else:
        mid = (listholilow[int(count1 / 2) - 1] + listholilow[int(count1 / 2)]) / 2
    print("cnt: " + str(sumholilow / count1) + ", " + str(mid))
    print("Winter  weekday records:")
    count1 = listweeklow.__len__()
    temp1 = int((count1 / 2) + 0.5)
    listweeklow.sort()
    if (count1 % 2 == 1):
        mid = listweeklow[temp1 - 1]
    else:
        mid = (listweeklow[int(count1 / 2) - 1] + listweeklow[int(count1 / 2)]) / 2
    print("cnt: " + str(sumweeklow / count1) + ", " + str(mid))
    print("If t1<=13.0, then:")
    print("Winter holiday records:")
    count1 = listholihigh.__len__()
    temp1 = int((count1 / 2) + 0.5)
    listholihigh.sort()
    if (count1 % 2 == 1):
        mid = listholihigh[temp1 - 1]
    else:
        mid = (listholihigh[int(count1 / 2) - 1] + listholihigh[int(count1 / 2)]) / 2
    print("cnt: " + str(sumholihigh / count1) + ", " + str(mid))
    print("Winter  weekday records:")
    count1 = listweekhigh.__len__()
    temp1 = int((count1 / 2) + 0.5)
    listweekhigh.sort()
    if (count1 % 2 == 1):
        mid = listweekhigh[temp1 - 1]
    else:
        mid = (listweekhigh[int(count1 / 2) - 1] + listweekhigh[int(count1 / 2)]) / 2
    print("cnt: " + str(sumweekhigh / count1) + ", " + str(mid))
if __name__=='__main__':
    main(sys.argv)