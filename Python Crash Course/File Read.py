

employee_file = open("Employees.txt", "a") # r for read, w for write will overwrite, a for append

print(employee_file.readable())
# print(employee_file.read())
# print(employee_file.readline())
# print(employee_file.readlines())



# _________________________________________________
employee_file.write("\nBarry - Marketing")

employee_file.close()

# _________________________________________________

new_file = open("index.html", 'w')

new_file.write("<p> This is an HTML file</p>")