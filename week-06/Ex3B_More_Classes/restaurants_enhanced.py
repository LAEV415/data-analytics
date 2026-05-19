class Restaurant:
    '''model for a restaurant'''

    def __init__(self, name, type):
        self.rest_name = name
        self.food_type = type
        self.number_served = 0
        self.customer_ratings = []
    
    def describe_rest(self):
        print(f'{self.rest_name} serves {self.food_type}')

    def rest_open(self):
        print(f'{self.rest_name} is open')

    def add_num_served(self):
        try:
            num = int(input('How many customers served today? '))
        except:
            print('Error: Please enter a number value only')
            self.add_num_served()
        else:
            self.number_served += num
    
    def print_num_served(self):
        print(f'{self.rest_name} has served {self.number_served} customers')

    def customer_rating(self):
        try:
            rate = int(input('How would you rate your experience today on a scale of 1-5 (5 being excellent)? '))
        except:
            print('Error: Please enter a number between 1 and 5')
            self.customer_rating()
        else:
            if (rate < 0 or rate > 5):
                print('Outside of Range Error: Please enter a number between 1 and 5')
                return self.customer_rating()
            self.customer_ratings.append(rate)
            print(f'Your rating was {rate}. The average rating for this restaurant is ' 
            f'{round(sum(self.customer_ratings) / len(self.customer_ratings), 2)}')


        

sbubby = Restaurant('Sbubby','Sanwatch')
big_cza = Restaurant('BigCza','Pizzo')
booger_king = Restaurant('Booger Kang','Boogers')

sbubby.describe_rest()
sbubby.rest_open()
big_cza.describe_rest()
big_cza.rest_open()
booger_king.describe_rest()
booger_king.rest_open()

# a) For each of your example restaurants, run print_num_served() to check the initial
# value. Then run add_num_served() a few times, inputting different values. Finally,
# run print_num_served() again to check the updated balance.

sbubby.print_num_served()
sbubby.add_num_served()
sbubby.add_num_served()
sbubby.add_num_served()
sbubby.print_num_served()

big_cza.print_num_served()
big_cza.add_num_served()
big_cza.add_num_served()
big_cza.add_num_served()
big_cza.print_num_served()

booger_king.print_num_served()
booger_king.add_num_served()
booger_king.add_num_served()
booger_king.add_num_served()
booger_king.print_num_served()

# b) For each of your example restaurants, run customer_rating() several times,
# inputting a different rating each time. Confirm that the average rating updates
# appropriately each time.

sbubby.customer_rating()
sbubby.customer_rating()
sbubby.customer_rating()

big_cza.customer_rating()
big_cza.customer_rating()
big_cza.customer_rating()

booger_king.customer_rating()
booger_king.customer_rating()
booger_king.customer_rating()

# c) For customer_rating(), try inputting a few “incorrect” values, like the number 6, a
# decimal number such as 2.5, and a word/phrase such as “5 stars!”. 
# Does your script return a result? An error? Update the method with conditional logic to
# account for different possible input types, so that if something other than an
# integer 1-5 is entered, the user is prompted to reenter their rating.