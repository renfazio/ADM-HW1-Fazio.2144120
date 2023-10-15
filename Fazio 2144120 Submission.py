# This file contains all the exercises (Problem 1 and Problem 2)

 ########################## PROBLEM 1 ##########################

### Introduction

#Say "Hello, World!" With Python

if __name__ == '__main__':
    print("Hello, World!")

#Python If-Else

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

msg1 = "Weird"
msg2 = "Not Weird"

if(n%2 != 0):
    print(msg1)
    
if (n%2 == 0 and n >= 2 and n <= 5):
    print(msg2)
    
if (n%2 == 0  and n >= 6 and n <= 20):
    print(msg1)

if (n%2 == 0  and n > 20):
    print(msg2)
    
#Arithmetic Operators
  
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a+b)
    print(a-b)
    print(a*b)
    
#Python: Division

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a//b)
    print(a/b)

#Loops

if __name__ == '__main__':
    n = int(input())
    i = 0
    while i<n:
        print(i*i)
        i+=1

#Write a function

def is_leap(year):
    leap = False
    
    if(year%4 == 0):
        leap = True
        if(year%100 == 0):
            leap = False
            if(year%400 ==0):
                leap = True
    return leap

#Print Function

if __name__ == '__main__':
    n = int(input())
    i=1
    s = ""
    while(i<=n):
        s += str(i)
        i+=1
    print(s)

### Data Types

#List Comprehensions

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
cordinate = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n]

print(cordinate)

#Find the Runner-Up Score!

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
scores = list(arr)

print (max(x for x in scores if x != max(scores)))

#Nested Lists

students = []

if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])  #store in nested list

#get the scores
scores = []
scores += [student[1] for student in students]

#get second lowest score
second_lowest_score = sorted(scores)[1]

#get the name of students having the second lowest score
names_second_lowest_score = []
names_second_lowest_score += [student[0] for student in students if student[1] == second_lowest_score]

#order names alphabetically
names_second_lowest_score.sort()

for name in names_second_lowest_score:
    print(name)

#Finding the percentage

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
#get marks of the student
marks = student_marks.get(query_name)
#get the average
average_marks = sum(marks) / len(marks)
#print with 2 places after the decimal
print("{:.2f}".format(average_marks))

#Lists

if __name__ == '__main__':
    N = int(input())
    
my_list = []

#Iterate through each command
for _ in range(N):
        command = input().strip().split()

        if command[0] == 'insert':
            position = int(command[1])
            element = int(command[2])
            my_list.insert(position, element)
        elif command[0] == 'print':
            print(my_list)
        elif command[0] == 'remove':
            element = int(command[1])
            my_list.remove(element)
        elif command[0] == 'append':
            element = int(command[1])
            my_list.append(element)
        elif command[0] == 'sort':
            my_list.sort()
        elif command[0] == 'pop':
            my_list.pop()
        elif command[0] == 'reverse':
            my_list.reverse()
            
# Tuples

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    
# Create a tuple 
tup = tuple(integer_list)

# Stamp the hash of the tuple
print(hash(tup))

### Strings

#sWAP cASE

def swap_case(s):
    s = s.swapcase()
    return s

#String Split and Join

def split_and_join(line):
    # write your code here
    line = line.split(" ")
    line = "-".join(line)
    return line
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

#What's Your Name?

#
# Complete the 'print_full_name' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING first
#  2. STRING last
#

def print_full_name(first, last):
    # Write your code here
    x = "Hello {} {}! You just delved into python."
    print (x.format(first,last))
    
#Mutations

def mutate_string(string, position, character):
    l = list(string)
    l[position] = character
    string = "".join(l)
    return string

#Find a string

def count_substring(string, sub_string):

    counter = 0
    start_index = 0

    while start_index < len(string):
        index = string.find(sub_string, start_index)
        if index != -1:
            counter += 1
            start_index = index + 1
        else:
            break
    
    return counter

#String Validators

if __name__ == '__main__':
    s = input()

res = False
for char in s:
    if(char.isalnum()):
        res = True
print (res)

res = False
for char in s:
    if(char.isalpha()):
        res = True
print (res)

res = False
for char in s:
    if(char.isdigit()):
        res = True
print (res)

res = False
for char in s:
    if(char.islower()):
        res = True
print (res)

res = False
for char in s:
    if(char.isupper()):
        res = True
print (res)

#Text Alignment

#Replace all ______ with rjust, ljust or center. 

thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))

#Text Wrap

