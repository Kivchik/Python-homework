import matplotlib.pyplot as plt

days = ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс']
steps = [7542, 10234, 8901, 11209, 5601, 14200, 8321]
sizes = [stps/100 for stps in steps]

plot = plt.plot(days, steps, label='Динамика кол-ва шагов')
plt.scatter(days, steps, s=sizes, label='Кол-во шагов')
ax = plt.axhline(y=10000, color='red', linestyle='--')
ax.set_label('Цель.')
plt.legend()

plt.show()