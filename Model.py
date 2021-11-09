import time
import datetime
from random import *

r_adr = ['Voli Avenue, 2, Lutsk, Volyn region, 43000',
         'Svitla Street, 2, Lutsk, Volyn region, 43000',
         'Kopernika Street, 2, Lutsk, Volyn region, 43000']


def insert(connection, table):

    if table == 1:
        id_c = int(input("Input new id: "))
        name = str(input("Input new name: "))
        adr = str(input("Input new adress: "))
        with connection.cursor() as cursor:
            cursor.execute("""INSERT INTO "Cinema"(id_cinema, name, adress) VALUES(%s, %s, %s);""",
                           (id_c, name, adr,))
            print("[INFO] Data was successfully inserted\n")
    elif table == 2:
        id_h = int(input("Input new id: "))
        id_c = int(input("Input new cinema id: "))
        seats = str(input("Input new number of seats: "))
        with connection.cursor() as cursor:
            cursor.execute("""INSERT INTO "Hall"(id_hall, id_cinema, number_of_seats) VALUES(%s, %s, %s);""",
                           (id_h, id_c, seats,))
            print("[INFO] Data was successfully inserted\n")
    elif table == 3:
        id_cr = int(input("Input new id: "))
        id_c = int(input("Input new cinema id: "))
        name = str(input("Input new name of the cashier: "))
        tickets = int(input("Input new number of the available tickets: "))
        with connection.cursor() as cursor:
            cursor.execute("""INSERT INTO "Cash register"(id_cr, id_cinema, 
                the_name_of_the_cashier, number_of_available_tickets) 
                VALUES(%s, %s, %s, %s);""", (id_cr, id_c, name, tickets,))
            print("[INFO] Data was successfully inserted\n")
    elif table == 4:
        id_t = int(input("Input new id: "))
        id_cr = int(input("Input new cash register id: "))
        id_hall = int(input("Input new hall id: "))
        id_film = int(input("Input new film: "))
        price = int(input("Input new price: "))
        date_entry = input("Input a date in YYYY-MM-DD format: ")
        year, month, day = map(int, date_entry.split('-'))
        time_entry = input("Input a time in HH:MM format: ")
        hour, minute = map(int, time_entry.split(':'))
        date_time = datetime.datetime(year, month, day, hour, minute)
        with connection.cursor() as cursor:
            cursor.execute("""INSERT INTO "Ticket"(id_ticket, id_cr, id_hall, film_id, price, date_and_time) 
                VALUES(%s, %s, %s, %s, %s, %s);""", (id_t, id_cr, id_hall, id_film, price, date_time,))
            print("[INFO] Data was successfully inserted\n")
    elif table == 5:
        id_f = int(input("Input new id: "))
        name = str(input("Input new name: "))
        time_entry = input("Input a duration in HH:MM format: ")
        hour, minute = map(int, time_entry.split(':'))
        duration = datetime.time(hour, minute)
        with connection.cursor() as cursor:
            cursor.execute("""INSERT INTO "Film"(id_film, name, duration) VALUES(%s, %s, %s);""",
                           (id_f, name, duration,))
            print("[INFO] Data was successfully inserted\n")
    else:
        print("\n[INFO] Error input, try again!\n")


