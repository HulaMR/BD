import time
from random import *
import psycopg2


def connect():
    connection = psycopg2.connect(
        database="Labs",
        user="postgres",
        password="4214",
        host="127.0.0.1")
    connection.autocommit = True
    return connection


def close():
    connection = connect()
    connection.close()


r_adr = ['Voli Avenue, 2, Lutsk, Volyn region, 43000',
         'Svitla Street, 2, Lutsk, Volyn region, 43000',
         'Kopernika Street, 2, Lutsk, Volyn region, 43000']


def insert(table, inp):
    connection = connect()
    if table == 1:
        with connection.cursor() as cursor:
            cursor.execute("""INSERT INTO "Cinema"(id_cinema, name, adress) VALUES(%s, %s, %s);""",
                           (inp[0], inp[1], inp[2],))

    elif table == 2:
        with connection.cursor() as cursor:
            cursor.execute("""INSERT INTO "Hall"(id_hall, id_cinema, number_of_seats) VALUES(%s, %s, %s);""",
                           (inp[0], inp[1], inp[2],))

    elif table == 3:
        with connection.cursor() as cursor:
            cursor.execute("""INSERT INTO "Cash register"(id_cr, id_cinema, 
                the_name_of_the_cashier, number_of_available_tickets) 
                VALUES(%s, %s, %s, %s);""", (inp[0], inp[1], inp[2], inp[3],))

    elif table == 4:
        with connection.cursor() as cursor:
            cursor.execute("""INSERT INTO "Ticket"(id_ticket, id_cr, id_hall, film_id, price, date_and_time) 
                VALUES(%s, %s, %s, %s, %s, %s);""", (inp[0], inp[1], inp[2], inp[3], inp[4], inp[5],))

    elif table == 5:
        with connection.cursor() as cursor:
            cursor.execute("""INSERT INTO "Film"(id_film, name, duration) VALUES(%s, %s, %s);""",
                           (inp[0], inp[1], inp[2],))


def insert_rand(table, count):
    connection = connect()
    if table == 1:
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

    elif table == 2:
        with connection.cursor() as cursor:
            cursor.execute("""INSERT INTO "Hall"(id_hall, id_cinema, number_of_seats) 
                 VALUES((SELECT(select count(id_hall) from "Hall")+1::int), 
                 (SELECT id_cinema FROM "Cinema" OFFSET 
                 floor(random()*(select count(id_cinema) from "Cinema")) LIMIT 1), 
                 trunc(random()*100+200)::int);""")

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

    elif table == 5:
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


def update(table, inp):
    connection = connect()

    n_id = inp[0]
    column = inp[1]
    new = inp[2]

    if table == 1:
        if column == 1:
            with connection.cursor() as cursor:
                cursor.execute("""update "Cinema" set name = %s where id_cinema = %s;""", (new, n_id,))

        elif column == 2:
            with connection.cursor() as cursor:
                cursor.execute("""update "Cinema" set adress = %s where id_cinema = %s;""", (new, n_id,))

    elif table == 2:
        if column == 1:
            with connection.cursor() as cursor:
                cursor.execute("""update "Hall" set id_cinema = %s where id_hall = %s;""", (new, n_id,))

        elif column == 2:
            with connection.cursor() as cursor:
                cursor.execute("""update "Hall" set number_of_seats = %s where id_hall = %s;""", (new, n_id,))

    elif table == 3:
        if column == 1:
            with connection.cursor() as cursor:
                cursor.execute("""update "Cash register" set id_cinema = %s where id_cr = %s;""", (new, n_id,))

        elif column == 2:
            with connection.cursor() as cursor:
                cursor.execute("""update "Cash register" set the_name_of_the_cashier = %s where id_cr = %s;""",
                               (new, n_id,))

        elif column == 3:
            with connection.cursor() as cursor:
                cursor.execute("""update "Cash register" set number_of_available_tickets = %s where id_cr = %s;""",
                               (new, n_id,))

    elif table == 4:
        if column == 1:
            with connection.cursor() as cursor:
                cursor.execute("""update "Ticket" set id_cr = %s where id_ticket = %s;""", (new, n_id,))

        elif column == 2:
            with connection.cursor() as cursor:
                cursor.execute("""update "Ticket" set id_hall = %s where id_ticket = %s;""",
                               (new, n_id,))

        elif column == 3:
            with connection.cursor() as cursor:
                cursor.execute("""update "Ticket" set film_id = %s where id_ticket = %s;""",
                               (new, n_id,))

        elif column == 4:
            with connection.cursor() as cursor:
                cursor.execute("""update "Ticket" set price = %s where id_ticket = %s;""",
                               (new, n_id,))

        elif column == 5:
            with connection.cursor() as cursor:
                cursor.execute("""update "Ticket" set date_and_time = %s where id_ticket = %s;""",
                               (new, n_id,))

    elif table == 5:

        if column == 1:
            with connection.cursor() as cursor:
                cursor.execute("""update "Film" set name = %s where id_film = %s;""", (new, n_id,))

        elif column == 2:
            with connection.cursor() as cursor:
                cursor.execute("""update "Film" set duration = %s where id_film = %s;""", (new, n_id,))


