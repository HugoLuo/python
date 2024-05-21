import csv

def func_csv():
    fcsv = open("file_csv.csv","r")
    fr = csv.reader(fcsv)
    for row in fr:
        print(row)
    fcsv.close()

func_csv()