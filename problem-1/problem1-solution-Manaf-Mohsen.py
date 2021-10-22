import subprocess
output = subprocess.getoutput("ls -l")
print(output)


def validateRecipe(fridge, ingredients):


	print(any(i in ingredients for i in fridge))





input1 = input('what is the ingredients ? ')
validateRecipe(['orange','banana'],input1)

close1=input("press anykey to exit") 