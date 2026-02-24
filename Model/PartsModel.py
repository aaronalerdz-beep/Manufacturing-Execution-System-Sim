from Connect.ConnPostgresql import crear_conexion # type: ignore

def insert_part(sequence,description,material,weight):
    conn = crear_conexion()
    if conn is None:
        return
    try:
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO parts (description,material,sequence,weight) VALUES (%s, %s,%s, %s)",
            (description,material,sequence,weight)
        )
        resultado = cur.fetchone()
        if resultado:
            nuevo_id = resultado[0]
        conn.commit()
        print(" Part added successfully.")
    except Exception as ex:
        print(" Error inserting Part:", ex)
    finally:
        cur.close()
        conn.close()
    return nuevo_id

def select_part():
    conn = crear_conexion()
    ids_list = []
    if conn is None:
        return ids_list
    try:
        cur = conn.cursor()
        cur.execute(
            "Select id_seq From parts",
        )
        resultados = cur.fetchall()
        ids_list = [t[0] for t in resultados]
        conn.commit()
        print(" successfully.")
    except Exception as ex:
        print(" Error inserting Part:", ex)
    finally:
        cur.close()
        conn.close()
    return ids_list