import random
import csv
import os
import time
from datetime import datetime as dt
from Other import validations as val
from Connect import ConnectCSV as csvc
from Connect import ConnPostgresql as cps
from Model import MachineModel as MModel
from Model import PartsModel as PModel
from Model import OrdersModel as OModel
from Model import ConfModel as CModel
from Model import CyclesModel as CYModel

partnuml = []
ordersl = []
pesos = [90, 10]
pesos2 = [90, 5, 5]
pesos3 = [5, 85, 5, 5]
pesos4 = [95, 5]


def main():
    
    
    global List_orders, List_numparts, list_machine, List_cycles, List_conf
    List_orders = csvc.Load_List_orders()
    List_numparts= csvc.Load_List_numparts()
    list_machine= csvc.Load_list_machine()
    List_cycles = csvc.Load_List_cycles()
    List_conf = csvc.Load_List_conf()
    while True:
        Add_Order()
        time.sleep(10.0) 
    #Opciones()
     


    
  
#add order
def Add_Order():
    if not List_orders:
        order_num = 100000
    else:
        order_num = int(List_orders[-1][0]) + 1
    quantityl = ["50","100","200"]
    quantity = random.choice(quantityl)
    partnuml = PModel.select_part()
    part_num = random.choice(partnuml)
    menos = ["1","10","20", "2","5"]
    f_quantity = int(quantity) - int(random.choice(menos))
    started_date = dt.now()
    addvar = [order_num,part_num,quantity,f_quantity,started_date]
    var_val = val.validation(addvar)
    if var_val is True:    
        List_orders.append(addvar)
        add_csv(addvar, 3)
        order = OModel.insert_order(part_num,quantity,f_quantity,started_date)
        Add_cycles(order)
        print("Agregado")
    #Opciones()

#add cycles 
def Add_cycles(order = list):
    conf = conf_machine()
    total_piezas = int(order[2])
    piezas_por_ciclol = [4,3]
    piezas_por_ciclo = random.choices(piezas_por_ciclol, weights=pesos4, k=1)[0]
    ciclos_totales = total_piezas // piezas_por_ciclo
    
    for i in range(ciclos_totales):
        time.sleep(2.0) 
        idcy = next_id(List_cycles)
        recorded_at = dt.now()
        finished = random.choices([True,False], weights=pesos, k=1)[0]
        addvar = [idcy, recorded_at, finished, piezas_por_ciclo, conf[0]]
        List_cycles.append(addvar)
        add_csv(addvar, 5)
        CYModel.insert_cycles(finished, piezas_por_ciclo, conf[0],order[0])

def conf_machine():
    machinel = []
    if not List_conf:
        idc = 1001
    else:
        idc = int(List_conf[-1][0]) + 1
    machinel = MModel.select_machine()
    machine = random.choice(machinel)  
    presure = [40,60]
    presure = random.choice(presure)
    gritl = [40,60]
    grit = random.choice(gritl)
    cycle_duration = 2
    operatorl = ["daniel","luis"]
    operator = random.choice(operatorl)    
    addvar = [idc,machine,presure,grit,cycle_duration,operator]
    var_val = val.validation(addvar)
    if var_val is True:    
        List_conf.append(addvar)
        add_csv(addvar, 4)
        idconf = CModel.insert_conf(machine,presure,grit,cycle_duration,operator)
        print(f"Este es el valor de idcong{idconf}")
        addvar = [idconf,machine,presure,grit,cycle_duration,operator]
        print("Agregado")  
        return addvar 

def Salirt():
    exit()
    

def add_csv(lista: list, case):
    
    if case == 1:
        filepath = "example.csv"
    elif case == 2:
        filepath = "example2.csv"
    elif case == 3:
        filepath = "example3.csv"
    elif case == 4:
        filepath = "example4.csv"
    elif case == 5:
        filepath = "example5.csv"
        
    else:
        return print("No List")
    file_exists = os.path.exists(filepath)
    try:
        with open(filepath, mode='a', newline='', encoding='utf-8') as file: 
            writer = csv.writer(file)
            writer.writerow(lista)
    except:    
        print("error to add the new line")
        
def next_id(list_data, start=1001):
    return start if not list_data else int(list_data[-1][0]) + 1

if __name__ == "__main__":
    main()