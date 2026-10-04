import matplotlib.pyplot as plt

days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
savings = [70, 85, 60, 90, 75]

plt.plot(days, savings)
plt.title('My weekly savings progress')
plt.xlabel('Days of the week')
plt.ylabel('Savings')
plt.grid(True)
plt.ylim(0, 100)
plt.show()
plt.plot(days, savings, marker='o', linestyle='dotted', color='black')
plt.title('My weekly savings progress')
plt.xlabel('Days of the week')
plt.ylabel('Savings')
plt.grid(True)
plt.ylim(0, 100)
plt.show()
plt.bar(days, savings, color='red')
plt.title('My weekly savings progress')
plt.xlabel('Days of the week')
plt.ylabel('Savings')
plt.grid(True)
plt.ylim(0, 100)
plt.show()