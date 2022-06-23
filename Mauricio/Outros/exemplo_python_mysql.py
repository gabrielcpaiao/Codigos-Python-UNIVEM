import mysql.connector
from mysql.connector import Error

try:
    con = mysql.connector.connect(host='localhost',database='Solução Ex 06',user='root',password='')

    consulta_sql = "select * from my_table"
    cursor = con.cursor()
    cursor.execute(consulta_sql)
    linhas = cursor.fetchall()
    print("N�mero total de registros retornados: ", cursor.rowcount)

    print("\nExibindo os regsitros cadastrados")
    for linha in linhas:
        print("campo1:", linha[0])
        print("campo2:", linha[1])
        print("campo3:", linha[2], "\n")
except Error as e:
    print("Erro ao acessar tabela MySQL", e)
finally:
    if (con.is_connected()):
        con.close()
        cursor.close()
        print("Conex�o ao MySQL encerrada")