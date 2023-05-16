# INGREDIENT TREATMENT FUNCTION

def checkQuanti(ingredinet, amount):
    
    quantity = "Nothing"
    
    if ingredinet == "Chicken" :
        if amount < 100 :
            quantity = "Few"
        elif amount < 300 :
            quantity = "Med"
        else :
            quantity = "Much"
        
    elif ingredinet == "Rice" :
        if amount < 200 :
            quantity = "Few"
        elif amount < 400 :
            quantity = "Med"
        else :
            quantity = "Much"

    elif ingredinet == "Broccoli" :
        if amount < 150 :
            quantity = "Few"
        elif amount < 300 :
            quantity = "Med"
        else :
            quantity = "Much"
        
    elif ingredinet == "Pepper" :
        if amount < 200 :
            quantity = "Few"
        elif amount < 400 :
            quantity = "Med"
        else :
            quantity = "Much"
        
    elif ingredinet == "Onion" :
        if amount < 100 :
            quantity = "Few"
        elif amount < 300 :
            quantity = "Med"
        else :
            quantity = "Much"

    elif ingredinet == "Garlic" :
        if amount < 50 :
            quantity = "Few"
        elif amount < 100 :
            quantity = "Med"
        else :
            quantity = "Much"
        
    elif ingredinet == "Tomato" :
        if amount < 250 :
            quantity = "Few"
        elif amount < 400 :
            quantity = "Med"
        else :
            quantity = "Much"
    
    elif ingredinet == "Beef" :
        if amount < 150 :
            quantity = "Few"
        elif amount < 400 :
            quantity = "Med"
        else :
            quantity = "Much"

    elif ingredinet == "Pasta" :
        if amount < 200 :
            quantity = "Few"
        elif amount < 400 :
            quantity = "Med"
        else :
            quantity = "Much"
        
    elif ingredinet == "Cheese" :
        if amount < 150 :
            quantity = "Few"
        elif amount < 400 :
            quantity = "Med"
        else :
            quantity = "Much"

    KB.tell(expr(f'HaveIngredient({ingredinet}, {quantity})')) 


# TOOL FUNCTION :

def Have_tool(tool) :

    KB.tell(expr(f'HaveTool({tool})'))


   

