import csv
import locale

path = "./Resources/02-Homeworks_03-Python_Instructions_PyBank_Resources_budget_data.csv"
totalMonths = 0
total = 0
currentPL = 0
previousPL = 0
pl_change = 0
#average_Change = 0.0
greatest_Increase = []
greatest_Decrease = []
locale.setlocale( locale.LC_ALL, '' )  #Line taken from StackOverflow


def calc_greatest_Changes(row):
    
    global greatest_Increase
    global greatest_Decrease
    
    #If current value is higher, then list is replaced by current row in greatest_Increase list
    if len(greatest_Increase) == 0:
        greatest_Increase = [row[0], row[2]]
    else: 
        #print(f"Comparison: {greatest_Increase[1]} vs {row[2]}")
        if greatest_Increase[1] < row[2]:
            greatest_Increase = [row[0], row[2]]
         #   print(f"Greatest increase: {greatest_Increase}")
    
    #If current value is lower, then list is replaced by current row in greatest_Decrease list
    if len(greatest_Decrease) == 0:
        greatest_Decrease = [row[0], row[2]]
    else: 
        #print(f"Comparison: {greatest_Decrease[1]} vs {row[2]}")
        if greatest_Decrease[1] > row[2]:
            greatest_Decrease = [row[0], row[2]]
            #print(f"Greatest decrease: {greatest_Decrease}")

with open(path, 'r') as csvfile:
    filereader = csv.reader(csvfile,delimiter=',')
    
    
    #Printing Header
    print("Financial Analysis")
    print("----------------------------")
    
    for row in filereader:
        #Printing Results
        #If it's not the header line
        if filereader.line_num>1:
            totalMonths = totalMonths+1
            total = total + int(row[1])
            #Validating if it's the first file record or not
            if filereader.line_num==2:
                previousPL = int(row[1])
            else:
                currentPL = int(row[1])
                pl_change = pl_change + currentPL - previousPL
                #Adding the profit or loss to record (row)
                row.append(currentPL - previousPL)
                #Calling function to get greatest increase and decrease in P/L
                calc_greatest_Changes(row)
                previousPL = currentPL
         
    
    print(f"Total Months: {totalMonths}")
    print(f"Total: $ {total}")
    print(f"Total: $ {pl_change/(totalMonths-1):.2f}") #float function taken from stackoverflow
    print(f"Greatest Increase in Profits: {greatest_Increase[0]} {locale.currency(greatest_Increase[1])}")
    print(f"Greatest Decrease in Profits: {greatest_Decrease[0]} {locale.currency(greatest_Decrease[1])}")


