def hypervolume(*lengths):
    i = iter(lengths)
    v = next(i)
    for length in i:
        v *= length
    return v


print(hypervolume(2, 4))


def hypervolume(length, *lenghts):
    v = length
    for item in lenghts:
        v *= item
    return v


hypervolume(3, 5, 7, 9)


def tag(name, **kwargs):
    print(name)
    print(kwargs)
    print(type(kwargs))


tag('img', src="Money.jpg", alt="Sunrise", border=1)


def tag_v2(name, **attributes):
    result = '<' + name
    for key, value in attributes.items():
        result += ' {k}="{v}"'.format(k=key, v=str(value))
    result += '>'
    return result


print(tag_v2('img', src="Money.jpg", alt="Sunrise", border=1))


def color(red, green, blue, **kwargs):
    print("r = " + str(red))
    print("g = " + str(green))
    print("b = " + str(blue))
    print(kwargs)


k = {'red': 21, 'green': 68, 'blue': 120, 'alpha': 53}
color(**k)

k = dict(red=21, green=68, blue=120, alpha=53)
color(**k)
