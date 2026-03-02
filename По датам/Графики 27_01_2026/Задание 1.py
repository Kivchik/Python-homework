import matplotlib.pyplot as plt

months = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"] # В легенду
temperature = [11, 7, 14, 14, 19, 23, 28, 29, 24, 19, 18, 11] # Ось Y

plt.plot(months, temperature, color="red", marker="o", markerfacecolor="blue", markersize=10)
plt.ylabel("Температура С°")
plt.xlabel("Месяц")
plt.title("График температуры в Сочи за 2025 год")

plt.show()