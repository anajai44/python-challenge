# task: create a Python script that analyzes the records to calculate each of the following values:

#  total number of months, net total amount of "Profit/Losses" over the entire period
# changes in "Profit/Losses" over the entire period, and then the average of those changes
# greatest increase in profits (date and amount) over the entire period
#  greatest decrease in profits (date and amount) over the entire period

import os
import csv

file = os.path.join('..', 'Resources', 'budget_data.csv')
with open('budget_data.csv','r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    header = next(csvreader)

    month_count = []
    profit = []
    change_profit = []

    for row in csvreader:
        month_count.append(row[0])
        profit.append(int(row[1]))
    for i in range(len(profit)-1):
        change_profit.append(profit[i+1]-profit[i])
                      
increase = max(change_profit)
decrease = min(change_profit)

month_increase = change_profit.index(max(change_profit))+1
month_decrease = change_profit.index(min(change_profit))+1 

clean_data=list(zip(month_count,profit, change_profit,increase, decrease, month_increase, month_decrease))    

output = os.path.join('..', 'Python-Challenge', 'PyBank', 'Analysis')
with open(output,"w") as txtfile:

    txtfile.writelines("Financial Analysis" + "\n" + "------------------------")
    for entry in clean_data:
        txtfile.writelines("Financial Analysis" + "\n" + "------------------------" + "\n" +
    f"Total Months:{len(month_count)}" + "\n" + f"Total: ${sum(profit)}" + 
    "\n" + f"Average Change: {round(sum(change_profit)/len(change_profit),2)}"
    "\n" + f"Greatest Increase in Profits: {month_count[month_increase]} (${(str(increase))})" +
    "\n" + f"Greatest Decrease in Profits: {month_count[month_decrease]} (${(str(decrease))})" +)


    with open(output_file, 'r') as readfile:
    print(readfile.read())



                      