Logs Analysis Project

This Project is internal reporting tool that will use information from
the database to discover what kind of articles the site's readers
like.The database contains newspaper articles, as well as the web server
log for the site. The log has a database row for each time a reader
loaded a web page. Using that information, This reporting tool will
answer questions about the site's user activity.

Prerequisites

1.  The VirtualBox VM environment

2.  The Vagrant configuration program

3.  Any linux based command line tool (for windows: git bash)

4.  python 3.x downloaded and installed

Getting Started

1.  Open Terminal

2.  Change default directory to project folder's directory.

3.  Now type vagrant up && vagrant ssh.

4.  After This type cd /vagrant

5.  After this type psql -d news -f newsdata.sql

6.  type psql -d news

7.  Now you are connected to psql

8.  vagrantfile and newsdata.sql is in project folder .

9.  querry to fetch the result of first problem- "select articles.title,
    count(articles.title)as num from articles, log where log.path =
    concat('/article/', articles.slug) group by articles. title order by
    num desc limit 3".

10. querry to fetch the result of second problem- " select authors.name,
    count(articles.author) as num from articles , authors, log where
    authors.id = articles.author and log.path = concat ('/article/',
    articles.slug) group by authors.name order by num desc;"

11. querry to fetch the result of third problem- "select
    d1,(prblm::decimal \* 100)/total::decimal as\
     perc from (select time::timestamp::date as d1,count(status)as
    total,sum (case when status like '404%' then 1 else 0 end)as prblm
    from log group by time::timestamp::date)as rslt where
    (prblm::decimal\*100)/total:: decimal\>1.0 order by perc desc;"

12. now type CTRL+D
13. After This type cd /vagrant
14. Now type python3 db_py.py and press as directed in code to view the
    result.

Note: For more information about running python in terminal/cmd [Click
Here](https://en.wikibooks.org/wiki/Python_Programming/Creating_Python_Programs "How to run application using cmd/terminal").

Built With

1.  Language Used

-   Python3

