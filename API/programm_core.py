# INGREDIENT TREATMENT FUNCTION
from aima3.logic import *



def check_quantity(ingredient, amount):
    
    quantity = "Nothing"
    
    if ingredient == "Chicken" :
        if amount < 100 :
            quantity = "Few"
        elif amount < 300 :
            quantity = "Med"
        else :
            quantity = "Much"
        
    elif ingredient == "Rice" :
        if amount < 200 :
            quantity = "Few"
        elif amount < 400 :
            quantity = "Med"
        else :
            quantity = "Much"

    elif ingredient == "Broccoli" :
        if amount < 150 :
            quantity = "Few"
        elif amount < 300 :
            quantity = "Med"
        else :
            quantity = "Much"
        
    elif ingredient == "Pepper" :
        if amount < 200 :
            quantity = "Few"
        elif amount < 400 :
            quantity = "Med"
        else :
            quantity = "Much"
        
    elif ingredient == "Onion" :
        if amount < 100 :
            quantity = "Few"
        elif amount < 300 :
            quantity = "Med"
        else :
            quantity = "Much"

    elif ingredient == "Garlic" :
        if amount < 50 :
            quantity = "Few"
        elif amount < 100 :
            quantity = "Med"
        else :
            quantity = "Much"
        
    elif ingredient == "Tomato" :
        if amount < 250 :
            quantity = "Few"
        elif amount < 400 :
            quantity = "Med"
        else :
            quantity = "Much"
    
    elif ingredient == "Beef" :
        if amount < 150 :
            quantity = "Few"
        elif amount < 400 :
            quantity = "Med"
        else :
            quantity = "Much"

    elif ingredient == "Pasta" :
        if amount < 200 :
            quantity = "Few"
        elif amount < 400 :
            quantity = "Med"
        else :
            quantity = "Much"
        
    elif ingredient == "Cheese" :
        if amount < 150 :
            quantity = "Few"
        elif amount < 400 :
            quantity = "Med"
        else :
            quantity = "Much"

    KB.tell(expr(f'HaveIngredient({ingredient}, {quantity})')) 


# TOOL FUNCTION :

def have_tool(tool) :

    KB.tell(expr(f'HaveTool({tool})'))




