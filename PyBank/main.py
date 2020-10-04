import csv

pyBank_input = "./Resources/02-Homeworks_03-Python_Instructions_PyBank_Resources_budget_data.csv"
pyBank_output = "./analysis/pyBank_Output.txt"
totalMonths = 0
total = 0
currentPL = 0
previousPL = 0
pl_change = 0
greatest_Increase = []
greatest_Decrease = []


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


    
with open(pyBank_input, 'r') as csvfile:
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
         
    average_Change = round(pl_change/(totalMonths-1),2)
    

    print(f"Total Months: {totalMonths}")
    print(f"Total: $ {total}")
    print(f"Average Change: $ {average_Change}") 
    print(f"Greatest Increase in Profits: {greatest_Increase[0]} (${greatest_Increase[1]})")
    print(f"Greatest Decrease in Profits: {greatest_Decrease[0]} (${greatest_Decrease[1]})")

#Writing output to text file
#with open(pyBank_output, 'w') as txtfile:
txtWriter = open(pyBank_output, 'w')
txtWriter.write('Total Months '+ str(totalMonths)+'\n')
txtWriter.write('Total: $'+ str(total)+'\n')
txtWriter.write('Average Change: $'+ str(average_Change)+'\n')
#txtWriter.write('Greatest Increase in Profits: '+ str(greatest_Increase[0])+' '+locale.currency(greatest_Increase[1])+'\n')
txtWriter.write('Greatest Increase in Profits: '+ str(greatest_Increase[0])+' ($'+str(greatest_Increase[1])+')\n')
txtWriter.write('Greatest Decrease in Profits: '+ str(greatest_Decrease[0])+' ($'+str(greatest_Decrease[1])+')\n')
#txtWriter.write('Greatest Decrease in Profits: '+ str(greatest_Decrease[0])+' '+locale.currency(greatest_Decrease[1])+'\n')
txtWriter.close()
#txtFileWriter = csv.writer(txtfile)
#txtFileWriter.writerow(['Total Months '+ str(totalMonths)+'\n'])
#txtFileWriter.writerow(['Total: $'+ str(total)])
#txtFileWriter.writerow(['Total: $'+str(float(pl_change/(totalMonths-1)))])
#txtFileWriter.writerow(['Greatest Increase in Profits:", greatest_Increase[0], " ", locale.currency(greatest_Increase[1])])
#txtFileWriter.writerow(["Greatest Decrease in Profits:", greatest_Decrease[0], " ", locale.currency(greatest_Decrease[1])])
