"""
the time in words
Given the time in numerals we may convert it into words, as shown below:
5:00 -> five o'clock
5:01 -> one minute past five
5:10 -> ten minutes past five
5:15 -> quater past five
5:28 -> twenty eight minutes past five
5:30 -> half past five
5:40 -> twenty minutes to six
5:45 -> a quater to six
5:47 -> thirteen minutes to six

at minutes = 0, use "o' clock"
at 1<= minutes < 30, use 'past'
at 30 < minutes use 'to'
"""

#!/bin/python3

import math
import os
import random
import re
import sys

def timeInWords(h, m):
    # Write your code here
    to_str = {0: "o' clock",
              1 : "one",
              2 : "two" ,
              3 : "three",
              4 : "four", 
              5 : "five", 
              6 : "six", 
              7 : "seven", 
              8 : "eight", 
              9 : "nine", 
              10: "ten", 
              11: "eleven", 
              12 : "twelve", 
              13 : "thirteen", 
              14: "fourteen", 
              15: "quarter", 
              16 : "sixteen", 
              17: "seventeen", 
              18: "eighteen", 
              19 : "nineteen", 
              20: "twenty", 
              21: "twenty one", #be carefull about how to write numbers, take a look at your desired output 
              22: "twenty two", 
              23: "twenty three", 
              24: "twenty four", 
              25:"twenty five", 
              26: "twenty six", 
              27: "twenty seven" , 
              28: "twenty eight", 
              29: "twenty nine", 
              30: "half"}
    pointed_str = {31 : to_str[29],
                   32 : to_str[28],
                   33 : to_str[27],
                   34 : to_str[26],
                   35 : to_str[25],
                   36: to_str[24], 
                   37: to_str[23], 
                   38: to_str[22], 
                   39: to_str[21], 
                   40: to_str[20], 
                   41: to_str[19], 
                   42: to_str[18], 
                   43: to_str[17], 
                   44: to_str[16], 
                   45: to_str[15], 
                   46: to_str[14], 
                   47: to_str[13], 
                   48: to_str[12], 
                   49: to_str[11], 
                   50: to_str[10], 
                   51: to_str[9], 
                   52: to_str[8], 
                   53: to_str[7], 
                   54: to_str[6] , 
                   55: to_str[5], 
                   56: to_str[4], 
                   57: to_str[3], 
                   58: to_str[2], 
                   59: to_str[1]}
    
     
    if m == 0:
        return f"{to_str[h]} {to_str[0]}"
        
    
    if m == 1:
        return f"{to_str[1]} minute past {to_str[h]}"
        
    if 1 < m < 30 and m!= 15: 
        return f"{to_str[m]} minutes past {to_str[h]}"
            
    if m == 15:
        return f"{to_str[15]} past {to_str[h]}"
        
    if m == 30:
        return f"{to_str[m]} past {to_str[h]}"
       
    if 30 < m < 59 and m!=45:
        return f"{pointed_str[m]} minutes to {to_str[h+1]}"
    #another way, understanding that passing the 30 minutes, the minutes = 60 - m, and avoiding using the pointed_str
    #   return f"{to_str[60-m]} minutes to {to_str[h+1]}"
         
    if m == 45:
        return f"a {pointed_str[m]} to {to_str[h+1]}"
        #another way
    #   return f"a {to_str[60-m]} to {to_str[h+1]}"
         
    if m==59 and h!=12:
        return f"{pointed_str[m]} minute to {to_str[h+1]}"
        #another way
    #   return f"{to_str[60-m]} minute to {to_str[h+1]}"

#this case is usually not contemplated, but 0<h<=12
    if m==59 and (h==12 or h==0):
        return f"{pointed_str[m]} minute to {to_str[1]}"

  
    
"""
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input().strip())

    m = int(input().strip())

    result = timeInWords(h, m)

    fptr.write(result)

    fptr.close()
"""

#tests
print (timeInWords(5, 47)) 
print (timeInWords(3, 00))
print (timeInWords(0, 59))


