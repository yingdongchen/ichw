"""Module for currency exchange
This module provides several string parsing functions to implement a 
simple currency exchange routine using an online currency service. 
The primary function in this module is exchange."""

  
def get_jstr(currency_from, currency_to, amount_from):   
    """Returns: jstr, string included information wanted
    In this get_jstr, the user is changing amount_from money in 
    currency currency_from to the currency currency_to. The value 
    returned represents jstr included what we want.

    The value returned has type str.

    Parameter currency_from: the currency on hand
    Precondition: currency_from is a string for a valid currency code

    Parameter currency_to: the currency to convert to
    Precondition: currency_to is a string for a valid currency code

    Parameter amount_from: amount of currency to convert
    Precondition: amount_from is a float""" 
    k='http://cs1110.cs.cornell.edu/2016fa/a1server.php?from={0}&to={1}&amt={2}'.format(currency_from,currency_to,amount_from)

    from urllib.request import urlopen
    doc = urlopen(k)
    docstr = doc.read()
    doc.close()
    jstr = docstr.decode('ascii')
    return jstr 
    
def get_number(jihe,amount_from):
    """Returns: wanting, float which tells the amount of currency received in the given exchange
    In this get_number, the user is giving jihe and amount_from,and returned a float telling
    received money

    The value returned has type float.

    Parameter jihe is a string including information ,just jstr in first function
    Precondition: jihe is a string for a valid parameter like jstr

    Parameter amount_from: amount of currency to convert
    Precondition: amount_from is a float"""
    p=''
    for i in jihe:
        if i.isdigit()==True or i=='.':
           p=p+i
        else:
           p=p
    wanting = float(p[len(str(amount_from)):])
    return wanting


def exchange(currency_from, currency_to, amount_from):
    """Returns: final_number, amount of currency received in the given exchange.

    In this exchange, the user is changing amount_from money in 
    currency currency_from to the currency currency_to. The value 
    returned represents the amount in currency currency_to.

    The value returned has type float.

    Parameter currency_from: the currency on hand
    Precondition: currency_from is a string for a valid currency code

    Parameter currency_to: the currency to convert to
    Precondition: currency_to is a string for a valid currency code

    Parameter amount_from: amount of currency to convert
    Precondition: amount_from is a float"""

    first_string=get_jstr(currency_from, currency_to, amount_from)
    final_number=get_number(first_string,amount_from)
    return final_number




"""Module for function test
This module provides several test functions to test if every function in the first module works well.
The primary function in this module is testAll()"""
def test_A():
    """to test the whole exchange function, pass if work well, or break down using ¡®AssertionError"""
    assert(exchange('USD','EUR',2.5)==2.0952375) 
    assert(exchange('CNY','AUD',20)==3.8473219279361)
    assert(exchange('KPW','JPY',5)==0.60476986361111)

def test_B():
    """to test the function get_jstr), pass if work well, or break down using ¡®AssertionError¡¯"""
    assert(get_jstr('USD','EUR',2.5)=='{ "from" : "2.5 United States Dollars", "to" : "2.0952375 Euros", "success" : true, "error" : "" }')
    assert(get_jstr('CNY','AUD',20)=='{ "from" : "20 Chinese Yuan", "to" : "3.8473219279361 Australian Dollars", "success" : true, "error" : "" }')
    assert(get_jstr('KPW','JPY',5)=='{ "from" : "5 North Korean Won", "to" : "0.60476986361111 Japanese Yen", "success" : true, "error" : "" }')



def test_C():
    """to test the function get_jstr), pass if work well, or break down using ¡®AssertionError¡¯""" 
    assert(get_number('{ "from" : "2.5 United States Dollars", "to" : "2.0952375 Euros", "success" : true, "error" : "" }',2.5)==2.0952375)
    assert(get_number('{ "from" : "20 Chinese Yuan", "to" : "3.8473219279361 Australian Dollars", "success" : true, "error" : "" }',20)==3.8473219279361)
    assert(get_number('{ "from" : "5 North Korean Won", "to" : "0.60476986361111 Japanese Yen", "success" : true, "error" : "" }',5)==0.60476986361111)

def testAll():
    """Return all test passed to show everything works well.
    In this testAll, our target is to test all cases
    pass if work well, or break down using ¡®AssertionError"""
    test_A()
    test_B()
    test_C()
    return "All tests passed"


print(testAll())
currency_from=input()
currency_to=input()
amount_from=input()
print(exchange(currency_from, currency_to, amount_from))
