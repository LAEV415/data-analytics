# 1. Create a script named greeting.py. Define a variable that contains the current hour (0-
# 23). Display one of the greetings below based on the current hour:

# Time                      Greeting
# until 10:00am             Good morning!
# 10:00am until 5:00pm      Good day!
# 5:00pm or later           Good evening!

current_time = 23

if (-1 < current_time < 10):
    print('Good morning!')
elif (10 < current_time < 17):
    print('Good day!')
elif (17 < current_time < 24):
    print('Good evening!')
else:
    print("You are not on earth.")

if ((0 <= current_time < 4) or current_time == 23):
    print("What are you doing up so late??")



