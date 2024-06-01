from colorama import Fore
from math import floor

# 1st Color
color1 = input(Fore.CYAN + '> Insert the 1st color like this: R, G, B: ' + Fore.RESET)
color1_RGB = [int(x) for x in color1.split(',')] # List with 1st color RGB values

print(f'\033[38;2;{color1_RGB[0]};{color1_RGB[1]};{color1_RGB[2]}m' + "░▒▓█ ABC abc 123 ### ⢠⣾⣿⣦\033[0m")

# 2st Color
color2 = input(Fore.CYAN + '> Insert the 2nd color like this: R, G, B: ' + Fore.RESET)
color2_RGB = [int(x) for x in color2.split(',')] # List with 2nd color RGB values

print(f'\033[38;2;{color2_RGB[0]};{color2_RGB[1]};{color2_RGB[2]}m' + "░▒▓█ ABC abc 123 ### ⢠⣾⣿⣦\033[0m")

# ASCII Gradient
def asciiGradient(pathAscii: str, factors=False, preview=False):
    ascii = ''.join(open(pathAscii, 'r')).strip()

    factor0 = (color2_RGB[0] - color1_RGB[0]) / (len(ascii) - ascii.count('\n'))
    factor1 = (color2_RGB[1] - color1_RGB[1]) / (len(ascii) - ascii.count('\n'))
    factor2 = (color2_RGB[2] - color1_RGB[2]) / (len(ascii) - ascii.count('\n'))

    ansiCode = '$([char]0x1b)'

    if preview == True:
        ansiCode = '\033'

    if factors == True:
        print(factor0)
        print(factor1)
        print(factor2)
    char = 0

    if preview == False:
        print('"',end='')

    while char != len(ascii):
        if ascii[char] == '\n' and preview == False:
            print('"\n"',end='')
            color1_RGB[0] = color1_RGB[0] + factor0

        if color1_RGB[0] != color2_RGB[0]:
            color1_RGB[0] = color1_RGB[0] + factor0

        if color1_RGB[1] != color2_RGB[1]:
            color1_RGB[1] = color1_RGB[1] + factor1
        
        if color1_RGB[2] != color2_RGB[2]:
            color1_RGB[2] = color1_RGB[2] + factor2
        
        if ascii[char] != '\n':
            print(f'{ansiCode}[38;2;{floor(color1_RGB[0])};{floor(color1_RGB[1])};{floor(color1_RGB[2])}m' + ascii[char], end='')
        elif ascii[char] == '\n' and preview==True:
            print()
        char += 1
    
    if preview == False:
        print('$([char]0x1b)[0m"')

# PATH
path = input (f'{Fore.CYAN}> Insert PATH to the ASCII .txt file is: {Fore.RESET}')

# Options
entry = input(f"""{Fore.CYAN}
> Insert {Fore.MAGENTA}1{Fore.CYAN} for preview of the ASCII art
> Insert {Fore.MAGENTA}2{Fore.CYAN} to generate the ASCII art{Fore.RESET}
""")

if entry == '1':
    print()
    asciiGradient(pathAscii=path, preview=True)
    print('\n> Run again to generate the ASCII art')

elif entry == '2':
    print()
    asciiGradient(pathAscii=path)

