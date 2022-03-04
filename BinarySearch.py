arr = [1,2,3,4,5,7,8,14,53,65,78,96,99]
start = 0
end = len(arr)-1
result = 0
searchNum = 99
steps = 1

while start<=end:
    middle = (start + end) // 2
    guess = arr[middle]
    if(guess==searchNum):
        result=guess
        break
    if(searchNum>guess):
        start=middle+1
    else:
        end=middle-1
    steps = steps+1

if (result==0):
    print("Number not found")
else:
    print("steps: " + str(steps))
    print(result)