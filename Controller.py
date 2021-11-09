from Model import *
from View import *


def menu(connection):
    x = int(input("1 to update\n"
                  "2 to delete\n"
                  "3 to insert\n"
                  "4 to select table\n"
                  "5 to search\n"
                  "6 to insert random\n"
                  "7 to end\n"
                  "Input: "))
    print("")
    if x == 1:
        table = tables()
        update(connection, table)

    elif x == 2:
        table = tables()
        delete(connection, table)

    elif x == 3:
        table = tables()
        insert(connection, table)

    elif x == 4:
        table = tables()
        f_t = select_table(connection, table)
        fetch(table, f_t)

    elif x == 5:
        table = tables()
        f_t = search(connection, table)
        fetch(table, f_t)

    elif x == 6:
        table = tables()

        insert_rand(connection, table)

    elif x == 7:
        return None

    else:
        print("\n[INFO] Error input, try again!\n")

    menu(connection)
