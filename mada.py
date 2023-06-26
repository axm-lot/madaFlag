import os
from termcolor import colored

program = '''
terminal_width = os.get_terminal_size().columns
margin = int(terminal_width * 0.45)
text_margin = int(terminal_width * 0.35)

flag_lines = [
    colored('       ', 'white', 'on_white') + colored('      ', 'red', 'on_red') + colored('      ', 'red', 'on_red'),
    colored('       ', 'white', 'on_white') + colored('      ', 'red', 'on_red') + colored('      ', 'red', 'on_red'),
    colored('       ', 'red', 'on_white') + colored('      ', 'green', 'on_green') + colored('      ', 'green', 'on_green'),
    colored('       ', 'green', 'on_white') + colored('      ', 'green', 'on_green') + colored('      ', 'green', 'on_green')
]

text = colored("Mba ho tena fahaleovantena ny amin'ny taona manaraka", 'red', 'on_white')

for line in flag_lines:
    print(' ' * margin + line)
print()
print(' ' * text_margin + text)
'''

# Execute the program with flag and text
exec(program, {'os': os, 'colored': colored})
