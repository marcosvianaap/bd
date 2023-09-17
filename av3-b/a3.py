import pymysql


# Conectar ao banco de dados Sakila
conn = pymysql.connect(
    host="localhost",
    user="bd2",
    password="root",
    database="sakila"
)

# Preparar e executar a consulta SQL de agregação
cursor = conn.cursor()

sqlb = """

    SELECT c.name AS categoria, AVG(f.length) AS media_duracao
    FROM film f
    INNER JOIN film_category fc ON f.film_id = fc.film_id
    INNER JOIN category c ON fc.category_id = c.category_id
    GROUP BY c.name
"""

cursor.execute(sqlb)

# Iterar pelos resultados e imprimir a média de duração por categoria
print("Média de Duração por Categoria:")
for (categoria, media_duracao) in cursor:
    print(f"{categoria}: {media_duracao} minutos")

# Fechar conexões
cursor.close()
conn.close()
