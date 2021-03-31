def startstop(func):
    def wrapper():
        print('Starting...')
        func()
        print('Finishes...')

    return wrapper


@startstop
def roll():
    print('Rolling...')


roll()
