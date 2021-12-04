from Manager import UseDataBase
import mysql.connector
from flask import flash
import json


'''Check if the film already exist'''


def filmExist( title: str, data: list, config: dict, show: str = 'show' )->bool:
    try:
        with UseDataBase(config) as cursor:

            # This shows more data to the user
            if show == 'show':
                sql = "select title, imgPath, data-> '$.Released', data-> '$.Genre', data-> '$.Director', data-> '$.Writer', data-> '$.Actors', data-> '$.Awards' from film where title=%s"

                cursor.execute(sql, (title, ) )
                res = cursor.fetchone()

            else:
                sql = "select data-> '$.Year', title, imgPath from film where title=%s"

                cursor.execute(sql, (title, ) )
                res = cursor.fetchone()

        # Whenever this film already exist append all in the arg data and return true
        if res:
            for i in res:
                data.append(i)
            
            return True
        else:
            False

    except mysql.connector.errors.ProgrammingError as err:
        flash('In this moment we are out of service please try later.', category="info")
        print('Error in **filmExist**', err)
        return False


'''Create a new row in the database'''
'''The tuple contains dict, title and img path'''

def AddToDatabase(data: tuple, config: dict)->bool:
    try:
        with UseDataBase(config) as cursor:
            sql = "insert into film(data, title, imgPath) values(%s, %s, %s)"
            cursor.execute(sql, (json.dumps(data[0]), data[1], data[2], ) )
        
        return True
    except mysql.connector.errors.ProgrammingError as err:
        flash('In this moment we are out of service please try later.', category="info")
        print('Error in **AddToDatabase**', err)
        return False