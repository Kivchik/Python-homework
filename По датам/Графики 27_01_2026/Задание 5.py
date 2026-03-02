import matplotlib.pyplot as plt

plt.figure(figsize=(10,6), dpi=300)


plt.subplot(2,2,1)

months = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"] # В легенду
temperature = [11, 7, 14, 14, 19, 23, 28, 29, 24, 19, 18, 11] # Ось Y

plt.plot(months, temperature, color="red", marker="o", markerfacecolor="blue", markersize=10)
plt.ylabel("Температура С°")
plt.xlabel("Месяц")
plt.title("График температуры в Сочи за 2025 год")
plt.xticks(rotation=75)


sp2 = plt.subplot(2,2,2)

variants = ["Комедия", "Фантастика", "Драма", "Боевик", "Детектив"]
votes = [8, 6, 4, 7, 5]

plt.bar(variants, votes, color="green", alpha=0.7)
plt.grid(True)
plt.title("Голосование за жанр фильма")
plt.xticks(rotation=75)


sp3 = plt.subplot(2,2,3)

categories = ["Еда", "Транспорт", "Развлечения", "Книги/курсы", "Прочее"]
spent = [2000, 500, 1000, 1000, 500]

explode = (0, 0, 0, 0.1, 0)
plt.pie(spent, labels=categories, autopct="%1.1f%%", explode=explode, shadow=True)
plt.title("Затраты из бюджета (5кр)")


sp4 = plt.subplot(2,2,4)

days = ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс']
steps = [7542, 10234, 8901, 11209, 5601, 14200, 8321]
sizes = [stps/100 for stps in steps]

plt.plot(days, steps, label='Динамика кол-ва шагов')
plt.scatter(days, steps, s=sizes, label='Кол-во шагов')
ax = plt.axhline(y=10000, color='red', linestyle='--')
ax.set_label('Цель.')
plt.legend()
plt.title("Динамика и цель по шагам")

plt.tight_layout()
#plt.subplots_adjust(wspace=0.4, hspace=2)

plt.savefig('my_plots.png', dpi=300, bbox_inches='tight')

plt.show()