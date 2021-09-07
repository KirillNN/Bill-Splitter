email = input()


def check_email(address):
    assert '@' in address, 'Try again!'
    return 'Done!'


check_email(email)
