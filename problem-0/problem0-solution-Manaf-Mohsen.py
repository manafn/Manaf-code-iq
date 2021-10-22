



def whereIsMyFood (fridge,item):

    storage = []

    for i, v in enumerate(fridge,start=0):

        

        if v == item :

            storage.append([v,i])
            
            

            

        elif v == fridge[-1] and not storage  :
            storage.append(-1)

    print(storage)




input1 = input('what is you are locking for ? ')
whereIsMyFood(['banana','orange','apple','orange','tomato'], input1)

close1=input("press anykey to exit") 