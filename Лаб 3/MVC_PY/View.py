import datetime


def start_menu():
    x = int(input("1 to update\n"
                  "2 to delete\n"
                  "3 to insert\n"
                  "4 to select table\n"
                  "5 to search\n"
                  "6 to insert random\n"
                  "7 to end\n"
                  "Input: "))
    if x < 1 or x > 7:
        err()
        start_menu()
    else:
        print("")
        return x


def tables():
    choice_table = int(input("Select a table:\n"
                             "1 = Cinema \n"
                             "2 = Hall\n"
                             "3 = Cash register\n"
                             "4 = Ticket\n"
                             "5 = Film\n"
                             "Input: "))
    if choice_table < 1 or choice_table > 5:
        err()
        tables()
    else:
        return choice_table


def input_insert(table):
    if table == 1:
        id_c = int(input("Input new id: "))
        name = str(input("Input new name: "))
        adr = str(input("Input new adress: "))

        inp = [id_c, name, adr]
        return inp

    elif table == 2:
        id_h = int(input("Input new id: "))
        id_c = int(input("Input new cinema id: "))
        seats = str(input("Input new number of seats: "))

        inp = [id_h, id_c, seats]
        return inp

    elif table == 3:
        id_cr = int(input("Input new id: "))
        id_c = int(input("Input new cinema id: "))
        name = str(input("Input new name of the cashier: "))
        tickets = int(input("Input new number of the available tickets: "))

        inp = [id_cr, id_c, name, tickets]
        return inp

    elif table == 4:
        id_t = int(input("Input new id: "))
        id_cr = int(input("Input new cash register id: "))
        id_hall = int(input("Input new hall id: "))
        id_film = int(input("Input new film: "))
        price = float(input("Input new price: "))
        date_entry = input("Input a date in YYYY-MM-DD format: ")
        year, month, day = map(int, date_entry.split('-'))
        time_entry = input("Input a time in HH:MM format: ")
        hour, minute = map(int, time_entry.split(':'))
        date_time = datetime.datetime(year, month, day, hour, minute)

        inp = [id_t, id_cr, id_hall, id_film, price, date_time]
        return inp
    elif table == 5:
        id_f = int(input("Input new id: "))
        name = str(input("Input new name: "))
        time_entry = input("Input a duration in HH:MM format: ")
        hour, minute = map(int, time_entry.split(':'))
        duration = datetime.time(hour, minute)

        inp = [id_f, name, duration]
        return inp


def input_update(table):
    new = None
    if table == 1:
        id_c = int(input("Num of id: "))
        column = int(input("1 = to upd name\n"
                           "2 = to upd adress\n"
                           "Input:"))
        if column == 1:
            new = str(input("New name: "))
        elif column == 2:
            new = str(input("New adress: "))
        else:
            err()
            input_update(table)

        inp = [id_c, column, new]
        return inp

    elif table == 2:
        id_h = int(input("Num of id: "))
        column = int(input("1 = to upd id_cinema\n"
                           "2 = to upd number of seats\n"
                           "Input:"))
        if column == 1:
            new = str(input("New cinema id: "))
        elif column == 2:
            new = str(input("New number of seats: "))
        else:
            err()
            input_update(table)

        inp = [id_h, column, new]
        return inp

    elif table == 3:
        id_cr = int(input("Num of id: "))
        column = int(input("1 = to upd id_cinema\n"
                           "2 = to upd the_name_of_the_cashier\n"
                           "3 = to upd number_of_available_tickets\n"
                           "Input:"))
        if column == 1:
            new = int(input("New cinema id: "))
        elif column == 2:
            new = str(input("New number of seats: "))
        elif column == 3:
            new = str(input("New number of seats: "))
        else:
            err()
            input_update(table)

        inp = [id_cr, column, new]
        return inp

    elif table == 4:
        id_t = int(input("Num of id: "))
        column = int(input("1 = to upd cash register id\n"
                           "2 = to upd hall id\n"
                           "3 = to upd film id\n"
                           "4 = to upd price\n"
                           "5 = to upd date and time\n"
                           "Input:"))

        if column == 1:
            new = int(input("New cash register id: "))
        elif column == 2:
            new = int(input("New hall id: "))
        elif column == 3:
            new = int(input("New film id: "))
        elif column == 4:
            new = float(input("New price: "))
        elif column == 5:
            date_entry = input("New date in YYYY-MM-DD format: ")
            year, month, day = map(int, date_entry.split('-'))
            time_entry = input("New time in HH:MM format: ")
            hour, minute = map(int, time_entry.split(':'))
            new = datetime.datetime(year, month, day, hour, minute)
        else:
            err()
            input_update(table)

        inp = [id_t, column, new]
        return inp

    elif table == 5:
        id_f = int(input("Num of id: "))
        column = int(input("1 = to upd name\n"
                           "2 = to upd duration\n"
                           "Input:"))
        if column == 1:
            new = str(input("New name: "))
        elif column == 2:
            time_entry = input("New duration in HH:MM format: ")
            hour, minute = map(int, time_entry.split(':'))
            new = datetime.time(hour, minute)
        else:
            err()
            input_update(table)

        inp = [id_f, column, new]
        return inp


