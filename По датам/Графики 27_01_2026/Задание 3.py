import matplotlib.pyplot as plt

categories = ["Еда", "Транспорт", "Развлечения", "Книги/курсы", "Прочее"]
spent = [2000, 500, 1000, 1000, 500]

explode = (0, 0, 0, 0.1, 0)
plt.pie(spent, labels=categories, autopct="%1.1f%%", explode=explode, shadow=True)
plt.show()