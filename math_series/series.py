def fibonacci(n):
    """
        Generates the nth Fibonacci series for a given number
        Arguments:
        n {integer} -- the number to find the Fibonacci series for
        Output:
        The nth Fibbonacci series  
    """
    if n == 0:
        return 0
    if n == 1:
        return 1  
    if n > 1:
        return fibonacci(n-1) + fibonacci(n-2) 
    if n < 0:
        return "Don't use  Negative values "    


def lucas(n):
    """
        Generates the nth Lucas series for a given number
        Arguments:
        n {integer} -- the number to find the Lucas series for
        Output:
        The nth Lucas series 
    """
    if n == 0:
        return 2
    if n==1:
        return 1
    if n > 1:
        return lucas(n-1) + lucas(n-2)
    if n < 0:
        return "Don't use  Negative values "      


def series_new(n,first_index,secound_index):
    """
        Generates a math series depending on the input arguments, for a given number
        Arguments:
        n {integer} -- the number to find the required series for
        first_index{integer} -- to determine the first digit for the summation
        secound_index{integer} -- to determine the second digit for the summation
        Output:
        The nth summation series for the number
    """
    if n == 0:
        return first_index
    if n == 1:
        return secound_index
    if n > 1:
        return series_new(n-1,first_index,secound_index) + series_new(n-2,first_index,secound_index)
    if n < 0:
        return "Don't use  Negative values "             




def sum_series(n,first_index=0,secound_index=1):
    """
        Generates a math series depending on the input arguments, for a given number
        Arguments:
        n {integer} -- the number to find the required series for
        first_index{integer} -- to determine the first digit for the summation
        secound_index{integer} -- to determine the second digit for the summation
        Output:
        The nth summation series for the number
    """

    if first_index == 0 and secound_index == 1:
        return fibonacci(n)
    elif first_index == 2 and secound_index == 1:
        return lucas(n)
    else :
        return series_new(n,first_index,secound_index)   

