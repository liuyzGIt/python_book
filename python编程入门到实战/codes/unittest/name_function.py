def get_formatted_name(first, last):
    full_name = first + ' ' + last
    return full_name.title()


if __name__== '__main__':
    print(get_formatted_name('tom', 'hanks'))
