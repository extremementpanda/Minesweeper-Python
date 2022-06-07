#Draw grid
def grid(n):
    #Top
    global x
    for row in range(n):

        #Top
        i=""
        if row == 0 :
            for col in range(n):
                i = i + "------"
            print(i)

        #Side
        i = ""
        for col in range(n):
            i = i + "|     "
        print(i + "|")   

        #Zeros inside grids
        i = ""
        x = 0
        for col in range(n):
            i = i + "|  " + str(x) + "  "
        print(i + "|")    

        #Bottom 
        i = ""
        for col in range(n):
            i = i + "|_____"
        print(i + "|")    




