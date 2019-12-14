import csv

file = open('extremum_20191213095238.csv', 'r', encoding='CP949')
data = csv.reader(file, delimiter=',')
next(data)
# next(data)

max_temps = []
min_temps = []

max_temp = -999.0
max_temp_date = ''

min_temp = 999.0
min_temp_date = ''

for row in data:
    if row[4] == '' or row[6] == '':
        continue

    print(row)
    if float(max_temp) < float(row[4]):
        max_temp = row[4]
        max_temp_date = row[2]

    if float(min_temp) > float(row[6]):
        min_temp = row[6]
        min_temp_date = row[2]

    max_temps.append(row[4])
    min_temps.append(row[6])

print("{} 때 최고기온 {} 입니다.".format(max_temp_date, max_temp))
print("{} 때 최저기온 {} 입니다.".format(min_temp_date, min_temp))

print(max_temps)
print(min_temps)


file.close()

import matplotlib.pyplot as plt

# plt.rc('font', family='Gulim')
# plt.title("graph title")
# plt.plot([10,20,30,40], [1,20,3,4])
# plt.show()

# plt.title("graph title")
# plt.plot([10,20,30,40], linestyle='--', label='data1')
# plt.plot([40,30,20,10], linestyle=':', label='data2')
# plt.show()

# plt.title('Seoul weather graph')
# plt.plot(max_temps, 'r', label='max tempiture')
# plt.plot(min_temps, 'b', label='min tempiture')
# plt.legend()
# plt.show()

# plt.hist(min_temps, bins=100)
# plt.show()