def insert_rand(connection, table):

    if table == 1:
        count = int(input("Input amount of data to generate: "))
        with connection.cursor() as cursor:

            for i in range(0, count):
                cursor.execute("""INSERT INTO "Cinema"(id_cinema, name, adress) 
                    VALUES((SELECT(select count(id_cinema) from "Cinema")+3::int),
                      (select (chr(ascii('B') + (random() * 25)::int) ||
                        chr(ascii('B') + (random() * 25)::int) ||
                        chr(ascii('B') + (random() * 25)::int) ||
                        chr(ascii('B') + (random() * 25)::int) ||
                        chr(ascii('B') + (random() * 25)::int)  
                        )), %s);""", (choice(r_adr),))
            print("[INFO] Random Data was successfully inserted\n")

    elif table == 2:
        with connection.cursor() as cursor:

            cursor.execute("""INSERT INTO "Hall"(id_hall, id_cinema, number_of_seats) 
                 VALUES((SELECT(select count(id_hall) from "Hall")+1::int), 
                 (SELECT id_cinema FROM "Cinema" OFFSET 
                 floor(random()*(select count(id_cinema) from "Cinema")) LIMIT 1), 
                 trunc(random()*100+200)::int);""")
            print("[INFO] Random Data was successfully inserted\n")

    elif table == 3:
        with connection.cursor() as cursor:

            cursor.execute("""INSERT INTO "Cash register"(id_cr, id_cinema, 
                the_name_of_the_cashier, number_of_available_tickets) 
                 VALUES(
                 (SELECT(select count(id_cr) from "Cash register")+2::int), 
                 (SELECT id_cinema FROM "Cinema" OFFSET 
                 floor(random()*(select count(id_cinema) from "Cinema")) LIMIT 1),
                (select (chr(ascii('B') + (random() * 25)::integer) ||
        chr(ascii('B') + (random() * 25)::integer) ||
        chr(ascii('B') + (random() * 25)::integer) ||
        chr(ascii('B') + (random() * 25)::integer) ||
        chr(ascii('B') + (random() * 25)::integer)  
       )), trunc(random()*100+200)::int);""")
        print("[INFO] Random Data was successfully inserted\n")

    elif table == 4:
        with connection.cursor() as cursor:

            cursor.execute("""INSERT INTO "Ticket"(
                id_ticket, id_cr, id_hall, film_id, price, date_and_time) 
                VALUES((SELECT(select count(id_ticket) from "Ticket")+1::int), 
                (SELECT id_cr FROM "Cash register" OFFSET 
                 floor(random()*(select count(id_cr) from "Cash register")) LIMIT 1), 
                (SELECT id_hall FROM "Hall" OFFSET 
                 floor(random()*(select count(id_hall) from "Hall")) LIMIT 1), 
                (SELECT id_film FROM "Film" OFFSET 
                 floor(random()*(select count(id_film) from "Film")) LIMIT 1), 
                trunc(random()*100+200)::int,
                (select NOW() + (random() * (interval '90 days')) + '30 days')
                );""")
        print("[INFO] Random Data was successfully inserted\n")

    elif table == 5:
        count = int(input("Input amount of data to generate: "))
        with connection.cursor() as cursor:

            for i in range(0, count):
                cursor.execute("""INSERT INTO "Film"(id_film, name, duration) 
                     VALUES(
                    (SELECT(select count(id_Film) from "Film")+1::int), 
                    (select (chr(ascii('B') + (random() * 24)::integer) ||
                            chr(ascii('B') + (random() * 24)::integer) ||
                            chr(ascii('B') + (random() * 24)::integer) ||
                            chr(ascii('B') + (random() * 24)::integer) ||
                            chr(ascii('B') + (random() * 24)::integer) ||
                            chr(ascii('B') + (random() * 24)::integer) ||
                            chr(ascii('B') + (random() * 24)::integer) ||
                            chr(ascii('B') + (random() * 24)::integer) )),
                    (select (random() * (interval '1 hour')) + '2 hour'))
                    ;""")
            print("[INFO] Random Data was successfully inserted\n")

    else:
        print("\n[INFO] Error input, try again!\n")


