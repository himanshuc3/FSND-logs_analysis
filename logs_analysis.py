#!/usr/bin/env python3
#
# logs_analysis.py - assignment for logs_analysis module
#
import psycopg2


if __name__ == '__main__':

    try:
        conn = psycopg2.connect("dbname=news")
        cur = conn.cursor()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    cur.execute(
        '''
            SELECT articles.title, count(*) as views
            FROM articles, log
            WHERE concat('/article/', articles.slug) = log.path
            and log.status = '200 OK'
            GROUP BY articles.title
            ORDER BY views DESC
            LIMIT 3;
        '''
    )
    pop_art = cur.fetchall()
    print("1. Most popular 3 articles of all time:")
    for tup in pop_art:
        print(tup[0] + "-", end=" ")
        print(tup[1])

    cur.execute(
        '''
            SELECT authors.name, result.views
            from authors,
            (SELECT articles.author, count(*) as views
            FROM articles, log
            WHERE concat('/article/', articles.slug) = log.path
            and log.status = '200 OK'
            GROUP BY articles.author
            ORDER BY views DESC) as result
            where authors.id = result.author;
        '''
    )
    pop_auth = cur.fetchall()
    print("================================================")
    print("1. Most popular article authors of all time:")
    for tup in pop_auth:
        print(tup[0] + "-", end=" ")
        print(tup[1])

    cur.execute(
        '''
            SELECT total.day, bad.requests as bad_requests,
            total.requests as total,
            bad.requests*100.0/total.requests as percent
            from
            (SELECT count(*) as requests, date_trunc('day', time) "day"
            from log
            group by day) as total,
            (SELECT count(*) as requests, date_trunc('day', time) "day"
            from log
            where status='404 NOT FOUND'
            group by day) as bad
            where total.day = bad.day
            and bad.requests > total.requests/100;
        '''
    )
    err = cur.fetchall()
    print("================================================")
    print("1. Days when error percentage was more than 1%:")
    for tup in err:
        print(tup[0].strftime('%B %d, %Y'), end=" ")
        print(tup[3])
