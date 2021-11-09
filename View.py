def tables():
    choice_table = int(input("Select a table:\n"
                             "1 = Cinema \n"
                             "2 = Hall\n"
                             "3 = Cash register\n"
                             "4 = Ticket\n"
                             "5 = Film\n"
                             "Input: "))
    return choice_table


def fetch(table, f_table):
    if table == 1:
        for i in f_table:
            print("\n""id_cinema =", i[0])
            print("name =", i[1])
            print("adress =", i[2], "\n")
    elif table == 2:
        for i in f_table:
            print("\n""id_hall =", i[0])
            print("id_cinema =", i[1])
            print("number_of_seats =", i[2], "\n")
    elif table == 3:
        for i in f_table:
            print("\n""id_cr =", i[0])
            print("id_cinema =", i[1])
            print("the_name_of_the_cashier =", i[2])
            print("number_of_available_tickets =", i[3], "\n")
    elif table == 4:
        for i in f_table:
            print("\n""id_ticket =", i[0])
            print("id_cr =", i[1])
            print("id_hall =", i[2])
            print("id_film =", i[3])
            print("price =", i[4])
            print("date_and_time =", i[5], "\n")
    elif table == 5:
        for i in f_table:
            print("\n""id_film =", i[0])
            print("name =", i[1])
            print("duration =", i[2], "\n")
