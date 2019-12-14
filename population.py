import csv
import matplotlib.pyplot as plt

file = open('201911_201911_인구변화.csv', 'r', encoding='CP949')
data = csv.reader(file, delimiter=',')
print(data)



male_population = []
female_population = []

for row in data:
    if '신림동' in row[0]:
        for population in row[3:24]:
            male_population.append(int(population.replace(',','')))

        for population in row[26:47]:
            female_population.append(int(population.replace(',','')))


# print(len(male_population))
# print(male_population)
# print(len(female_population))
# print(female_population)

#꺽은선 그래프
# x = [str(i * 5) for i in range(len(male_population))]
# plt.title('population')
# plt.plot(male_population)
# #xticks(x 눈금, x눈금 라벨)
# plt.xticks([i for i in range(len(male_population))], x)
# help(plt.xticks())
# plt.show()

#막대 ㄱ래프
# x = [str(i * 5) for i in range(len(male_population))]
# print(x)
# print(male_population)
# plt.title('population')
# plt.bar(range(len(male_population)), male_population)
# #xticks(x 눈금, x눈금 라벨)
# plt.xticks([i for i in range(len(male_population))], x)
#
# plt.show()

#bash 그래프
plt.title('population')
reverse_female = []
for female in female_population:
    print(-female)
    reverse_female.append(-female)
#barsh(y좌표, x데이터)
plt.barh([str(i * 5) for i in range(len((male_population)))], male_population, label='male')
plt.barh([str(i * 5) for i in range(len((female_population)))], reverse_female, label='female')

plt.legend()
plt.show()

#xticks(x 눈금, x눈금 라벨)
# plt.xticks([i for i in range(len(male_population))], x)

