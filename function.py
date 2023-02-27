import simpleaudio as sa  # importing the audio playing library

# Dictionary of alphanumeric and their respective morse code
code = {'A': '01',
        'B': '1000',
        'C': '1010',
        'D': '100',
        'E': '0',
        'F': '0010',
        'G': '110',
        'H': '0000',
        'I': '00',
        'J': '0111',
        'K': '101',
        'L': '0100',
        'M': '11',
        'N': '10',
        'O': '111',
        'P': '0110',
        'Q': '1101',
        'R': '010',
        'S': '000',
        'T': '1',
        'U': '001',
        'V': '0001',
        'W': '011',
        'X': '1001',
        'Y': '1011',
        'Z': '1100',
        '1': '01111',
        '2': '00111',
        '3': '00011',
        '4': '00001',
        '5': '00000',
        '6': '10000',
        '7': '11000',
        '8': '11100',
        '9': '11110',
        '0': '11111', 
        }

# list of alphanumeric for check
alpha_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
              'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8',
              '9', ' ']


def morse_to_alphanumeric(morse):
    check = True
    # check weather all character of the input is morse character ie. '0' and '1'
    for i in morse:
        if i != '0' and i != '1' and i != ' ':
            check = False

    if check:                       # if the check is passes then the conversion is executed
        # this function return the respective character of the part of morse
        def morse_to_char(morse):
            global code
            for i in code:
                if code[i] == morse:
                    return i

        k = 0
        message = ''
        # in this while loop the construction of the message takes place, converting each morse part to character
        # and concatenate to the message string
        while True:
            space = False
            code = ''
            # in this for loop the morse parts are separated from the input string
            for i in range(len(morse)):
                if k > len(morse) - 1:
                    break
                if morse[k] == ' ':
                    if morse[k + 1] == ' ' and k <= len(morse):
                        k += 1
                        space = True
                    k += 1
                    break
                code += morse[k]
                k += 1

            # here the morse part is converted to character and added to the message string
            message += morse_to_char(code)
            if k >= len(morse) - 1:
                break
            if space:
                message += ' '
        return message

    # return following statement if check fails
    return 'Enter Valid Morse Code'


def alpha_to_morse(message):
    check = True
    # check weather all character of the input is alphanumeric
    for i in message:
        x = False
        for j in alpha_list:
            if i == j:
                x = True
        if not x:
            check = False
            break

    if check:
        morse = ''
        index = 0
        for i in message:           # take each character of the message and do the conversion process
            for j in code:          # get the morse value of the character from the code dictionary
                if i == j:
                    morse += code[j] # add the morse part to the morse string
                    break
            morse += ' ' if index < len(message) - 1 else ''
            index += 1
        return morse

    # return following statement if check fails
    return 'Only Alphabets and Numbers are accepted'


# importing the sound files
dat_sound = sa.WaveObject.from_wave_file("dat.wav")
dit_sound = sa.WaveObject.from_wave_file("dit.wav")
space_sound = sa.WaveObject.from_wave_file("space.wav")


# play the sound respect to the morse
def morse_play(morse):
    for i in morse:
        if i == '1':
            dat_play = dat_sound.play()
            dat_play.wait_done()

        if i == '0':
            dit_play = dit_sound.play()
            dit_play.wait_done()

        if i == ' ':
            space_play = space_sound.play()
            space_play.wait_done()
