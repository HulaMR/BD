import time
from faker import Faker
from random import *
import datetime
from sqlalchemy import create_engine, Column, ForeignKey, Integer, String, Interval, Numeric, TIMESTAMP, and_
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine('postgresql://postgres:4214@localhost:5432/Labs', echo=False)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

fake = Faker()


class Cinema(Base):
    __tablename__ = 'Cinema'
    id_cinema = Column(Integer, primary_key=True)
    name = Column(String)
    adress = Column(String)

    crs = relationship('Cash_register')
    halls = relationship('Hall')

    def __init__(self, id_cinema: int, name: str, adress: str):
        self.id_cinema = id_cinema
        self.name = name
        self.adress = adress


class Cash_register(Base):
    __tablename__ = 'Cash_register'
    id_cr = Column(Integer, primary_key=True)
    id_cinema = Column(Integer, ForeignKey('Cinema.id_cinema'))
    the_name_of_the_cashier = Column(String)
    number_of_available_tickets = Column(Integer)

    tick = relationship('Ticket')

    def __init__(self, id_cr: int, id_cinema: int, the_name_of_the_cashier: str, number_of_available_tickets: int):
        self.id_cr = id_cr
        self.id_cinema = id_cinema
        self.the_name_of_the_cashier = the_name_of_the_cashier
        self.number_of_available_tickets = number_of_available_tickets


class Hall(Base):
    __tablename__ = 'Hall'
    id_hall = Column(Integer, primary_key=True)
    id_cinema = Column(Integer, ForeignKey('Cinema.id_cinema'))
    number_of_seats = Column(Integer)

    tickets = relationship('Ticket')

    def __init__(self, id_hall: int, id_cinema: int, number_of_seats: int):
        self.id_hall = id_hall
        self.id_cinema = id_cinema
        self.number_of_seats = number_of_seats


class Ticket(Base):
    __tablename__ = 'Ticket'
    id_ticket = Column(Integer, primary_key=True)
    id_cr = Column(Integer, ForeignKey('Cash_register.id_cr'))
    id_hall = Column(Integer, ForeignKey('Hall.id_hall'))
    id_film = Column(Integer, ForeignKey('Film.id_film'))
    price = Column(Numeric)
    date_and_time = Column(TIMESTAMP)

    def __init__(self, id_ticket: int, id_cr: int, id_hall: int, id_film: int, price: float,
                 date_and_time: datetime.datetime):
        self.id_ticket = id_ticket
        self.id_cr = id_cr
        self.id_hall = id_hall
        self.id_film = id_film
        self.price = price
        self.date_and_time = date_and_time


class Film(Base):
    __tablename__ = 'Film'
    id_film = Column(Integer, primary_key=True)
    name = Column(String)
    duration = Column(Interval)

    tickets = relationship('Ticket')

    def __init__(self, id_film: int, name: str, duration: datetime.time):
        self.id_film = id_film
        self.name = name
        self.duration = duration


def start():
    Base.metadata.create_all(engine)


def insert(table, inp):
    if table == 1:
        cin1 = Cinema(inp[0], inp[1], inp[2])
        session.add(cin1)
        session.commit()

    elif table == 2:
        h1 = Hall(inp[0], inp[1], inp[2])
        session.add(h1)
        session.commit()

    elif table == 3:
        cr1 = Cash_register(inp[0], inp[1], inp[2], inp[3])
        session.add(cr1)
        session.commit()

    elif table == 4:
        t1 = Ticket(inp[0], inp[1], inp[2], inp[3], inp[4], inp[5])
        session.add(t1)
        session.commit()

    elif table == 5:
        f1 = Film(inp[0], inp[1], inp[2])
        session.add(f1)

        session.commit()


