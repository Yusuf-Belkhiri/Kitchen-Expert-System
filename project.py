from logic import *

#Ingredients

# KB.tell(expr('Ingredient(Chicken)'))
# KB.tell(expr('Ingredient(Rice)'))
# KB.tell(expr('Ingredient(Broccoli)'))
# KB.tell(expr('Ingredient(Pepper)'))
# KB.tell(expr('Ingredient(Onion)'))
# KB.tell(expr('Ingredient(Garlic)'))
# KB.tell(expr('Ingredient(Tomato)'))
# KB.tell(expr('Ingredient(Beef)'))
# KB.tell(expr('Ingredient(Pasta)'))
# KB.tell(expr('Ingredient(Cheese)'))


#Youcef code :


# Tools
# KB.tell(expr('Tool(Pan)'))
# KB.tell(expr('Tool(Pot)'))
# KB.tell(expr('Tool(Grater)'))
# KB.tell(expr('Tool(CuttingBoard)'))
# KB.tell(expr('Tool(Mixer)'))

# # Quantities
# KB.tell(expr('Quantity(Few)'))
# KB.tell(expr('Quantity(Med)'))
# KB.tell(expr('Quantity(Much)'))

# #Ingredients




#     # Recipies
# # KB.tell(expr('HaveIngredient(Tomato, Medium) & HaveTool(Pan) & Have(Pepper, Much) ==> CanMake(Hmiss)'))  



global KB 
KB = FolKB()


# Rules
    # Quantities

KB.tell(expr('HaveIngredient(x, Much) ==> HaveIngredient(x, Med)'))
KB.tell(expr('HaveIngredient(x, Med) ==> HaveIngredient(x, Few)'))

    #Queries

KB.tell(expr('HaveIngredient(Chicken, Med) & HaveIngredient(Broccoli, Med) & HaveIngredient(Onion, Few) & HaveIngredient(Garlic, Few) & ( HaveTool(Pan) / HaveTool(Pot) ) ==> CanCook(Chicken_and_broccoli_stir_fry)'))


KB.tell(expr('HaveIngredient(Beef, Med) & HaveIngredient(Broccoli, Med) & HaveIngredient(Onion, Few) & HaveIngredient(Garlic, Few) & ( HaveTool(Pan) / HaveTool(Pot) ) ==> CanCook(Beef_and_broccoli_stir_fry)'))




KB.tell(expr('HaveIngredient(Rice, Much) & HaveIngredient(Broccoli, Few) & HaveIngredient(Cheese, Med) & ( HaveTool(Pan) / HaveTool(Pot) ) ==> CanCook(Cheesy_broccoli_and_rice_casserole)'))




KB.tell(expr('HaveIngredient(Chicken, Med) & HaveIngredient(Rice, Much) & HaveIngredient(Cheese, Med) & ( HaveTool(Pan) / HaveTool(Pot) ) ==> CanCook(Chicken_and_rice_casserole)'))



KB.tell(expr('HaveIngredient(Beef, Few) & HaveIngredient(Pepper, Med) & HaveIngredient(Rice, Much) & HaveIngredient(Cheese, Few) & ( HaveTool(Pan) / HaveTool(Pot) ) ==> CanCook(Stuffed_Peppers)'))




KB.tell(expr('HaveIngredient(Chicken, Few) & HaveIngredient(Broccoli, Med) & HaveIngredient(Onion, Few) & HaveIngredient(Pepper, Few) & HaveIngredient(Garlic, Few) & HaveIngredient(Tomato, Med) & HaveTool(Pot) ==> CanCook(Chicken_and_vegetable_soup)'))


KB.tell(expr('HaveIngredient(Beef, Few) & HaveIngredient(Broccoli, Med) & HaveIngredient(Onion, Few) & HaveIngredient(Pepper, Few) & HaveIngredient(Garlic, Few) & HaveIngredient(Tomato, Med) & HaveTool(Pot)  ==> CanCook(Beef_and_vegetable_soup)'))



KB.tell(expr('HaveIngredient(Pasta, Much) & HaveIngredient(Tomato, Med) & HaveIngredient(Cheese, Med) & ( HaveTool(Pan) / HaveTool(Oven) ) ==> CanCook(Cheesy_pasta_bake)'))




KB.tell(expr('HaveIngredient(Beef, Much) & HaveIngredient(Onion, Few) & HaveIngredient(Garlic, Med) & ( HaveTool(Pan) / HaveTool(Oven) ) ==> CanCook(Beef_and_onion_stir_fry)'))



KB.tell(expr('HaveIngredient(Chicken, Much) & HaveIngredient(Pasta, Much) & HaveIngredient(Cheese, Med) & HaveTool(Oven) ==> CanCook(Cheesy_Chicken_pasta)'))



KB.tell(expr('HaveIngredient(Chicken, Much) & HaveIngredient(peeper, Med) & HaveIngredient(Onion, Few) & HaveIngredient(Garlic, Few) & ( HaveTool(Pan) / HaveTool(Oven) ) ==> CanCook(Chicken_fajitas)'))



KB.tell(expr('HaveIngredient(Beef, Much) & HaveIngredient(Tomato, Med) & HaveIngredient(Onion, Few) & HaveIngredient(Garlic, Few) & ( HaveTool(Pan) / HaveTool(Oven) ) ==> CanCook(Beef_tacos)'))



KB.tell(expr('HaveIngredient(Rice, Much) & HaveIngredient(Tomato, Med) & HaveIngredient(Cheese, Med) & ( HaveTool(Pan) / HaveTool(Pot) ) ==> CanCook(Cheesy_tomato_and_rice_casserole)'))



KB.tell(expr('HaveIngredient(Broccoli, Much) & HaveIngredient(chesse, Med) & HaveIngredient(Onion, Few) & HaveIngredient(Garlic, Few) & HaveTool(Pot) ==> CanCook(Broccoli_and_cheese_soup)'))



KB.tell(expr('HaveIngredient(Chicken, Med) & HaveIngredient(Pasta, Much) & HaveIngredient(Cheese, Med) & ( HaveTool(Pan) / HaveTool(Pot) ) ==> CanCook(Chicken_alfredo_pasta)'))



KB.tell(expr('HaveIngredient(Beef, Much) & HaveIngredient(Broccoli, Much) & HaveIngredient(Cheese, Med) & HaveIngredient(Garlic, Few) & ( HaveTool(Pan) / HaveTool(Pot) ) ==> CanCook(Beef_and_broccoli_casserole)'))



KB.tell(expr('HaveIngredient(Garlic, Few) & HaveIngredient(Cheese, Med) & HaveTool(Pan) ==> CanCook(Cheesy_garlic_bread)'))



KB.tell(expr('HaveIngredient(Tomato, Med) & HaveIngredient(Cheese, Much) & HaveTool(Pan) ==> CanCook(Tomato_and_cheese_omelet)'))



KB.tell(expr('HaveIngredient(Beef, Med) & HaveIngredient(Cheese, Much) & HaveIngredient(Onion, Med) & HaveIngredient(Garlic, Few) & HaveTool(Oven) ==> CanCook(Beef_and_cheese_quesadillas)'))



KB.tell(expr('HaveIngredient(Chicken, Med) & HaveIngredient(Cheese, Much) & HaveIngredient(Onion, Med) & HaveIngredient(Pepper, Few) & HaveTool(Oven) ==> CanCook(Chicken_and_cheese_quesadillas)'))








#TREATMENT PART :
