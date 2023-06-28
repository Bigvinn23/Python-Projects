# This file holds functions used to convert from base 10 to other bases

chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

def convert_base(num, target_base: int, original_base:int=10):
    if(target_base == 10):
        num = str(num)

        if(len(num) > 1):
            val = get_num(num[0]) * pow(original_base, len(num) - 1)
            endnum = val + convert_base(num[1:], target_base, original_base)
            return endnum
        else:
            return get_num(num[0])
    
    if(original_base != 10):
        # convert the number to base ten
        num_10 = convert_base(num, 10, original_base)

        # then convert the number to the real target base
        endnum = convert_base(num_10, target_base, 10)
        return endnum

    else:
        # divide num by target base and store qoutient and remainder
        qoutient = int(num / target_base)
        remainder = num % target_base

        if(qoutient == 0):
            return get_symbol(remainder)

        elif(qoutient < target_base):
            return get_symbol(qoutient) + get_symbol(remainder)
        
        else:
            return convert_base(qoutient, target_base, original_base) + get_symbol(remainder)
    

# this function handles getting the symbol the number would represent eg 10 -> A, 15 -> F, etc
def get_symbol(num):
    return chars[int(num)]

def get_num(symbol):
    return int(chars.index(symbol))