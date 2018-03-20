pi = 3.14159
radius = 2.2
# area of circle equation <- this is a comment
area = pi*(radius**2)
print(area)

# change values of radius <- another comment
# use comments to help others understand what you are doing in code
radius = radius + 1
print(area)     # area doesn't change
area = pi*(radius**2)
print(area)


#############################
#### COMMENTING LINES #######
#############################
# to comment MANY lines at a time, highlight all of them then CTRL+1
# do CTRL+1 again to uncomment them
# try it on the next few lines below!
#
#area = pi*(radius**2)
#print(area)
#radius = radius + 1
#area = pi*(radius**2)
#print(area)

#############################
#### AUTOCOMPLETE #######
#############################
# Spyder can autocomplete names for you
# start typing a variable name defined in your program and hit tab 
# before you finish typing -- try it below
variable=2
variable

# define a variable
a_very_long_variable_name_dont_name_them_this_long_pls = 0

# below, start typing a_ve then hit tab... cool, right!
# use autocomplete to change the value of that variable to 1
a_very_long_variable_name_dont_name_them_this_long_pls
# use autocomplete to write a line that prints the value of that long variable
# notice that Spyder also automatically adds the closed parentheses for you!

print("type(1)")
print(type(1))
print(type(0))
print(type(3.0))
print(type(12343.1230))
print(type('a'))
print(type("a"))
print(type(True))
print(type(False))

print(float(3)) # Int 3 is converted into float 3.0
print(int(5.9)) # float 5.9 will be converted into int 5


3+5 #The result won't be displayed in the console
print(4+5)

varA = 1
varB = "Manju"
if type(varA) == str or type(varB) == str:
    print('string involved')
elif varA > varB:
    print('bigger')
elif varA == varB:
    print('equal')
else:
    # If none of the above conditions are true,
    # it must be the case that varA < varB
    print('smaller')