import csv
import statistics
import math
from scipy import stats

file = "mistralFULL"
num_students = 31

apriori = []
with open(f'{file}.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile, delimiter=';', quotechar='"')
    rows = list(reader)
    for i in range(3, len(rows)):
        key = rows[i][1] + ' ; "' + rows[i][3] + '"'
        if key not in apriori:
            apriori.append(key)

total = [[[] for _ in range(len(apriori))] for __ in range(num_students)]

with open(f'{file}.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile, delimiter=';', quotechar='"')
    rows = list(reader)
    for i in range(3, len(rows)):
        student_idx = int(rows[i][0])
        inference_key = rows[i][1] + ' ; "' + rows[i][3] + '"'
        inference_idx = apriori.index(inference_key)
        try:
            score = float(rows[i][4].replace(',', '.'))
            total[student_idx][inference_idx].append(score)
        except ValueError:
            pass  # Skip bad data

student_avg = [[
    statistics.mean(total[student][inference]) if total[student][inference] else 0.0
    for inference in range(len(apriori))
] for student in range(num_students)]

inference_averages = []
inference_counts = []
inference_conf_intervals = []

for j in range(len(apriori)):
    scores = [student_avg[i][j] for i in range(num_students)]
    n = len(scores)
    mean_val = statistics.mean(scores)
    if n > 1:
        sem = stats.sem(scores)
        ci_range = stats.t.ppf(0.975, df=n - 1) * sem
    else:
        ci_range = 0.0
    inference_averages.append(mean_val)
    inference_counts.append(n)
    inference_conf_intervals.append(ci_range)

for idx, key in enumerate(apriori):
    print(f"Inference: {key}")
    print(f"  - Average across students: {inference_averages[idx]:.2f}")
    print(f"  - Students counted: {inference_counts[idx]}")
    print(f"  - 95% CI: ±{inference_conf_intervals[idx]:.2f}")
