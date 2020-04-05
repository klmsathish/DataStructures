import array as arr
float = arr.array('d',[10.24,10.54,67.34,99.43])            #creating a float array (d - double)
float.insert(4,42.67)                                       #inserting(position,value)
float.insert(5,78.42)
float.append(456.12)                                        #same as insertion without position defining(just value) 
float.remove(10.54)                                         #removing just giving the value
print("Index : ",float.index(67.34))                                          #accessiing the required index
 
print("Updated array : [ ",end = "")
for a in float:
    print(a,end = " ")
print(']')