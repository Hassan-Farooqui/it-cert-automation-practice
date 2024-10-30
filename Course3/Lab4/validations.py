import re



def validate_user(username, minlen):

    # Usernames can only use letters, numbers, dots, and underscores

    if not re.match('^[a-z0-9._]*$', username):

        return False

    # Usernames can't begin with a number or a dot

    if username[0].isnumeric() or username[0] == '.':

        return False

    # Username must be at least 'minlen' characters

    if len(username) < minlen:

        return False

    return True



# Test cases

print(validate_user("blue.kale", 3))  # True

print(validate_user(".red_quinoa", 3))  # False

print(validate_user("red_quinoa", 4))  # True

print(validate_user("blue.kale", 4))  # False


