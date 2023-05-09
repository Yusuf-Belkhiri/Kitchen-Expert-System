#Ingredients

BC.tell(expr('Ingredient(Chicken)'))
BC.tell(expr('Ingredient(Rice)'))
BC.tell(expr('Ingredient(Broccoli)'))
BC.tell(expr('Ingredient(pepper)'))
BC.tell(expr('Ingredient(Onion)'))
BC.tell(expr('Ingredient(Garlic)'))
BC.tell(expr('Ingredient(Tomato)'))
BC.tell(expr('Ingredient(beef)'))
BC.tell(expr('Ingredient(Pasta)'))
BC.tell(expr('Ingredient(Cheese)'))


#Queries


BC.tell(expr('HaveIngredient(Chicken, Med) & HaveIngredient(Broccoli, Med) & HaveIngredient(Onion, Few) & HaveIngredient(Garlic, Few) & ( HaveTool(Pan) / HaveTool(Pot) ) ==> CanCook(Chicken_and_broccoli_stir_fry)'))


BC.tell(expr('HaveIngredient(Beef, Med) & HaveIngredient(Broccoli, Med) & HaveIngredient(Onion, Few) & HaveIngredient(Garlic, Few) & ( HaveTool(Pan) / HaveTool(Pot) ) ==> CanCook(Beef_and_broccoli_stir_fry)'))




BC.tell(expr('HaveIngredient(Rice, Much) & HaveIngredient(Broccoli, Few) & HaveIngredient(Cheese, Med) & ( HaveTool(Pan) / HaveTool(Pot) ) ==> CanCook(Cheesy_broccoli_and_rice_casserole)'))




BC.tell(expr('HaveIngredient(Chicken, Med) & HaveIngredient(Rice, Much) & HaveIngredient(Cheese, Med) & ( HaveTool(Pan) / HaveTool(Pot) ) ==> CanCook(Chicken_and_rice_casserole)'))



BC.tell(expr('HaveIngredient(Beef, Few) & HaveIngredient(Pepper, Med) & HaveIngredient(Rice, Much) & HaveIngredient(Cheese, Few) & ( HaveTool(Pan) / HaveTool(Pot) ) ==> CanCook(Stuffed_peppers)'))




BC.tell(expr('HaveIngredient(Chicken, Few) & HaveIngredient(Broccoli, Med) & HaveIngredient(Onion, Few) & HaveIngredient(Pepper, Few) & HaveIngredient(Garlic, Few) & HaveIngredient(Tomato, Med) & HaveTool(Pot) ==> CanCook(Chicken_and_vegetable_soup)'))


BC.tell(expr('HaveIngredient(Beef, Few) & HaveIngredient(Broccoli, Med) & HaveIngredient(Onion, Few) & HaveIngredient(Pepper, Few) & HaveIngredient(Garlic, Few) & HaveIngredient(Tomato, Med) & HaveTool(Pot)  ==> CanCook(Beef_and_vegetable_soup)'))



BC.tell(expr('HaveIngredient(Pasta, Much) & HaveIngredient(Tomato, Med) & HaveIngredient(Cheese, Med) & ( HaveTool(Pan) / HaveTool(Oven) ) ==> CanCook(Cheesy_pasta_bake)'))




BC.tell(expr('HaveIngredient(Beef, Much) & HaveIngredient(Onion, Few) & HaveIngredient(Garlic, Med) & ( HaveTool(Pan) / HaveTool(Oven) ) ==> CanCook(Beef_and_onion_stir_fry)'))



BC.tell(expr('HaveIngredient(Chicken, Much) & HaveIngredient(Pasta, Much) & HaveIngredient(Cheese, Med) & HaveTool(Oven) ==> CanCook(Cheesy_Chicken_pasta)'))



BC.tell(expr('HaveIngredient(Chicken, Much) & HaveIngredient(peeper, Med) & HaveIngredient(Onion, Few) & HaveIngredient(Garlic, Few) & ( HaveTool(Pan) / HaveTool(Oven) ) ==> CanCook(Chicken_fajitas)'))



BC.tell(expr('HaveIngredient(Beef, Much) & HaveIngredient(Tomato, Med) & HaveIngredient(Onion, Few) & HaveIngredient(Garlic, Few) & ( HaveTool(Pan) / HaveTool(Oven) ) ==> CanCook(Beef_tacos)'))



BC.tell(expr('HaveIngredient(Rice, Much) & HaveIngredient(Tomato, Med) & HaveIngredient(Cheese, Med) & ( HaveTool(Pan) / HaveTool(Pot) ) ==> CanCook(Cheesy_tomato_and_rice_casserole)'))



BC.tell(expr('HaveIngredient(Broccoli, Much) & HaveIngredient(chesse, Med) & HaveIngredient(Onion, Few) & HaveIngredient(Garlic, Few) & HaveTool(Pot) ==> CanCook(Broccoli_and_cheese_soup)'))



BC.tell(expr('HaveIngredient(Chicken, Med) & HaveIngredient(Pasta, Much) & HaveIngredient(Cheese, Med) & ( HaveTool(Pan) / HaveTool(Pot) ) ==> CanCook(Chicken_alfredo_pasta)'))



BC.tell(expr('HaveIngredient(Beef, Much) & HaveIngredient(Broccoli, Much) & HaveIngredient(Cheese, Med) & HaveIngredient(Garlic, Few) & ( HaveTool(Pan) / HaveTool(Pot) ) ==> CanCook(Beef_and_broccoli_casserole)'))



BC.tell(expr('HaveIngredient(Garlic, Few) & HaveIngredient(Cheese, Med) & HaveTool(Pan) ==> CanCook(Cheesy_garlic_bread)'))



BC.tell(expr('HaveIngredient(Tomato, Med) & HaveIngredient(Cheese, Much) & HaveTool(Pan) ==> CanCook(Tomato_and_cheese_omelet)'))



BC.tell(expr('HaveIngredient(Beef, Med) & HaveIngredient(Cheese, Much) & HaveIngredient(Onion, Med) & HaveIngredient(Garlic, Few) & HaveTool(Oven) ==> CanCook(Beef_and_cheese_quesadillas)'))



BC.tell(expr('HaveIngredient(Chicken, Med) & HaveIngredient(Cheese, Much) & HaveIngredient(Onion, Med) & HaveIngredient(Pepper, Few) & HaveTool(Oven) ==> CanCook(Chicken_and_cheese_quesadillas)'))


