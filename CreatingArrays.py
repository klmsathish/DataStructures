import array as arr
int = arr.array('i',[1,2,3])
char = arr.array('u',['s','a','t','h','i','s','h'])
print(int)
print(char)
print("the new created int array is :", end ="")
for a in int:
    print(a)
print("the new created char array is :", end ="")
for a in char:
    print(a)


    # 'b'         signed integer     1   
    # 'B'         unsigned integer   1   
    # 'u'         Unicode character  2  
    # 'h'         signed integer     2   
    # 'H'         unsigned integer   2   
    # 'i'         signed integer     2   
    # 'I'         unsigned integer   2   
    # 'l'         signed integer     4   
    # 'L'         unsigned integer   4   
    # 'q'         signed integer     8  
    # 'Q'         unsigned integer   8  
    # 'f'         floating point     4   
    # 'd'         floating point     8   

