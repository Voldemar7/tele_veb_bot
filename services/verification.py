from lexicon.lexicon_ua import LEXICON


# Функція, яка провіряє, чи є такий логін в базі данних
def check_login(name_login: str):
    if len(name_login) < 4:
        return 'check_login'
    else:
        return 'not_check_login'


# Функція, яка провіряє коректність пароля
def corect_password(password: str):
    if len(password) >= 8:
        return 'corect_password'
    else:
        'not_corect_password'
