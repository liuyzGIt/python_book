
def list_sum(num_list):
    if len(num_list) == 1:
        return num_list[0]
    else:
        return num_list[0] + list_sum(num_list[1:])
    
print(list_sum([1, 2, 3, 4, 5]))


def fact(n):
    if n == 1:
        return n
    else:
        return n * fact(n-1)
       
print(fact(5))


num_str = '0123456789ABCDEF'
def to_str(n, base):
    if n < base:
        return num_str[n]
    else:
        return to_str(n // base, base) + num_str[n % base]

print(to_str(999, 2))


def reverse_word(word):
    if len(word) == 1:
        return word
    else:
        return word[-1] + reverse_word(word[:-1])
print(reverse_word('abcde'))
    
    
def is_huiwen(data):
    if len(data) <= 1:
        return True
    else:
        return data[0] == data[-1] and is_huiwen(data[1:-1])

print(is_huiwen('kayzak'))

