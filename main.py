import time
start_time = time.time()
import pandas as pd
import csv
with open('t8.shakespeare.txt','r+') as shakesFile:
    reData = shakesFile.read().lower()
    paraData = reData.split(" ")
    with open('find_words.txt',) as d:
        findWord = d.read().split()
        data = pd.read_csv('french_dictionary.csv',header=None)
    # print(list(data[0]).index("about"))
with open('result.csv','w',newline='') as writeFile:
    wf = csv.writer(writeFile)
    for x in findWord:
        if x in paraData:
            reData = reData.replace(x,list(data[1])[list(data[0]).index(x)])
            wf.writerow([x,list(data[1])[list(data[0]).index(x)], reData.count( list(data[1])[list(data[0]).index(x)] ) ])
 
with open(r't8.shakespeare.txt','w') as wr:
    wr.write(reData)
print("--- %s seconds ---" % (time.time() - start_time))