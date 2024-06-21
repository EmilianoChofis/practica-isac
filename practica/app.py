import os
import pymysql
import json


def lambda_handler(event, context):
    try:
        # Parámetros de conexión a la base de datos
        DB_HOST = os.environ['DB_HOST']
        DB_USER = os.environ['DB_USER']
        DB_PASSWORD = os.environ['DB_PASSWORD']
        DB_NAME = os.environ['DB_NAME']

        # Conexión a la base de datos
        connection = pymysql.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )

        try:
            with connection.cursor() as cursor:
                # Ejecutar una consulta
                sql = "SELECT NOW() as current_time;"
                cursor.execute(sql)
                result = cursor.fetchone()
                print("Query result:", result)

            return {
                'statusCode': 200,
                'body': json.dumps({
                    'message': 'Consulta ejecutada exitosamente',
                    'current_time': result['current_time'].strftime('%Y-%m-%d %H:%M:%S')
                })
            }

        except Exception as e:
            print("Error executing query:", str(e))
            return {
                'statusCode': 500,
                'body': json.dumps({
                    'message': 'Error ejecutando la consulta',
                    'error': str(e)
                })
            }

        finally:
            connection.close()
            print("Connection closed")

    except Exception as e:
        print("Error connecting to the database:", str(e))
        return {
            'statusCode': 500,
            'body': json.dumps({
                'message': 'Error conectando a la base de datos',
                'error': str(e)
            })
        }