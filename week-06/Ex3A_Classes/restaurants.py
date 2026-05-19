class Restaurant:
    '''model for a restaurant'''

    def __init__(self, name, type):
        self.rest_name = name
        self.food_type = type
    
    def describe_rest(self):
        print(f'{self.rest_name} serves {self.food_type}')

    def rest_open(self):
        print(f'{self.rest_name} is open')

sbubby = Restaurant('Sbubby','Sanwatch')
big_cza = Restaurant('BigCza','Pizzo')
booger_king = Restaurant('Booger Kang','Boogers')

sbubby.describe_rest()
sbubby.rest_open()
big_cza.describe_rest()
big_cza.rest_open()
booger_king.describe_rest()
booger_king.rest_open()