def wrap(string, max_width):
    paragraphs = string.split('\n')
    wrapped_paragraphs = []

    for paragraph in paragraphs:
        wrapped_lines = textwrap.wrap(paragraph, max_width)
        wrapped_paragraphs.extend(wrapped_lines)

    return '\n'.join(wrapped_paragraphs)

#Designer Door Mat

# Enter your code here. Read input from STDIN. Print output to STDOUT
#get the Mat size
N, M = map(int,input().split(" "))

if 5 < N < 101 and 15 < M < 303 and N%2 != 0:
    for i in range((N-1)//2):
        print(('.|.'*i).rjust((M//2)-1,'-')+ '.|.' + ('.|.'*i).ljust((M//2)-1,'-'))

print(('WELCOME'.center(M,'-')))
for i in range((N-1)//2):
    print(('.|.'*((N//2)-i-1)).rjust((M//2)-1,'-')+ '.|.'+ ('.|.'*((N//2)-i-1)).ljust((M//2)-1,'-'))

#String Formatting

def print_formatted(number):
    width = len(bin(number)[2:]) 
    i = 1
    while(i <= number):
        decimal = str(i)
        octal = oct(i)[2:]
        hexadecimal = hex(i)[2:].upper()
        binary = bin(i)[2:]
        
        print(f"{decimal.rjust(width)} {octal.rjust(width)} {hexadecimal.rjust  (width)} {binary.rjust(width)}")
        i += 1
    
#Alphabet Rangoli

import string
def print_rangoli(size):
    # Get the alphabet characters
    alphabet = string.ascii_lowercase  

    lines = []  

    # Create the top part of the rangoli
    for i in range(size):
        s = '-'.join(alphabet[size-1:i:-1] + alphabet[i:size])
        lines.append((s).center(size*4-3, '-'))

    # Print the top part of the rangoli in reverse order
    for line in lines[::-1]:
        print(line)

    for line in lines[1:]:
        print(line)
        
#Capitalize!

# Complete the solve function below.
def solve(s):
    #Split the input string into words 
    l = s.split(" ")
    x = []
    empty = ""
    
    #Iterate through each word in the input string
    for i in l:
        if i == "":
            x += " "
        elif len(i)==1:
            x += i.upper() + " "
        else:
            x += i[0].upper() + i[1:] + " "
            

    for i in x:
        empty += i
        
    return(empty)

#Merge the Tools!

def merge_the_tools(string, k):
    n = len(string)
    L = n // k  #Number of substrings
    
    for i in range(L):
        # Extract the substring
        substring = string[i * k: (i + 1) * k]
        seen = set()
        
        #Build the subsequence
        subsequence = ''
        for char in substring:
            if char not in seen:
                subsequence += char
                seen.add(char)
        
        print(subsequence)

### Sets

#Introduction to Sets

def average(array):
    # your code goes here
    average = sum(set(array))/len(set(array)) 
    return average

#No Idea!

# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m = input().split()
integers = input().split() 
A = set(input().split()) 
B = set(input().split()) 
happiness = 0

#Iterate and compute for both sets
for i in integers:
    if i in A:
        happiness += 1
    if i in B:   
        happiness -= 1
                
print(happiness)

#Symmetric Difference

# Enter your code here. Read input from STDIN. Print output to STDOUT
#Take inputs
m = int(input())
list1 = set(map(int, input().split()))

n = int(input())
list2 = set(map(int, input().split()))

#Find differences
difference1 = list1 - list2
difference2 = list2 - list1

#Combine and sort the differences
merged_differences = sorted(list(difference1) + list(difference2))

for diff in merged_differences:
    print(diff)

#Set .add()

# Enter your code here. Read input from STDIN. Print output to STDOUT
my_set = set()

N = int(input())
for i in range(N):
    x = input()
    my_set.add(x)
print(len(my_set))  

#Set .discard(), .remove() & .pop()

n_ofElements = int(input())
my_set = set(map(int, input().split()))
N_ofCommands = int(input())

#Iterate and Compute
for i in range(N_ofCommands):
    x = input().split()
    if x[0] == 'pop':
        my_set.pop()
    if x[0] == 'remove':
        my_set.remove(int(x[1]))
    if x[0] == 'discard':
        my_set.discard(int(x[1]))
        
print(sum(my_set)) 

#Set .union() Operation

# Enter your code here. Read input from STDIN. Print output to STDOUT
#Get Input
n_ofEnglishStudents = int(input())
s1 = set(map(int, input().split()))
n_ofFrenchStudents = int(input())
s2 = set(map(int, input().split()))

counter = 0

s3 = set(s1.union(s2))

for i in s3:
    counter += 1
   
print(counter)    

#Set .intersection() Operation

# Enter your code here. Read input from STDIN. Print output to STDOUT
#Get Input
n_ofEnglishStudents = int(input())
s1 = set(map(int, input().split()))
n_ofFrenchStudents = int(input())
s2 = set(map(int, input().split()))

counter = 0

s3 = set(s1.intersection(s2))
for i in s3:
    counter += 1
    
print(counter) 

#Set .difference() Operation

# Enter your code here. Read input from STDIN. Print output to STDOUT
#Get Input
n_ofEnglishStudents = int(input())
s1 = set(map(int, input().split()))
n_ofFrenchStudents= int(input())
s2 = set(map(int, input().split()))

counter = 0

s3 = set(s1.difference(s2))
for i in s3:
    counter += 1
    
print(counter) 

#Set .symmetric_difference() Operation

# Enter your code here. Read input from STDIN. Print output to STDOUT
#Get Input
n_ofEnglishStudents = int(input())
s1 = set(map(int, input().split()))
n_ofFrenchStudents= int(input())
s2 = set(map(int, input().split()))
counter = 0

s3 = set(s1.symmetric_difference(s2))
for i in s3:
    counter += 1
    
print(counter) 

#Set Mutations

# Enter your code here. Read input from STDIN. Print output to STDOUT
nA = int(input())
setA = set(map(int, input().split()))
N = int(input())

for i in range(N):
    x1 = input().split()
    x2 = map(int,input().split())
    
    if x1[0] == 'intersection_update':
        setA.intersection_update(x2)
    elif x1[0] == 'symmetric_difference_update':
        setA.symmetric_difference_update(x2)
    elif x1[0] == 'difference_update':
        setA.difference_update(x2)
    elif x1[0] == 'update':
        setA.update(x2)
        
print(sum(setA))

#The Captain's Room 

# Enter your code here. Read input from STDIN. Print output to STDOUT

def find_captains_room(K, room_numbers):
    
    # Create a set for room numbers seen once
    unique_rooms = set()

    # Create a set for room numbers seen more than once
    groups = set()

    for room in room_numbers:
        if room in unique_rooms:
            #Room is already in unique_rooms, it's a potential group
            groups.add(room)
        else:
            #Room is not in unique_rooms, it's seen for the first time
            unique_rooms.add(room)

    #Subtract potential groups from unique rooms to find the Captain's room
    captains_room = set(unique_rooms.symmetric_difference(groups))

    #The result is a set, so convert it to a list and extract the Captain's room
    return list(captains_room)[0]

if __name__ == "__main__":
    K = int(input().strip())  
    room_numbers = list(map(int, input().split()))  

    captains_room_number = find_captains_room(K, room_numbers)
    print(captains_room_number)

#Check Subset

# Enter your code here. Read input from STDIN. Print output to STDOUT
def check_subset():
    T = int(input().strip())

    #Get Input and compute
    for _ in range(T):
        num_elements_A = int(input().strip())  
        setA = set(map(int, input().split()))  

        num_elements_B = int(input().strip())  
        setB = set(map(int, input().split()))  

        #Check if set A is a subset of set B
        is_subset = setA.issubset(setB)
        print(is_subset)

if __name__ == "__main__":
    check_subset()

#Check Strict Superset

# Enter your code here. Read input from STDIN. Print output to STDOUT

def is_strict_superset(set_A, n, other_sets):
    #Convert the elements of set A to a set
    set_A = set_A.split()
    set_A = set(set_A)

    for i in range(n):
        #Convert the elements of each other set to a set
        other_set = other_sets[i].split()
        other_set = set(other_set)

        #Check if set A is a strict superset
        if not set_A.issuperset(other_set):
            return False

    return True

if __name__ == "__main__":
    #Get Input
    setA = input()
    n_set = int(input())
    other_sets = []
    for i in range(n_set):
        other_set = input()
        other_sets.append(other_set)

    result = is_strict_superset(setA, n_set, other_sets)
    print(result)


### Collections

#collections.Counter()

from collections import Counter

def calculate_earnings(X_numberOfShoes, shoes_sizes, N_customers, customer_requests):
    
    # Count the available shoes sizes
    available_shoes = Counter(shoes_sizes)

    total_earnings = 0

    # Process customer requests and calculate earnings
    for i in range(N_customers):
        desired_size, price = customer_requests[i]
        if available_shoes[desired_size] > 0:
            total_earnings += price
            available_shoes[desired_size] -= 1

    return total_earnings

#Get Input
X_numberOfShoes = int(input().strip())
shoes_sizes = list(map(int, input().split()))
N_customers = int(input().strip())

customer_requests = []
for i in range(N_customers):
    size, price = map(int, input().split())
    customer_requests.append((size, price))

earnings = calculate_earnings(X_numberOfShoes, shoes_sizes, N_customers, customer_requests)
print(earnings)

#DefaultDict Tutorial

from collections import defaultdict

def find_word_occurrences(n, m, group_a, group_b):
    # Create a default dictionary 
    word_occurrences = defaultdict(list)

    # Iterate through group A and record the indices of each word
    for i in range(n):
        word = group_a[i]
        word_occurrences[word].append(i+1)

    # Check occurrences for group B words
    for word in group_b:
        if word in word_occurrences:
            print(' '.join(str(index) for index in word_occurrences[word]))
        else:
            print('-1')


n, m = map(int, input().split())
group_a = [input().strip() for _ in range(n)]
group_b = [input().strip() for _ in range(m)]

# Find and print word occurrences
find_word_occurrences(n, m, group_a, group_b)

#Collections.namedtuple()

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple

#Initialize a named tuple for student information
Student = namedtuple('Student', ['ID', 'MARKS', 'CLASS', 'NAME'])

#Get total number of students and column names
N = int(input().strip())
columns = input().split()

#Map column names to their respective indices
column_indices = {column.upper(): index for index, column in enumerate(columns)}

#Initialize total marks and count
total_marks = 0
count = 0

#Get student information and calculate total marks
for i in range(N):
    student_info = input().split()
    student = Student(ID=student_info[column_indices['ID']],
                      MARKS=int(student_info[column_indices['MARKS']]),
                      CLASS=student_info[column_indices['CLASS']],
                      NAME=student_info[column_indices['NAME']])
    total_marks += student.MARKS
    count += 1

average_marks = total_marks / count

print('{:.2f}'.format(average_marks))

#Collections.OrderedDict()

from collections import OrderedDict

def calculate_net_price(item_count):
    item_dict = OrderedDict()
    
    #Get item names and prices and operate
    for _ in range(item_count):
        item_info = input().split()
        item = ' '.join(item_info[:-1])
        price = int((item_info[-1]))
        item_dict[item] = item_dict.get(item, 0) + price

    return item_dict

#Get number of items 
N = int(input().strip())

# Calculate net price for each item
item_net_prices = calculate_net_price(N)

# Print item names and net prices in order of first occurrence
for item, net_price in item_net_prices.items():
    print(f'{item} {net_price}')

#Word Order

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict

n = int(input().strip())
word_occurrences = OrderedDict()

#Get the input and count occurrences
for i in range(n):
    word = input().strip()
    word_occurrences[word] = word_occurrences.get(word, 0) + 1


print(len(word_occurrences))

#Print the number of occurrences
for word, count in word_occurrences.items():
    print(count, end=" ")

#Collections.deque()

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque

#Get number of operations
N = int(input().strip())

# Initialize an empty deque
d = deque()

#Get method names, values and perform the specified operations
for _ in range(N):
    operation, *values = input().split()
    if hasattr(d, operation):
        getattr(d, operation)(*map(int, values))

print(*d)

#Company Logo

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


if __name__ == '__main__':
    
    #Get Input, count the occurrences of each character and sort
    s = Counter(sorted([i for i in input()]))
    #Find the top three most common characters in the string.
    x = {key: value for key, value in sorted(s.items(), key=lambda x: x[1],         reverse = True)}
    
    counter = 0
    for k in x:
        print(k, x[k])
        counter +=1
        if counter == 3:
            break

### Date and Time

#Calendar Module

# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar

#Initialize Days
days = ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY']

#Get Input
month, day, year = map(int, input().split())

print(days[calendar.weekday(year, month, day)])

#Time Delta

#!/bin/python3

import math
import os
import random
import re
import sys
from datetime import datetime

# Complete the time_delta function below.
def time_delta(t1, t2):
    #Convert the input date-time strings into datetime objects
    date1 = datetime.strptime(t1, '%a %d %b %Y %H:%M:%S %z')
    date2 = datetime.strptime(t2, '%a %d %b %Y %H:%M:%S %z')
    
    #Return the calculation of the time difference between the two datetime
    return str(abs(int((date1-date2).total_seconds()))) 


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()


### Exceptions

# Exceptions

# Enter your code here. Read input from STDIN. Print output to STDOUT
#Get Input
T = int(input())

#Iterate and Compute
for i in range(T):
    a, b = [x for x in input().split()]
    
    try:
        print( int(a)//int(b) ) 
    except ValueError as v:
        print('Error Code:', v)
    except ZeroDivisionError as z:
        print('Error Code:', z)   

### Python Functionals

#Map and Lambda Function

cube = lambda x: x**3 # complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers

    if(n == 1):
        return [0]
    elif(n == 0):
        return []
    else:
        fibo = [0, 1]    
        for i in range(n-2):
            fibo.append(fibo[-1]+fibo[-2])
        
        return fibo 

### Built-ins

#Zipped!

# Enter your code here. Read input from STDIN. Print output to STDOUT
#Get Input
N, X = map(int, input().split())

my_list = []
for i in range(X):
    my_list.append(list(map(float, input().split())))
    
stud = list(zip(*my_list))

for i in stud:
    print(sum(i)/len(i))

#Athlete Sort

#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    NM = input().split()

    N = int(NM[0])

    M = int(NM[1])

    arr = []

    for i in range(N):
        arr.append(list(map(int, input().rstrip().split())))

    K = int(input())

    arr.sort(key = lambda x: x[K])

    for i in arr:
        appoggio = ""
        for j in i:
            appoggio += str(j) + " "
        print(appoggio)

#ginortS

# Enter your code here. Read input from STDIN. Print output to STDOUT
s = input()

low = ""
up = ""
N_ofEven = ""
N_ofOdd = ""

#Iterate and Compute
for i in s:
    if i.islower():
        low += i
    elif i.isupper():
        up += i
    elif(i.isdigit() and int(i)%2 == 0):
        N_ofEven += i
    elif(i.isdigit() and int(i)%2 != 0):
        N_ofOdd += i
        
x = sorted(low), sorted(up), sorted(N_ofOdd), sorted(N_ofEven)       
result = ""

for i in x:
    for j in i:
        result += j
        
print(result)    

### XML

#XML 1 - Find the Score

def get_attr_number(node):
    #Using iter(), cause if not, will count right
    iterable_node = node.iter()  
    score = 0
    for i in iterable_node:
        score += len(i.keys())
    return score

#XML2 - Find the Maximum Depth

maxdepth = 0
def depth(elem, level):
    global maxdepth
    # Write your code goes here
    #Start from the root
    if level == maxdepth:
        maxdepth += 1 
        
    #If an elem can have some children
    for child in elem:
        depth(child, level+1)


 ########################## PROBLEM 2 ##########################

#Birthday Cake Candles

 #!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#
from collections import Counter

def birthdayCakeCandles(candles):
    # Write your code here    
    a = Counter(candles)
    tallest_candles = a[max(a)]
    return tallest_candles

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()


#Number Line Jumps

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#

def kangaroo(x1, v1, x2, v2):
    #Check if kangaroos will ever meet
    if (v1 == v2 and x1 != x2) or (v1 < v2 and (x2 - x1) % (v1 - v2) != 0):
        return "NO"
    
    #Calculate the number of jumps needed to meet
    jumps = (x2 - x1) / (v1 - v2)
    
    #Check if the number of jumps is non-negative and an integer
    if jumps >= 0 and jumps.is_integer():
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()

#Viral Advertising

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'viralAdvertising' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def viralAdvertising(n):
    # Write your code here
    # Initial number of people who receive the advertisement
    shared = 5  
    cumulative_likes = 0  

    for day in range(1, n + 1):
        #Number of people who like the advertisement on the current day
        likes = shared // 2  
        cumulative_likes += likes
        #Number of people who receive the advertisement on the next day
        shared = likes * 3  

    return cumulative_likes

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()

#Recursive Digit Sum

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def superDigit(n, k):
    # Write your code here
    
    if len(n) == 1:
        #Final result
        return n
    

    #But now we want the len(n) == 1
    else:
        length = sum(list(map(int, n)))
        return superDigit(str(length*k), 1)
        
        
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()


#Insertion Sort - Part 1

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    #Value to be inserted
    e = arr[n - 1]
      
    i = n - 2

    #Shift elements to the right until we find the correct position for e
    while i >= 0 and arr[i] > e:
        arr[i + 1] = arr[i]
        i -= 1
        print(' '.join(map(str, arr)))

    #Insert the value e
    arr[i + 1] = e
    print(' '.join(map(str, arr)))  
    
    
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)

#Insertion Sort - Part 2

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort2' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort2(n, arr):
    # Write your code here
    # Iterate through the array starting from the second element
    for i in range(1, n):
        #Current element to be inserted
        key = arr[i]  
        j = i - 1

        #Move elements that are greater than key,
        #to one position ahead of their current position
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        #Insert the current element at its correct position
        arr[j + 1] = key
        print(' '.join(map(str, arr)))  


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)
