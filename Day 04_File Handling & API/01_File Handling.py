# Writing to a file 
f = open ("sanchal.txt", "w")
f.write("My name is Sanchal.")
f.close()

print("File creation successful.........")


# Reading A file 
f = open ("sanchal.txt", "r")
content = f.read()
print(content)
f.close()


# Appending a file 
f = open ("sanchal.txt", "a")
f.write("\n I like Pyhton")
f.close()


#------------------------------------------------------------------------------------------

with open("student.txt","w") as f:
    f.write()




#------------------------------------------------------------------------------------------

# The old manual way:
file = open("Example.txt","r")
try:
    data = file.read()
finally:
    file.close()


with open("Example.txt","r") as file:
    data = file.read()
    print(data)


