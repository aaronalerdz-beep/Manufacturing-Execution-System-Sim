from Connect.ConnPostgresql import crear_conexion # type: ignore

def insert_order(part_num,quantity,f_quantity,started_date):
    conn = crear_conexion()
    nuevo_id = None
    if conn is None:
        return
    try:
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO production_orders (part_id,target_quantity,final_quantity,start_time) VALUES (%s, %s,%s, %s) RETURNING *",
            (part_num,quantity,f_quantity,started_date)
        )
        
        resultado = cur.fetchone()
        if resultado:
            nuevo_id = resultado
        conn.commit()
        print(" Order added successfully.")
    except Exception as ex:
        print(" Error inserting Order:", ex)
    finally:
        cur.close()
        conn.close()
    return nuevo_id
