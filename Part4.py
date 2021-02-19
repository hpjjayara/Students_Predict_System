
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
    
#function to calculate progression outcome
def calculateProgressionOutcome(passes,defer,fail):
    global progress,trailing,excluded,retriever
    if (passes==120 and defer==0 and fail==0 ):
        print("Progress")
        progress= progress+1
    elif(passes==100):
        print("Progress-module-trailer")
        trailing=trailing+1
    elif(fail>=80):
        print("Exclude")
        excluded=excluded+1
    elif(fail<=60):
        print("Do not Progress-module retriever")
        retriever=retriever+1

#function to check user wants to quit
def isQuit(passes):
    if (passes=="q"):
        return True
    else:
        return False

#function to display histogram
def showHistogram(progress,trailing,excluded,retriever):
    print("Progress ",progress,":\t",end=' ')
    for j in range(0, progress):
        print("*", end=' ')
    print("\n")
                    
            
    print("trailing ",trailing,":\t",end=' ')
    for j in range(0, trailing):
        print("*", end=' ')
    print("\n")
                        
            
    print("retriever",retriever,":\t",end=' ')
    for j in range(0, retriever):
        print("*", end=' ')
    print("\n")
                        

    print("excluded ",excluded,":\t",end=' ')
    for j in range(0, excluded):
        print("*", end=' ')
    print("\n")

#function to display vertical histogram
def showVerticalHistogram(progress,trailing,excluded,retriever):
     header = ['progress','trailing','retriever','excluded']
     print(' '.join(header))
     for x in range(max(progress,trailing,retriever,excluded)):
        print(' {0}     {1}     {2}     {3}'.format(        #have to line up(format position)
            '*' if x < progress  else '  ',
            '   *' if x < trailing  else '   ',
            '     *' if x < retriever else '    ',
            '      *' if x < excluded  else '   '))

#function to add a list
def getUserInput():
    my_list=[]
    print("Enter student's credite row by row as passes, defer, fail:")

    while True:
        values=input()
        if values=='q':
            break
        else:
            
            # conver to the list
            element = values.split (",")
            my_list.append(element)
            
            print(element)
    return my_list
           
#start
progress=0
trailing=0
retriever=0
excluded=0 
list=getUserInput()
for element in list:
    if len(element)==3:
    
        passes=element[0]
        defer=element[1]
        fail=element[2]
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
        
    
    else:
        pass

showHistogram(progress,trailing,excluded,retriever)
showVerticalHistogram(progress,trailing,excluded,retriever)

   
        
   