def delete(table, nid):
    connection = connect()

    if table == 1:
        with connection.cursor() as cursor:
            cursor.execute("""DELETE from "Cinema" WHERE id_cinema = %s;""", (nid,))

    elif table == 2:
        with connection.cursor() as cursor:
            cursor.execute("""DELETE from "Hall" WHERE id_hall = %s;""", (nid,))

    elif table == 3:
        with connection.cursor() as cursor:
            cursor.execute("""DELETE from "Cash register" WHERE id_cr = %s;""", (nid,))

    elif table == 4:
        with connection.cursor() as cursor:
            cursor.execute("""DELETE from "Ticket" WHERE id_ticket = %s;""", (nid,))

    elif table == 5:
        with connection.cursor() as cursor:
            cursor.execute("""DELETE from "Film" WHERE id_film = %s;""", (nid,))


def select_table(table, inp):
    connection = connect()

    string = inp[0]
    n_id = inp[1]

    if table == 1:
        if string == 1:
            with connection.cursor() as cursor:
                cursor.execute("""SELECT * FROM "Cinema" where id_cinema = %s;""", (n_id,))
                return cursor.fetchmany(1)

        elif string == 2:
            with connection.cursor() as cursor:
                cursor.execute("""SELECT * FROM "Cinema";""")
                return cursor.fetchall()

    elif table == 2:
        if string == 1:
            with connection.cursor() as cursor:
                cursor.execute("""SELECT * FROM "Hall" where id_hall = %s;""", (n_id,))
                return cursor.fetchmany(1)

        elif string == 2:
            with connection.cursor() as cursor:
                cursor.execute("""SELECT * FROM "Hall";""")
                return cursor.fetchall()

    elif table == 3:
        if string == 1:
            with connection.cursor() as cursor:
                cursor.execute("""SELECT * FROM "Cash register" where id_cr = %s;""", (n_id,))
                return cursor.fetchmany(1)

        elif string == 2:
            with connection.cursor() as cursor:
                cursor.execute("""SELECT * FROM "Cash register";""")
                return cursor.fetchall()

    elif table == 4:
        if string == 1:
            with connection.cursor() as cursor:
                cursor.execute("""SELECT * FROM "Ticket" where id_ticket = %s;""", (n_id,))
                return cursor.fetchmany(1)

        elif string == 2:
            with connection.cursor() as cursor:
                cursor.execute("""SELECT * FROM "Ticket";""")
                return cursor.fetchall()

    elif table == 5:
        if string == 1:
            with connection.cursor() as cursor:
                cursor.execute("""SELECT * FROM "Film" where id_film = %s;""", (n_id,))
                return cursor.fetchmany(1)

        elif string == 2:
            with connection.cursor() as cursor:
                cursor.execute("""SELECT * FROM "Film";""")
                return cursor.fetchall()