def insert_rand(table, count):
    if table == 1:
        for i in range(0, count):
            cin1 = Cinema((session.query(Cinema.id_cinema).count() + 3), fake.company(), fake.address())
            session.add(cin1)
            session.commit()

    elif table == 2:
        r_id_c = randrange(1, session.query(Cinema.id_cinema).count())
        num = randint(150, 400)

        cr1 = Hall((session.query(Hall.id_hall).count() + 2), r_id_c, num)
        session.add(cr1)
        session.commit()

    elif table == 3:
        r_id_c = randrange(1, session.query(Cinema.id_cinema).count())
        num = randint(150, 400)

        cr1 = Cash_register((session.query(Cash_register.id_cr).count() + 2), r_id_c, fake.name(), num)
        session.add(cr1)
        session.commit()

    elif table == 4:
        r_id_cr = randrange(1, session.query(Cash_register.id_cr).count())
        r_id_h = randrange(1, session.query(Hall.id_hall).count())
        r_id_f = randrange(1, session.query(Film.id_film).count())
        r_price = float(randrange(50, 150))
        dt = datetime.datetime(randrange(2021, 2022), randrange(1, 12), randrange(1, 30),
                               randrange(10, 22), randrange(1, 59))

        t1 = Ticket((session.query(Ticket.id_ticket).count() + 2), r_id_cr, r_id_h, r_id_f, r_price, dt)
        session.add(t1)
        session.commit()

    elif table == 5:
        for i in range(0, count):
            t = datetime.time(randrange(1, 3), randrange(1, 59))
            f1 = Film((session.query(Film.id_film).count() + 2), fake.word(), t)
            session.add(f1)
            session.commit()


def select_table(table, inp):
    string = inp[0]

    if table == 1:
        if string == 1:
            n_id = inp[1]
            cin = session.query(Cinema).filter(Cinema.id_cinema == int(n_id)).first()
            r = [cin.name, cin.adress]
            return r

        elif string == 2:
            cin = session.query(Cinema)
            return cin

    elif table == 2:
        if string == 1:
            n_id = inp[1]
            cin = session.query(Hall).filter(Hall.id_hall == int(n_id)).first()
            r = [cin.id_cinema, cin.number_of_seats]
            return r

        elif string == 2:
            cin = session.query(Hall)
            return cin

    elif table == 3:
        if string == 1:
            n_id = inp[1]
            cin = session.query(Cash_register).filter(Cash_register.id_cr == int(n_id)).first()
            r = [cin.id_cinema, cin.the_name_of_the_cashier, cin.number_of_available_tickets]
            return r

        elif string == 2:
            cin = session.query(Cash_register)
            return cin

    elif table == 4:
        if string == 1:
            n_id = inp[1]
            cin = session.query(Ticket).filter(Ticket.id_ticket == int(n_id)).first()
            r = [cin.id_cr, cin.id_hall, cin.id_film, cin.price, cin.date_and_time]
            return r

        elif string == 2:
            cin = session.query(Ticket)
            return cin

    elif table == 5:
        if string == 1:
            n_id = inp[1]
            cin = session.query(Film).filter(Film.id_film == int(n_id)).first()
            r = [cin.name, cin.duration]
            return r

        elif string == 2:
            cin = session.query(Film)
            return cin


