import numpy as np
import matplotlib.pyplot as plt

path = r'C:\Users\Bartek\PycharmProjects\GdanskPopulation\data.csv'
data = np.genfromtxt(path, delimiter=',')

year = data[0]
population = data[1]
women = data[2]
men = data[3]
plt.title('Gdansk population in years 2000-2019')
plt.xlabel('Year')
plt.ylabel('Population')

def general_plot():
    plt.xticks(year[::2])
    y = np.arange(200000, 500000, 10000)
    plt.yticks(y)
    plt.plot(year, population, '.-', color = 'green', label = 'population')
    plt.plot(year, women, '.-', color = 'pink', label = 'women')
    plt.plot(year, men, '.-', color = 'blue', label = 'men')
    plt.grid(linestyle = '--', linewidth = '0.2')
    plt.legend()
    plt.show()

def stairs_plot():
    plt.xticks(year[::2])
    plt.step(year, population , label='population')
    plt.plot(year, population, 'o--', color='grey', alpha=0.3)
    plt.grid(axis='x', color='0.95')
    plt.legend()
    plt.show()

def women_men_plot():
    plt.xticks(year[::2])
    plt.step(year, women, label='women')
    plt.plot(year, women, 'o--', color='red', alpha=0.3)

    plt.step(year, men, label='men')
    plt.plot(year, men, 'o--', color='blue', alpha=0.3)

    plt.grid(axis='x', color='0.95')
    plt.legend()
    plt.show()