def search(table, inp):
    connection = connect()

    column = inp[0]

    if table == 1:
        if column == 1:
            a = inp[1]
            b = inp[2]
            with connection.cursor() as cursor:
                start = time.time()
                cursor.execute("""SELECT * FROM "Cinema" WHERE %s <= id_cinema and id_cinema <= %s;""", (a, b,))
                finish = time.time()

                search_duration = finish - start
                f_a = cursor.fetchall()
                ret = [f_a, search_duration]
                return ret

        elif column == 2:
            txt = inp[1]
            with connection.cursor() as cursor:
                start = time.time()
                cursor.execute("""SELECT * FROM "Cinema" WHERE 
                    to_tsvector(name) || to_tsvector(adress) 
                    @@ plainto_tsquery(%s);;""", (txt,))
                finish = time.time()
                search_duration = finish - start
                f_a = cursor.fetchall()
                ret = [f_a, search_duration]
                return ret

    elif table == 2:

        if column == 1:
            a = inp[1]
            b = inp[2]
            with connection.cursor() as cursor:
                start = time.time()
                cursor.execute("""SELECT * FROM "Hall" WHERE %s <= id_hall and id_hall <= %s;""", (a, b,))
                finish = time.time()

                search_duration = finish - start
                f_a = cursor.fetchall()
                ret = [f_a, search_duration]
                return ret

        elif column == 2:
            a = inp[1]
            b = inp[2]
            with connection.cursor() as cursor:
                start = time.time()
                cursor.execute("""SELECT * FROM "Hall" WHERE %s <= id_cinema and id_cinema <= %s;""", (a, b,))
                finish = time.time()

                search_duration = finish - start
                f_a = cursor.fetchall()
                ret = [f_a, search_duration]
                return ret

        elif column == 3:
            a = inp[1]
            b = inp[2]
            with connection.cursor() as cursor:
                start = time.time()
                cursor.execute("""SELECT * FROM "Hall" WHERE %s <= number_of_seats and
                     number_of_seats <= %s;""", (a, b,))
                finish = time.time()

                search_duration = finish - start
                f_a = cursor.fetchall()
                ret = [f_a, search_duration]
                return ret

    elif table == 3:
        if column == 1:
            a = inp[1]
            b = inp[2]
            with connection.cursor() as cursor:
                start = time.time()
                cursor.execute("""SELECT * FROM "Cash register" WHERE %s <= id_cr and id_cr <= %s;""", (a, b,))
                finish = time.time()

                search_duration = finish - start
                f_a = cursor.fetchall()
                ret = [f_a, search_duration]
                return ret

        elif column == 2:
            a = inp[1]
            b = inp[2]
            with connection.cursor() as cursor:
                start = time.time()
                cursor.execute("""SELECT * FROM "Cash register" WHERE %s <= id_cinema and id_cinema <= %s;""",
                               (a, b,))
                finish = time.time()

                search_duration = finish - start
                f_a = cursor.fetchall()
                ret = [f_a, search_duration]
                return ret

        elif column == 3:
            txt = inp[1]
            with connection.cursor() as cursor:
                start = time.time()
                cursor.execute("""SELECT * FROM "Cash register" WHERE to_tsvector(the_name_of_the_cashier) 
                    @@ plainto_tsquery(%s);;""", (txt,))
                finish = time.time()

                search_duration = finish - start
                f_a = cursor.fetchall()
                ret = [f_a, search_duration]
                return ret

        elif column == 4:
            a = inp[1]
            b = inp[2]
            with connection.cursor() as cursor:
                start = time.time()
                cursor.execute("""SELECT * FROM "Cash register" WHERE %s <= number_of_available_tickets and
                    number_of_available_tickets <= %s;""", (a, b,))
                finish = time.time()

                search_duration = finish - start
                f_a = cursor.fetchall()
                ret = [f_a, search_duration]
                return ret

    elif table == 4:

        if column == 1:
            a = inp[1]
            b = inp[2]
            with connection.cursor() as cursor:
                start = time.time()
                cursor.execute("""SELECT * FROM "Ticket" WHERE %s <= id_ticket and id_ticket <= %s;""", (a, b,))
                finish = time.time()

                search_duration = finish - start
                f_a = cursor.fetchall()
                ret = [f_a, search_duration]
                return ret

        elif column == 2:
            a = inp[1]
            b = inp[2]
            with connection.cursor() as cursor:
                start = time.time()
                cursor.execute("""SELECT * FROM "Ticket" WHERE %s <= id_cr and id_cr <= %s;""", (a, b,))
                finish = time.time()

                search_duration = finish - start
                f_a = cursor.fetchall()
                ret = [f_a, search_duration]
                return ret

        elif column == 3:
            a = inp[1]
            b = inp[2]
            with connection.cursor() as cursor:
                start = time.time()
                cursor.execute("""SELECT * FROM "Ticket" WHERE %s <= id_hall and id_hall <= %s;""", (a, b,))
                finish = time.time()

                search_duration = finish - start
                f_a = cursor.fetchall()
                ret = [f_a, search_duration]
                return ret

        elif column == 4:
            a = inp[1]
            b = inp[2]
            with connection.cursor() as cursor:
                start = time.time()
                cursor.execute("""SELECT * FROM "Ticket" WHERE %s <= film_id and film_id <= %s;""", (a, b,))
                finish = time.time()

                search_duration = finish - start
                f_a = cursor.fetchall()
                ret = [f_a, search_duration]
                return ret

        elif column == 5:
            a = inp[1]
            b = inp[2]
            with connection.cursor() as cursor:
                start = time.time()
                cursor.execute("""SELECT * FROM "Ticket" WHERE %s <= price and price <= %s;""", (a, b,))
                finish = time.time()

                search_duration = finish - start
                f_a = cursor.fetchall()
                ret = [f_a, search_duration]
                return ret

        elif column == 6:
            a = inp[1]
            b = inp[2]
            with connection.cursor() as cursor:
                start = time.time()
                cursor.execute("""SELECT * FROM "Ticket" WHERE %s <= date_and_time and date_and_time <= %s;""",
                               (a, b,))
                finish = time.time()

                search_duration = finish - start
                f_a = cursor.fetchall()
                ret = [f_a, search_duration]
                return ret

    elif table == 5:
        if column == 1:
            a = inp[1]
            b = inp[2]
            with connection.cursor() as cursor:
                start = time.time()
                cursor.execute("""SELECT * FROM "Film" WHERE %s <= id_film and id_film <= %s;""", (a, b,))
                finish = time.time()

                search_duration = finish - start
                f_a = cursor.fetchall()
                ret = [f_a, search_duration]
                return ret

        elif column == 2:
            txt = inp[1]
            with connection.cursor() as cursor:
                start = time.time()
                cursor.execute("""SELECT * FROM "Film" WHERE to_tsvector(name) 
                    @@ plainto_tsquery(%s);;""", (txt,))
                finish = time.time()

                search_duration = finish - start
                f_a = cursor.fetchall()
                ret = [f_a, search_duration]
                return ret

        elif column == 3:
            a = inp[1]
            b = inp[2]
            with connection.cursor() as cursor:
                start = time.time()
                cursor.execute("""SELECT * FROM "Film" WHERE %s <= duration and duration <= %s;""", (a, b,))
                finish = time.time()

                search_duration = finish - start
                f_a = cursor.fetchall()
                ret = [f_a, search_duration]
                return ret
