def check_bogo(coffee=0):
    if coffee/2 < 1:
        return False
    else:
        return True


def check_chmk(chai=0, milk=0):
    if chai >= 1 and milk >= 1:
        return True
    else:
        return False


def check_appl(apple=0):
    if apple >= 3:
        return True
    else:
        return False


def check_apom(oatmeal=0, apple=0):
    if oatmeal >= 1 and apple >= 1:
        return True
    else:
        return False