def forwardChainQuery(params):
    # create kb

    KB = FolKB()
    
    results = []

    # Rules
        # Quantities

    KB.tell(expr('HaveIngredient(x, Much) ==> HaveIngredient(x, Med)'))
    KB.tell(expr('HaveIngredient(x, Med) ==> HaveIngredient(x, Few)'))

        #Queries

    KB.tell(expr('HaveIngredient(Chicken, Med) & HaveIngredient(Broccoli, Med) & HaveIngredient(Onion, Few) & HaveIngredient(Garlic, Few) & ( HaveTool(Pan)  ) ==> CanCook(Chicken_and_broccoli_stir_fry)'))

    KB.tell(expr('HaveIngredient(Chicken, Med) & HaveIngredient(Broccoli, Med) & HaveIngredient(Onion, Few) & HaveIngredient(Garlic, Few) & ( HaveTool(Pot)  ) ==> CanCook(Chicken_and_broccoli_stir_fry)'))


    KB.tell(expr('HaveIngredient(Beef, Med) & HaveIngredient(Broccoli, Med) & HaveIngredient(Onion, Few) & HaveIngredient(Garlic, Few) &  HaveTool(Pan) ==> CanCook(Beef_and_broccoli_stir_fry)'))
    
    
    KB.tell(expr('HaveIngredient(Beef, Med) & HaveIngredient(Broccoli, Med) & HaveIngredient(Onion, Few) & HaveIngredient(Garlic, Few) & HaveTool(Pot)  ==> CanCook(Beef_and_broccoli_stir_fry)'))




    KB.tell(expr('HaveIngredient(Rice, Much) & HaveIngredient(Broccoli, Few) & HaveIngredient(Cheese, Med) &  HaveTool(Pan)==> CanCook(Cheesy_broccoli_and_rice_casserole)'))

    KB.tell(expr('HaveIngredient(Rice, Much) & HaveIngredient(Broccoli, Few) & HaveIngredient(Cheese, Med) & HaveTool(Pot)  ==> CanCook(Cheesy_broccoli_and_rice_casserole)'))




    KB.tell(expr('HaveIngredient(Chicken, Med) & HaveIngredient(Rice, Much) & HaveIngredient(Cheese, Med) & HaveTool(Pan) ==> CanCook(Chicken_and_rice_casserole)'))
    
    KB.tell(expr('HaveIngredient(Chicken, Med) & HaveIngredient(Rice, Much) & HaveIngredient(Cheese, Med) & HaveTool(Pot)  ==> CanCook(Chicken_and_rice_casserole)'))



    KB.tell(expr('HaveIngredient(Beef, Few) & HaveIngredient(Pepper, Med) & HaveIngredient(Rice, Much) & HaveIngredient(Cheese, Few) & HaveTool(Pan)  ==> CanCook(Stuffed_Peppers)'))
    
    KB.tell(expr('HaveIngredient(Beef, Few) & HaveIngredient(Pepper, Med) & HaveIngredient(Rice, Much) & HaveIngredient(Cheese, Few) & HaveTool(Pot)  ==> CanCook(Stuffed_Peppers)'))




    KB.tell(expr('HaveIngredient(Chicken, Few) & HaveIngredient(Broccoli, Med) & HaveIngredient(Onion, Few) & HaveIngredient(Pepper, Few) & HaveIngredient(Garlic, Few) & HaveIngredient(Tomato, Med) & HaveTool(Pot) ==> CanCook(Chicken_and_vegetable_soup)'))
    
    


    KB.tell(expr('HaveIngredient(Beef, Few) & HaveIngredient(Broccoli, Med) & HaveIngredient(Onion, Few) & HaveIngredient(Pepper, Few) & HaveIngredient(Garlic, Few) & HaveIngredient(Tomato, Med) & HaveTool(Pot)  ==> CanCook(Beef_and_vegetable_soup)'))



    KB.tell(expr('HaveIngredient(Pasta, Much) & HaveIngredient(Tomato, Med) & HaveIngredient(Cheese, Med) & HaveTool(Pan) ==> CanCook(Cheesy_pasta_bake)'))

    KB.tell(expr('HaveIngredient(Pasta, Much) & HaveIngredient(Tomato, Med) & HaveIngredient(Cheese, Med) & HaveTool(Oven)  ==> CanCook(Cheesy_pasta_bake)'))




    KB.tell(expr('HaveIngredient(Beef, Much) & HaveIngredient(Onion, Few) & HaveIngredient(Garlic, Med) & HaveTool(Pan)  ==> CanCook(Beef_and_onion_stir_fry)'))
    
    KB.tell(expr('HaveIngredient(Beef, Much) & HaveIngredient(Onion, Few) & HaveIngredient(Garlic, Med) & HaveTool(Oven)  ==> CanCook(Beef_and_onion_stir_fry)'))



    KB.tell(expr('HaveIngredient(Chicken, Much) & HaveIngredient(Pasta, Much) & HaveIngredient(Cheese, Med) & HaveTool(Oven) ==> CanCook(Cheesy_Chicken_pasta)'))


    KB.tell(expr('HaveIngredient(Chicken, Much) & HaveIngredient(peeper, Med) & HaveIngredient(Onion, Few) & HaveIngredient(Garlic, Few) & HaveTool(Pan) ==> CanCook(Chicken_fajitas)'))
    
    KB.tell(expr('HaveIngredient(Chicken, Much) & HaveIngredient(peeper, Med) & HaveIngredient(Onion, Few) & HaveIngredient(Garlic, Few) &  HaveTool(Oven) ==> CanCook(Chicken_fajitas)'))



    KB.tell(expr('HaveIngredient(Beef, Much) & HaveIngredient(Tomato, Med) & HaveIngredient(Onion, Few) & HaveIngredient(Garlic, Few) & HaveTool(Pan) ==> CanCook(Beef_tacos)'))
    
    
    KB.tell(expr('HaveIngredient(Beef, Much) & HaveIngredient(Tomato, Med) & HaveIngredient(Onion, Few) & HaveIngredient(Garlic, Few) & HaveTool(Oven)  ==> CanCook(Beef_tacos)'))



    KB.tell(expr('HaveIngredient(Rice, Much) & HaveIngredient(Tomato, Med) & HaveIngredient(Cheese, Med) &  HaveTool(Pan) ==> CanCook(Cheesy_tomato_and_rice_casserole)'))
    
    KB.tell(expr('HaveIngredient(Rice, Much) & HaveIngredient(Tomato, Med) & HaveIngredient(Cheese, Med) & HaveTool(Pot)  ==> CanCook(Cheesy_tomato_and_rice_casserole)'))



    KB.tell(expr('HaveIngredient(Broccoli, Much) & HaveIngredient(chesse, Med) & HaveIngredient(Onion, Few) & HaveIngredient(Garlic, Few) & HaveTool(Pot) ==> CanCook(Broccoli_and_cheese_soup)'))



    KB.tell(expr('HaveIngredient(Chicken, Med) & HaveIngredient(Pasta, Much) & HaveIngredient(Cheese, Med) &  HaveTool(Pan) ==> CanCook(Chicken_alfredo_pasta)'))
    
    KB.tell(expr('HaveIngredient(Chicken, Med) & HaveIngredient(Pasta, Much) & HaveIngredient(Cheese, Med) & HaveTool(Pot)==> CanCook(Chicken_alfredo_pasta)'))



    KB.tell(expr('HaveIngredient(Beef, Much) & HaveIngredient(Broccoli, Much) & HaveIngredient(Cheese, Med) & HaveIngredient(Garlic, Few) &  HaveTool(Pan)  ==> CanCook(Beef_and_broccoli_casserole)'))
    
    KB.tell(expr('HaveIngredient(Beef, Much) & HaveIngredient(Broccoli, Much) & HaveIngredient(Cheese, Med) & HaveIngredient(Garlic, Few) &  HaveTool(Pot)  ==> CanCook(Beef_and_broccoli_casserole)'))



    KB.tell(expr('HaveIngredient(Garlic, Few) & HaveIngredient(Cheese, Med) & HaveTool(Pan) ==> CanCook(Cheesy_garlic_bread)'))



    KB.tell(expr('HaveIngredient(Tomato, Med) & HaveIngredient(Cheese, Much) & HaveTool(Pan) ==> CanCook(Tomato_and_cheese_omelet)'))



    KB.tell(expr('HaveIngredient(Beef, Med) & HaveIngredient(Cheese, Much) & HaveIngredient(Onion, Med) & HaveIngredient(Garlic, Few) & HaveTool(Oven) ==> CanCook(Beef_and_cheese_quesadillas)'))



    KB.tell(expr('HaveIngredient(Chicken, Med) & HaveIngredient(Cheese, Much) & HaveIngredient(Onion, Med) & HaveIngredient(Pepper, Few) & HaveTool(Oven) ==> CanCook(Chicken_and_cheese_quesadillas)'))



    # .why here  because if it is a global variable then it will be polluted
    # polluted means we have new facts in our knowledge base that should only last for this cycle
    # when a user enters all information we insert them as facts
    # we get this info from params
    # we query the knowldege base fol_fc_ask() 
    # we return a list of meals 