def update(connection, table):

    if table == 1:
        id_c = int(input("Num of id: "))
        column = int(input("1 = to upd name\n"
                           "2 = to upd adress\n"
                           "Input:"))
        if column == 1:
            new = str(input("New name: "))
            with connection.cursor() as cursor:
                cursor.execute("""update "Cinema" set name = %s where id_cinema = %s;""", (new, id_c,))
                print("[INFO] Data was successfully upd\n")
        elif column == 2:
            new = str(input("New adress: "))
            with connection.cursor() as cursor:
                cursor.execute("""update "Cinema" set adress = %s where id_cinema = %s;""", (new, id_c,))
                print("[INFO] Data was successfully upd\n")
        else:
            print("\n[INFO] Error input, try again!\n")
            update(connection, 1)

    elif table == 2:
        id_h = int(input("Num of id: "))
        column = int(input("1 = to upd id_cinema\n"
                           "2 = to upd number of seats\n"
                           "Input:"))
        if column == 1:
            new = str(input("New cinema id: "))
            with connection.cursor() as cursor:
                cursor.execute("""update "Hall" set id_cinema = %s where id_hall = %s;""", (new, id_h,))
                print("[INFO] Data was successfully upd\n")
        elif column == 2:
            new = str(input("New number of seats: "))
            with connection.cursor() as cursor:
                cursor.execute("""update "Hall" set number_of_seats = %s where id_hall = %s;""", (new, id_h,))
                print("[INFO] Data was successfully upd\n")
        else:
            print("\n[INFO] Error input, try again!\n")
            update(connection, 2)

    elif table == 3:
        id_cr = int(input("Num of id: "))
        column = int(input("1 = to upd id_cinema\n"
                           "2 = to upd the_name_of_the_cashier\n"
                           "3 = to upd number_of_available_tickets\n"
                           "Input:"))
        if column == 1:
            new = int(input("New cinema id: "))
            with connection.cursor() as cursor:
                cursor.execute("""update "Cash register" set id_cinema = %s where id_cr = %s;""", (new, id_cr,))
                print("[INFO] Data was successfully upd\n")
        elif column == 2:
            new = str(input("New number of seats: "))
            with connection.cursor() as cursor:
                cursor.execute("""update "Cash register" set the_name_of_the_cashier = %s where id_cr = %s;""",
                               (new, id_cr,))
                print("[INFO] Data was successfully upd\n")
        elif column == 3:
            new = str(input("New number of seats: "))
            with connection.cursor() as cursor:
                cursor.execute("""update "Cash register" set number_of_available_tickets = %s where id_cr = %s;""",
                               (new, id_cr,))
                print("[INFO] Data was successfully upd\n")
        else:
            print("\n[INFO] Error input, try again!\n")
            update(connection, 3)

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
            with connection.cursor() as cursor:
                cursor.execute("""update "Ticket" set id_cr = %s where id_ticket = %s;""", (new, id_t,))
                print("[INFO] Data was successfully upd\n")
        elif column == 2:
            new = int(input("New hall id: "))
            with connection.cursor() as cursor:
                cursor.execute("""update "Ticket" set id_hall = %s where id_ticket = %s;""",
                               (new, id_t,))
                print("[INFO] Data was successfully upd\n")
        elif column == 3:
            new = int(input("New film id: "))
            with connection.cursor() as cursor:
                cursor.execute("""update "Ticket" set film_id = %s where id_ticket = %s;""",
                               (new, id_t,))
                print("[INFO] Data was successfully upd\n")
        elif column == 4:
            new = int(input("New price: "))
            with connection.cursor() as cursor:
                cursor.execute("""update "Ticket" set price = %s where id_ticket = %s;""",
                               (new, id_t,))
                print("[INFO] Data was successfully upd\n")
        elif column == 5:
            date_entry = input("New date in YYYY-MM-DD format: ")
            year, month, day = map(int, date_entry.split('-'))
            time_entry = input("New time in HH:MM format: ")
            hour, minute = map(int, time_entry.split(':'))
            new = datetime.datetime(year, month, day, hour, minute)
            with connection.cursor() as cursor:
                cursor.execute("""update "Ticket" set date_and_time = %s where id_ticket = %s;""",
                               (new, id_t,))
                print("[INFO] Data was successfully upd\n")
        else:
            print("\n[INFO] Error input, try again!\n")
            update(connection, 4)

    elif table == 5:
        id_f = int(input("Num of id: "))
        column = int(input("1 = to upd name\n"
                           "2 = to upd duration\n"
                           "Input:"))
        if column == 1:
            new = str(input("New name: "))
            with connection.cursor() as cursor:
                cursor.execute("""update "Film" set name = %s where id_film = %s;""", (new, id_f,))
                print("[INFO] Data was successfully upd\n")
        elif column == 2:
            time_entry = input("New duration in HH:MM format: ")
            hour, minute = map(int, time_entry.split(':'))
            new = datetime.time(hour, minute)
            with connection.cursor() as cursor:
                cursor.execute("""update "Film" set duration = %s where id_film = %s;""", (new, id_f,))
                print("[INFO] Data was successfully upd\n")
        else:
            print("\n[INFO] Error input, try again!\n")
            update(connection, 5)

    else:
        print("\n[INFO] Error input, try again!\n")


