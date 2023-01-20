import csv
import os

number_of_months = 0
total = 0
change_sum = 0
current_month = ""
current_value = 0
last_value = 0
monthly_change = 0
biggest_increase_value = 0
biggest_increase_day = ""
biggest_decrease_value = 0
biggest_decrease_day = ""


count_neg_delta = 0

budget_file = os.path.join('Resources', 'budget_data.csv')


with open(budget_file, mode='r') as data_file:

    
    csvFile = csv.reader(data_file)
    next(csvFile)   
    
    for line in csvFile:
        current_month = line[0]        
        current_value = int(line[1])   
        total += current_value         
        monthly_change = current_value - last_value
        change_sum += monthly_change
        last_value = current_value
        number_of_months += 1


        if monthly_change > 0:
            if monthly_change > biggest_increase_value:
                biggest_increase_value = monthly_change
                biggest_increase_day = current_month
        else:  
            if monthly_change < biggest_decrease_value:
                biggest_decrease_value = monthly_change
                biggest_decrease_day = current_month

print()
print("Financial Analysis")
print("-----------------------")
print("Number of months: {}".format(number_of_months))
print("Total: {}".format(total))
print("Greatest Increase in Profits: {} ({})".format(biggest_increase_day, biggest_increase_value))
print("Greatest Decrease in Profits: {} ({})".format(biggest_decrease_day, biggest_decrease_value))
print("Average Change: {}".format(round(change_sum/number_of_months, 2)))



