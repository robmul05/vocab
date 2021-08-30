import psycopg2 as pg

conn = pg.connect(host='localhost',dbname='vocab', user='robert', password='sqltime')
cur = conn.cursor()

# def vocab(wrd, df):
#     key = wrd
#     value = df
#     wrd_dfn = dict(zip(key,value))
#     return wrd_dfn

while True:
    wrd = input('Give me word')
    if wrd == 'STOP':
        break
    dfn = input('Give me def')
    pos = input('Give me POS')
    cur.execute("INSERT INTO wl (word,def,pos) VALUES (%s,%s,%s);", (wrd, dfn, pos))

conn.commit()

conn.close()