def delete(connection, table):

    if table == 1:
        id_c = int(input("Num of id: "))
        with connection.cursor() as cursor:
            cursor.execute("""DELETE from "Cinema" WHERE id_cinema = %s;""", (id_c,))
            print("[INFO] Data was successfully deleted\n")
    elif table == 2:
        id_h = int(input("Num of id: "))
        with connection.cursor() as cursor:
            cursor.execute("""DELETE from "Hall" WHERE id_hall = %s;""", (id_h,))
            print("[INFO] Data was successfully deleted\n")
    elif table == 3:
        id_cr = int(input("Num of id: "))
        with connection.cursor() as cursor:
            cursor.execute("""DELETE from "Cash register" WHERE id_cr = %s;""", (id_cr,))
            print("[INFO] Data was successfully deleted\n")
    elif table == 4:
        id_t = int(input("Num of id: "))
        with connection.cursor() as cursor:
            cursor.execute("""DELETE from "Ticket" WHERE id_ticket = %s;""", (id_t,))
            print("[INFO] Data was successfully deleted\n")
    elif table == 5:
        id_f = int(input("Num of id: "))
        with connection.cursor() as cursor:
            cursor.execute("""DELETE from "Film" WHERE id_film = %s;""", (id_f,))
            print("[INFO] Data was successfully deleted\n")
    else:
        print("\n[INFO] Error input, try again!\n")


def select_table(connection, table):

    if table == 1:
        string = int(input("1 = to one str\n"
                           "2 = to all str\n"
                           "Input:"))
        if string == 1:
            id_c = int(input("Num of id: "))
            with connection.cursor() as cursor:
                cursor.execute("""SELECT * FROM "Cinema" where id_cinema = %s;""", (id_c,))
                return cursor.fetchmany(1)

        elif string == 2:
            with connection.cursor() as cursor:
                cursor.execute("""SELECT * FROM "Cinema";""")
                return cursor.fetchall()
        else:
            print("\n[INFO] Error input, try again!\n")
            select_table(connection, 1)

    elif table == 2:
        string = int(input("1 = to one str\n"
                           "2 = to all str\n"
                           "Input:"))
        if string == 1:
            id_c = int(input("Num of id: "))
            with connection.cursor() as cursor:
                cursor.execute("""SELECT * FROM "Hall" where id_hall = %s;""", (id_c,))
                return cursor.fetchmany(1)

        elif string == 2:
            with connection.cursor() as cursor:
                cursor.execute("""SELECT * FROM "Hall";""")
                return cursor.fetchall()
        else:
            print("\n[INFO] Error input, try again!\n")
            select_table(connection, 2)

    elif table == 3:
        string = int(input("1 = to one str\n"
                           "2 = to all str\n"
                           "Input:"))
        if string == 1:
            id_c = int(input("Num of id: "))
            with connection.cursor() as cursor:
                cursor.execute("""SELECT * FROM "Cash register" where id_cr = %s;""", (id_c,))
                return cursor.fetchmany(1)

        elif string == 2:
            with connection.cursor() as cursor:
                cursor.execute("""SELECT * FROM "Cash register";""")
                return cursor.fetchall()
        else:
            print("\n[INFO] Error input, try again!\n")
            select_table(connection, 3)

    elif table == 4:
        string = int(input("1 = to one str\n"
                           "2 = to all str\n"
                           "Input:"))
        if string == 1:
            id_c = int(input("Num of id: "))
            with connection.cursor() as cursor:
                cursor.execute("""SELECT * FROM "Ticket" where id_ticket = %s;""", (id_c,))
                return cursor.fetchmany(1)

        elif string == 2:
            with connection.cursor() as cursor:
                cursor.execute("""SELECT * FROM "Ticket";""")
                return cursor.fetchall()
        else:
            print("\n[INFO] Error input, try again!\n")
            select_table(connection, 4)

    elif table == 5:
        string = int(input("1 = to one str\n"
                           "2 = to all str\n"
                           "Input:"))
        if string == 1:
            id_f = int(input("Num of id: "))
            with connection.cursor() as cursor:
                cursor.execute("""SELECT * FROM "Film" where id_film = %s;""", (id_f,))
                return cursor.fetchmany(1)

        elif string == 2:
            with connection.cursor() as cursor:
                cursor.execute("""SELECT * FROM "Film";""")
                return cursor.fetchall()
        else:
            print("\n[INFO] Error input, try again!\n")
            select_table(connection, 5)

    else:
        print("\n[INFO] Error input, try again!\n")


