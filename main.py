import sqlalchemy
from sqlalchemy.orm import sessionmaker
from models import create_tables, Publisher, Book, Shop, Stock, Sale


def isint(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


password = ''
db = ''

DSN = f'postgresql://postgres:{password}@localhost:5432/{db}'
engine = sqlalchemy.create_engine(DSN)

create_tables(engine)


Session = sessionmaker(bind=engine)
session = Session()

publisher1 = Publisher(name='Нижполиграф')
publisher2 = Publisher(name='Алтапрес')
publisher3 = Publisher(name='Советская Сибирь')
book1 = Book(title='Из тьмы веков', id_publisher=1)
book2 = Book(title='Наставление верующим', id_publisher=2)
book3 = Book(title='Ар-Рахик Аль-Махтум', id_publisher=3)
shop1 = Shop(name='Jeanne books')
shop2 = Shop(name='Ассалам')
stock1 = Stock(id_book=1, id_shop=1, count=5)
stock2 = Stock(id_book=2, id_shop=2, count=7)
stock3 = Stock(id_book=3, id_shop=1, count=4)
sale1 = Sale(price='455 руб. 00 коп.', date_sale='19 февраля 2019 года', id_stock=1, count=1)
sale2 = Sale(price='1530', date_sale='02.06.2020', id_stock=2, count=2)
sale3 = Sale(price='10$', date_sale='01 октябрь 2022', id_stock=3, count=1)
session.add_all([publisher1, publisher2, publisher3, book1, book2, book3, shop1,
                 shop2, stock1, stock2, stock3, sale1, sale2, sale3])
session.commit()

relations = session.query(Shop).join(Stock).join(Book).join(Publisher)
inp_pub = input('Введите имя или id издателя: ')


if isint(inp_pub):
    filtred2 = relations.filter(Publisher.id == inp_pub).all()
    for shops in filtred2:
        print(f'{shops.id}. {shops.name}')
else:
    filtred1 = relations.filter(Publisher.name == inp_pub).all()
    for shops in filtred1:
        print(f'{shops.id}. {shops.name}')

session.close()
