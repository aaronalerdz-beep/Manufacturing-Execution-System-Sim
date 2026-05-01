import requests
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

# La IP que configuramos antes para que sea accesible
endpoint = "/MachineConf"
baseUrl = "https://localhost:5010/api/v1"


def PostConfigMachine(id_machine,pressure,grit,cycle_duration, operator):
    url = f"{baseUrl}/machineConf"
    
    payload = {
        "machineIdSeq": id_machine,
        "pressure": pressure,
        "grit": grit,
        "cycle_duration": cycle_duration,
        "operator_name": operator
    }
    print(payload)
    try:
        response = requests.post(url, json=payload, verify=False)
        if response.status_code == 201:
            return response.json()
        else:
            print(f"Error al crear config: {response.text}")
            return None
    except Exception as e:
        print(f"Error de conexión: {e}")
        return None


def PostCycles(finished, piezas_por_ciclo, conf,order):
    url = f"{baseUrl}/newCycle"
    
    payload = {
        "parts_per_cycle": piezas_por_ciclo,
        "finished": finished,
        "machineConfigId": conf,
        "productionOrderId": order
    }
    try:
        response = requests.post(url, json=payload, verify=False)
        if response.status_code == 201:
            return response.json()
        else:
            print(f"Error al crear cycle: {response.text} Cycle")
            return None
    except Exception as e:
        print(f"Error de conexión: {e} Cycle")
        return None
    