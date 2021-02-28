from csv import reader

month = 0
net_total_amt = 0

with open(r"C:\Users\cperr\Desktop\Python-Challenge\PyBank\Resources\budget_data.csv") as file:
    csv_reader = reader(file, delimiter=',')
    next(csv_reader, None)

#Looping through the csvfile to return desired results
    for row in csv_reader:
        month = month + 1
        net_total_amt = net_total_amt + int(row[1])
    print("Total Month:", month)
    print(f"Net Total Amount: ${net_total_amt}\n")

#Calculating the change from one month to the next by 
#Creating a new column and record the value by shifting the current month 1 row down.
profit_loss_previous = 0
profit_loss_change = 0
profit_loss_change_list = []
month_change = []
greatest_increase = ["", 0]
greatest_decrease = ["", 99999999999]

#changes of profit_loss calculations
profit_loss_change = int(row[1]) - profit_loss_previous
profit_loss_previous = int(row[1])
month_change = month_change + [row[0]]
# print(month_change)

#Greatest Increase value
if (profit_loss_change > greatest_increase[1]):
    greatest_increase[1] = profit_loss_change
    greatest_increase[0] = row[0]
    if (profit_loss_change < greatest_decrease[1]):
        greatest_decrease[0] = row[0]
        greatest_decrease[1] = profit_loss_change
if len(profit_loss_change_list) !=0:
    average_change = sum(profit_loss_change_list) / len(profit_loss_change_list)
else:
     average_change = 0

print("Average Change:", average_change)

#average_change = sum(differences) / len(differences)