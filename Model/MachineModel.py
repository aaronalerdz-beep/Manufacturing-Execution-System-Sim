from Connect.ConnPostgresql import crear_conexion # type: ignore

def insert_machine(name, area):
    conn = crear_conexion()
    if conn is None:
        return
    try:
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO machines (name_machine, area) VALUES (%s, %s)",
            (name, area)
        )
        conn.commit()
        print(" Machine added successfully.")
    except Exception as ex:
        print(" Error inserting machine:", ex)
    finally:
        cur.close()
        conn.close()
        
def select_machine():
    conn = crear_conexion()
    ids_list = []
    if conn is None:
        return ids_list
    try:
        cur = conn.cursor()
        cur.execute(
            "Select idm From machines",
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
