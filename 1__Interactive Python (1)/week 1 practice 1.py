#convert miles to feet
def miles_to_feet(miles):
    feet = 5280 * miles
    return feet

#test miles_to_feet
feet_test1 = miles_to_feet(1)
feet_test2 = miles_to_feet(5280)
print feet_test1, feet_test2

#get total seconds from hours, minutes, and seconds
def total_seconds(hours, minutes, seconds):
    total = (hours * 60 ** 2) + (minutes * 60) + seconds
    return total

#test total_seconds
total_test1 = total_seconds(1, 0, 0)
total_test2 = total_seconds(24, 24, 24)
print total_test1, total_test2

#calculate rectangle perimeter
def rectangle_perimeter(width, height):
    perimeter = 2 * width + 2 * height
    return perimeter

#test rectangle_perimeter
perimeter_test1 = rectangle_perimeter(5, 5)
perimeter_test2 = rectangle_perimeter(10, 5)
print perimeter_test1, perimeter_test2

# calculate rectangle area
def rectangle_area(width, height):
    area = width * height
    return area

# test rectangle_area
area_test1 = rectangle_area(5, 5)
area_test2 = rectangle_area(10, 5)
print area_test1, area_test2

# calculate circle circumference
import math
def circle_circumference(radius):
    circum = 2 * math.pi * radius
    return circum

# test circle_circumference
circ_test1 = circle_circumference(100)
circ_test2 = circle_circumference(3)
print circ_test1, circ_test2

# calculate circle area
def circle_area(radius):
    area = math.pi * radius ** 2
    return area

# test circle_area
circarea_test1 = circle_area(100)
circarea_test2 = circle_area(3)
print circarea_test1, circarea_test2

# calculate future value
def future_value(present_value, annual_rate, years):
    future = present_value * (1.0 + 0.01 * annual_rate) ** years
    return future

# test future_rate
future_test1 = future_value(1, 1, 1)
future_test2 = future_value(1000, 7, 10)
print future_test1, future_test2

# create name tag
def name_tag(first_name, last_name):
    tag = "My name is " + str(first_name) + " " + str(last_name)
    return tag

# test name_tag
name_test1 = name_tag("Michael", "Confiado")
name_test2 = name_tag("Anthony", "Lucien")
print name_test1, name_test2

# create name age string
def name_and_age(name, age):
    sentence = name + " is " + str(age) + " years old."
    return sentence

# test name_and_age
sentence_test1 = name_and_age("Michael", 32)
sentence_test2 = name_and_age("Anthony", 31)
print sentence_test1, sentence_test2

# calculate point distance
def distance(x0, y0, x1, y1):
    dist = ((x0 - x1) ** 2 + (y0 - y1) ** 2) ** 0.5
    return dist

# test distance
distance_test1 = distance(1, 1, 2, 2)
distance_test2 = distance(1, 2, 3, 4)
print distance_test1, distance_test2

# calculate area of triangle
def triangle_area(x0, y0, x1, y1, x2, y2):
    a = distance(x0, y0, x1, y1)
    b = distance(x0, y0, x2, y2)
    c = distance(x1, y1, x2, y2)
    s = 0.5 * (a + b + c)
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return area

# test triangle_area
triarea_test1 = triangle_area(1, 1, 2, 2, 1, 2)
triarea_test2 = triangle_area(1, 1, 3, 3, 1, 3)
print triarea_test1, triarea_test2

# print digits
def print_digits(number):
    tens = number // 10
    ones = number % 10
    print "The tens digit is " + str(tens) + ", and the ones digit is " + str(ones) + "."

# test digits
print_digits(10)
print_digits(67)

# let's play powerball!
import random
def powerball():
    a = random.randrange(1, 60)
    b = random.randrange(1, 60)
    c = random.randrange(1, 60)
    d = random.randrange(1, 60)
    e = random.randrange(1, 60)
    f = random.randrange(1, 60)
    p = random.randrange(1, 36)
    print "Today's numbers are " + str(a) + ", " + str(b) + ", " + str(c) + ", " + str(d) + ", " + str(e) + ", and " + str(f) + ". The Powerball number is " + str(p) + "."
    
# test powerball
powerball()
powerball()
powerball()






















