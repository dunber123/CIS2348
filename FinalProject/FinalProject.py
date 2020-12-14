# Rhahan Sarwar
# 1818962

import csv
import datetime as datetime

'''These three functions are used to open and read the given csv files and append them into new lists'''


def manufacturer_function():
    manu_list = []
    with open('ManufacturerList.csv', 'r') as csvfile:
        csv_list = csv.reader(csvfile, delimiter=',')
        row_num = 1
        for row in csv_list:
            manu_list.append(row)
            row_num += 1
    return manu_list


def price_function():
    price_list = []
    with open('PriceList.csv', 'r') as csvfile:
        csv_list = csv.reader(csvfile, delimiter=',')
        row_num = 1
        for row in csv_list:
            price_list.append(row)
            row_num += 1
    return price_list


def service_function():
    service_list = []
    with open('ServiceDatesList.csv', 'r') as csvfile:
        csv_list = csv.reader(csvfile, delimiter=',')
        row_num = 1
        for row in csv_list:
            service_list.append(row)
            row_num += 1
    return service_list

'''This part is calling upon the functions'''
manufacturer_function()
price_function()
service_function()

'''Creating a new list that will take the information from the given csv files 
and create a combined file containing all the data and sorting them by manufacturer alphabetically'''

'''Part 1a - Create new Full Inv List '''

complete_inv = manufacturer_function()
for all_items in complete_inv:
    for price_items in price_function():
        if all_items[0] == price_items[0]:
            all_items.append(price_items[1])
    for date in service_function():
        if all_items[0] == date[0]:
            all_items.append(date[1])
    all_items.append(all_items[3])
    all_items.pop(3)

complete_inv.sort()
complete_inv.sort(key=lambda x: x[1])

'''This part is creating a list for the types of products within the csv file'''

Types = []
for items in complete_inv:
    if [items[2]] in Types:
        pass
    else:
        Types.append([items[2]])
for all_items in complete_inv:
    for items in Types:
        if all_items[2] == items[0]:
            items.append([all_items[0], all_items[1], all_items[3], all_items[4], all_items[5]])

'''Creating a list that holds the items that have passed their service date based on the current date'''
past_date = []

today = datetime.date.today()

for items in complete_inv:
    lst_date = items[4].split("/")
    date_of_service = datetime.date(int(lst_date[2]), int(lst_date[0]), int(lst_date[1]))
    if date_of_service < today:
        past_date.append(items)
past_date.sort(key=lambda x: x[4])

'''Find the damaged items and put them into a list'''
dmgd_inv = []

for all_items in complete_inv:
    if all_items[5] == 'damaged':
        dmgd_inv.append([all_items[0], all_items[1], all_items[2], all_items[3], all_items[4]])
dmgd_inv.sort(key=lambda x: x[3])

'''This function is used for creating the FullInventory csv file'''


def all_inv_list_function():
    with open('FullInventory.csv', 'w+', newline='') as csvfile:
        creator = csv.writer(csvfile)
        for line in complete_inv:
            creator.writerow(line)


"""The list to csv function along with the for loop will create csv files based on the type of product the item is"""


def csv_conversion(name, list):
    with open(name, 'w+', newline='') as csvfile:
        creator = csv.writer(csvfile)
        for line in list:
            creator.writerow(line)


for row in Types:
    csv_conversion('{}Inventory.csv'.format(row[0].capitalize()), row[1:])

''' this function will be used to create the PastServiceDateInventory csv file based on the current date'''


def past_date_list_function():
    with open('PastServiceDateInventory.csv', 'w+', newline='') as csvfile:
        creator = csv.writer(csvfile)
        for line in past_date:
            creator.writerow(line)


'''this function is used to create a damaged inventory csv '''


def damaged_list_function():
    with open('DamagedInventory.csv', 'w+', newline='') as csvfile:
        creator = csv.writer(csvfile)
        for line in dmgd_inv:
            creator.writerow(line)


all_inv_list_function()
past_date_list_function()
damaged_list_function()

'''This function takes the user's input and searches throughout the new lists to output the given request if applicable'''
''' It will parse through the multiple lists and check for duplications/service dates/damaged status before outputing the proper answer'''


def item_search_function():
    user_input = input()
    print()
    user_input_list = user_input.split()
    manu_input = ''
    item_type = ''
    item_lst = []
    item_found = False
    for inp in user_input_list:  ### This part of the function will take the user's input and search throughout the list regardless of their input phrasing ###
        for item_row in complete_inv:
            if inp == item_row[1] or inp.capitalize() == item_row[1]:
                manu_input = item_row[1]
            elif inp.lower() == item_row[1] or inp + ' ' == item_row[1]:
                manu_input = item_row[1]
            elif inp.lower() + ' ' == item_row[1] or inp.capitalize() + ' ' == item_row[1]:
                manu_input = item_row[1]
    if manu_input != ' ':
        for inp in user_input_list:
            for item_row in complete_inv:
                if item_row[1] == manu_input:
                    if inp == item_row[2] or inp.capitalize() == item_row[2] or inp.lower() == item_row[2]:
                        lst_date = item_row[4].split("/")
                        date_of_service = datetime.date(int(lst_date[2]), int(lst_date[0]), int(lst_date[1]))
                        if date_of_service >= today and item_row[5] != 'damaged':
                            item_type = item_row[2]
                            item_found = True
                            item_lst.append(item_row)
    if item_found:
        item_lst.sort(key=lambda x: x[3])
        items_cost = item_lst[0][3]
        print("Your item is: {} {} {} {}".format(item_lst[0][0], item_lst[0][1], item_lst[0][2], item_lst[0][3]))

        similar_lst = []
        for item_row in complete_inv:
            if item_row[1] != manu_input and item_row[2] == item_type:
                lst_date = item_row[4].split("/")
                date_of_service = datetime.date(int(lst_date[2]), int(lst_date[0]), int(lst_date[1]))
                if date_of_service >= today and item_row[5] != 'damaged':
                    similar_lst.append(item_row)
        similar_lst.sort(key=lambda x: x[3])
        if len(similar_lst) > 0:
            for x in similar_lst:
                sim_items = similar_lst[
                    min(range(len(similar_lst)), key=lambda i: int(similar_lst[i][3]) - int(items_cost))]

                print("\nYou may, also, consider: {} {} {} {}".format(sim_items[0], sim_items[1], sim_items[2],
                                                                      sim_items[3]))
    else:
        print("No such item in inventory (Check Spelling)")

### While loop is used to get user input and call upon function ###

while True:
    print("\nDo you want to check for an item in inventory? \nY to continue, Q to quit")
    quest = input()
    if quest == 'y' or quest == 'Y':
        print("\nTo check for an item in inventory,")
        print("type the manufacturer and item in the format")
        print("'Manufacturer Item' and press enter (Ex: Apple phone).")
        item_search_function()
    elif quest == 'q' or quest == 'Q':
        break
    else:
        print("Please choose either Y or Q")
