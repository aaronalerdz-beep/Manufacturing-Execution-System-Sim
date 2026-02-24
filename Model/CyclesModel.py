from Connect.ConnPostgresql import crear_conexion # type: ignore

def insert_cycles(finished, piezas_por_ciclo, conf,idorder):
    conn = crear_conexion()

    if conn is None:
        return
    try:
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO cycles (finished,parts_per_cycle,config_id,order_id) VALUES (%s, %s,%s,%s)",
            (finished,piezas_por_ciclo,conf,idorder)
        )
        conn.commit()
        print(" Cycle added successfully.-------------------------------------------------")
    except Exception as ex:
        print(" Error inserting Cycle:", ex)
    finally:
        cur.close()
        conn.close()