#    the interface takes care of display
    for param in params:
        KB.tell(expr(param))
    temp = fol_fc_ask(KB, expr('CanCook(y)'))
    
    l = list(temp)

    #print("You have choosed the second option")
   # print(l)
    res= []
    for i in range(len(l)) :
        res.append(str(l[i].get(y)))

    return res




def food_first_option_second_option(params, dish = ""):
    # create kb

    KB = FolKB()
    
    results = []

    # Rules
        # Quantities

    KB.tell(expr('HaveIngredient(x, Much) ==> HaveIngredient(x, Med)'))
    KB.tell(expr('HaveIngredient(x, Med) ==> HaveIngredient(x, Few)'))

        #Queries

    KB.tell(expr('HaveIngredient(Chicken, Med) & HaveIngredient(Broccoli, Med) & HaveIngredient(Onion, Few) & HaveIngredient(Garlic, Few) & ( HaveTool(Pan)  ) ==> CanCook(Chicken_and_broccoli_stir_fry)'))

    KB.tell(expr('HaveIngredient(Chicken, Med) & HaveIngredient(Broccoli, Med) & HaveIngredient(Onion, Few) & HaveIngredient(Garlic, Few) & ( HaveTool(Pot)  ) ==> CanCook(Chicken_and_broccoli_stir_fry)'))


    KB.tell(expr('HaveIngredient(Beef, Med) & HaveIngredient(Broccoli, Med) & HaveIngredient(Onion, Few) & HaveIngredient(Garlic, Few) &  HaveTool(Pan) ==> CanCook(Beef_and_broccoli_stir_fry)'))
    
    
    KB.tell(expr('HaveIngredient(Beef, Med) & HaveIngredient(Broccoli, Med) & HaveIngredient(Onion, Few) & HaveIngredient(Garlic, Few) & HaveTool(Pot)  ==> CanCook(Beef_and_broccoli_stir_fry)'))




    KB.tell(expr('HaveIngredient(Rice, Much) & HaveIngredient(Broccoli, Few) & HaveIngredient(Cheese, Med) &  HaveTool(Pan)==> CanCook(Cheesy_broccoli_and_rice_casserole)'))

    KB.tell(expr('HaveIngredient(Rice, Much) & HaveIngredient(Broccoli, Few) & HaveIngredient(Cheese, Med) & HaveTool(Pot)  ==> CanCook(Cheesy_broccoli_and_rice_casserole)'))




    KB.tell(expr('HaveIngredient(Chicken, Med) & HaveIngredient(Rice, Much) & HaveIngredient(Cheese, Med) & HaveTool(Pan) ==> CanCook(Chicken_and_rice_casserole)'))
    
    KB.tell(expr('HaveIngredient(Chicken, Med) & HaveIngredient(Rice, Much) & HaveIngredient(Cheese, Med) & HaveTool(Pot)  ==> CanCook(Chicken_and_rice_casserole)'))



    KB.tell(expr('HaveIngredient(Beef, Few) & HaveIngredient(Pepper, Med) & HaveIngredient(Rice, Much) & HaveIngredient(Cheese, Few) & HaveTool(Pan)  ==> CanCook(Stuffed_Peppers)'))
    
    KB.tell(expr('HaveIngredient(Beef, Few) & HaveIngredient(Pepper, Med) & HaveIngredient(Rice, Much) & HaveIngredient(Cheese, Few) & HaveTool(Pot)  ==> CanCook(Stuffed_Peppers)'))




    KB.tell(expr('HaveIngredient(Chicken, Few) & HaveIngredient(Broccoli, Med) & HaveIngredient(Onion, Few) & HaveIngredient(Pepper, Few) & HaveIngredient(Garlic, Few) & HaveIngredient(Tomato, Med) & HaveTool(Pot) ==> CanCook(Chicken_and_vegetable_soup)'))
    
    


    KB.tell(expr('HaveIngredient(Beef, Few) & HaveIngredient(Broccoli, Med) & HaveIngredient(Onion, Few) & HaveIngredient(Pepper, Few) & HaveIngredient(Garlic, Few) & HaveIngredient(Tomato, Med) & HaveTool(Pot)  ==> CanCook(Beef_and_vegetable_soup)'))



    KB.tell(expr('HaveIngredient(Pasta, Much) & HaveIngredient(Tomato, Med) & HaveIngredient(Cheese, Med) & HaveTool(Pan) ==> CanCook(Cheesy_pasta_bake)'))

    KB.tell(expr('HaveIngredient(Pasta, Much) & HaveIngredient(Tomato, Med) & HaveIngredient(Cheese, Med) & HaveTool(Oven)  ==> CanCook(Cheesy_pasta_bake)'))




    KB.tell(expr('HaveIngredient(Beef, Much) & HaveIngredient(Onion, Few) & HaveIngredient(Garlic, Med) & HaveTool(Pan)  ==> CanCook(Beef_and_onion_stir_fry)'))
    
    KB.tell(expr('HaveIngredient(Beef, Much) & HaveIngredient(Onion, Few) & HaveIngredient(Garlic, Med) & HaveTool(Oven)  ==> CanCook(Beef_and_onion_stir_fry)'))



    KB.tell(expr('HaveIngredient(Chicken, Much) & HaveIngredient(Pasta, Much) & HaveIngredient(Cheese, Med) & HaveTool(Oven) ==> CanCook(Cheesy_Chicken_pasta)'))


    KB.tell(expr('HaveIngredient(Chicken, Much) & HaveIngredient(peeper, Med) & HaveIngredient(Onion, Few) & HaveIngredient(Garlic, Few) & HaveTool(Pan) ==> CanCook(Chicken_fajitas)'))
    
    KB.tell(expr('HaveIngredient(Chicken, Much) & HaveIngredient(peeper, Med) & HaveIngredient(Onion, Few) & HaveIngredient(Garlic, Few) &  HaveTool(Oven) ==> CanCook(Chicken_fajitas)'))



    KB.tell(expr('HaveIngredient(Beef, Much) & HaveIngredient(Tomato, Med) & HaveIngredient(Onion, Few) & HaveIngredient(Garlic, Few) & HaveTool(Pan) ==> CanCook(Beef_tacos)'))
    
    
    KB.tell(expr('HaveIngredient(Beef, Much) & HaveIngredient(Tomato, Med) & HaveIngredient(Onion, Few) & HaveIngredient(Garlic, Few) & HaveTool(Oven)  ==> CanCook(Beef_tacos)'))



    KB.tell(expr('HaveIngredient(Rice, Much) & HaveIngredient(Tomato, Med) & HaveIngredient(Cheese, Med) &  HaveTool(Pan) ==> CanCook(Cheesy_tomato_and_rice_casserole)'))
    
    KB.tell(expr('HaveIngredient(Rice, Much) & HaveIngredient(Tomato, Med) & HaveIngredient(Cheese, Med) & HaveTool(Pot)  ==> CanCook(Cheesy_tomato_and_rice_casserole)'))



    KB.tell(expr('HaveIngredient(Broccoli, Much) & HaveIngredient(chesse, Med) & HaveIngredient(Onion, Few) & HaveIngredient(Garlic, Few) & HaveTool(Pot) ==> CanCook(Broccoli_and_cheese_soup)'))



    KB.tell(expr('HaveIngredient(Chicken, Med) & HaveIngredient(Pasta, Much) & HaveIngredient(Cheese, Med) &  HaveTool(Pan) ==> CanCook(Chicken_alfredo_pasta)'))
    
    KB.tell(expr('HaveIngredient(Chicken, Med) & HaveIngredient(Pasta, Much) & HaveIngredient(Cheese, Med) & HaveTool(Pot)==> CanCook(Chicken_alfredo_pasta)'))



    KB.tell(expr('HaveIngredient(Beef, Much) & HaveIngredient(Broccoli, Much) & HaveIngredient(Cheese, Med) & HaveIngredient(Garlic, Few) &  HaveTool(Pan)  ==> CanCook(Beef_and_broccoli_casserole)'))
    
    KB.tell(expr('HaveIngredient(Beef, Much) & HaveIngredient(Broccoli, Much) & HaveIngredient(Cheese, Med) & HaveIngredient(Garlic, Few) &  HaveTool(Pot)  ==> CanCook(Beef_and_broccoli_casserole)'))



    KB.tell(expr('HaveIngredient(Garlic, Few) & HaveIngredient(Cheese, Med) & HaveTool(Pan) ==> CanCook(Cheesy_garlic_bread)'))



    KB.tell(expr('HaveIngredient(Tomato, Med) & HaveIngredient(Cheese, Much) & HaveTool(Pan) ==> CanCook(Tomato_and_cheese_omelet)'))



    KB.tell(expr('HaveIngredient(Beef, Med) & HaveIngredient(Cheese, Much) & HaveIngredient(Onion, Med) & HaveIngredient(Garlic, Few) & HaveTool(Oven) ==> CanCook(Beef_and_cheese_quesadillas)'))



    KB.tell(expr('HaveIngredient(Chicken, Med) & HaveIngredient(Cheese, Much) & HaveIngredient(Onion, Med) & HaveIngredient(Pepper, Few) & HaveTool(Oven) ==> CanCook(Chicken_and_cheese_quesadillas)'))



    # .why here  because if it is a global variable then it will be polluted
    # polluted means we have new facts in our knowledge base that should only last for this cycle
    # when a user enters all information we insert them as facts
    # we get this info from params
    # we query the knowldege base fol_fc_ask() 
    # we return a list of meals 
