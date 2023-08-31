##############################
##### 데이터 베이스 코드  #####
##############################

import sys
import pymysql

#데이터 베이스 연결
def dbconnect(case):
    try:
        conn = pymysql.connect(
            host="192.168.1.125",
            user="ras",
            password="1234",
            database= case
        )

    except pymysql.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)
    return conn

#모든 데이터 출력
def search_data(conn, table , list , name):
    cur = conn.cursor()
    # sql = 'SELECT '+list+' FROM ' + name
    #list = price
    #table = snack
    #name = 포카칩
    sql = f'SELECT {list} FROM {table} WHERE name = "{name}"'

    cur.execute(sql)
    results = cur.fetchall()
    return results

def find_Check_Dialog(conn,table):
    cur = conn.cursor()
    sql = "SELECT name,price,location FROM " + table
    cur.execute(sql)
    results = cur.fetchall()
    #튜플을 리스트로 변환하여 int형을 str형으로 변환 후 다시 튜플 형태로 복귀
    str_results = []
    for row in results:
        formatted_row = tuple(str(item) for item in row)
        str_results.append(formatted_row)
    str_results_tuple = tuple(str_results)
    return str_results_tuple

