

def menu():
    while True:
        # choice for path in menu
        main_menu = ["LIST", "ADD", "DELETE", "Q"]
        main_input = input(f"\n\n╷------------------------------╷"
                           f"\n│            MENU              │"
                           f"\n│                              │\n│{main_menu}│"
                           f"\n╵------------------------------╵\n> ").upper()
        # getting lists
        if main_input == main_menu[0]:
            list_display()
        # add clients to txt
        elif main_input == main_menu[1]:
            add_clients()
        # delete clients from txt
        elif main_input == main_menu[2]:
            delete_clients()
        # quit
        elif main_input == main_menu[3]:
            exit("You left")


def get_lower(prompt):  # function -> return the str (lower) input
    return str(input(prompt)).lower()


def list_display():
    fp = open("clients.txt").read().splitlines()
    # choice for filters
    main_display = ["PAID", "NOT PAID", "ANY", "FILTER", "Q"]
    while True:
        main_input = input(f"\n\n╷------------------------------------------╷"
                           f"\n│                  LIST                    │"
                           f"\n│                                          │\n│{main_display}│"
                           f"\n╵------------------------------------------╵\n> ").upper()
        # overall display ╷ │
        if main_input != main_display[4] and main_input in main_display:
            print("\n" + "╷------------╷------------╷-------------------------╷------------╷------------╷------------"
                         "╷------------╷------------╷------------╷------------╷"
                         "\n│DATE:       │N° CLIENT:  │NAME:                    "
                         "│N° BILL:    │NET:        │PAID:       │PAID DATE:  │METHOD:     │BANK:       │N° CHQ:     │"
                         "\n" + "│------------│------------│-------------------------│------------│------------│-------"
                                "-----"
                         "│------------│------------│------------│------------│")
        # choice for paid filter
        if main_input == main_display[0]:
            for lines in fp:
                x = lines.split(":")
                if x[5] == "y":  # x5 for paid state
                    paint(lines)
        # choice for not paid filter
        elif main_input == main_display[1]:
            for lines in fp:
                x = lines.split(":")
                if x[5] == "n":  # x5 for not paid state
                    paint(lines)
        # choice for no filter
        elif main_input == main_display[2]:
            for lines in fp:
                paint(lines)
        # choice for special filter
        elif main_input == main_display[3]:
            while True:
                filter_user = get_lower(f"[date/n°client/paid date]: ")

                if filter_user == "date":  # choice for date filter
                    filter_date = get_lower(f"Date: ")
                    for lines in fp:
                        x = lines.split(":")
                        if x[0] == filter_date:  # x0 for date
                            paint(lines)

                    break

                elif filter_user == "n°client":  # choice for n°client filter
                    filter_number = get_lower(f"N° Client: ")
                    for lines in fp:
                        x = lines.split(":")
                        if x[1] == filter_number:  # x1 for n°client
                            paint(lines)

                    break

                elif filter_user == "paid date":  # choice for paid date filter
                    filter_paid_date = get_lower(f"Paid date: ")
                    for lines in fp:
                        x = lines.split(":")
                        if x[5] == "yes":  # first seeing if the list is equal to paid
                            # I made this to not get the list index out of range
                            if x[6] == filter_paid_date:  # x6 for paid date
                                paint(lines)

                    break
        elif main_input == main_display[4]:
            break
        print("\n")


def add_clients():  # add clients, add the date, the name, the number, the bill etc..
    # str (lowercase) inputs
    client_date = get_lower(f"Date: ")
    client_number = get_lower(f"N° Client: ")
    client_name = get_lower(f"Name: ")
    client_bill = get_lower(f"N° Bill: ")
    client_net_payable = get_lower(f"Net payable: ")

    while True:  # if paid or not + paid date
        paid_or_not = get_lower(f"Paid? [y/n]: ")

        if paid_or_not == "y":  # path of paid choice
            paid_date = get_lower(f"Paid date: ")

            while True:  # esp/chq/vir
                esp_chq_vir = get_lower(f"[esp/chq/vir]: ")

                if esp_chq_vir == "chq":  # chq input + bt/soc/bp
                    chq_bank = get_lower(f"[bt/soc/bp]: ")
                    chq_number = get_lower(f"N° Chq: ")

                    with open("clients.txt", "a") as fp:  # end of paid choice
                        fp.write(f"{client_date}:{client_number}:{client_name}:{client_bill}:{client_net_payable}"
                                 f":{paid_or_not}:{paid_date}:{esp_chq_vir}:{chq_bank}:{chq_number}\n")
                        fp.close()

                    break

                elif esp_chq_vir == "esp" or esp_chq_vir == "vir":  # esp/vir input + end of paid choice
                    with open("clients.txt", "a") as fp:
                        fp.write(f"{client_date}:{client_number}:{client_name}:{client_bill}:{client_net_payable}"
                                 f":{paid_or_not}:{paid_date}:{esp_chq_vir}\n")
                        fp.close()

                    break

            break

        elif paid_or_not == "n":  # path of not paid choice
            with open("clients.txt", "a") as fp:  # end of not paid choice
                fp.write(f"{client_date}:{client_number}:{client_name}:{client_bill}:{client_net_payable}"
                         f":{paid_or_not}\n")
                fp.close()

            break


def delete_clients():  # zero
    client_number = input(f"N° Bill: ")
    fp = open("clients.txt").read().splitlines()
    y = ""
    for lines in fp:
        x = lines.split(":")
        if x[3] != client_number:
            y += lines + "\n"
    with open("clients.txt", "w") as fp:
        fp.write(y)
        fp.close()


def paint(prompt):
    x = prompt.split(":")
    output = "│"
    for element in x:
        if int(x.index(element)) == 2:
            while True:
                if len(element) != 25:
                    element += " "
                else:
                    break
        else:
            if len(element) < 12:
                while True:
                    if len(element) != 12:
                        element += " "
                    else:
                        break
        output += element + "│"
    output += "\n" + "╵------------╵------------╵-------------------------╵------------╵------------╵------------" \
                     "╵------------╵------------╵------------╵------------╵"
    print(output)


menu()
