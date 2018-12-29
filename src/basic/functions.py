#A function with docstring:    
def readable_timedelta(days):
    """
    Return a string of the number of weeks and days included in days.

    Parameters:
    days -- number of days to convert (int)

    Returns:
    string of the number of weeks and days included in days
    """
    weeks = days // 7
    remainder = days % 7
    return "{} week(s) and {} day(s)".format(weeks, remainder)

# test your function
print(readable_timedelta(10))


global_variable = "a global variable"
def about_scope_variable():
    local_variable = "You can read {} inside of a function, but can not write within".format(global_variable)
    print(local_variable)