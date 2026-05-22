import os

invoices = """INV_001,Acme Corp,1500,SUCCESS,95
INV_002,Beta Ltd,2000,FAILED,40
INV_003,Gamma Inc,750,SUCCESS,85
INV_004,Delta Co,1200,FAILED,60
INV_005,Echo Ltd,900,SUCCESS,72"""

BASE_DIR = r"C:\Users\49206071\Python\IDP_Python"
FILE_DIR = os.path.join(BASE_DIR,"Samplefiles")
FILE_NAME = "invoices.txt"

os.makedirs(FILE_DIR, exist_ok=True)

Full_file_path = os.path.join(FILE_DIR,FILE_NAME)
if __name__=="__main__":
    if not os.path.exists(Full_file_path):
        with open(Full_file_path, "w") as file:
            file.write(invoices)
            print("file created ✅")
    else:
        print("file already exist ✅")