def search(connection, table):

    if table == 1:
        column = int(input("1 = to search id\n"
                           "2 = to search name or adress\n"
                           "Input:"))
        if column == 1:
            a = int(input("Input start: "))
            b = int(input("Input finish: "))
            with connection.cursor() as cursor:
                start = time.time()
                cursor.execute("""SELECT * FROM "Cinema" WHERE %s <= id_cinema and id_cinema <= %s;""", (a, b,))
                finish = time.time()
                print("\nSearch duration = ", finish - start)
                return cursor.fetchall()

        elif column == 2:
            txt = str(input("Input text: "))
            with connection.cursor() as cursor:
                start = time.time()
                cursor.execute("""SELECT * FROM "Cinema" WHERE 
                    to_tsvector(name) || to_tsvector(adress) 
                    @@ plainto_tsquery(%s);;""", (txt,))
                finish = time.time()
                print("\nSearch duration = ", finish - start)
                return cursor.fetchall()
        else:
            print("\n[INFO] Error input, try again!\n")
            search(connection, 1)

    elif table == 2:
        column = int(input("1 = to search hall id\n"
                           "2 = to search cinema id\n"
                           "3 = to search numbers of seats\n"
                           "Input:"))
        if column == 1:
            a = int(input("Input start: "))
            b = int(input("Input finish: "))
            with connection.cursor() as cursor:
                start = time.time()
                cursor.execute("""SELECT * FROM "Hall" WHERE %s <= id_hall and id_hall <= %s;""", (a, b,))
                finish = time.time()

                print("\nSearch duration = ", finish - start)
                return cursor.fetchall()

        elif column == 2:
            a = int(input("Input start: "))
            b = int(input("Input finish: "))
            with connection.cursor() as cursor:
                start = time.time()
                cursor.execute("""SELECT * FROM "Hall" WHERE %s <= id_cinema and id_cinema <= %s;""", (a, b,))
                finish = time.time()
                print("\nSearch duration = ", finish - start)
                return cursor.fetchall()

        elif column == 3:
            a = int(input("Input start: "))
            b = int(input("Input finish: "))
            with connection.cursor() as cursor:
                start = time.time()
                cursor.execute("""SELECT * FROM "Hall" WHERE %s <= number_of_seats and
                     number_of_seats <= %s;""", (a, b,))
                finish = time.time()

                print("\nSearch duration = ", finish - start)
                return cursor.fetchall()
        else:
            print("\n[INFO] Error input, try again!\n")
            search(connection, 2)

    elif table == 3:
        column = int(input("1 = to search cash register id\n"
                           "2 = to search cinema id\n"
                           "3 = to search the_name_of_the_cashier\n"
                           "4 = to search number_of_available_tickets\n"
                           "Input:"))
        if column == 1:
            a = int(input("Input start: "))
            b = int(input("Input finish: "))
            with connection.cursor() as cursor:
                start = time.time()
                cursor.execute("""SELECT * FROM "Cash register" WHERE %s <= id_cr and id_cr <= %s;""", (a, b,))
                finish = time.time()

                print("\nSearch duration = ", finish - start)
                return cursor.fetchall()

        elif column == 2:
            a = int(input("Input start: "))
            b = int(input("Input finish: "))
            with connection.cursor() as cursor:
                start = time.time()
                cursor.execute("""SELECT * FROM "Cash register" WHERE %s <= id_cinema and id_cinema <= %s;""",
                               (a, b,))
                finish = time.time()

                print("\nSearch duration = ", finish - start)
                return cursor.fetchall()

        elif column == 3:
            txt = str(input("Input name: "))
            with connection.cursor() as cursor:
                start = time.time()
                cursor.execute("""SELECT * FROM "Cash register" WHERE to_tsvector(the_name_of_the_cashier) 
                    @@ plainto_tsquery(%s);;""", (txt,))
                finish = time.time()

                print("\nSearch duration = ", finish - start)
                return cursor.fetchall()

        elif column == 4:
            a = int(input("Input start: "))
            b = int(input("Input finish: "))
            with connection.cursor() as cursor:
                start = time.time()
                cursor.execute("""SELECT * FROM "Cash register" WHERE %s <= number_of_available_tickets and
                    number_of_available_tickets <= %s;""", (a, b,))
                finish = time.time()

                print("\nSearch duration = ", finish - start)
                return cursor.fetchall()
        else:
            print("\n[INFO] Error input, try again!\n")
            search(connection, 3)

    elif table == 4:
        column = int(input("1 = to search ticket id\n"
                           "2 = to search cash register id\n"
                           "3 = to search hall id\n"
                           "4 = to search film id\n"
                           "5 = to search price\n"
                           "6 = to search date and time\n"
                           "Input:"))
        if column == 1:
            a = int(input("Input start: "))
            b = int(input("Input finish: "))
            with connection.cursor() as cursor:
                start = time.time()
                cursor.execute("""SELECT * FROM "Ticket" WHERE %s <= id_ticket and id_ticket <= %s;""", (a, b,))
                finish = time.time()

                print("\nSearch duration = ", finish - start)
                return cursor.fetchall()

        elif column == 2:
            a = int(input("Input start: "))
            b = int(input("Input finish: "))
            with connection.cursor() as cursor:
                start = time.time()
                cursor.execute("""SELECT * FROM "Ticket" WHERE %s <= id_cr and id_cr <= %s;""", (a, b,))
                finish = time.time()

                print("\nSearch duration = ", finish - start)
                return cursor.fetchall()

        elif column == 3:
            a = int(input("Input start: "))
            b = int(input("Input finish: "))
            with connection.cursor() as cursor:
                start = time.time()
                cursor.execute("""SELECT * FROM "Ticket" WHERE %s <= id_hall and id_hall <= %s;""", (a, b,))
                finish = time.time()

                print("\nSearch duration = ", finish - start)
                return cursor.fetchall()

        elif column == 4:
            a = int(input("Input start: "))
            b = int(input("Input finish: "))
            with connection.cursor() as cursor:
                start = time.time()
                cursor.execute("""SELECT * FROM "Ticket" WHERE %s <= film_id and film_id <= %s;""", (a, b,))
                finish = time.time()

                print("\nSearch duration = ", finish - start)
                return cursor.fetchall()

        elif column == 5:
            a = float(input("Input start: "))
            b = float(input("Input finish: "))
            with connection.cursor() as cursor:
                start = time.time()
                cursor.execute("""SELECT * FROM "Ticket" WHERE %s <= price and price <= %s;""", (a, b,))
                finish = time.time()

                print("\nSearch duration = ", finish - start)
                return cursor.fetchall()

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
            with connection.cursor() as cursor:
                start = time.time()
                cursor.execute("""SELECT * FROM "Ticket" WHERE %s <= date_and_time and date_and_time <= %s;""",
                               (a, b,))
                finish = time.time()

                print("\nSearch duration = ", finish - start)
                return cursor.fetchall()
        else:
            print("\n[INFO] Error input, try again!\n")
            search(connection, 4)

    elif table == 5:
        column = int(input("1 = to search film id\n"
                           "2 = to search name\n"
                           "3 = to search duration\n"
                           "Input: "))
        if column == 1:
            a = int(input("Input start: "))
            b = int(input("Input finish: "))
            with connection.cursor() as cursor:
                start = time.time()
                cursor.execute("""SELECT * FROM "Film" WHERE %s <= id_film and id_film <= %s;""", (a, b,))
                finish = time.time()

                print("\nSearch duration = ", finish - start)
                return cursor.fetchall()

        elif column == 2:
            txt = str(input("Input text: "))
            with connection.cursor() as cursor:
                start = time.time()
                cursor.execute("""SELECT * FROM "Film" WHERE to_tsvector(name) 
                    @@ plainto_tsquery(%s);;""", (txt,))
                finish = time.time()

                print("\nSearch duration = ", finish - start)
                return cursor.fetchall()

        elif column == 3:

            time_entry_a = input("New start duration in HH:MM format: ")
            hour, minute = map(int, time_entry_a.split(':'))
            a = datetime.time(hour, minute)

            time_entry_b = input("New finish duration in HH:MM format: ")
            hour, minute = map(int, time_entry_b.split(':'))
            b = datetime.time(hour, minute)
            with connection.cursor() as cursor:
                start = time.time()
                cursor.execute("""SELECT * FROM "Film" WHERE %s <= duration and duration <= %s;""", (a, b,))
                finish = time.time()

                print("\nSearch duration = ", finish - start)
                return cursor.fetchall()
        else:
            print("\n[INFO] Error input, try again!\n")
            search(connection, 5)

    else:
        print("\n[INFO] Error input, try again!\n")
