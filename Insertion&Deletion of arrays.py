import array as arr
int = arr.array('i',[1,2,9])
int.insert(3,6)                                                #(position,value)
print("After insertion :", end ="")
for a in int:
    print(a)

import array as arr
int = arr.array('i',[1,2,9])
int.remove(9)                                                  #(value to be deleted)
print("After deletion :", end ="")
for a in int:
    print(a)

                                   