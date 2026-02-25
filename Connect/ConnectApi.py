import requests
import os
from dotenv import load_dotenv

load_dotenv()

# La IP que configuramos antes para que sea accesible
endpoint = "/order/status/created"
baseUrl = "http://localhost:5224/api"


def GetCreatedOrders():
    try:
        response = requests.get(baseUrl+endpoint)
        
        if response.status_code == 200:
            orders = response.json()
            return orders
        else:
            print(f"Error {response.status_code}")
            
    except Exception as e:
        print(f"Exception: {e}")

def GetMachin():
    try:
        response = requests.get(baseUrl+'/machine')
        
        if response.status_code == 200:
            machines = response.json()
            return machines['data']
        else:
            print(f"Error {response.status_code}")
            
    except Exception as e:
        print(f"Exception: {e}")

def PostConfigMachine(id_machine,pressure,grit,cycle_duration, operator):
    url = f"{baseUrl}/config"
    
    payload = {
        "machinesIdSeq": id_machine,
        "pressure": pressure,
        "grit": grit,
        "cycle_duration": cycle_duration,
        "operator_name": operator
    }
    try:
        response = requests.post(url, json=payload)
        if response.status_code == 201:
            return response.json()
        else:
            print(f"Error al crear config: {response.text}")
            return None
    except Exception as e:
        print(f"Error de conexión: {e}")
        return None


def PostCycles(finished, piezas_por_ciclo, conf,order):
    url = f"{baseUrl}/cycle"
    
    payload = {
        "parts_per_cycle": piezas_por_ciclo,
        "finished": finished,
        "machineConfIdSeq": conf,
        "productionOrderIdSeq": order
    }
    try:
        response = requests.post(url, json=payload)
        if response.status_code == 201:
            return response.json()
        else:
            print(f"Error al crear config: {response.text}")
            return None
    except Exception as e:
        print(f"Error de conexión: {e}")
        return None
    
def FinishOrder(id):
    url = f"{baseUrl}/order/{id}/status"
    payload = {
        "status": "Finished"
    }
    try:
        response = requests.put(url, json=payload)
        if response.status_code == 200:
            print(f"Order {id} is Finished")
            return response.json()
        else:
            print(f"Error al crear config: {response.text}")
            return None
    except Exception as e:
        print(f"Error de conexión: {e}")
        return None