"""
1. Save each invoice as individual JSON file
   named as INV_001_extracted.json, INV_002_extracted.json etc.
2. Read each saved file back
3. Print vendor and amount from each file
"""
import json
from pathlib import Path
basedir = Path(__file__).resolve().parent/"exported_json"
basedir.mkdir(parents=True , exist_ok= True)

def generate_invoice_json(inv):
    filename = f"{inv['invoice_id']}_extracted.json"
    try:
        filepath = basedir/filename
        
        with open(filepath ,"w") as file:
            json.dump(inv,file, indent=4)
        print(f"Saved: {filename} ✅")
    except IOError as e:
        raise IOError(f"[ERROR] Could not save json {e}")
    return filepath

def process_invoices(invoices):
    filepath = []
    for inv in invoices:
        filepath.append(generate_invoice_json(inv))
    read_json_file(filepath)
    

def read_json_file(filepath):
    print("\nReading saved files:")
    for file in filepath:
        try:
            with open(file, "r") as f:
                filename = file.name
                invoice = json.load(f)
                print(
                    f"{filename} → Vendor: {invoice['vendor']:<10} | Amount: ${invoice['amount']}"
                )
        except FileNotFoundError as e:
            raise FileNotFoundError(f"[ERROR] Could not found : {invoice['invoice_id']}_extracted.json")
        except json.JSONDecodeError as e:
            raise ValueError(f"[ERROR] invalid json format {e}")

invoices = [
    {"invoice_id": "INV_001", "vendor": "Acme Corp", "amount": 1500.0, "status": "SUCCESS", "confidence": 95},
    {"invoice_id": "INV_002", "vendor": "Beta Ltd",  "amount": 2000.0, "status": "FAILED",  "confidence": 40},
    {"invoice_id": "INV_003", "vendor": "Gamma Inc", "amount": 750.0,  "status": "SUCCESS", "confidence": 85},
]

if __name__=="__main__":
    process_invoices(invoices)