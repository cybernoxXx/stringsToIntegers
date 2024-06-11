def convertStrToInt(number):

    DIGITS_STR_TO_INT = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    position = 1
    conversion = 0
    isNegative = False

    # Checking if the string represent a negative number or not
    if number[0] == '-':
        isNegative = True
        # Removing the negative sign
        newNumber = number[1:]
    else:
        # Putting the number in a new list
        newNumber = number

    # Cycling all elements in the list starting from the last one
    for i in range(len(newNumber)-1, -1, -1):
        # The converted number is the conversion calculated until now plus the conversion of the element I'm considering multiplied by his position
        conversion = conversion + (DIGITS_STR_TO_INT[newNumber[i]] * position)
        # The position of the next element
        position *= 10

    if isNegative:
        return conversion * -1
    else:
        return conversion


for i in range(-10000, 10000):
    assert convertStrToInt(str(i)) == i