def del_id():
    nid = int(input("Num of id: "))
    return nid


def input_select():
    string = int(input("1 = to one str\n"
                       "2 = to all str\n"
                       "Input:"))
    if string == 1:
        nid = int(input("Num of id: "))
        inp = [string, nid]
        return inp

    elif string == 2:
        inp = [string]
        return inp

    else:
        err()
        input_select()


def input_search(table):
    if table == 1:
        column = int(input("1 = to search id\n"
                           "2 = to search name or adress\n"
                           "Input:"))
        if column == 1:
            a = int(input("Input start: "))
            b = int(input("Input finish: "))
            inp = [column, a, b]
            return inp
        elif column == 2:
            txt = str(input("Input text: "))
            inp = [column, txt]
            return inp
        else:
            err()
            input_select(table)

    elif table == 2:
        column = int(input("1 = to search hall id\n"
                           "2 = to search cinema id\n"
                           "3 = to search numbers of seats\n"
                           "Input:"))
        if column == 1:
            a = int(input("Input start: "))
            b = int(input("Input finish: "))
            inp = [column, a, b]
            return inp
        elif column == 2:
            a = int(input("Input start: "))
            b = int(input("Input finish: "))
            inp = [column, a, b]
            return inp
        elif column == 3:
            a = int(input("Input start: "))
            b = int(input("Input finish: "))
            inp = [column, a, b]
            return inp
        else:
            err()
            input_select(table)

    elif table == 3:
        column = int(input("1 = to search cash register id\n"
                           "2 = to search cinema id\n"
                           "3 = to search the_name_of_the_cashier\n"
                           "4 = to search number_of_available_tickets\n"
                           "Input:"))
        if column == 1 or column == 2 or column == 4:
            a = int(input("Input start: "))
            b = int(input("Input finish: "))
            inp = [column, a, b]
            return inp

        elif column == 3:
            txt = str(input("Input text: "))
            inp = [column, txt]
            return inp

        else:
            err()
            input_select(table)

    elif table == 4:
        column = int(input("1 = to search ticket id\n"
                           "2 = to search cash register id\n"
                           "3 = to search hall id\n"
                           "4 = to search film id\n"
                           "5 = to search price\n"
                           "6 = to search date and time\n"
                           "Input:"))
        if column == 1 or column == 2 or column == 3 or column == 4:
            a = int(input("Input start: "))
            b = int(input("Input finish: "))
            inp = [column, a, b]
            return inp
        elif column == 5:
            a = float(input("Input start: "))
            b = float(input("Input finish: "))
            inp = [column, a, b]
            return inp
        elif column == 6:
            date_entry_a = input("New start date in YYYY-MM-DD format: ")
            year, month, day = map(int, date_entry_a.split('-'))
            time_entry_a = input("New start time in HH:MM format: ")
            hour, minute = map(int, time_entry_a.split(':'))
            a = datetime.datetime(year, month, day, hour, minute)

            date_entry_b = input("New finish date in YYYY-MM-DD format: ")
            year, month, day = map(int, date_entry_b.split('-'))
            time_entry_b = input("New finish time in HH:MM format: ")
            hour, minute = map(int, time_entry_b.split(':'))
            b = datetime.datetime(year, month, day, hour, minute)

            inp = [column, a, b]
            return inp
        else:
            err()
            input_select(table)

    elif table == 5:
        column = int(input("1 = to search film id\n"
                           "2 = to search name\n"
                           "3 = to search duration\n"
                           "Input: "))
        if column == 1:
            a = int(input("Input start: "))
            b = int(input("Input finish: "))
            inp = [column, a, b]
            return inp
        elif column == 2:
            txt = str(input("Input text: "))
            inp = [column, txt]
            return inp
        elif column == 3:
            time_entry_a = input("New start duration in HH:MM format: ")
            hour, minute = map(int, time_entry_a.split(':'))
            a = datetime.time(hour, minute)

            time_entry_b = input("New finish duration in HH:MM format: ")
            hour, minute = map(int, time_entry_b.split(':'))
            b = datetime.time(hour, minute)

            inp = [column, a, b]
            return inp
        else:
            err()
            input_select(table)


