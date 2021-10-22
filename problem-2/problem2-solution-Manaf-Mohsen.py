# import subprocess
# output = subprocess.getoutput("ls -l")
# print(output)


def validateRecipeWithQuantity(fridge, ingredients):

	# if ingredients.items() in fridge.items() :
	
	for key in list(fridge.keys()):  

		for key2 in list(ingredients.keys()):  

			if key == key2:

				if ingredients[key2] <= fridge[key]:
					print(key2 +' is available you can cook')
				else:
					print(key2 +' is NOT available you can\'t cook')






validateRecipeWithQuantity({'orange':1,'banana':2,'egg':1,'milk':2},{'orange':1,'milk':3})

close1=input("\n \n  press anykey to exit") 