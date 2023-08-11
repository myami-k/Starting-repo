

def start_menu():
    steps = ["REGISTER", "LOG IN", "QUIT"]
    print(str(steps).replace("'", ""))
    while True:
        enter = str(input("> ")).upper()
        if enter == steps[0]:
            register()
        elif enter == steps[1]:
            user_registration = log_in()
            user_account, user_password, user_bank =\
                user_registration[0], user_registration[1], int(user_registration[2])
            menu(user_account, user_password, user_bank)
        else:
            exit("(start_menu)")


def register():
    new_account = input("ACCOUNT: ")
    new_password = input("PASSWORD: ")
    new_coins = 0
    with open("registrations.txt", "a") as fp:
        fp.write(f"{new_account}:{new_password}:{new_coins}\n")
        fp.close()


def log_in():
    fp_registrations = open("registrations.txt").read().splitlines()
    enter_account = input("ACCOUNT: ")
    enter_password = input("PASSWORD: ")
    for lines in fp_registrations:
        saved_account, saved_password, saved_coins = lines.split(":")
        saved_registrations = [saved_account, saved_password, saved_coins]
        if enter_account == saved_registrations[0] and enter_password == saved_registrations[1]:
            return saved_registrations
    exit("(log_in)")


def menu(account, password, bank):
    steps = ["STATS", "ADD", "REMOVE", "QUIT"]
    print(str(steps).replace("'", ""))
    while True:
        enter = str(input("> ")).upper()
        if enter == steps[0]:
            print(f"[ACCOUNT: {account}] [PASSWORD: {password}] [BANK: {bank}]")
        elif enter == steps[1]:
            amount = get_int("AMOUNT: ")
            bank = add_coins(amount, bank)
        elif enter == steps[2]:
            amount = get_int("AMOUNT: ")
            bank = remove_coins(amount, bank)
        else:
            exit("(menu)")
        save_stats(account, password, bank)


def save_stats(account, password, bank):
    fp_registrations = open("registrations.txt").read().splitlines()
    x = ""
    for lines in fp_registrations:
        saved_account, saved_password, saved_coins = lines.split(":")
        saved_registrations = [saved_account, saved_password, saved_coins]
        if account == saved_registrations[0] and password == saved_registrations[1]:
            x += f"{saved_account}:{password}:{bank}\n"
        else:
            x += f"{saved_account}:{saved_password}:{saved_coins}\n"
    with open("registrations.txt", "w") as fp:
        fp.write(x)
        fp.close()


def add_coins(amount, bank):
    bank += amount
    return bank


def remove_coins(amount, bank):
    bank -= amount
    return bank


def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            exit("(get_int)")


start_menu()
