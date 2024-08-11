calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()
    length = len(string)
    upper = string.upper()
    lower = string.lower()
    return (length, upper, lower)


def is_contains(string, list_to_search):
    count_calls()
    lower_string = string.lower()
    for item in list_to_search:
        if lower_string == item.lower():
            return True
    return False


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)
