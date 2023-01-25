"""
Kendall Outlaaw
Data Analysis Fundamentals - Project 2 Task 3
January 24, 2023

The objective of this project is to practice and understand how to write cutom functions
and how to use the functions from the math module.

Use built-in functions and 
functions from the math module.

To illustrate the ability to call functions and 
display useful results to the user. 

Use your textbook and the examples in this repo to get ideas.

"""

import math

# define some functions

def get_area_of_lot(length, width):
    """
    Return area of a lot given the length and width of the lot.

    Could this fail?
    This program colud fail if the user enters a negative number or a 0.
    This is why it's important to apply the try and catch to protect our code.
    """


    # Use a try / except / finally block when something 
    # could go wrong

    try:
        area = length * width
        return area
    except Exception as ex:
        print(f"Error: {ex}")
        return None


# -------------------------------------------------------------



# define more functions here (see instuctions)

def average_hours_worked(mon,tue,wed,thu):
    """
    In this example, we will Return the Average Number of Hours Worked Per Week
    At our organization, we work Monday thru Thursday only and 10 hours per day
    """

    try:
        weekly_hours = mon + tue + wed + thu
        weekly_avg = (mon + tue + wed + thu, 'The Average Hours Worked per Week is', weekly_hours/4)
        return weekly_avg

    except Exception as ex:
        print(f"Error: {ex}")
        return None



# -------------------------------------------------------------


def weekly_wage(mon,tue,wed,thu):
    """
    In this example, we will Return the Weekly Pay of an Employee Per Week
    At our organization, we work Monday thru Thursday only and 10 hours per day

    We will use the math.fabs() method which returns the absolute value of a number, as a float.
    This method will ensure that we are only getting postive values for hours worked and hourly rate
    """

    try:
        
        hourly_rate = 35
        weekly_pay = math.fabs((mon * hourly_rate)) + math.fabs((tue * hourly_rate)) + math.fabs((wed * hourly_rate)) + math.fabs((thu * hourly_rate))
        
        return weekly_pay

    except Exception as ex:
        print(f"Error: {ex}")
        return None


# -------------------------------------------------------------


def annual_wage(mon,tue,wed,thu):
    """
    In this example, we will Return the Annual Pay of an Employee
    At our organization, we work Monday thru Thursday only and 10 hours per day

    We will use the math.fabs() method which returns the absolute value of a number, as a float.
    This method will ensure that we are only getting postive values for hours worked and hourly rate
    """

    try:
        
        hourly_rate = 35
        weekly_pay = math.fabs((mon * hourly_rate)) + math.fabs((tue * hourly_rate)) + math.fabs((wed * hourly_rate)) + math.fabs((thu * hourly_rate))
        annual_pay =  weekly_pay * 52

        return annual_pay

    except Exception as ex:
        print(f"Error: {ex}")
        return None




# -------------------------------------------------------------
# Call some functions and execute code!

# This is very standard Python - it means
# "If this module is the one being executed, i.e., the main module"
   
# Literally: "if this module name == the name of the main module"
if __name__ == "__main__":

    # call your functions here (see instructions)
    print("Explore some functions in the math module")
    print()
    print(f"math.comb(5,1) = {math.comb(5,1)}")
    print(f"math.perm(5,1) = {math.perm(5,1)}")
    print()
    print(f"The Area of the Lot(6,2) = {get_area_of_lot(6, 2)}")
    print()
    print(f"The Average Hours Worked = {average_hours_worked(10, 10, 10, 10)}")
    print()
    print(f"The Weekly Wage = {weekly_wage(10, 10, 10, 10)}")
    print()
    print(f"The Annual Wage = {annual_wage(10, 10, 10, 10)}")
    print()