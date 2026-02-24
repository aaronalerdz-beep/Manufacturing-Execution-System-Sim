import csv
import os
from datetime import datetime as dt

lista = []
List_orders = []
List_numparts = []
list_machine = []
List_cycles = []
List_conf = []
ordersl = []
partnuml = []
pesos = [90, 10]
pesos2 = [90, 5, 5]


def Load_list_machine():
    try:
        filepath = "example.csv"
        file_exists = os.path.exists(filepath)
        with open(filepath, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                list_machine.append(row)
        return list_machine
    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
        return []
    
def Load_List_numparts():
    try:
        filepath = "example2.csv"
        with open(filepath, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                List_numparts.append(row)
        return List_numparts
    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
        return []
    
def Load_List_orders():
    try:
        filepath = "example3.csv"
        with open(filepath, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                List_orders.append(row)
        return List_orders
    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
        return []
    
def Load_List_cycles():
    try:
        filepath = "example4.csv"
        with open(filepath, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                List_cycles.append(row)
        return List_cycles
    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
        return []
    
def Load_List_conf():
    try:
        filepath = "example5.csv"
        with open(filepath, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                List_conf.append(row)
        return List_conf
    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
        return []
    
    
