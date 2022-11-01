import pandas as pd
import numpy as np

df = pd.read_csv('/Users/jazzopardi/Desktop/CS 677/Homework_8/Homework/bakery dataset/BreadBasket_DMS_output.csv')

# Question 1 

df_hour = df.groupby('Hour')['Transaction'].count().sort_values(ascending = False).head(1) 
# 11 am was the most popular hour

df_week = df.groupby('Weekday')['Transaction'].count().sort_values(ascending = False).head(1)
# Saturday was the most popular day

df_period = df.groupby('Period')['Transaction'].count().sort_values(ascending = False).head(1)
# afternoon was the most popular period

# Question 2

df_rev_hour = df.groupby('Hour')['Item_Price'].sum().sort_values(ascending = False).head(1)
# 11 am generated the most revenue

df_rev_week = df.groupby('Weekday')['Item_Price'].sum().sort_values(ascending = False).head(1)
# Saturday generated the most revenue

df_rev_period = df.groupby('Period')['Item_Price'].sum().sort_values(ascending = False).head(1)
# afternoon generated most revenue

# Question 3

df.groupby('Item')['Item'].count().sort_values(ascending = False).head(1)
# Coffee is the most popular


df.groupby('Item')['Item'].count().sort_values(ascending = True).head(5)

# Adjustment, Chicken sandwich are the least popular

# Question 4 

# need to find the average amount of transactoins per day

transactions = df.groupby('Weekday')['Transaction'].count()

lst = []

for n in transactions:
    n = n / 23 # number of weeks in the data set
    lst.append(n)
    
for n in lst:
    n = n / 50
    print(n)
    
# Friday you need 3
# Monday you need 2 or 3
# Saturday you need 5
# Sunday you need 3
# Thursday you need 3
# Tuesday you need 3
# Wednesday you need 3

# Question 5

food = []
drink = []
unknown = []