def update(table, inp):
    n_id = inp[0]
    column = inp[1]
    new = inp[2]

    if table == 1:
        if column == 1:
            cin = session.query(Cinema).filter(Cinema.id_cinema == int(n_id)).first()
            cin.name = new
            session.commit()

        elif column == 2:
            cin = session.query(Cinema).filter(Cinema.id_cinema == int(n_id)).first()
            cin.adress = new
            session.commit()

    elif table == 2:
        if column == 1:
            cin = session.query(Hall).filter(Hall.id_hall == int(n_id)).first()
            cin.id_cinema = new
            session.commit()

        elif column == 2:
            cin = session.query(Hall).filter(Hall.id_hall == int(n_id)).first()
            cin.number_of_seats = new
            session.commit()

    elif table == 3:
        if column == 1:
            cin = session.query(Cash_register).filter(Cash_register.id_cr == int(n_id)).first()
            cin.id_cinema = new
            session.commit()

        elif column == 2:
            cin = session.query(Cash_register).filter(Cash_register.id_cr == int(n_id)).first()
            cin.the_name_of_the_cashier = new
            session.commit()

        elif column == 3:
            cin = session.query(Cash_register).filter(Cash_register.id_cr == int(n_id)).first()
            cin.number_of_available_tickets = new
            session.commit()

    elif table == 4:
        if column == 1:
            cin = session.query(Ticket).filter(Ticket.id_ticket == int(n_id)).first()
            cin.id_cr = new
            session.commit()

        elif column == 2:
            cin = session.query(Ticket).filter(Ticket.id_ticket == int(n_id)).first()
            cin.id_hall = new
            session.commit()

        elif column == 3:
            cin = session.query(Ticket).filter(Ticket.id_ticket == int(n_id)).first()
            cin.id_film = new
            session.commit()

        elif column == 4:
            cin = session.query(Ticket).filter(Ticket.id_ticket == int(n_id)).first()
            cin.price = new
            session.commit()

        elif column == 5:
            cin = session.query(Ticket).filter(Ticket.id_ticket == int(n_id)).first()
            cin.date_and_time = new
            session.commit()

    elif table == 5:
        if column == 1:
            cin = session.query(Film).filter(Film.id_film == int(n_id)).first()
            cin.name = new
            session.commit()

        elif column == 2:
            cin = session.query(Film).filter(Film.id_film == int(n_id)).first()
            cin.duration = new
            session.commit()


def delete(table, n_id):

    if table == 1:
        cin = session.query(Cinema).filter(Cinema.id_cinema == int(n_id)).first()
        session.delete(cin)
        session.commit()

    elif table == 2:
        cin = session.query(Hall).filter(Hall.id_hall == int(n_id)).first()
        session.delete(cin)
        session.commit()

    elif table == 3:
        cin = session.query(Cash_register).filter(Cash_register.id_cr == int(n_id)).first()
        session.delete(cin)
        session.commit()

    elif table == 4:
        cin = session.query(Ticket).filter(Ticket.id_ticket == int(n_id)).first()
        session.delete(cin)
        session.commit()

    elif table == 5:
        cin = session.query(Film).filter(Film.id_film == int(n_id)).first()
        session.delete(cin)
        session.commit()


