# -*- coding: cp936 -*-
import sys
import os
import sqlite3
from bs4 import BeautifulSoup


os.chdir(os.path.dirname(sys.argv[0]))

import download

stdi,stdo,stde = sys.stdin,sys.stdout,sys.stderr

reload(sys)
sys.setdefaultencoding('utf8')
sys.stdin,sys.stdout,sys.stderr = stdi,stdo,stde
'''
url_0 ='https://list.jd.com/list.html?cat=12218,12221&page=1&sort=sort_rank_asc&trans=1&JL=6_0_0#J_main'
url_1 ='https://list.jd.com/list.html?cat=12218,12221&page=2&sort=sort_rank_asc&trans=1&JL=6_0_0#J_main'
url_2 ='https://list.jd.com/list.html?cat=12218,12221&page=3&sort=sort_rank_asc&trans=1&JL=6_0_0#J_main'
'''
#京东地址
url = 'https://list.jd.com/list.html?cat=12218,12221&page='

fruit_price = []
fruit_name = []
'''
html = download.download(''.join((url,repr(1),'&sort=sort_rank_asc&trans=1&JL=6_0_0#J_main')))
fruit_soup = BeautifulSoup(html,'html.parser')
res =  fruit_soup.findAll('em')

if i:
    fruit_name.append(i)
'''
 

for i in range(10):
    html = download.download(''.join((url,repr(i),'&sort=sort_rank_asc&trans=1&JL=6_0_0#J_main')))
    fruit_soup = BeautifulSoup(html,'html.parser')
    res = fruit_soup.findAll('em')
    print type(res)
    for i in res:
        if i.string:
            if len(i.string.strip())>10:
                fruit_name.append(i.string.strip())


fin_res = enumerate(fruit_name)
                

        
connect_sql = sqlite3.connect('example.db')
c = connect_sql.cursor()

del_table = "DROP TABLE fruits"
create_table = "CREATE TABLE fruits(id text,name text)"


for i in fruit_name:
    print i



print "length: ",len(fruit_name)


try:
    c.execute(create_table)
    print "创建表"
except:
    c.execute(del_table)
    print "删除已存在表,并重新创建"
    c.execute(create_table)

#写入数据

    c.executemany("insert into fruits(id,name) values (?,?)",fin_res)

connect_sql.commit()
connect_sql.close()




