# Finding Numbers in a Haystack
#In this assignment you will read through and parse a file with text and numbers. 
# You will extract all the numbers in the file and compute the sum of the numbers.
# Data Files
# We provide two files for this assignment. One is a sample file where we give you the sum for your testing, 
# and the other is the actual data you need to process for the assignment.
# Sample data: http://py4e-data.dr-chuck.net/regex_sum_42.txt (There are 90 values with a sum=445833)
# Actual data: http://py4e-data.dr-chuck.net/regex_sum_1505039.txt (There are 72 values and the sum ends with 531)
# These links open in a new window. 
# Make sure to save the file into the same folder as you will be writing your Python program. 
# Note: Each student will have a distinct data file for the assignment - so only use your own data file for analysis.

import re
fhandle = open('regex_sum_1505039.txt')
numlist = list()
for line in fhandle:
    line = line.rstrip()
    num = re.findall('[0-9]+', line)
    if len(num) < 1:
        continue
    elif len(num) == 1:
        num1 = int(num[0])
        numlist.append(num1)
    elif len(num) == 2:
        num1 = int(num[0])
        num2 = int(num[1])
        numlist.append(num1)
        numlist.append(num2)
    else:
        num1 = int(num[0])
        num2 = int(num[1])
        num3 = int(num[2])
        numlist.append(num1)
        numlist.append(num2)
        numlist.append(num3)
sum_num_int = sum(numlist)
print(len(numlist))
print(sum_num_int)