def search(table, inp):
    column = inp[0]

    if table == 1:
        if column == 1:
            a = inp[1]
            b = inp[2]

            start_t = time.time()

            cin = session.query(Cinema).filter(
                and_(Cinema.id_cinema >= int(a)), Cinema.id_cinema <= int(b)
            ).all()

            finish = time.time()
            search_duration = finish - start_t

            ret = [cin, search_duration]
            return ret

        elif column == 2:
            txt = inp[1]
            start_t = time.time()

            cin = session.query(Cinema).filter(
                and_(Cinema.name == txt), Cinema.adress == txt
            ).all()

            finish = time.time()
            search_duration = finish - start_t

            ret = [cin, search_duration]
            return ret

    elif table == 2:

        if column == 1:
            a = inp[1]
            b = inp[2]
            start_t = time.time()

            cin = session.query(Hall).filter(
                and_(Hall.id_hall >= int(a)), Hall.id_hall <= int(b)
            ).all()

            finish = time.time()
            search_duration = finish - start_t

            ret = [cin, search_duration]
            return ret

        elif column == 2:
            a = inp[1]
            b = inp[2]
            start_t = time.time()

            cin = session.query(Hall).filter(
                and_(Hall.id_cinema >= int(a)), Hall.id_cinema <= int(b)
            ).all()

            finish = time.time()
            search_duration = finish - start_t

            ret = [cin, search_duration]
            return ret

        elif column == 3:
            a = inp[1]
            b = inp[2]
            start_t = time.time()

            cin = session.query(Hall).filter(
                and_(Hall.number_of_seats >= int(a)), Hall.number_of_seats <= int(b)
            ).all()

            finish = time.time()
            search_duration = finish - start_t

            ret = [cin, search_duration]
            return ret

    elif table == 3:
        if column == 1:
            a = inp[1]
            b = inp[2]
            start_t = time.time()

            cin = session.query(Cash_register).filter(
                and_(Cash_register.id_cr >= int(a)), Cash_register.id_cr <= int(b)
            ).all()

            finish = time.time()
            search_duration = finish - start_t

            ret = [cin, search_duration]
            return ret

        elif column == 2:
            a = inp[1]
            b = inp[2]
            start_t = time.time()

            cin = session.query(Cash_register).filter(
                and_(Cash_register.id_cinema >= int(a)), Cash_register.id_cinema <= int(b)
            ).all()

            finish = time.time()
            search_duration = finish - start_t

            ret = [cin, search_duration]
            return ret

        elif column == 3:
            txt = inp[1]
            start_t = time.time()

            cin = session.query(Cash_register).filter(Cash_register.the_name_of_the_cashier == txt).all()

            finish = time.time()
            search_duration = finish - start_t

            ret = [cin, search_duration]
            return ret

        elif column == 4:
            a = inp[1]
            b = inp[2]
            start_t = time.time()

            cin = session.query(Cash_register).filter(
                and_(Cash_register.number_of_available_tickets >= int(a)),
                Cash_register.number_of_available_tickets <= int(b)
            ).all()

            finish = time.time()
            search_duration = finish - start_t

            ret = [cin, search_duration]
            return ret

    elif table == 4:

        if column == 1:
            a = inp[1]
            b = inp[2]
            start_t = time.time()

            cin = session.query(Ticket).filter(
                and_(Ticket.id_ticket >= int(a)), Ticket.id_ticket <= int(b)
            ).all()

            finish = time.time()
            search_duration = finish - start_t

            ret = [cin, search_duration]
            return ret

        elif column == 2:
            a = inp[1]
            b = inp[2]
            start_t = time.time()

            cin = session.query(Ticket).filter(
                and_(Ticket.id_cr >= int(a)), Ticket.id_cr <= int(b)
            ).all()

            finish = time.time()
            search_duration = finish - start_t

            ret = [cin, search_duration]
            return ret

        elif column == 3:
            a = inp[1]
            b = inp[2]
            start_t = time.time()

            cin = session.query(Ticket).filter(
                and_(Ticket.id_hall >= int(a)), Ticket.id_hall <= int(b)
            ).all()

            finish = time.time()
            search_duration = finish - start_t

            ret = [cin, search_duration]
            return ret

        elif column == 4:
            a = inp[1]
            b = inp[2]
            start_t = time.time()

            cin = session.query(Ticket).filter(
                and_(Ticket.id_film >= int(a)), Ticket.id_film <= int(b)
            ).all()

            finish = time.time()
            search_duration = finish - start_t

            ret = [cin, search_duration]
            return ret

        elif column == 5:
            a = inp[1]
            b = inp[2]
            start_t = time.time()

            cin = session.query(Ticket).filter(
                and_(Ticket.price >= float(a)), Ticket.price <= float(b)
            ).all()

            finish = time.time()
            search_duration = finish - start_t

            ret = [cin, search_duration]
            return ret

        elif column == 6:
            a = inp[1]
            b = inp[2]
            start_t = time.time()

            cin = session.query(Ticket).filter(
                and_(Ticket.date_and_time >= a), Ticket.date_and_time <= b
            ).all()

            finish = time.time()
            search_duration = finish - start_t

            ret = [cin, search_duration]
            return ret

    elif table == 5:
        if column == 1:
            a = inp[1]
            b = inp[2]
            start_t = time.time()

            cin = session.query(Film).filter(
                and_(Film.id_film >= a), Film.id_film <= b
            ).all()

            finish = time.time()
            search_duration = finish - start_t

            ret = [cin, search_duration]
            return ret

        elif column == 2:
            txt = inp[1]
            start_t = time.time()

            cin = session.query(Film).filter(Film.name == txt).all()

            finish = time.time()
            search_duration = finish - start_t

            ret = [cin, search_duration]
            return ret

        elif column == 3:
            a = inp[1]
            b = inp[2]
            start_t = time.time()

            cin = session.query(Film).filter(
                and_(Film.duration >= a), Film.duration <= b
            ).all()

            finish = time.time()
            search_duration = finish - start_t

            ret = [cin, search_duration]
            return ret
