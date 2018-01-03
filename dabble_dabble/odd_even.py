

def is_odd(number):
    if number % 2 == 0:
        return False
    else:
        return True

num_entered = input("Enter a number >")

if is_odd(num_entered):
    print "Odd number entered."
else:
    print "even number entered."