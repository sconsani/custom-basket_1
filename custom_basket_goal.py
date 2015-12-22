basket_items = {"chocolate": 5.99, "cheese": 7.99, "crackers": 4.99, "popcorn":6.99, "white wine": 10.99, "red wine": 11.99, "beer": 8.99}

final_quant = {"chocolate": 0, "cheese": 0, "crackers": 0, "popcorn":0, "white wine": 0, "red wine": 0, "beer": 0}


def welcome():
    welcome_quest = raw_input("Hi! Welcome to Sammy's Custom Baskets! Would you like to make a basket? yes/no ").lower()
    if welcome_quest == "yes":
        print "Let's get started! Here is a list of options to add to your basket: "
        for keys in basket_items.keys():
            print keys + ", ", 
   

    else:
        print "No problem! Thanks for the visit, bye!"
        exit()

welcome()

print "\n "
print "----------------------------------------------"


def chocolate():
    print "NOW FIRST: CHOCOLATE!!!"
    choc_quest = raw_input ("Would you like to add chocolate to your basket? ").lower()
    if choc_quest == "yes":
        choc_qty = raw_input("how many chocolate bars would you like? ")
        choc_qty = int(choc_qty)
        final_quant['chocolate'] = choc_qty
        
        print "\n "
        if choc_qty > 1:
            print "Great! adding" , choc_qty , "bars to your basket now!"
        else: 
            print "Great! adding" , choc_qty , "bar to your basket now!"

    else:
        print "\n "
        print "wow... no chocolate? okay! On to the next- CHEESE!!!"
        pass

chocolate()
# print final_quant

print "\n"
print "-----------------------------------"


def cheese ():
    print "CHEEEESEEEE TIIIIIMMMEEE!"
    cheese_quest = raw_input ("would you like me to add cheese to your basket? ").lower()
    if cheese_quest == "yes":
        cheese_qty = raw_input ("how many pieces of cheese would you like? ")
        cheese_qty = int(cheese_qty)
        final_quant ['cheese'] = cheese_qty

        print "\n"
        if cheese_qty >1:
            print "cheessyyy baby, adding" , cheese_qty , "piece to your basket now"
        else:
            print "cheessyyy baby, adding" , cheese_qty , "pieces to your basket now"
    else:
        print "\n"
        print "No worries! Let's continue!"
        pass

cheese()
# print final_quant        

print "-----------------------------------"
print "\n"


def crackers():
    print "HOW ABOUT SOME CRACKERS?!"

    crackers_quest = raw_input ("would you like me to add crackers to your basket? ").lower()

    if crackers_quest == "yes":
        crackers_qty = raw_input ("how many boxes of crackers would you like? ")
        crackers_qty = int(crackers_qty)
        final_quant ['crackers'] = crackers_qty

        print "\n"
        if crackers_qty >1:
            print "great! im adding" , crackers_qty , "boxes of crackers to your basket now!"
        else:
            print "great! im adding" , crackers_qty , "box of crackers to your basket now!"
    else:
        print "\n"
        print "Okay, okay... no crackers."
        pass

crackers()
# print final_quant

print "-------------------------------------"
print " \n"

def popcorn():
    popcorn_quest = raw_input ("How about some POPCORN!?! ")
    if popcorn_quest == "yes":
        popcorn_qty = raw_input ("how many bags of gourmet popcorn would you like? ")
        popcorn_qty = int(popcorn_qty)
        final_quant ['popcorn'] = popcorn_qty

        print "\n"
        if popcorn_qty >1:
            print "sweet! adding" , popcorn_qty , "bags of gourmet popcorn to your basket now!!!"
        else:
            print "sweet! adding" , popcorn_qty , "bag of gourmet popcorn to your basket now!!!"
    else:
        "\n"
        print "Alright... no popcorn. No problem. How abouttttt ALCOHOL!!!"
        pass

popcorn()
# print final_quant

print "-------------------------------------"
print "\n"





