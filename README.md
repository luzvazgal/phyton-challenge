# phyton-challenge
Homework 3

This folder has a couple of Python programs: PyBank and PyPoll

PyBank
Python script for analyzing financial records data located in CSV file.  The dataset is composed of two columns: Date and Profit/Losses. 

Python script analyzes the records to calculate each of the following:

-The total number of months included in the dataset
-The net total amount of "Profit/Losses" over the entire period
-The average of the changes in "Profit/Losses" over the entire period
-The greatest increase in profits (date and amount) over the entire period
-The greatest decrease in losses (date and amount) over the entire period

Code components
* Using fileIterator to read each file row
* Managing each row as a List to get all their elements
The output is written to a TXT file using writer method

PyPoll
Python script for analyzing votes in a samll, rural town.  The dataset is composed of two columns: Voter Id, County and Candidate which is in a CSV file (election_data.csv). 

Python script analyzes the records to calculate each of the following:

-The total number of votes cast
-A complete list of candidates who received votes
-The percentage of votes each candidate won
-The total number of votes each candidate won
-The winner of the election based on popular vote.

Code components
* Using fileIterator to read each file row
* Dictionary to have candidate (key) : Number of votes (values)
* Managing each row as a List to get all their elements
* The output is written to a TXT file using writer method
