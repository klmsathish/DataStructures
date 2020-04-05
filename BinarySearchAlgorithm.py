def binarysearch(list_sort,len,x):
    l = 0
    r=len-1
    while l<=r:
        mid=int((l+r)//2)
        if(x==list_sort[mid]):
            print("Entered number is found", x ,"at the index",mid)
            return -1
        elif(x>list_sort[mid]):
            l=mid+1
        elif(x<list_sort[mid]):
            r=mid-1
    print("entered number not found")
    return -1
mylist=[]
c=int(input("enter the size of array:"))
for i in range(c):
    d=int(input("enter the number:"))
    mylist.append(d)
mylist.sort()
print(mylist)
x=int(input("enter the number to search :"))
binarysearch(mylist,c,x)