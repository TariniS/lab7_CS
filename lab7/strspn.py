#Tarini Srikanth
#Instructor: Clark Turner
#Project: Lab 7

def my_strspn(str1,str2):
    length=0
    strList1 = list(str1)
    strList2= list(str2)
    #initializing the arrays
    count=0
    newList = []
    for char2 in strList2:
        #goes through string list
        for char1 in strList1:
            #goes through list 1
            if char2==char1:
                newList.append(char1)
                #adding to new list if it equals the char
    for i in range(len(strList1)):
        if strList1[i] not in newList:
            #if the char is not in the new list, end the for loop
            break
        else:
            count=count+1
    return count
        

