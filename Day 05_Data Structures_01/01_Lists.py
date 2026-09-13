# Lists application:

vehicle = ["sedan","SUV","XUV"]
print(vehicle)
print(vehicle[0])
 

# Append
vehicle.append("jeep")
print(vehicle)

# Insertion
vehicle.insert(1, "BMW")   # Add at position 1
print (vehicle)

# Removal
vehicle.remove("jeep")     # remove by value 
print(vehicle)

# POP : Remove the last element
vehicle.pop()             # Remove the last element
print(vehicle)

# Length of the list:
print(len(vehicle))
print(vehicle.sort())


# Slicing a list:

num = [1,2,3,4,5,6,7,8,9,10]
print(num[0:5])  # 1,2,3,4
print(num[5:])   # 6,7,8,9,10
print(num[:5])   # 1,2,3,4
print(num[::2]) # Prints Steps of gap here (2-1) = gap of 1 


# Comprehensive Way :! line

num = [i for i in range(1,6)]
print(num)   # 1, 2, 3, 4, 5 

# Even numbers
num = [i for i in range (0,6) if i %2 ==0 ] 
print (num)

#Squares 
num = [i*i for i in range (0,6)]
print (num)
 
