from Connect.ConnPostgresql import crear_conexion # type: ignore


def select_join():
    conn = crear_conexion()
    join_list = []
    if conn is None:
        return join_list
    try:
        cur = conn.cursor()
        cur.execute(
            """SELECT
            cy.id AS cycle_id,
            cy.recorded_at,
            cy.finished,
            cy.parts_per_cycle,
            mc.id,
            mc.pressure,
            mc.grit,
            mc.cycle_duration,
            mc.operator_name,
            mc.created_at,
            po.order_num,
            po.target_quantity,
            po.final_quantity,
            po.start_time,
            pt.id_seq,
            pt.description,
            pt.material,
            pt.sequence,
            pt.weight
            FROM
            cycles AS cy
            INNER JOIN
            machine_config AS mc
            ON cy.config_id= mc.id
            INNER JOIN
            production_orders AS po
            ON cy.order_id = po.order_num
            INNER JOIN
            parts AS pt 
            ON po.part_id= pt.id_seq;
            """
        )
        resultados = cur.fetchall()
        join_list = [t for t in resultados]
        print("successfully.")
    except Exception as ex:
        print(" Error inserting Part:", ex)
    finally:
        cur.close()
        conn.close()
    return join_list