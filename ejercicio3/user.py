import mysql.connector
from repository import Users
from flask import Flask

# esto va en otro archivo
def connection_database(host, user, password, database, port):
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database,
        port=int(port),
    )

    return connection


def execute_query_with_commit(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    cursor.close()


def execute_query(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    return result

def connection_close(connection):
    connection.close()
# fin esto va en otro archivo


@app.route('//create/user/1/Juan/67', methods=['GET'], endpoint='insert_user')
def insert_user(user_id, user_name, user_edad):
    query = "INSERT INTO usuarios (id, nombre, edad) VALUES (%s, '%s', %s);" % (user_id, user_name, user_edad)
    connection = connection_database()
    try:
        execute_query_with_commit(connection, query)
    except Exception as e:
        return print('No se ha podido insertar el usuario'), 500
    connection.close()
    return print('Se ha insertado el usuario'), 200


if __name__ == '__main__':
    connection = connection_database('localhost', 'root', 'root', 'usuarios', '3307')
    type_instruction = input('Ingrese el tipo de instruccion: ')
    connection.close()