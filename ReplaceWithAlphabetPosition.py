#a=map(chr, range(97, 123))
#print a

def alphabet_position(text):
    dic=dict() #creates a dictionary
    new_list=[] # An empty list
    a=map(chr, range(97, 123)) # alphabet for a to z
    for i in range(len(a)): #index of a list starts from 0 so add one to it to get 26
        dic[a[i]]=(i+1) #This ensures that "a" starts from 1 and not o
    convert_lower=text.lower() # convert all the strings passed as a parameter to lower case
    split_string=convert_lower.split() #split it to get a list
    join= list("".join(split_string)) #join the slited list
    p ="".join([i for i in join if i.isalpha()]) #get raid of all non alphabetical characters
    for i in range(len(p)): #loop through the lenght of the parameter text
        if (dic[p[i]]): #it it appears in the dictionary
            new_list.append(((dic[p[i]])))#append the value of the key to new_list
    new_list=str(new_list).strip('[]') #strip the list of the brackkes
    final_String=new_list.replace(",","")# replace the comma with no space
    return final_String #return the final string








print (alphabet_position("I am my sarpong and yes this is python programming language who the hell do you think you are ."))
