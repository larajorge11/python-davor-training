def is_adult(age):
    if age > 18:
        return True
    else:
        return False


result = is_adult(30)
print(result)


def convertGender(gender="unknown"):
    if gender.upper() == 'M':
        return 'Male'
    elif gender.upper() == 'F':
        return 'Female'
    else:
        return f"Gender {gender} is unknown"


print(convertGender("F"))
print(convertGender("M"))
print(convertGender("m"))
print(convertGender("g"))
