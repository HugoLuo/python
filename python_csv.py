import csv

def func_csv_read():
    fcsv = open("file_csv.csv","r")
    fr = csv.reader(fcsv)
    for row in fr:
        print(row)
    fcsv.close()

# func_csv_read()

def func_csv_write():
    headers = ['Symbol','Price','Date','Time','Change','Volume']
    rows = [('AA',1.23,'3/23/2023','9:30am',-0.18,181000),
            ('AIG',2.16,'7/24/2023','5:30pm',-1.223,2332)]
    fcsv = open("file_csv1.csv","w+")
    fw = csv.writer(fcsv)
    fw.writerow(headers)
    for i in range(len(rows)):
        fw.writerow(rows[i])
    print("Writing is done")
    fcsv.close()

func_csv_write()
