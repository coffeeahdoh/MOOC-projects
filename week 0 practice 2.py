#miles to feet
mi = 13
ft = 5280 * mi
print ft

#total seconds
h = 15
m = 15
s = 300
total_seconds = (h * 60 ** 2) + (m * 60) + s
print total_seconds

#perimeter
w = 30
h = 30
perimeter = 2 * w + 2 * h
print perimeter

#area
area = w * h
print area

#area circle
PI = 3.14
r = 10
area_cir = PI * r ** 2
print area_cir

#compounding interest
present_value = 1000
annual_rate = 7
years = 10
future_value = present_value * (1.00 + 0.01 * annual_rate) ** 10
print future_value

#name tag
first_name = "Michael"
last_name = "Confiado"
name_tag = "My name is " + first_name + " " + last_name + "."
print name_tag

#age
name = first_name + " " + last_name
age = 32
statement = name + " is " + str(age) + " years old."
print statement

#distance
x0, y0 = -2, 4
x1, y1 = 1, 6
distance = ((x0 - x1) ** 2 + (y0 - y1) ** 2) ** 0.5
print distance

#Heron's tri area
x2, y2 = 2, 1
a = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
b = ((x0 - x2) ** 2 + (y0 - y2) ** 2) ** 0.5
c = distance
s = 0.5 * ( a + b + c )
area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
print area