#    the interface takes care of display
    for param in params:
        KB.tell(expr(param))    # This loop add the new facts into the KB, depending on the infos the user has introduce, so we can do the farward chaining
    temp = fol_fc_ask(KB, expr('CanCook(y)'))
    
    l = list(temp)   #delete this libe after you check the validation of the function 
    #print(l)
    if dish  :
       # print("You have choosed the first option \n")
        for i in range(len(l)) :
            if str(l[i].get(y)) == dish :  # I used the function 'str()' because for some reason, the get() function return a variable with the name of the dish, so to do the comparision correctly, I needed to convert it into a string
                return True
        return False
    else :
        print("You have choosed the second option \n")
        for i in range(len(l)) :
            print(str(l[i].get(y)))  

    return "\n"













def food_first_option(params, dish): # This functon is for job to do the backward chaining, the first parameter (params) is a list of the facts(strings) that must be added to our KB, the second one is the dish to check if we can cook or not(string)
    # create kb

    KB = FolKB()
    
    results = []

    # Rules
        # Quantities

    KB.tell(expr('HaveIngredient(x, Much) ==> HaveIngredient(x, Med)'))
    KB.tell(expr('HaveIngredient(x, Med) ==> HaveIngredient(x, Few)'))

        #Queries

    KB.tell(expr('HaveIngredient(Chicken, Med) & HaveIngredient(Broccoli, Med) & HaveIngredient(Onion, Few) & HaveIngredient(Garlic, Few) & ( HaveTool(Pan)  ) ==> CanCook(Chicken_and_broccoli_stir_fry)'))

    KB.tell(expr('HaveIngredient(Chicken, Med) & HaveIngredient(Broccoli, Med) & HaveIngredient(Onion, Few) & HaveIngredient(Garlic, Few) & ( HaveTool(Pot)  ) ==> CanCook(Chicken_and_broccoli_stir_fry)'))


    KB.tell(expr('HaveIngredient(Beef, Med) & HaveIngredient(Broccoli, Med) & HaveIngredient(Onion, Few) & HaveIngredient(Garlic, Few) &  HaveTool(Pan) ==> CanCook(Beef_and_broccoli_stir_fry)'))
    
    
    KB.tell(expr('HaveIngredient(Beef, Med) & HaveIngredient(Broccoli, Med) & HaveIngredient(Onion, Few) & HaveIngredient(Garlic, Few) & HaveTool(Pot)  ==> CanCook(Beef_and_broccoli_stir_fry)'))




    KB.tell(expr('HaveIngredient(Rice, Much) & HaveIngredient(Broccoli, Few) & HaveIngredient(Cheese, Med) &  HaveTool(Pan)==> CanCook(Cheesy_broccoli_and_rice_casserole)'))

    KB.tell(expr('HaveIngredient(Rice, Much) & HaveIngredient(Broccoli, Few) & HaveIngredient(Cheese, Med) & HaveTool(Pot)  ==> CanCook(Cheesy_broccoli_and_rice_casserole)'))




    KB.tell(expr('HaveIngredient(Chicken, Med) & HaveIngredient(Rice, Much) & HaveIngredient(Cheese, Med) & HaveTool(Pan) ==> CanCook(Chicken_and_rice_casserole)'))
    
    KB.tell(expr('HaveIngredient(Chicken, Med) & HaveIngredient(Rice, Much) & HaveIngredient(Cheese, Med) & HaveTool(Pot)  ==> CanCook(Chicken_and_rice_casserole)'))



    KB.tell(expr('HaveIngredient(Beef, Few) & HaveIngredient(Pepper, Med) & HaveIngredient(Rice, Much) & HaveIngredient(Cheese, Few) & HaveTool(Pan)  ==> CanCook(Stuffed_Peppers)'))
    
    KB.tell(expr('HaveIngredient(Beef, Few) & HaveIngredient(Pepper, Med) & HaveIngredient(Rice, Much) & HaveIngredient(Cheese, Few) & HaveTool(Pot)  ==> CanCook(Stuffed_Peppers)'))




    KB.tell(expr('HaveIngredient(Chicken, Few) & HaveIngredient(Broccoli, Med) & HaveIngredient(Onion, Few) & HaveIngredient(Pepper, Few) & HaveIngredient(Garlic, Few) & HaveIngredient(Tomato, Med) & HaveTool(Pot) ==> CanCook(Chicken_and_vegetable_soup)'))
    
    


    KB.tell(expr('HaveIngredient(Beef, Few) & HaveIngredient(Broccoli, Med) & HaveIngredient(Onion, Few) & HaveIngredient(Pepper, Few) & HaveIngredient(Garlic, Few) & HaveIngredient(Tomato, Med) & HaveTool(Pot)  ==> CanCook(Beef_and_vegetable_soup)'))



    KB.tell(expr('HaveIngredient(Pasta, Much) & HaveIngredient(Tomato, Med) & HaveIngredient(Cheese, Med) & HaveTool(Pan) ==> CanCook(Cheesy_pasta_bake)'))

    KB.tell(expr('HaveIngredient(Pasta, Much) & HaveIngredient(Tomato, Med) & HaveIngredient(Cheese, Med) & HaveTool(Oven)  ==> CanCook(Cheesy_pasta_bake)'))




    KB.tell(expr('HaveIngredient(Beef, Much) & HaveIngredient(Onion, Few) & HaveIngredient(Garlic, Med) & HaveTool(Pan)  ==> CanCook(Beef_and_onion_stir_fry)'))
    
    KB.tell(expr('HaveIngredient(Beef, Much) & HaveIngredient(Onion, Few) & HaveIngredient(Garlic, Med) & HaveTool(Oven)  ==> CanCook(Beef_and_onion_stir_fry)'))



    KB.tell(expr('HaveIngredient(Chicken, Much) & HaveIngredient(Pasta, Much) & HaveIngredient(Cheese, Med) & HaveTool(Oven) ==> CanCook(Cheesy_Chicken_pasta)'))


    KB.tell(expr('HaveIngredient(Chicken, Much) & HaveIngredient(peeper, Med) & HaveIngredient(Onion, Few) & HaveIngredient(Garlic, Few) & HaveTool(Pan) ==> CanCook(Chicken_fajitas)'))
    
    KB.tell(expr('HaveIngredient(Chicken, Much) & HaveIngredient(peeper, Med) & HaveIngredient(Onion, Few) & HaveIngredient(Garlic, Few) &  HaveTool(Oven) ==> CanCook(Chicken_fajitas)'))



    KB.tell(expr('HaveIngredient(Beef, Much) & HaveIngredient(Tomato, Med) & HaveIngredient(Onion, Few) & HaveIngredient(Garlic, Few) & HaveTool(Pan) ==> CanCook(Beef_tacos)'))
    
    
    KB.tell(expr('HaveIngredient(Beef, Much) & HaveIngredient(Tomato, Med) & HaveIngredient(Onion, Few) & HaveIngredient(Garlic, Few) & HaveTool(Oven)  ==> CanCook(Beef_tacos)'))



    KB.tell(expr('HaveIngredient(Rice, Much) & HaveIngredient(Tomato, Med) & HaveIngredient(Cheese, Med) &  HaveTool(Pan) ==> CanCook(Cheesy_tomato_and_rice_casserole)'))
    
    KB.tell(expr('HaveIngredient(Rice, Much) & HaveIngredient(Tomato, Med) & HaveIngredient(Cheese, Med) & HaveTool(Pot)  ==> CanCook(Cheesy_tomato_and_rice_casserole)'))



    KB.tell(expr('HaveIngredient(Broccoli, Much) & HaveIngredient(chesse, Med) & HaveIngredient(Onion, Few) & HaveIngredient(Garlic, Few) & HaveTool(Pot) ==> CanCook(Broccoli_and_cheese_soup)'))



    KB.tell(expr('HaveIngredient(Chicken, Med) & HaveIngredient(Pasta, Much) & HaveIngredient(Cheese, Med) &  HaveTool(Pan) ==> CanCook(Chicken_alfredo_pasta)'))
    
    KB.tell(expr('HaveIngredient(Chicken, Med) & HaveIngredient(Pasta, Much) & HaveIngredient(Cheese, Med) & HaveTool(Pot)==> CanCook(Chicken_alfredo_pasta)'))



    KB.tell(expr('HaveIngredient(Beef, Much) & HaveIngredient(Broccoli, Much) & HaveIngredient(Cheese, Med) & HaveIngredient(Garlic, Few) &  HaveTool(Pan)  ==> CanCook(Beef_and_broccoli_casserole)'))
    
    KB.tell(expr('HaveIngredient(Beef, Much) & HaveIngredient(Broccoli, Much) & HaveIngredient(Cheese, Med) & HaveIngredient(Garlic, Few) &  HaveTool(Pot)  ==> CanCook(Beef_and_broccoli_casserole)'))



    KB.tell(expr('HaveIngredient(Garlic, Few) & HaveIngredient(Cheese, Med) & HaveTool(Pan) ==> CanCook(Cheesy_garlic_bread)'))



    KB.tell(expr('HaveIngredient(Tomato, Med) & HaveIngredient(Cheese, Much) & HaveTool(Pan) ==> CanCook(Tomato_and_cheese_omelet)'))



    KB.tell(expr('HaveIngredient(Beef, Med) & HaveIngredient(Cheese, Much) & HaveIngredient(Onion, Med) & HaveIngredient(Garlic, Few) & HaveTool(Oven) ==> CanCook(Beef_and_cheese_quesadillas)'))



    KB.tell(expr('HaveIngredient(Chicken, Med) & HaveIngredient(Cheese, Much) & HaveIngredient(Onion, Med) & HaveIngredient(Pepper, Few) & HaveTool(Oven) ==> CanCook(Chicken_and_cheese_quesadillas)'))



    for param in params:
        KB.tell(expr(param))     # This loop add the new facts into the KB, depending on the infos the user has introduce, so we can do the farward chaining
    temp = fol_fc_ask(KB, expr('CanCook(y)'))
    
    l = list(temp)

    print(l)                    #delete this libe after you check the validation of the function 

    print("You have choosed the first option \n")
    for i in range(len(l)) :
        if str(l[i].get(y)) == dish :     # I used the function 'str()' because for some reason, the get() function return a variable with the name of the dish, so to do the comparision correctly, I needed to convert it into a string
            return True
    return False











