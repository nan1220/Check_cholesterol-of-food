from bs4 import BeautifulSoup
import requests
url='https://www.ucsfhealth.org/education/cholesterol-content-of-foods'
response = requests.get(url)
doc=BeuutifulSoup(response.text, 'html.parser')
#doc=BeautifulSoup(response.content, 'html.parser')
#Ig,this works as well.

tables=doc.select('table')
#there are 3 tables in the page

parsed_table=[]
for table in tables:
    for row in table.select('tr')[1:]:
        buffer_row=[]
        for data in row.select('td'):
            buffer_row.append(data.get_text())
        parsed_table.append(buffer_row)
#output is a list of lists
# [['Milk (non-fat)', '1 cup', '4', '0', '0'],
#  ['Milk (low-fat)', '1 cup', '10', '3', '2'],
#  ['Milk (whole)', '1 cup', '33', '8', '5'],
#  ['Yogurt (non-fat)', '1 cup', '10', '0', '0'],
#  ['Yogurt (whole)', '1 cup', '29', '7', '5'],
#  ['Cheddar cheese', '1 oz', '30', '9', '6'],
#  ['Cottage cheese (low-fat)', '1 cup', '10', '2', '2'],
#  ['Butter', '1 tsp', '11', '4', '3'],
#  ['Margarine', '1 tsp', '0', '4', '1'],
#  ['Vegetable oils\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0',
#   '1 tsp',
#   '0',
#   '5',
#   '1 - 2 '],
#  ['Tofu', '1/2 cup', '0', '11', '2'],
#  ['Pinto beans', '1/2 cup', '0', '1', '0'],
#  ['Egg', '1', '212', '5', '2'],
#  ['Halibut', '3 ½ oz', '41', '3', '0'],
#  ['Salmon', '3 ½ oz', '63', '12', '2'],
#  ['Oysters', '3 ½ oz', '55', '2', '1'],
#  ['Crab', '3 ½ oz', '52', '1', '0'],
#  ['Lobster', '3 ½ oz', '71', '1', '0'],
#  ['Tuna (in water)', '3 ½ oz', '30', '1', '0'],
#  ['Shrimp', '3 ½ oz', '194', '1', '0'],
#  ['Squid', '3 ½ oz', '231', '1', '0'],
#  ['Beef (ground, lean)\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0',
#   '3 ½ oz',
#   '78',
#   '18',
#   '7'],
#  ['Beef (short ribs)', '3 ½ oz', '94', '42', '18'],
#  ['Beef (sirloin)', '3 ½ oz', '89', '12', '5'],
#  ['Beef liver', '3 ½ oz', '389', '5', '2'],
#  ['Veal (top round)', '3 ½ oz', '135', '5', '2'],
#  ['Lamb (foreshank)', '3 ½ oz', '106', '14', '6'],
#  ['Ham', '3 ½ oz', '53', '6', '2'],
#  ['Pork (tenderloin)', '3 ½ oz', '79', '6', '2'],
#  ['Pork (chop)', '3 ½ oz', '85', '25', '10'],
#  ['Chicken liver', '3 ½ oz', '631', '6', '2'],
#  ['Chicken (no skin)', '3 ½ oz', '85', '5', '1']]
#Output is truncated. There are 32 lists in the output

#len(parsed_table) #32

cholesterol_content=[]
for sub_full_list in parsed_table:
    sub_select_list=sub_full_list[0:2]
    sub_select_list.append(int(sub_full_list[2]))
    cholesterol_content.append(sub_select_list)
#output is a list of 32 lists
# [['Milk (non-fat)', '1 cup', 4],
#  ['Milk (low-fat)', '1 cup', 10],
#  ['Milk (whole)', '1 cup', 33],
#... so on

#cholesterol_content.index(['Vegetable oils\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0', '1 tsp', 0]) #9

cholesterol_content[9][0]='Vegetable oils'
cholesterol_content[9]
#['Vegetable oils', '1 tsp', 0]
#I corrected the name of the food item

food_list=[]
for sub_list in cholesterol_content:
    food_list.append(sub_list[0])
#output is a list of 32 food items
print('Here is the food list you can check:\n',food_list)
#['Milk (non-fat)', 'Milk (low-fat)', 'Milk (whole)', 'Yogurt (non-fat)', 'Yogurt (whole)', 'Cheddar cheese', 'Cottage cheese (low-fat)', 'Butter', 'Margarine', 'Vegetable oils', 'Tofu', 'Pinto beans', 'Egg', 'Halibut', 'Salmon', 'Oysters', 'Crab', 'Lobster', 'Tuna (in water)', 'Shrimp', 'Squid', 'Beef (ground, lean)', 'Beef (short ribs)', 'Beef (sirloin)', 'Beef liver', 'Veal (top round)', 'Lamb (foreshank)', 'Ham', 'Pork (tenderloin)', 'Pork (chop)', 'Chicken liver', 'Chicken (no skin)']

food=input('Enter the food name: ')
for i in range(len(food_list)):
    if food_list[i]==food:
         print(f'The cholesterol content of {food} is {cholesterol_content[i][2]} mg per {cholesterol_content[i][1]} {food.lower}.')
        break
    elif i==len(food_list)-1:
        print('Food not found.')
#Enter the food name: Egg
#The cholesterol content of Egg is 212 mg per 1 egg.