def alcohol():
    def morebeer():
        morebeer_quest = raw_input ("Did you also want to add beer? ").lower()
        if morebeer_quest == "yes":
            beer_qty = raw_input ("how many bottles of beer would you like? ")
            beer_qty = int(beer_qty)
            final_quant ['beer'] = beer_qty

            print "\n"
            print "adding it to your basket now!"
            print "Let's review your order!"
        else:
            "\n"
            print "well that comes to the end of production! let me review your order with you!"

    def morewine():
        morewine_quest = raw_input ("Did you also want to wine? ").lower()
        if morewine_quest == "yes":
            wine_choice = raw_input ("red or white? ")
            if wine_choice == "red":
                winered_qty = raw_input ("how many bottles would you like? ")
                winred_qty = int(winered_qty)
                final_quant ['red wine'] = winered_qty

                print "\n"
                print "adding it to your basket now!"
                print "Let's review your order!"

            elif wine_choice == "white":
                winewhite_qty = raw_input ("how many bottles would you like? ")
                winwhite_qty = int(winewhite_qty)
                final_quant ['white wine'] = winewhite_qty

                print "\n"
                print "adding it to your basket now!"
                print "Let's review your order!"

            else: 
                print "\n"
                print "sorry didn't quite catch that..."
                print beerwine_quest
        else:
            "\n"
            print "well that comes to the end of production! let me review your order with you!"

    alcohol_quest = raw_input ("Shall I add alcohol to your basket? ").lower()
    if alcohol_quest == "yes":
        beerwine_quest = raw_input ("would you like beer or wine? ")
        if beerwine_quest == "beer":
            beer_qty = raw_input ("how many bottles of beer would you like? ")
            beer_qty = int(beer_qty)
            final_quant ['beer'] = beer_qty

            print "\n"
            print "adding it to your basket now!"
            morewine()

        elif beerwine_quest == "wine":
            wine_choice = raw_input ("red or white? ")
            if wine_choice == "red":
                winered_qty = raw_input ("how many bottles would you like? ")
                winered_qty = int(winered_qty)
                final_quant ['red wine'] = winered_qty

                print "\n"
                print "adding it to your basket now!"
                morebeer()

            elif wine_choice == "white":
                winewhite_qty = raw_input ("how many bottles would you like? ")
                winewhite_qty = int(winewhite_qty)
                final_quant ['white wine'] = winewhite_qty

                print "\n"
                print "adding it to your basket now!"
                morebeer()

            else: 
                print "\n"
                print "sorry didn't quite catch that..."
                print beerwine_quest

    else:
        "\n"
        print "well that comes to the end of production! let me review your order with you!"

alcohol()

for items, number in final_quant.items():
    print items, number


def costquant ():
    choc_cost = (basket_items['chocolate'])
    choc_quant = (final_quant ['chocolate'])
    total_choc = choc_cost * choc_quant


    cheese_cost = (basket_items['cheese'])
    cheese_quant = (final_quant ['cheese'])
    total_cheese = cheese_cost * cheese_quant


    crackers_cost = (basket_items['crackers'])
    crackers_quant = (final_quant ['crackers'])
    total_crackers = crackers_cost * crackers_quant


    popcorn_cost = (basket_items['popcorn'])
    popcorn_quant = (final_quant ['popcorn'])
    total_pop = popcorn_cost * popcorn_quant


    whitewine_cost = float(basket_items['white wine'])
    whitewine_quant = float(final_quant ['white wine'])
    totalwhite =  whitewine_cost * whitewine_quant


    redwine_cost = float(basket_items['red wine'])
    redwine_quant = float(final_quant ['red wine'])
    total_red = redwine_cost * redwine_quant


    beer_cost = (basket_items['beer'])
    beer_quant = (final_quant ['beer'])
    total_beer = beer_cost * beer_quant

    total_basket_cost = total_choc + total_cheese + total_crackers + total_pop + totalwhite + total_red + total_beer

    print "Grand Total:$" , total_basket_cost

costquant()

# from flask import Flask, render_template
# app = Flask(__name__) 

# @app.route('/basketlist')
# def count():
#     words = ["hahaha", "heyyyy", "ahhhhh"]
#     numbers = range(3)

#     return render_template('counter.html', numbers=numbers, words=words)
   
# if __name__=='__main__':
#     app.run(debug=True)













