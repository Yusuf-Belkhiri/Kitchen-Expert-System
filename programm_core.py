# INGREDIENT TREATMENT FUNCTION

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


   
def fnct():
    available_dishes = []
    for dish in dishes:
        available_dishes.append(list(KB.ask_generator(expr"")))