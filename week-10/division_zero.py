# try and except
# try: 
#     print(5/0)
# except ZeroDivisionError:
#     print('hello')


while True:
    first_number = input('\n First number: ')

    # if first_number == 'q':
    #     break

    second_number = input('\n Second number: ')
    # if second_number =='q':
    #     break

    try:
        result = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print('cannot divide by 0!')
    except ValueError:
        print('enter an integer')
    else: 
        print(f'result is : {result}')
    