for n in df.itertuples():
    if n[-2] == 'Bread':
        food.append(n)
    if n[-2] == 'Scandinavian':
        unknown.append(n)
    if n[-2] == 'Hot chocolate':
        drink.append(n)
    if n[-2] == 'Jam':
        food.append(n)
    if n[-2] == 'Cookies':
        food.append(n)
    if n[-2] == 'Muffin':
        food.append(n)
    if n[-2] == 'Coffee':
        drink.append(n)
    if n[-2] == 'Pastry':
        food.append(n)
    if n[-2] == 'Medialuna':
        food.append(n)
    if n[-2] == 'Tea':
        drink.append(n)
    if n[-2] == 'NONE':
        unknown.append(n)
    if n[-2] == 'Tartine':
        unknown.append(n)
    if n[-2] == 'Basket':
        unknown.append(n)
    if n[-2] == 'Mineral water':
        drink.append(n)
    if n[-2] == 'Farm House':
        unknown.append(n)
    if n[-2] == 'Fudge':
        food.append(n)
    if n[-2] == 'Juice':
        drink.append(n)
    if n[-2] == 'Ella\'s Kitchen Pouches':
        unknown.append(n)
    if n[-2] == 'Victorian Sponge':
        food.append(n)
    if n[-2] == 'Firttata':
        food.append(n)
    if n[-2] == 'Hearty & Seasonal':
        unknown.append(n)
    if n[-2] == 'Soup':
        food.append(n)
    if n[-2] == 'Pick and Mix Bowls':
        food.append(n)
    if n[-2] == 'Smoothies':
        drink.append(n)
    if n[-2] == 'Cake':
        food.append(n)
    if n[-2] == 'Mighty Protein':
        unknown.append(n)
    if n[-2] == 'Chicken san':
        food.append(n)
    if n[-2] == 'Coke':
        drink.append(n)
    if n[-2] == 'My-5 Fruit Shoot':
        unknown.append(n)
    if n[-2] == 'Focaccia':
        food.append(n)
    if n[-2] == 'Sandwich':
        food.append(n)
    if n[-2] == 'Alfajores':
        unknown.append(n)
    if n[-2] == 'Eggs':
        food.append(n)
    if n[-2] == 'Brownie':
        food.append(n)
    if n[-2] == 'Dulce de Leche':
        unknown.append(n)
    if n[-2] == 'Honey':
        food.append(n)
    if n[-2] == 'The BART':
        unknown.append(n)
    if n[-2] == 'Granola':
        food.append(n)
    if n[-2] == 'Fairy Doors':
        unknown.append(n)
    if n[-2] == 'Empanadas':
        food.append(n)
    if n[-2] == 'Keeping It Local':
        unknown.append(n)
    if n[-2] == 'Art Tray':
        unknown.append(n)
    if n[-2] == 'Bowl Nic Pitt':
        unknown.append(n)
    if n[-2] == 'Bread Pudding':
        food.append(n)
    if n[-2] == 'Adjustment':
        unknown.append(n)
    if n[-2] == 'Truffles':
        unknown.append(n)
    if n[-2] == 'Chimichurri Oil':
        unknown.append(n)
    if n[-2] == 'Bacon':
        food.append(n)
    if n[-2] == 'Spread':
        food.append(n)
    if n[-2] == 'Kids biscuit':
        food.append(n)
    if n[-2] == 'Siblings':
        unknown.append(n)
    if n[-2] == 'Caramel bites':
        food.append(n)
    if n[-2] == 'Jammie Dodgers':
        food.append(n)
    if n[-2] == 'Tiffin':
        unknown.append(n)
    if n[-2] == 'Olum & polenta':
        food.append(n)
    if n[-2] == 'Polenta':
        food.append(n)
    if n[-2] == 'The Nomad':
        unknown.append(n)
    if n[-2] == 'Hack the stack':
        unknown.append(n)
    if n[-2] == 'Bakewell':
        unknown.append(n)
    if n[-2] == 'Lemon and coconut':
        food.append(n)
    if n[-2] == 'Toast':
        food.append(n)
    if n[-2] == 'Scone':
        food.append(n)
    if n[-2] == 'Crepes':
        food.append(n)
    if n[-2] == 'Vegan mincepie':
        food.append(n)
    if n[-2] == 'Bare Popcorn':
        food.append(n)
    if n[-2] == 'Muesli':
        food.append(n)
    if n[-2] == 'Crisps':
        food.append(n)
    if n[-2] == 'Pintxos':
        unknown.append(n)
    if n[-2] == 'Gingerbread syrup':
        food.append(n)
    if n[-2] == 'Panatone':
        food.append(n)
    if n[-2] == 'Brioche and salami':
        food.append(n)
    if n[-2] == 'Afternoon with the baker':
        unknown.append(n)
    if n[-2] == 'Salad':
        food.append(n)
    if n[-2] == 'Chicken Stew':
        food.append(n)
    if n[-2] == 'Spanish Brunch':
        unknown.append(n)
    if n[-2] == 'Raspberry shortbreak sandwich':
        food.append(n)
    if n[-2] == 'Extra Salami or Feta':
        food.append(n)
    if n[-2] == 'Duck egg':
        food.append(n)
    if n[-2] == 'Baguette':
        food.append(n)
    if n[-2] == 'Valentin\'s card':
        unknown.append(n)
    if n[-2] == 'Tshirt':
        unknown.append(n)
    if n[-2] == 'Vegan Feast':
        food.append(n)
    if n[-2] == 'Postcard':
        unknown.append(n)
    if n[-2] == 'Nomad bag':
        unknown.append(n)
    if n[-2] == 'Chocolates':
        food.append(n)
    if n[-2] == 'Coffee granules':
        food.append(n)
    if n[-2] == 'Drinking chocolate spoons':
        unknown.append(n)
    if n[-2] == 'Christmas common':
        unknown.append(n)
    if n[-2] == 'Argentina night':
        unknown.append(n)
    if n[-2] == 'Half slice Monster':
        unknown.append(n)
    if n[-2] == 'Gift voucher':
        unknown.append(n)
    if n[-2] == 'Cherry me Dried fruit':
        food.append(n)
    if n[-2] == 'Mortimer':
        unknown.append(n)
    if n[-2] == 'Raw bars':
        food.append(n)
    if n[-2] == 'Tacos/Fajita':
        food.append(n)
    

