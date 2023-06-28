"""
There are three main cases when converting numbers between bases:
    1. Convert from base 10 to another base
    2. Convert to base 10 from another base
    3. The current and target bases are not 10

The convert_base function will handle all 3 of these cases

Below are explanations of how the use cases will be handled:
    1. Convert from base 10 to another base
        - divide the input by the target base and store the qoutient (as an integer) and remainder
        - if the end of recursion has been reached (qoutient > target base), return the appropriate values 
        - convert the remainder to its appropriate symbol, this will be the last element of the output
        - recursively call the convert_base function on the qoutient to get the rest of the output
        - append the result of the recursive call to the remainder symbol and return the result

    2. Convert to base 10 from another base
        - if the end of recursion has been reached (input number has 1 digit), return the appropriate values
        - extract and store the first element of the input number
        - convert the first element to its appropriate value
        - multiply this value by the apprpriate power of the target base
        - recursively call the convert_base function on the rest of the input's elements
        - add the result of this recursive call to the first value and return the result

    3. The current and target bases are not 10
        - recursively call the convert_base function on the input num to convert it to base 10 (case 2) and store the result
        - recursively call the convert_base function on the earlier result to convert it to the actual target base (case 1) and return the result

There will be two helper functions; one (get_symbol) will be used to convert a number into its appropriate symbol and the other (get_num) will convert a symbol back into it's associated number. These will use an array of symbols
"""

symbols = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

# MAIN FUNCTIONS
def convert_base(num, target_base:int, original_base:int=10):
    # Case 1
    if(original_base == 10):
        num = int(num)
        quotient = int(num / target_base)
        remainder = num % target_base

        # check for recursion end
        if(quotient == 0):
            return get_symbol(remainder)
        elif(quotient < target_base):
            return get_symbol(quotient) + get_symbol(remainder)
        
        # recursion continues
        else:
            return convert_base(quotient, target_base, original_base)

    # Case 2
    elif(target_base == 10):
        num = str(num)

        # check for recursion end
        if(len(num) <= 1):
            return get_num(num[0])

        # recursion continues
        else:
            return (get_num(num[0]) * pow(original_base, len(num) - 1)) + convert_base(num[1:], target_base, original_base)


    # Case 3
    else:
        num_10 = convert_base(num, 10, original_base)
        return convert_base(num_10, target_base, 10)

# HELPER FUNCTIONS
def get_symbol(num:int):
    return symbols[num]

def get_num(symbol:str):
    return symbols.index(symbol) if (symbol in symbols) else '%'
