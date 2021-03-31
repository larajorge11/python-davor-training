from decorators import print_return_data


@print_return_data
def return_greeting(name):
    print('Creating greeting')
    return f"Hi {name}"


hi_davor = return_greeting("Davor")
print(hi_davor)

print(return_greeting.__name__)


print("One, 'two', \"three\", four, \\five\\ once, 'I' caught a fish '//alive\\\\' ")