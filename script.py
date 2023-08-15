import sys
# check full path of the system when runs by Code Runner extension. 
# Execute via the OUTPUT in the console environment
print(sys.version)
print(sys.executable)

def greet(who_to_greet):
    greeting = 'Hello, {}'.format(who_to_greet)
    return greeting

print(greet('World'))
print(greet('MacSakaow'))