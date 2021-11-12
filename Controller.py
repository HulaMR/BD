from Model import *
from View import *


def menu():
    x = start_menu()

    if x == 1:
        table = tables()
        inp = input_update(table)
        try:
            update(table, inp)
        except Exception as _ex:
            err_except(_ex)
        data(x)

    elif x == 2:
        table = tables()
        n_id = del_id()
        try:
            delete(table, n_id)
        except Exception as _ex:
            err_except(_ex)
        data(x)

    elif x == 3:
        table = tables()
        inp = input_insert(table)
        try:
            insert(table, inp)
        except Exception as _ex:
            err_except(_ex)
        data(x)

    elif x == 4:
        f_t = None
        table = tables()
        inp = input_select()
        try:
            f_t = select_table(table, inp)
        except Exception as _ex:
            err_except(_ex)
        fetch(table, f_t)

    elif x == 5:
        f_t = None
        table = tables()
        inp = input_search(table)
        try:
            f_t = search(table, inp)
        except Exception as _ex:
            err_except(_ex)
        fetch(table, f_t[0])
        search_time(f_t[1])

    elif x == 6:
        table = tables()
        if table == 1 or table == 5:
            count = count_rand()
            try:
                insert_rand(table, count)
            except Exception as _ex:
                err_except(_ex)
        else:
            try:
                insert_rand(table, None)
            except Exception as _ex:
                err_except(_ex)
        data(x)

    elif x == 7:
        close()
        print_close()
        return None

    menu()
