from payament_times.in_time import *
import config
from payament_times.twelve_months import twelve_months
from payament_times.nine_months import nine_months
from payament_times.six_months import six_months
from payament_times.tree_months import tree_months



def credit_payament(desired_car, time_option):
    if(time_option == 1):
        return (in_time(desired_car))
    elif(time_option == 2):
        return (tree_months(desired_car))
    elif(time_option == 3):
        return (six_months(desired_car))
    elif(time_option == 4):
        return (nine_months(desired_car))
    elif(time_option == 5):
        return (twelve_months(desired_car))

