import csv 
from sewa import Sewa 

FILE_NAME = "sewa_data.csv" 

def load_data():
    sewa_list = []
    try:
        with open(FILE_NAME, mode='r', newline='') as file: 
            reader = csv.reader(file) 
            for row in reader:
                sewa = Sewa.from_list(row)
                sewa_list.append(sewa)
    except FileNotFoundError:
        open(FILE_NAME, mode='w').close()  
    return sewa_list

def save_data(sewa_list):
    with open(FILE_NAME, mode='w', newline='') as file: 
        writer = csv.writer(file)
        for sewa in sewa_list:
            writer.writerow(sewa.to_list())