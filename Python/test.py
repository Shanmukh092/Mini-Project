import matplotlib.pyplot as plt

income = 20000
spendings = 20500

plt.bar(["Earnings","Spendings"],[income,spendings])

plt.title("Earnings VS Spendings")

plt.show()

plt.clf()
plt.title("Spendings VS Savings")
plt.bar(["Spendings","Savings"],[spendings,income-spendings])
plt.show()


print(ord('a')-ord('A'))
print(chr(ord('1')-32))
print('1'.upper())

