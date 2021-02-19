

#function to covert to integer
def validateInteger(passes,defer,fail):
    passes = int(passes or "0")
    defer = int(defer or "0")
    fail =int(fail or "0")
    return passes,defer,fail
    
#function to validate range
def validateRange(passes,defer,fail):
    if(passes%20 == 0 and defer%20 ==0 and fail%20 ==0):
       return True
    return False

#function to get validate total
def validateTotal(passes,defer,fail):
    total = passes+defer+fail
    if (passes <= 120 and defer <= 120 and fail <=120 and total == 120): #check to conditions
        return True
    return False
    
#function in calculate progression outcome
def calculateProgressionOutcome(passes,defer,fail):
    if (passes==120 and defer==0 and fail==0 ):
        print("Progress")
    elif(passes==100):
        print("Progress-module-trailer")
    elif(fail>=80):
        print("Exclude")
    elif(fail<=60):
        print("Do not Progress-module retriever")

#start
passes =input('Enter passes marks:')#take input from user
defer =input('Enter defer marks:') #take input from user
fail =input('Enter fail marks:')  #take input from user

try:    
    passes,defer,fail = validateInteger(passes,defer,fail) #call validate integer function
except:
    print("Integers required")
else:
    if(validateRange(passes,defer,fail)): #call validate range function
        if(validateTotal(passes,defer,fail)):
            calculateProgressionOutcome(passes,defer,fail) #call calculate progression outcome 
        else:
            print("Total incorrect")
    else:
        print("Range error")
    
   

