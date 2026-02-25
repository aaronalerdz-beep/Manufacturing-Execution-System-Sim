import random
import csv
import os
import time
from datetime import datetime as dt
from Other import validations as val
from Connect import ConnectApi as capi
from Model import CyclesModel as CYModel

partnuml = []
ordersl = []
pesos = [90, 10]
pesos2 = [90, 5, 5]
pesos3 = [5, 85, 5, 5]
pesos4 = [95, 5]


def main():
    list_orders = capi.GetCreatedOrders()
    print(list_orders)
    conf = conf_machine()
    for order in list_orders:
        Add_cycles(order,conf['idSeq'])
        capi.FinishOrder(order['idSeq'])


     
#add cycles 
def Add_cycles(order,conf):
    total_piezas = order['quantity'] 
    piezas_por_ciclo = 4
    ciclos_totales = total_piezas // piezas_por_ciclo

    for i in range(ciclos_totales):
        piezas_por_ciclol = [4, 3]
        is_finished = random.choices(piezas_por_ciclol, weights=pesos4, k=1)[0]
        capi.PostCycles(is_finished, piezas_por_ciclo, conf,order['idSeq'])

def conf_machine():
    machinel = []
    machinel = capi.GetMachin()
    machine = random.choice(machinel)  
    id_machine = machine["idSeq"]
    pressurel = [40,60]
    pressure = random.choice(pressurel)
    gritl = [40,60]
    grit = random.choice(gritl)
    cycle_duration = 2
    operatorl = ["daniel","luis"]
    operator = random.choice(operatorl)    
    addvar = [id_machine,pressure,grit,cycle_duration,operator]
    var_val = val.validation(addvar)
    if var_val is True:    
        idconf = capi.PostConfigMachine(id_machine,pressure,grit,cycle_duration,operator)
        print(f"Este es el valor de idcong{idconf}")
        addvar = [idconf,id_machine,pressure,grit,cycle_duration,operator]
        print("Agregado")  
        return idconf 
    

def Salirt():
    exit()

if __name__ == "__main__":
    main()