def fetch(table, f_table, inp):
    if table == 1:
        if inp[0] == 1:
            print("\n""name =", f_table[0])
            print("adress =", f_table[1], "\n")

        elif inp[0] == 2:
            for i in f_table:
                print("\n""id_cinema =", i.id_cinema)
                print("name =", i.name)
                print("adress =", i.adress, "\n")

    elif table == 2:
        if inp[0] == 1:
            print("\n""id_cinema =", f_table[0])
            print("number_of_seats =", f_table[1], "\n")

        elif inp[0] == 2:
            for i in f_table:
                print("\n""id_hall =", i.id_hall)
                print("id_cinema =", i.id_cinema)
                print("number_of_seats =", i.number_of_seats, "\n")

    elif table == 3:
        if inp[0] == 1:
            print("\n""id_cinema =", f_table[0])
            print("the_name_of_the_cashier =", f_table[1])
            print("number_of_available_tickets =", f_table[2], "\n")

        elif inp[0] == 2:
            for i in f_table:
                print("\n""id_cr =", i.id_cr)
                print("id_cinema =", i.id_cinema)
                print("the_name_of_the_cashier =", i.the_name_of_the_cashier)
                print("number_of_available_tickets =", i.number_of_available_tickets, "\n")

    elif table == 4:
        if inp[0] == 1:
            print("\n""id_cr =", f_table[0])
            print("id_hall =", f_table[1])
            print("id_film =", f_table[2])
            print("price =", f_table[3])
            print("date_and_time =", f_table[4], "\n")

        elif inp[0] == 2:
            for i in f_table:
                print("\n""id_ticket =", i.id_ticket)
                print("id_cr =", i.id_cr)
                print("id_hall =", i.id_hall)
                print("id_film =", i.id_film)
                print("price =", i.price)
                print("date_and_time =", i.date_and_time, "\n")

    elif table == 5:
        if inp[0] == 1:
            print("\n""name =", f_table[0])
            print("duration =", f_table[1], "\n")

        elif inp[0] == 2:
            for i in f_table:
                print("\n""id_film =", i.id_film)
                print("name =", i.name)
                print("duration =", i.duration, "\n")


def data(task):
    if task == 1:
        print("\n[INFO] Data was successfully upd\n")
    elif task == 2:
        print("\n[INFO] Data was successfully deleted\n")
    elif task == 3:
        print("\n[INFO] Data was successfully inserted\n")
    elif task == 6:
        print("\n[INFO] Random Data was successfully inserted\n")


def count_rand():
    count = int(input("Input amount of data to generate: "))
    return count


def search_time(t):
    print("\nSearch duration = ", t, "\n")


def err():
    print("\n[INFO] Error input, try again!\n")


def print_close():
    print("[INFO] PostgreSQL connection closed")


def err_except(_ex):
    print("[INFO] Error while working with PostgreSQL", _ex)