food_price = 0

drink_price = 0 

        
for n in food:
    food_price = n[-1] + food_price
    
for n in drink:
    drink_price = n[-1] + drink_price
    

round(food_price / len(food), 2) # 4.71 is the average price food

round(drink_price / len(drink), 2) # 8.41 is the average price of food

# Question 6

sum_food = 0 
sum_drink = 0 

for n in food:
    sum_food += n[-1]
    
round(sum_food,2) # 477260.77 from food

for n in drink:
    sum_drink += n[-1]
    
round(sum_drink,2) # 69532.79

# The coffee shop makes more money off food than drink. 

# Question 7

df_top_five = df.groupby(['Weekday', 'Item'])['Item'].count()


df_top_five = pd.DataFrame(data = df_top_five)

top_five = df_top_five['Item'].sort_values(ascending = False)

top_five['Saturday'].head(6)
#Coffee    1103
#Bread      760
#Tea        288
#Cake       246
#Pastry     166
top_five['Sunday'].head(6)
#Coffee       825
#Bread        473
#Tea          171
#Cake         167
#Medialuna    134
top_five['Monday'].head(6)
#Coffee      681
#Bread       360
#Tea         193
#Pastry      105
#Sandwich    101
top_five['Tuesday'].head(6)
#Coffee    710
#Bread     350
#Tea       194
#Cake      139
#Pastry    119
top_five['Wednesday'].head(6)
#Coffee    628
#Bread     405
#Tea       188
#Cake      123
#Pastry    103
top_five['Thursday'].head(6)
#Coffee      670
#Bread       450
#Tea         183
#Cake        141
#Pastry      121
top_five['Friday'].head(6)
#Coffee      854
#Bread       527
#Tea         218
#Sandwich    134
#Cake        120

# Coffee, Bread, Tea, Cake are the most popular

# Question 8

bottom_five = df_top_five['Item'].sort_values(ascending = True)

bottom_five['Saturday'].head(5)
#Bowl Nic Pitt                    1
#Cherry me Dried fruit            1
#Raspberry shortbread sandwich    1
#Mortimer                         1
#Lemon and coconut                1
bottom_five['Sunday'].head(5)
#Argentina Night       1
#Bacon                 1
#Brioche and salami    1
#Chicken sand          1
#Chocolates            1
bottom_five['Monday'].head(5)
#Pick and Mix Bowls            1
#Mighty Protein                1
#Extra Salami or Feta          1
#Dulce de Leche                1
#Drinking chocolate spoons     1
bottom_five['Tuesday'].head(5)
#Bowl Nic Pitt                 1
#Chocolates                    1
#Drinking chocolate spoons     1
#Ella's Kitchen Pouches        1
#Gift voucher                  1
bottom_five['Wednesday'].head(5)
#Victorian Sponge     1
#Adjustment           1
#Gingerbread syrup    1
#Mortimer             1
#Crepes               1
bottom_five['Thursday'].head(5)
#Spread                1
#Nomad bag             1
#Lemon and coconut     1
#Argentina Night       1
#Brioche and salami    1
bottom_five['Friday'].head(5)
#Vegan Feast         1
#Valentine's card    1
#The BART            1
#Chimichurri Oil     1
#Fairy Doors         1

# this list doesn't really stay the same

# Question 9

df_drinks = df.groupby(['Transaction', 'Item']).count()

df_drinks

drink_names = []
for n in drink:
    drink_names.append(n[-2])

drink_names = set(drink_names)

lst = []

for x in df_drinks.itertuples():
    for n in drink_names:
        if n in x[0][1]:
            lst.append(x[0])

new_df = pd.DataFrame(data = lst, columns = ['Transaction', 'Drink'])

new_df = new_df.groupby('Transaction')['Drink'].count()

new_df # each transaction and how many drinks were bought
