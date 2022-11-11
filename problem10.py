"""
10. Why does this expression cause an error? How can you fix it?
'I have eaten ' + 99 + ' burritos.'
"""


"""
Answer....

This expression causes an error because 99 is in the form of integer and 'I have eaten' and
'burritos' are in the form of string. We know that concatination of string and integer is 
not allowed in python.

We can fix it by typecasting 99 into string and then concatinating it with them
'I have eaten' + '99' + 'burritos' like this.

"""