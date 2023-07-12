# создание базы данных и сесии по работе с ней
import sqlalchemy as sa
import sqlalchemy.orm as orm
from sqlalchemy.orm import Session
import sqlalchemy.ext.declarative as dec

SqlAlchemyBase = orm.declarative_base()

created = None  # создана ли сессия

def global_init(db_file):
    global created  # доступ к функции

    if created:
        return

    if not db_file or not db_file.strip():
        raise Exception("Забыли подключить файл базы!")

    conn_str = f'sqlite:///{db_file.strip()}?check_same_thread=False'  # мы не используем тот же самый поток данных
    print(f'Мы подключились к базе: {conn_str}')

    engine = sa.create_engine(conn_str, echo=False)
    created = orm.sessionmaker(bind=engine) # создаем сессию и привязываем к engine
    from . import all_models

    SqlAlchemyBase.metadata.create_all(engine)
def create_session() -> Session:  # будет возвращать сессию
    global created
    return created