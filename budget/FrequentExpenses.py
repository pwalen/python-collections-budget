from budget import Expense
import collections
import matplotlib.pyplot as plt

expenses = Expense.Expenses()
# To execute the file on my local machine I need to use the following path instead of data/spending_data.csv
# '/Users/pawelwalenda/PycharmProjects/python-collections-budget/data/spending_data.csv'
expenses.read_expenses('data/spending_data.csv')

spending_categories = []
for expense in expenses.list:
    spending_categories.append(expense.category)


spending_counter = collections.Counter(spending_categories)

print(spending_counter)

top5 = spending_counter.most_common(5)

categories, count = zip(*top5)

fig, ax = plt.subplots()

ax.bar(categories, count)
ax.set_title('# of Purchases by Category')

plt.show()