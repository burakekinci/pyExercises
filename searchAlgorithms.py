from time import perf_counter
import math

array = []

for i in range(1000000):
    array.append(i)


def linearSearch(Arr, Value):
    start_time = perf_counter()
    for i in range(len(Arr)):
        if Arr[i] == Value:
            print ("Linear Position index: ",i)
            stop_time = perf_counter()
            print(stop_time-start_time)
            return

def binarySearch(Arr, Value):
    start_time = perf_counter()
    leftSpot = 0
    rightSpot = len(Arr)-1
   
    while (leftSpot <= rightSpot):
        midSpot = (leftSpot + rightSpot) // 2
        if Arr[midSpot] != Value:
            if Arr[midSpot] >=  Value:
                rightSpot = midSpot
            else:
                leftSpot = midSpot
        else:
            print("Binary Position index: ",midSpot)
            stop_time = perf_counter()
            print(stop_time-start_time)
            return

def jumpSearch(Arr, Value):
    start_time = perf_counter()
    n = len(Arr)
    step = int(math.sqrt(n))
    prev = 0
    endOfBlock = prev+step-1
    
    while prev != n-1:
        if Arr[endOfBlock] < Value:
            prev += step
            endOfBlock += step
        elif Arr[endOfBlock] >= Value:
            if Arr[prev] == Value:
                print(prev)
                stop_time = perf_counter()
                print(stop_time-start_time)
                return
            prev +=1 
        


   


jumpSearch(array,1000)
binarySearch(array,1000)
print("--------------------------")

jumpSearch(array,900000)
binarySearch(array,900000)


