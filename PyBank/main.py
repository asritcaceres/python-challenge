# import the data
import os
import csv

#path to collect data

budget_csv = os.path.join ('Resources','budget_data.csv')

#Variables for outputs
months = []
profit_loss = []
rev_changes = []


#Variables for data
number_months = 0
net_profit_loss = 0
change_rev =0
greatest_increase=0
greatest_increase_month=0
greatest_decrease = 0
profit_loss2=0
previous_change = 0




#link the csv to open and read
with open (budget_csv, 'r') as csvfile:
    csvreader= csv.reader (csvfile, delimiter=',')

    header = next (csvreader)

#for loop to go through the dates and sum up
    first_row = next(csvreader)
    net_profit_loss= int(first_row[1])
    previous_change= net_profit_loss
    
    for row in csvreader:
        months.append(row [0])
        net_change=int(row[1])-previous_change
        previous_change=int(row[1])
        profit_loss.append (net_change)
        net_profit_loss += int(row [1])
        
     
 
    number_months = len(months) + 1
    print (f'Total Months:  {number_months}')
    print (f'Total:  ${net_profit_loss}')
    #print (profit_loss)
    #number_profit = len(profit_loss)
    #print (number_profit)
 

    # figure out the differnce month to month for the years in data
    #profit_loss2 = [int(profit_loss[i+1]) - int(profit_loss[i]) for i in range(len(profit_loss)-1)]
    #print (profit_loss2)
    #number_profit2=len(profit_loss2)
    #print (number_profit2)
    add_avg_change = sum(profit_loss)
    #print (add_avg_change)

    #find average
    change_rev = round(add_avg_change/len(profit_loss), 2)
    print (f'Average Change: ${change_rev}')

    #calculate max/min in profitloss2
    max_change = max(profit_loss)
    min_change= min(profit_loss)
    #print (f'Greatest Increase: ${max_change}')
    #print (f'Greatest Decrease: ${min_change}')

    
    #find index associated with max/min
    max_month_index = profit_loss.index(max_change)
    min_month_index = profit_loss.index(min_change)

    #assign the best/worst month to the index
    best_month = months[max_month_index]
    worst_month = months[min_month_index]
    #print (best_month)
    #print (worst_month)
    print (f'Greatest Increase in Profits: {best_month}, ${max_change}')
    print (f'Greatest Decrease in Profits: {worst_month}, ${min_change}')

#Write out to:
    output_file_budget = os.path.join('Resources', 'budget_data_v2.text')

#write mode
    with open(output_file_budget, 'w') as txtfile:

        txtfile.write(f'Financial Analysis\n')
        txtfile.write(f'-----------------\n')
        txtfile.write(f'Total Months:  {number_months}\n')
        txtfile.write(f'Total:  ${net_profit_loss}\n')
        txtfile.write(f'Average Change: ${change_rev}\n')
        txtfile.write(f'Greatest Increase in Profits: {best_month}, ${max_change}\n')
        txtfile.write(f'Greatest Decrease in Profits: {worst_month}, ${min_change}\n')
