friends = []

print("The current array 'friends' contains these names",friends)

for numb in range(1,101):
    extra_func = str(input("Would you like to find, add or delete any names from this array?: "))
    
    if extra_func == "add":
        add_first = str(input("What first name would you like to add?: "))
        add_last = str(input("What surname would you like to add?: "))
        friends.append([add_first, add_last])
        print(friends)
    
    if extra_func == "delete":
        del_first = str(input("What first name would you like to delete?: "))
        del_last = str(input("What surname would you like to delete?: "))
        found = False
        index = 0 
    
        while found == False and index <= len(friends) - 1: 
            if del_first == friends[index][0] and del_last == friends[index][1]:
                found = True
                variable = index
            index = index + 1 
        del friends[variable]
        print(friends)
    
    if extra_func == "find":
        find_first = str(input("What first name would you like to find?: "))
        find_last = str(input("What surname would you like to find?: "))
        found = False
        index = 0 
        
        while found == False and index <= len(friends) - 1: 
            if find_first == friends[index][0] and find_last == friends[index][1]:
                found = True
            index = index + 1 
       
        if found == True:
           print("The name",find_first, find_last,"is in the array")
        else:
            print("The name",find_first, find_last,"is not in the array")
            
