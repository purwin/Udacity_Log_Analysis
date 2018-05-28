# -*- coding: utf-8 -*-

import psycopg2
from datetime import datetime

# Your task is to create a reporting tool that prints out reports (in plain text) based on the data in the database.

# 1. What are the most popular three articles of all time?
# "Princess Shellfish Marries Prince Handsome" — 1201 views
def pop_articles():
	db = psycopg2.connect("dbname=news")
	c = db.cursor()
	c.execute('''
	  select title, group_articles.c
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
	print results

# 2. Who are the most popular article authors of all time?
# Ursula La Multa — 2304 views
def pop_authors():
  pass

# 3. On which days did more than 1% of requests lead to errors?
# July 29, 2016 — 2.5% errors
def pop_days():
  pass