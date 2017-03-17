""""
This program runs with the a .csv file names comics.csv. The file needs to be in the same folder as the python program.
This program will contain information with regards a store that owns and sells comic books.
The program will ask the user to select from a menu of 6 options. After selecting one of the 10 options
from the option menu the script will grab the inventory file and provide the information requested.

The comics divided by:
Grade Condition--Mint=A+;Near Mint/Awesome=A;Good/Great=B+;Ok=B;Fair=B-;Bad=C
Publisher--Atlas;Charlton;DC;Dell;Fawcet;Gold Key;Marvel;Megaton;Modern

"""""

import csv
import sys
import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
from sortedcontainers import SortedDict

dict= {}
x=0

f = open('comics.csv',encoding='utf8')
my_file = csv.reader(f)

headers=['Publisher', 'Comic_Issue_Number', 'Title', 'Description', 'Condition', 'Grade_Condition', 'Price_Paid', 'Price_Tag']
comics = pd.read_csv("comics.csv",header=None, names=headers)


def read_in_csv():
    sales = pd.read_csv('comics.csv')
    sales.columns = ['Publisher', 'Comic_Issue_Number', 'Title', 'Description', 'Condition', 'Grade_Condition', 'Price_Paid', 'Price_Tag']
    print(sales.head())

print("******WELCOME TO COMICLAND*****")


def print_menu():
    print('1. Look Whole Inventory')
    print('2. Save Inventory in CSV file')
    print('3. Count of Comics by Grade Condition')
    print('4. Number of Comics by Publisher')
    print('5. Display list of comics by Publisher')
    print('6. Comics Price Tag Plot')
    print('7. Quit')

# setup counter to store choices
menu_choice = 0

print_menu()

while menu_choice != 7:

    try:
        menu_choice = int(input("Type in a number (1-7): "))

    except:

        print("***Please Type an INTEGER NUMBER from 1-7***")


    if menu_choice == 1:
        print(comics)

    elif menu_choice == 2:
        comics.to_csv("comics1.csv", sep="|", encoding='utf-8')

    elif menu_choice == 3:
        for row in my_file:
            Title = row[5]
            if Title in dict:
                dict[Title] = dict[Title] + 1
            else:
                dict[Title] = 1
        print(dict)

    elif menu_choice == 4:
        publisher_count=comics['Publisher'].value_counts()
        print(publisher_count)

    elif menu_choice == 5:
        print('****Select Publisher****')

        def print_menu1():
            print('1. Atlas')
            print('2. Charlton')
            print('3. DC')
            print('4. Dell')
            print('5. Fawcett')
            print('6. Gold Key')
            print('7. Marvel')
            print('8. Megaton')
            print('9. Modern')
            print('10. Return to main menu')

        menu_choice1 = 0

        print_menu1()

        while menu_choice1 != 10:

            try:
                menu_choice1 = int(input("Type in a number (1-10): "))

            except:

                print("***Please Type an INTEGER NUMBER from 1-10***")

            if menu_choice1 == 1:
                Atlas = comics[comics['Publisher'] == "Atlas"]
                print(Atlas)

            elif menu_choice1 == 2:
                Charlton = comics[comics['Publisher'] == "Charlton"]
                print(Charlton)

            elif menu_choice1 == 3:
                DC = comics[comics['Publisher'] == "DC"]
                print(DC)

            elif menu_choice1 == 4:
                Dell = comics[comics['Publisher'] == "Dell"]
                print(Dell)

            elif menu_choice1 == 5:
                Fawcett = comics[comics['Publisher'] == "Fawcett"]
                print(Fawcett)

            elif menu_choice1 == 6:
                Gold_Key = comics[comics['Publisher'] == "Gold Key"]
                print(Gold_Key)

            elif menu_choice1 == 7:
                Marvel = comics[comics['Publisher'] == "Marvel"]
                print(Marvel)

            elif menu_choice1 == 8:
                Megaton = comics[comics['Publisher'] == "Megaton"]
                print(Megaton)

            elif menu_choice1 == 9:
                Modern = comics[comics['Publisher'] == "Modern"]
                print(Modern)
            else:
                print_menu1()

    elif menu_choice == 6:
        comics_grouped = comics.groupby('Publisher', as_index=False).sum()
        print(comics_grouped)


    else:
        print_menu()