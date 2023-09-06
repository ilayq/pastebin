from sqlite3 import connect
from abc import ABC, abstractmethod 


class DB(ABC):
    def __init__(self):
        self.reinit()

    @abstractmethod
    def add_paste(self, contenthash: str, content: str) -> bool:
        pass

    @abstractmethod
    def get_paste(self, contenthash: str) -> str:
        pass
    
    @abstractmethod
    def reinit(self):
        ...


class sqliteDB(DB):
    def add_paste(self, contenthash: str, content: str) -> bool:
        with connect('db.sqlite') as con:
            cur = con.cursor()
            try:
                cur.execute(
                    '''
                        insert into links values (?, ?)
                    ''', (contenthash, content)
                )
                return True
            except Exception as e:
                print(e)
                con.rollback()
                return False
            
    def reinit(self):
        with connect('db.sqlite') as con:
            cur = con.cursor()
            cur.execute('''
                        drop table if exists links
                        ''')
            cur.execute('''
                        create table if not exists links(
                            contenthash text(64) primary key,
                            content text not null
                        )
                        ''')

    def get_paste(self, contenthash: str) -> str:
        with connect('db.sqlite') as con:
            cur = con.cursor()
            for row in cur.execute('''select contenthash, content from links
                                    where contenthash = ?''', (contenthash, )):
                return row[1]
