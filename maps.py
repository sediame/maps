import sys, webbrowser, pyperclip

if len(sys.argv) > 1:
    argument = sys.argv[1:]
    print(argument)
    address = "+".join(argument)
else:
    address = pyperclip.paste()

print(address)
webbrowser.open('https://www.google.de/maps/place/' + address)
