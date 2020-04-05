def insertionsort(array):
       for index in range(1, len(array)):
            currentValue = array[index]
            currentPosition = index
            while currentPosition > 0 and array[currentPosition - 1] > currentValue:
                array[currentPosition] = array[currentPosition -1]
                currentPosition = currentPosition - 1
            array[currentPosition] = currentValue

my_ar = []
max = int(input("Enter the range"))
for i in range(max):
    data = int(input("Enter Data : "))
    my_ar.append(data)
insertionsort(my_ar)
print(my_ar)

