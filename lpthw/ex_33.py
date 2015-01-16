def print_numbers(end_number, increment):
    i = 0
    numbers = []
    
#    while i < end_number:
    for i in range(end_number):
        print "At the top of i is %d" % i
        numbers.append(i)

        i += increment
        print "Numbers now: ", numbers
        print "At the bottom of i is %d" % i

    print "The numbers: "
    for num in numbers:
        print num

print_numbers(6, 2)