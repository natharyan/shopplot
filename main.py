import matplotlib.pyplot as plt
from matplotlib.pyplot import show, plot
import mysql.connector as dat
import csv
from statistics import mean, median, mode

show(block=False)

def timings():
    x1=['09:00 AM']
    y1=['0']
    left=[]
    with open("timings.csv","r") as file:
        obj=csv.reader(file)
        for row in obj:
            x1+=[row[0]]
            y1+=[row[1]]

    #x-coordinate of bar
    for i in range(1,len(x1)+1):
        left+=[i]
    
    # plotting a bar chart
    plt.bar(left, y1, tick_label = x1,
            width = 0.8, color = ['red','blue', 'green'])
    
    # naming the x-axis
    plt.xlabel('Time')
    # naming the y-axis
    plt.ylabel('Customers')
    # plot title
    plt.title('Timings')
    l=[]
    for i in x1:
        l+=[float(i[:2])]
    print("average customers in store =",mean(l))
    
    # function to show the plot
    plt.show()
    

def items():
    x1=['Watermelon']
    y1=['0']
    left=[]
    with open("items.csv","r") as file:
        obj=csv.reader(file)
        for row in obj:
            x1+=[row[0]]
            y1+=[row[1]]

    #x-coordinate of bar
    for i in range(1,len(x1)+1):
        left+=[i]
    
    # plotting a bar chart
    plt.bar(left, y1, tick_label = x1,
            width = 0.8, color = ['red','blue', 'green'])
    
    # naming the x-axis
    plt.xlabel('Item Name')
    # naming the y-axis
    plt.ylabel('Amount')
    # plot title
    plt.title('Items purchased')
    
    l=[]
    for i in y1:
        l+=[int(i)]
    val=max(l)
    pos=y1.index(str(val))
    print(x1[pos],"has maximum frequency of",val)
    # function to show the plot
    plt.show()
    
while True:
    t=input("Prompt: ")
    if t=='customers':
        timings()
    elif t=='items':
        items()
    else:
        break