if __name__ == "__main__":
    #print(food_first_option_second_option(['HaveIngredient(Chicken, Med)' , 'HaveIngredient(Cheese, Much)' , 'HaveIngredient(Onion, Med)' , 'HaveIngredient(Pepper, Few)' ,'HaveTool(Oven)', 'HaveIngredient(Garlic, Few)', 'HaveIngredient(Beef, Med)'], "Chicken_and_cheese_quesadillas"))

    
    
    print(food_first_option(['HaveIngredient(Chicken, Med)' , 'HaveIngredient(Cheese, Much)' , 'HaveIngredient(Onion, Med)' , 'HaveIngredient(Pepper, Few)' ,'HaveTool(Oven)', 'HaveIngredient(Garlic, Few)', 'HaveIngredient(Beef, Med)'], ""))
    
    food_second_option(['HaveIngredient(Chicken, Med)' , 'HaveIngredient(Cheese, Much)' , 'HaveIngredient(Onion, Med)' , 'HaveIngredient(Pepper, Few)' ,'HaveTool(Oven)', 'HaveIngredient(Garlic, Few)', 'HaveIngredient(Beef, Med)'])

    print('\n')
    
     




#Choose if you wanna work with 2 functions (food_first_option/food_second_option) or you wanna work with just hybred one (food_first_option_second_option)