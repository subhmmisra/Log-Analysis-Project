import psycopg2


def connect_db():
    """Connect to the PostgreSQL database and returns a database connection."""
    db = psycopg2.connect("dbname=news")
    cur = db.cursor()
    return db, cur


def fetch_result1():
    db, cur = connect_db()
    query = "select articles.title, count(articles.title)as num from articles, \
    log where log.path = concat('/article/', articles.slug) group by articles.\
    title order by num desc limit 3;"
    cur.execute(query)
    result = cur.fetchall()
    db.close()
    print ("\nPopular Articles:\n")
    for i in range(0, len(result), 1):
        print ("\"" + result[i][0] + "\" - " + str(result[i][1]) + " views\n")
        print("------------------------------------------------------------")


def fetch_result2():

    db, cur = connect_db()
    query = " select authors.name, count(articles.author) as num from articles\
    , authors, log where authors.id = articles.author and log.path = concat\
    ('/article/', articles.slug) group by authors.name order by num desc;"
    cur.execute(query)
    result = cur.fetchall()
    db.close()
    print ("\nPopular Authors:\n")
    for i in range(0, len(result), 1):
        print ("\"" + result[i][0] + "\" - " + str(result[i][1]) + " views\n")
        print("------------------------------------------------------------")


def fetch_result3():
    db, cur = connect_db()
    query = "select d1,(prblm::decimal * 100)/total::decimal as\
    perc from (select time::timestamp::date as d1,count(status)as total,sum\
    (case when status like '404%' then 1 else 0 end)as prblm from log group \
    by time::timestamp::date)as rslt where (prblm::decimal*100)/total::\
    decimal>1.0 order by perc desc;"
    cur.execute(query)
    result = cur.fetchall()
    db.close()
    print ("\nDays with more than 1% of errors:\n")
    for i in range(0, len(result), 1):
        print (str(result[i][0]) + " - "+str(result[i][1])+" % errors found\n")
        print("------------------------------------------------------------")

if __name__ == '__main__':
    while True:
        print("choose among the following:")
        a1 = input("1. Popular authors\n2.Popular articles\n3.Error date\n")
        if a1 == '1':
            fetch_result1()
        elif a1 == '2':
            fetch_result2()
        elif a1 == '3':
            fetch_result3()
        else:
            break
