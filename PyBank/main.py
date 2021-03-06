from csv import reader

month = 0
total_net_amt = 0
profit_loss_change_list = []
month_change = []
greatest_increase = ["", 0]
greatest_decrease = ["", 99999999999]

with open(r"C:\Users\cperr\Desktop\Python-Challenge\PyBank\Resources\budget_data.csv") as file:
    csv_reader = reader(file, delimiter=',')
    next(csv_reader, None)

    first_row = next(csv_reader)
    month = month + 1
    total_net_amt = total_net_amt + int(first_row[1])
    # print("Total Month:", month)
    # print(f"Net Total Amount: ${total_net_amt}\n")
    previous_change = int(first_row[1])
#Looping through the csvfile to return desired results
    for row in csv_reader:
        month = month + 1
        total_net_amt = total_net_amt + int(row[1])

        profit_loss_change = int(row[1]) - previous_change
        previous_change = int(row[1])
        # print(profit_loss_change)
        profit_loss_change_list = profit_loss_change_list + [profit_loss_change]
        month_change = month_change + [row[0]]
        # print(month_change)
        #Creating conditionals to set what the profit_loss_change index based on month row
        if profit_loss_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = profit_loss_change
        if profit_loss_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease [1] = profit_loss_change
#Calculating the average change by diving the sum of the profit_loss_change list with the count of rows available in that list
average_change = sum(profit_loss_change_list)/len(profit_loss_change_list)
#Printing all results as per instructions
print("Financial Analysis")
print("--------------------------------------------------")
print("Total Months:", month)
print(f"Total: ${total_net_amt}\n")
print(f"Average Change: ${average_change}\n")
print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")

#Summary of results as Output
output = (
   f"\nFinancial Analysis\n"
   f"----------------------------\n"
   f"Total Months: {month}\n"
   f"Total: ${total_net_amt}\n"
   f"Average Change: ${average_change}\n"
   f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
   f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

#Exporting summary table to textfile
with open("C:\\Users\\cperr\\Desktop\\Python-Challenge1\\PyBank\\Analysis\\bank.txt", 'w') as text_file:
    text_file.write(output)