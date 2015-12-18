basket_items = ["chocolate", " cheese", " crackers", " popcorn", " alcohol"]
basket_note = "Let's get started! Here is a list of options to add to your basket: "
welcome_quest = raw_input ("Hi! Welcome to Sammy's Custom Baskets! Would you like to make a basket? ")

if welcome_quest == "yes":
    print basket_note
    print ',' .join(basket_items) + "."

else:
    print "No problem! Thanks for the visit, bye!"
    exit (0)

print "----------------------------------------------"

choc_treats = ["chocolate covered oreos, ghirardelli milk chocolate bars, or chocolate chip cookies!"]
choc_intro = "Here are our delicious chocolate options: "

print "NOW FIRST: CHOCOLATE!!!"

print choc_intro
print ',' .join(choc_treats) + "."

choc_quest = raw_input ("Would you like to add chocolate to your basket? ")


#create an empty dictionary called users_basket

 # "Cheeses": cheese_qty, "crackers": crack_qty, "popcorn": pop_qty, "alcohol": alch_qty}

if choc_quest == "yes":
    choc_qty = raw_input ("how many chocolate bars would you like? ")
    print "Great! adding" , int(choc_qty) , "to your basket now!"
# add this quantity to my user's basket next to chocolate.
else:
    print "wow... no chocolate? okay! On to the next- CHEESE!!!"

# users_basket = {"chocolate bars": choc_qty}

# users_basket ["chocolate bars"] = choc_qty

print "-----------------------------------"

print "CHEEEESEEEE TIIIIIMMMEEE!"

cheese_quest = raw_input ("would you like me to add cheese to your basket? ")


if cheese_quest == "yes":
    cheese_qty = raw_input ("how many pieces of cheese would you like? ")
    print "cheessyyy baby, adding" , int(cheese_qty) , "to your basket now"
    #add this quantity to my user's basket next to cheese.
else:
    print "wow... no cheese? okay! On to the next- CRACKERS!!!"

# users_basket ["cheese"] = cheese_qty

#how to add price as part of the dictionary for each item detail...

print "-----------------------------------"

print "HOW ABOUT SOME CRACKERS?!"

crackers_quest = raw_input ("would you like me to add crackers to your basket? ")

if crackers_quest == "yes":
    print "great! im adding a box to your basket now!"
    # users_basket ["crackers"] = 1
else:
    print "wow... no crackers? okay! On to the next- POPCORN!!!"
    # exit (0)

print "-------------------------------------"

popcorn_quest = raw_input ("How about some POPCORN!?! ")

if popcorn_quest == "yes":
    print "sweet! adding it to your basket now!!!"
else:
    print "wow... no popcorn? okay! On to the next- ALCOHOL!!!"

# print "-------------------------------------"

            ##ALCOHOL QUESTIONS HERE FROM FIXALCOHOL.PY##

print "-------------------------------------"

alcohol_quest = raw_input ("Shall I add alcohol to your basket? ")

if alcohol_quest == "yes":
    beerwine_quest = raw_input ("would you like beer or wine? ")
    if beerwine_quest == "beer":
        beer_qty = raw_input ("how many bottles of beer would you like? ")
#add beer_qty to the users_basket
        print "adding it to your basket now!"
        print "time to review your order!!!"
    elif beerwine_quest == "wine":
        wine_choice = raw_input ("red or white? ")

    if wine_choice == "red":
        winered_qty = raw_input ("how many bottles would you like? ")
        print "adding it to your basket now!"
        print "-------------------------------------"
        print "time to review your order!!!"
    elif wine_choice == "white":
        winewhite_qty = raw_input ("how many bottles would you like? ")
        print "adding it to your basket now!"
        print "-------------------------------------"
        print "time to review your order!!!"
    else: 
        print "sorry didn't quite catch that..."
        print beerwine_quest
else:
    print "well that comes to the end of production! let me review your order with you!"
#     print end_note






# if beerwine_quest == "beer":
#     beer_qty = raw_input ("how many bottles of beer would you like? ")
# #add beer_qty to the users_basket
#     print "adding it to your basket now!"
#     print "time to review your order!!!"
# elif beerwine_quest == "wine":
#     wine_choice = raw_input ("red or white? ")

#     if wine_choice == "red":
#         winered_qty = raw_input ("how many bottles would you like? ")
#         print "adding it to your basket now!"
#         print "-------------------------------------"
#         print "time to review your order!!!"
#     elif wine_choice == "white":
#         winewhite_qty = raw_input ("how many bottles would you like? ")
#         print "adding it to your basket now!"
#         print "-------------------------------------"
#         print "time to review your order!!!"
#     else: 
#         print "sorry didn't quite catch that..."
#         print beerwine_quest
# else: 
#     print "sorry didn't quite catch that..."
#     print beerwine_quest

#store beer_qty or winered_qty or winewhite_qty in the dictionary. change alcohol to beer or wine and add the quantity from the input. 


# print "-------------------------------------"
print "CUSTOM BASKET ORDER REVIEW"
#print list of users_basket in a list with title, price, and quantity, then...
#print the total cost of the basket-- through a function of adding all items in basket... 





# 1. i need to save all user choices into a dictionary? so i can print it out at the end and come up with a basket price total
# #create an empty dictionary called users_basket

#  # "Cheeses": cheese_qty, individual price, "crackers": crack_qty, individual price, "popcorn": pop_qty, individual price, "alcohol": alch_qty, individual price}
# 2. i might want to ask if the user is 21 or above so they can continue with adding alcohol to their basket. 
# ##if user is 21 or above:
#     #print beerwine_quest = raw_input ("would you like beer or wine? ")
# ##else:
#     ##print "i'm sorry i cant let you order alcohol if you're not of age. Let's review the rest of your order!" 
# 3. the "no" side of my answers doesnt work as well as the yes side.. there are some problems
# 4. once this works both yes and no.. i might want to add other options for each category of food. like types of chocolate or different cheese or differnt types of popcorn etc. but how do i manage the user input and what i have saved as options.. 
# # if the item is in choc_choice: (store into user_basket but save their input if it is ex. chocolate, covered, or oreos... save that as "chocolate covered oreos ($2.99)") how to save their input as something else. if given one of the words. 
# #     print great! im adding it to your basket now!
# # else:
# #     print im sorry could you try that again, i dont see that in my list of choices. 
# #     print choc_quest
# 5. beer wine question at the end. how to manage their answer... how to save that specificity to the dictionary. alcohol: beer: 4 bottles: $8 each









