list = [1,2,3,4,5] # In binary search, the list is always sorted

first = 1
last = len(list)
found = False
search_data = int(input("Enter the data to search: "))

while last>=first and not found:
    mid = int((first + last)/2)
    if search_data == mid:
        found = True

    elif search_data > mid:
        first = mid + 1

    else:
        last = mid - 1

if found == True:
    print("Data Found!!")

else:
    print("Data not available")
