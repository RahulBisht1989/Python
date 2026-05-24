import os
base_dir= r"D:\Python\IDP_Python\file_handling\output_txtfiles"
os.makedirs(base_dir,exist_ok=True)
file_path= os.path.join(base_dir,"dataset.txt")

invoice_data="""INV_001,Acme Corp,1500,SUCCESS,95
INV_002,Beta Ltd,2000,FAILED,40
INV_003,Gamma Inc,750,SUCCESS,85
INV_004,Delta Co,1200,FAILED,60
INV_005,Echo Ltd,900,SUCCESS,72"""

if __name__=="__main__":
    if not os.path.exists(file_path):
            with open(file_path, "w") as file:
                file.write(invoice_data)
                print("file created ✅")
    else:
            print("file already exist ✅")

    





