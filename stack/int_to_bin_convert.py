from initial_stack import stack

def binary_conversion(dec_num):
    s = stack()

    while dec_num > 0:
        remainder = dec_num % 2
        s.push(remainder)
        dec_num = dec_num//2

    bin_num = ""
    while not s.is_empty():
        bin_num += str(s.pop())
    return bin_num


print(binary_conversion(300))
