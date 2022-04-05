# determine if number is even
def is_even(integer):
    return (integer % 2) == 0

# test is_even
print is_even(4)

# is a person cool?
def is_cool(name):
    return name == ("Joe" or "John" or "Stephen")
        
print is_cool("Michael")

# is it lunchtime?
def is_lunchtime(hour, is_am):
    return (hour == 11 and is_am) or (hour == 12 and not is_am)

print is_lunchtime(11, True)

# is it a leap year?
def is_leap_year(year):
    return ((year % 4) == 0 and ((year % 100) != 0 or (year % 400 == 0)))
            
print is_leap_year(2000)

# do the intervals intersect?
def interval_intersect(a, b, c, d):
    return (b >= c) and (d >= a)
    #return (c <= b) and (a <= d)

print interval_intersect(1, 3, 4, 100)

# name and age with validation
def name_and_age(name, age):
    if(age < 0):
        return "Error: Invalid age."
    else:
        return name + " is " + str(age) + " years old."
    
print name_and_age("Michael", -40)

# print tens and ones digits
def print_digits(number):
    if(number < 0 or number > 100):
        print "Error: Input is not a two-digit number."
    else:
        tens = number // 10 
        ones = number % 10
        print "The tens digit is " + str(tens) + \
              " and the ones digit is " + str(ones) + "."

print_digits(1000)

# look up a name from an array
def name_lookup(first_name):
    if(first_name == "Joe"):
        return "Warren"
    elif(first_name == "Scott"):
        return "Rixner"
    elif(first_name == "John"):
        return "Greiner"
    elif(first_name == "Stephen"):
        return "Wong"
    else:
        return "Error: Not an instructor"

print name_lookup("Stephen")

# tranlate to pig latin
def pig_latin(word):
    first_letter = word[0]
    rest_of_word = word[1 : ]
    if first_letter == ("a" or "e" or "i" or "u" or "o"):
        return first_letter + rest_of_word + "way"
    else:
        return rest_of_word + first_letter + "ay"

print pig_latin("python")

# quadratic equation
def smaller_root(a, b, c):
    discriminant = (b ** 2) - (4 * a * c)
    if discriminant < 0 or a == 0:
        print "Error: No real solutions"
    else:
        discriminant_sqrt = discriminant ** 0.5
        if a > 0:
            smaller = -discriminant_sqrt
        else:
            smaller = discriminant_sqrt
        return (-b + smaller) / (2 * a)

print smaller_root(1, 2, 3)













