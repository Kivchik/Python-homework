import matplotlib.pyplot as plt

variants = ["Комедия", "Фантастика", "Драма", "Боевик", "Детектив"]
votes = [8, 6, 4, 7, 5]

plt.bar(variants, votes, color="green", alpha=0.7)
plt.grid(True)

plt.show()