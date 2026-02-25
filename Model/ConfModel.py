from Connect.ConnPostgresql import crear_conexion # type: ignore

def insert_conf(machine,presure,grit,cycle_duration, operator):
    conn = crear_conexion()
    nuevo_id = None
    if conn is None:
        return
    try:
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO machine_config (machine_id,pressure,grit,cycle_duration,operator_name) VALUES (%s, %s,%s, %s, %s) RETURNING id",
            (machine,presure,grit,cycle_duration,operator)
        )
        resultado = cur.fetchone()
        if resultado:
            nuevo_id = resultado[0]
        conn.commit()
        print(f"Conf added successfully.-{nuevo_id}")
    except Exception as ex:
        print(" Error inserting Conf:", ex)
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
            "Select id From machine_config",
        )
        resultados = cur.fetchall()
        ids_list = [t[0] for t in resultados]
        conn.commit()
        print("successfully.")
    except Exception as ex:
        print(" Error inserting Part:", ex)
    finally:
        cur.close()
        conn.close()
    return ids_list