import random
import csv
import os
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
pesos = [99, .1]
pesos2 = [90, 5, 5]
pesos3 = [85, 5,  5, 5]
pesos4 = [95, 5]


def main():

    conn = cps.crear_conexion()
    global List_orders, List_numparts, list_machine, List_cycles, List_conf
    List_orders = csvc.Load_List_orders()
    List_numparts= csvc.Load_List_numparts()
    list_machine= csvc.Load_list_machine()
    List_cycles = csvc.Load_List_cycles()
    List_conf = csvc.Load_List_conf()
    Opciones()
     
def Opciones():
    print("\nOptions:")
    print("1. Add Machine")
    print("2. Add Part Number")
    print("3. Add Production Order")
    print("4. Salir")
    option = input("Elije:")

    match option:
        case "1":
            Add_machine()
        case "2":
            Add_Partnum()
        case "3":
            Add_Order()
        case "4":
            Salirt()
        case _:
            print("NO valido")
            Opciones()

#add Machine
def Add_machine():
    if not list_machine:
        idm = 1001
    else:
        idm = int(list_machine[-1][0]) + 1
    name_machine = input("Name Machine: ")
    area = input("Name Area: ")
    addvar = [idm,name_machine,area]
    var_val = val.validation(addvar)
    if var_val is True:    
        list_machine.append(addvar)
        add_csv(addvar, 1)
        MModel.insert_machine(addvar[1], addvar[2])
        print("Agregado")
    Opciones()
    
#add Part Number
def Add_Partnum():
    if not List_numparts:
        part_num = 100000
    else:
        part_num = int(List_numparts[-1][0]) + 1
    materialL = ["Platic","2xxx" ,"6xxx","7xxx"]
    material = random.choice(materialL)
    descriptionl = ["Regular produccion","FAI","Rework","Part of Service"]
    description = random.choices(descriptionl, weights=pesos3, k=1)[0]
    sequencel = ["1.Clean-2.Sandblast-3.TopCoat","1.Clean-2.Sandblast","1.Sandblast-2.TopCoat"]
    sequence = random.choices(sequencel, weights=pesos2, k=1)[0]
    weightl = [5,1,0.1]
    weight = random.choice(weightl)
    addvar = [part_num,description,sequence,material,weight]
    var_val = val.validation(addvar)
    if var_val is True:    
        List_numparts.append(addvar)
        add_csv(addvar, 2)
        PModel.insert_part(sequence,description,material,weight)
        print("Agregado")
    Opciones()

  
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
    Add_cycles(addvar)
    var_val = val.validation(addvar)
    if var_val is True:    
        List_orders.append(addvar)
        add_csv(addvar, 3)
        OModel.insert_order(part_num,quantity,f_quantity,started_date)
        print("Agregado")
    Opciones()

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

#add cycles 
def Add_cycles(addvar = list):
    conf = conf_machine()
    total_piezas = int(addvar[2])
    piezas_por_ciclol = [4,3]
    piezas_por_ciclo = random.choices(piezas_por_ciclol, weights=pesos4, k=1)[0]
    ciclos_totales = total_piezas // piezas_por_ciclo
    
    for i in range(ciclos_totales):
        idcy = next_id(List_cycles)
        recorded_at = dt.now()
        finished = random.choices([True,False], weights=pesos, k=1)[0]
        addvar = [idcy, recorded_at, finished, piezas_por_ciclo, conf[0]]
        List_cycles.append(addvar)
        add_csv(addvar, 5)
        CYModel.insert_cycles(finished, piezas_por_ciclo, conf[0])

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