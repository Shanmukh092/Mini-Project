'''
Problem Statement: Smart Expense Tracker with Insights
Many individuals struggle to track daily expenses and understand spending patterns. Build a Python application that
allows users to log, categorize, and analyze their expenses.
    Objectives
        ==> Record daily expenses (date, category, amount, description)
        ==> Categorize spending (Food, Travel, Bills, etc.)
        ==> Generate monthly summaries and insights
    Key Features
        ==> CLI or simple GUI input system
        ==> Data storage using CSV or JSON
        ==> Monthly expense summary
        ==> Category-wise breakdown (pie chart using libraries like matplotlib)
        ==> Detect highest spending category
'''

import csv
import matplotlib.pyplot as plt

expenses = {}

while(True):
    print("Choose any Below")
    print("1. Add Expense")
    print("2. Get Summary")
    print("3. Exit")
    ch = int(input())
    if(ch==1):
        print("Choose Category Eg:Food, Travel, Bills, etc..")
        cat = input()
        cat = cat.lower()
        print("Enter Spendings:")
        spendings = int(input())
        if(cat in expenses):
            expenses[cat] = expenses[cat]+spendings
        else:
            expenses[cat] = spendings
    
    elif(ch==2):
        maxSpendings = 0
        maxSpendingsCategory = ""
        for exp in expenses:
            if(maxSpendings<expenses[exp]):
                maxSpendings = expenses[exp]
                maxSpendingsCategory = exp
        print(f"You are spending most of the amont in {maxSpendingsCategory} which is Rs.{maxSpendings} try to avoid next time")

        lables = []

        spendings = []

        for exp in expenses:
            lables.append(exp)
            spendings.append(expenses[exp])
        
        plt.figure()
        plt.pie(spendings,labels=lables,autopct='%1.1f%%')
        plt.title("Your Monthly Expenses")
        plt.show()

        print("Please Enter Your Income For Better Comparission:")

        income = int(input())

        plt.clf()
        plt.title("Earnings VS Spendings")
        plt.bar(["Earnings","Spendings"],[income,sum(spendings)])
        plt.show()

        plt.clf()
        plt.title("Spendings VS Savings")
        plt.bar(["Spendings","Savings"],[sum(spendings),income-sum(spendings)])
        plt.show()

    elif(ch==3):
        lables = []
        spendings = []

        for exp in expenses:
            lables.append(exp)
            spendings.append(expenses[exp])

        plt.pie(spendings,labels=lables,autopct='%1.1f%%')
        plt.title("Your Monthly Expenses")

        plt.show()

        with open("expenses.csv", "w", newline="") as file:

            writer = csv.writer(file)
            writer.writerow(["Category", "Amount"])
            
            for key, value in expenses.items():
                writer.writerow([key[0].upper()+key[1:], value])
            expenses.clear()
            break
    else:
        print("Invalid Choice Plese A valid One..")
    
