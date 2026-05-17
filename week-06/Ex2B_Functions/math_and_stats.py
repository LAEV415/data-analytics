import random
import math
import statistics

# 2. Create a few starting variables to work with:

vals_1_100 = range(1,100)
vals_sample = random.sample(vals_1_100, 75)
vals_choices = random.choices(vals_1_100, k = 200)
radius = random.randint(3,10)
pi = math.pi
line_break = '------------------------------------------------------------------------------------'

# 3. Use a combination of functions from all three modules to create calculations that will
# support the following output (and be sure to use comments to document your code
# as you work!):
#
# _Experimenting with a subset of integers 1-100:
# Sum of 75 sample values from 1 to 100: ____
# Average of 75 sample values: ____
# Median of 75 sample values: ____
# _Experimenting with a superset of 200 values, integers 1-100:
# Average of 200 values: ____
# Median of 200 values: ____
# Mode of 200 values: ____
# Standard deviation of 200 values: ____
# Variance of 200 values: ____
# _Modeling a random circle:
# Radius = __, area = ____ (rounded up to the nearest integer)
# Radius = __, area = ____ (rounded down to the nearest integer)

sum_75 = math.fsum(vals_sample) #vals_sample is an iterable list allowing us to use math.fsum
avg_75 = round(statistics.mean(vals_sample), 4) #mean = avg; getting avg of 75 sample values
med_75 = statistics.median(vals_sample) #Getting median of 75 values using statistics library func

#using vals_choices which contains 200 vals
avg_200 = round(statistics.mean(vals_choices), 4) #getting avg of vals_choices
med_200 = statistics.median(vals_choices) #finding median of vals_choices using stats library
mod_200 = statistics.mode(vals_choices) #finding mode of vals_choices using stats lib
std_200 = round(statistics.stdev(vals_choices), 4) #finding std dev of vals_choices using stats lib
var_200 = round(statistics.variance(vals_choices), 4) #finding variance using stats lib

area_up = math.ceil(pi * math.pow(radius, 2)) #Using math.ceil to round up to nearest int
area_down = math.floor(pi * math.pow(radius, 2)) #Using math.floor to round down to nearest int


# a) Your final print statement should include the printed headers each beginning with
# an underscore and the line breaks between sections in your output. For the line
# breaks, use print('\n')

print('Experimenting with a subset of integers 1-100:' "\n"
      f'Sum of 75 sample values from 1 to 100: {sum_75}' "\n"
      f'Average of 75 sample values:{avg_75}' "\n"
      f'Median of 75 sample values: {med_75}' "\n"
      f'{line_break}')

print('Experimenting with a superset of 200 values, integers 1-100:' "\n"
      f'Average of 200 values: {avg_200}' "\n"
      f'Median of 200 values: {med_200}' "\n"
      f'Mode of 200 values: {mod_200}' "\n"
      f'Standard deviation of 200 values: {std_200}' "\n"
      f'Variance of 200 values: {var_200}' "\n"
      f'{line_break}')

print('Modeling a random circle:' "\n"
      f'Radius = {radius}, area = {area_up} (rounded up to the nearest integer)' "\n"
      f'Radius = {radius}, area = {area_down} (rounded down to the nearest integer)' "\n"
      f'{line_break}')