def menu_option():
    print('Menu')
    print('-------------')
    print('1. Encode')
    print('2. Decode')
    print('3. Quit')
def encoded_pass(encode_pass):
    pass_list = [int(x) for x in str(encode_pass)]
    encoded_list = [x + 3 for x in pass_list]
    encoded_list_str = map(str, encoded_list)
    encoded_password = ''.join(encoded_list_str)
    return encoded_password


if __name__ == '__main__':
    program=True
    while program==True:
        menu_option()
        print('')
        menu_selection=input('Please enter an option: ')
        if menu_selection=='1':
            encode_pass=input('Please enter your password to encode: ')
            e_pass =encoded_pass(encode_pass)
            print('Your password has been encoded and stored!')
        if menu_selection=='2':
            print(f'The encoded password is {e_pass} and the original password is {decoded_pass(e_pass)}.')
        if menu_selection=='3':
            program=False
        print('')


