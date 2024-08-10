alphabet = {
    'A': '• ---',
    'B': '--- • • •',
    'C': '--- • --- •',
    'D': '--- • •',
    'E': '•',
    'F': '• • --- •',
    'G': '--- --- •',
    'H': '• • • •',
    'I': '• •',
    'J': '• --- --- ---',
    'K': '--- • ---',
    'L': '• --- • •',
    'M': '--- ---',
    'N': '--- •',
    'O': '--- --- ---',
    'P': '• --- --- •',
    'Q': '--- --- • ---',
    'R': '• --- •',
    'S': '• • •',
    'T': '---',
    'U': '• • ---',
    'V': '• • • ---',
    'W': '• --- ---',
    'X': '--- • • ---',
    'Y': '--- • --- ---',
    'Z': '--- --- • •',
    '1': '• --- --- --- ---',
    '2': '• • --- --- ---',
    '3': '• • • --- ---',
    '4': '• • • • ---',
    '5': '• • • • •',
    '6': '--- • • • •',
    '7': '--- --- • • •',
    '8': '--- --- --- • •',
    '9': '--- --- --- --- •',
    '0': '--- --- --- --- ---'
}

continue_play = 'yes'

while continue_play == 'yes':
    user_input = input('Type some text you wish to convert to morse code: ')
    input_list_caps = list(user_input.upper())

    morse_code_list = [alphabet[char] for char in input_list_caps]
    morse_code = ' '.join(morse_code_list)

    print(f'Original text: {user_input}\nMorse code: {morse_code}')

    continue_play = input('Do you wish to convert some more text? (yes/no): ')

