# -*- coding: utf-8 -*-

import psycopg2
import datetime

# 1. Query the three most popular articles of all time.
def pop_articles():
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    c.execute('''select title, group_articles.c
    from articles
    join (select path, count(*) as c
    from log
    where path != '/'
    group by log.path) as group_articles
    on group_articles.path = concat('/article/', articles.slug)
    order by group_articles.c desc
    limit 3;
    ''')
    results = c.fetchall()
    db.close()
    print "1. What are the most popular three articles of all time?"
    for x, y in results:
        print "\"{}\" — {:,} views".format(x, int(y))

# 2. Query the most popular article authors of all time.
def pop_authors():
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    c.execute('''select authors.name, group_authors.c
    from authors
    join (select articles.author, count(*) as c
    from articles
    join log
    on log.path = concat('/article/', articles.slug)
    group by articles.author
    order by c desc) group_authors
    on authors.id = group_authors.author;
    ''')
    results = c.fetchall()
    db.close()
    print "\n\n2. Who are the most popular article authors of all time?"
    for x, y in results:
        print "{} — {:,} views".format(x, int(y))

# 3. Query the days when more than 1% of requests lead to errors.
def pop_days():
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    c.execute('''select *
    from (
    select time::date as ymd, err.err_count * 100.0 / count(*) as percentage
    from log
    join (select time::date as err_ymd, count(*) as err_count
    from log
    where status != '200 OK'
    group by err_ymd) as err
    on time::date = err.err_ymd
    group by ymd, err.err_count
    order by percentage desc) as table_err_percent
    where table_err_percent.percentage > 1;
    ''')
    results = c.fetchall()
    db.close()
    print "\n\n3. On which days did more than 1% of requests lead to errors?"
    for x, y in results:
        print "{} — {}% errors".format(x.strftime('%B %d, %Y'), round(y, 2))

if __name__ == '__main__':
    pop_articles()
    pop_authors()
    pop_days()
