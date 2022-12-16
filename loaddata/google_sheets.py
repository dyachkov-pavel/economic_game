import ssl
import warnings

import numpy as np
import pandas as pd

ssl._create_default_https_context = ssl._create_unverified_context
warnings.filterwarnings('ignore', '.*The frame.append method*', )


def hashpricedf(a):
    hashprice = {}
    for i in a.drop(columns=['price']).name.to_list():
        hashprice[i] = a.loc[a.name == i].index.to_list()[0]
    return hashprice


def opern(df):
    s = []
    for i in [str(i) for i in range(1, 20)]:
        s.append(df[i])
    return s


def depozit(arr):
    if arr == '—':
        return 0
    else:
        return 1


def lastoper(d):
    try:

        i = d.index(0.0)
        if i <= 5:
            return (str(d[0:5])).replace('[', '').replace(']', '').replace('"', '')
        else:
            return (str(d[i - 5:i])).replace('[', '').replace(']', '').replace('"', '')

    except ValueError:
        return (str(d[len(d) - 5:len(d)])).replace('[', '').replace(']', '').replace('"', '')


def renamestockstoindex(s):
    return


class DfGetter():
    def url_gen(self):
        '''
        :param id: Айди документа.
        :param name: Имя листа
        :return: Ссылку на лист.
        '''
        return 'https://docs.google.com/spreadsheets/d/{0}/gviz/tq?tqx=out:csv&sheet={1}'.format(
            self.id,
            self.name)

    def stockurl_gen(self):
        '''
        :return:Ссылки на лист с акциями
        '''
        return ['https://docs.google.com/spreadsheets/d/{0}/gviz/tq?tqx=out:csv&sheet={1}'.format(
            self.stockid,
            self.stocknames[0]),
            'https://docs.google.com/spreadsheets/d/{0}/gviz/tq?tqx=out:csv&sheet={1}'.format(
                self.stockid,
                self.stocknames[1])]

    '''
    Некст 4 метода генерят нужные таблы
    '''

    def dataframegen(self):
        df = pd.read_csv(self.url, encoding='utf-8')
        df['Кредит'] = df['Кредит'].apply(depozit)
        df['Депозит'] = df['Депозит'].apply(depozit)
        df = df.fillna(0.0)
        df = df.drop(columns=['Банк',])
        df['operation'] = df.loc[:, '1':'19'].apply(
            opern, axis=1).apply(lastoper)
        df = df.drop(columns=[str(i) for i in range(1, 20)])
        df = df.rename(
            columns={'Название команды': 'name',
                     'Unnamed: 2': 'number',
                     'Unnamed: 3': 'key',
                     'Депозит': 'depozit',
                     'Кредит': 'credit',
                     'Unnamed: 4': 'money'})
        df = df.set_index('name')
        return df

    def dataprices(self):
        '''
        Цены всех акций
        index|название акции|цена
        '''
        df = pd.read_csv(self.stockurl[0], encoding='utf-8').drop(
            columns='Акция').T.rename(columns={0: 'price'})
        df['name'] = df.index
        df['new'] = [i for i in range(9)]
        df = df.set_index('new')
        return df.reindex(columns=['name', 'price'])


    def datastocks(self):
        '''
        Инфа о кол-ве акций у каждо команды
        Название команды|количество|айди акции из self.prices
        '''
        print(self.stockurl[1])
        a = pd.read_csv(self.stockurl[1], encoding="utf-8").set_index( # .drop(columns="Номер карточки")
            "Команда").fillna(0).drop(columns=["Баланс на карте","Итого"])
        a=a.loc[a.index.dropna()]
        df_new = pd.DataFrame({"amount": [], "share_id": [], "team_id": []})
        for i in a.index.to_list():
            for j in a.columns.to_list():
                if (a.at[i, j] != 0).any():
                    df_new = df_new.append(
                        {'amount': int(a.at[i, j]),
                         'share_id': j,
                         'team_id': i},
                        ignore_index=True)
        """df_new = df_new.rename(
            columns={'share_id': 'team_id',
                     'team_id': 'share_id'}
        )"""
        df_new.amount = df_new.amount.apply(int)
        return df_new

    def operationteam(self):
        '''
        Таблица операций команды
        Номер счета|операция
        '''
        b = self.datateamtest.filter(
            ['number', 'operation']).set_index('number')
        try:
            b = b.operation.str.split(',', expand=True).drop(columns=[5, 6, 7])
        except:
            b = b.operation.str.split(',', expand=True)
            print('govno')
        new_df = pd.DataFrame({'id': [], 'op': []})
        for i in b.index.to_list():
            for j in range(5):
                new_df = new_df.append(
                    {'id': i, 'op': b.at[i, j].replace(",", ".")}, ignore_index=True)
        new_df.id = new_df.id.apply(int)
        try:
            new_df.op = new_df.op.apply(float)
        except:
            new_df.op = new_df.op.str.strip(""""' """).apply(float)
        new_df = new_df.set_index('id')
        return new_df

    def __init__(self):
        self.id = '1bdNo96H8GZR0_o2GPGCOl3QoOo7Qb4PM6LF7JwI-PDE'  # Айди общей гугл таблицы
        self.name = 'ALL_BANKS'
        self.stockid = '1a6mCq73_wdFhr1g5NmURZrHlnMiX5o3DND4946_F3Sc'  # Айди таблы с акциями
        self.stocknames = ['Prices', 'Stocks']
        self.url = self.url_gen()  # Генерит ссылку на общую таблицу
        self.stockurl = self.stockurl_gen()
        self.datateamtest = self.dataframegen()
        self.datateam = self.datateamtest.drop(columns='operation')
        # Вся инфа о команде, таблица вида
        # Название команды|номер счета|пароль|итог|депозит|кредит|
        # Название команды-индекс таблицы
        # Депозит и кредит представляются в виде 0,1,где
        # 0-отсутствует
        # 1-есть
        self.prices = self.dataprices()
        self.hashprice = hashpricedf(self.prices)
        self.stocks = self.datastocks()  # Кол-во акций команды
        self.operations = self.operationteam()  # Операции команды