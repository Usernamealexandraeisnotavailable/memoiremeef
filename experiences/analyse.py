import csv
import statistics
import scipy
import math
data = []
previous_x = None
previous_y = None
z = 0
file = "tests/gemma3"
with open(f'{file}.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile, delimiter=';', quotechar='"')
    rows = list(reader)
    for i_row in range(3, len(rows)):
        row = rows[i_row]
        x = int(row[0])
        y = int(row[1])
        value = float(row[-1].replace(',', '.'))
        if z%31 == 0 :
            z = 0
        while len(data) <= x:
            data.append([])
        while len(data[x]) <= z:
            data[x].append([])
        while len(data[x][z]) <= y:
            data[x][z].append(None)
        data[x][z][y] = value
        z += 1
data_avg = []
data_len = []
for numetu in range(len(data)):
    avg_row = []
    len_row = []
    for numllm in range(len(data[numetu])):
        values = data[numetu][numllm]
        avg_row.append(statistics.mean(values))
        # len_row.append(len(values))
    data_avg.append(avg_row)
    data_len.append(len(data[numetu]))
stdvals = []
pvalues = []
avg_redim = []
print(f"\"Modèle :\";\"{file}\"")
for i in range(len(data_avg)) :
    if scipy.stats.chi.cdf(math.sqrt(30)*statistics.stdev(data_avg[i])/11,30) != 0 :
        stdvals += [statistics.stdev(data_avg[i])]
        pvalues += [scipy.stats.chi.cdf(math.sqrt(30)*statistics.stdev(data_avg[i])/11,30),0.05]
        avg_redim += data_avg[i]
print("moyenne",statistics.mean(avg_redim))
print("stdev",statistics.stdev(avg_redim))
print("len",len(avg_redim))
print([math.log(p,0.05) for p in pvalues])
print(math.log(statistics.harmonic_mean(pvalues),0.05))
print((statistics.mean(avg_redim)-50)/(statistics.stdev(avg_redim)/math.sqrt(len(avg_redim))))
print("log0.05(p)",math.log(scipy.stats.norm.cdf(((statistics.mean(avg_redim)-50)/(statistics.stdev(avg_redim)/math.sqrt(len(avg_redim))))),0.05))
"""for i in range(len(pvalues)) :
    print(f"Élève {i+1};{statistics.mean(data_avg[i])};{str(stdvals[i]).replace('.',',')};{str(math.log(pvalues[i],0.05)).replace('.',',')}")
print(f"{str(math.log(statistics.harmonic_mean(pvalues),0.05).replace('.',',')}")"""
