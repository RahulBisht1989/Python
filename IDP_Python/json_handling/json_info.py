"""json.dumps() — Python Dict to JSON String"""
# import json
# invoice = {
#     "invoice_id" : "INV_001",
#     "vendor"     : "Acme Corp",
#     "amount"     : 1500.0,
#     "status"     : "SUCCESS"
# }

# json_string =json.dumps(invoice, indent= 4)

# print(json_string)

"""json.loads() — JSON String to Python Dict"""
# import json
# json_string = '{"invoice_id": "INV_001", "vendor": "Acme Corp", "amount": 1500.0}'

# invoice = json.loads(json_string)

# print(f"{invoice['invoice_id']} : {invoice['amount']}")

"""
json.dump() — Python Dict to JSON File
json.load() — JSON File to Python Dict
dumps / loads   → work with STRINGS   (s = string)
dump  / load    → work with FILES
"""

"""Real IDP Example — Complete JSON Pipeline"""
#Step 1 — Extract Invoice Data and Save as JSON
import os, json
from pathlib import Path

# def save_invoice_json(invoice, output_dir):
#     """
#     Saves extracted invoice data as individual JSON file.
#     One JSON file per invoice.
#     """
#     filename = f'{invoice["invoice_id"]}_extracted.json'
#     filepath = os.path.join(output_dir,filename)
#     try:
#         with open(filepath, "w") as file:
#             json.dump(invoice, file, indent=4)

#         print(f"[SUCCESS] Saved: {filename}")

#         return filepath
#     except IOError as e:
#         raise IOError(f"[ERROR] Could not save JSON: {e}")

# invoice = {
#     "invoice_id"  : "INV_001",
#     "vendor"      : "Acme Corp",
#     "amount"      : 1500.0,
#     "status"      : "SUCCESS",
#     "confidence"  : 95
# }

# if __name__=="__main__":
#     base_path = Path(__file__).resolve().parent/"exported_json"

#     os.makedirs(base_path, exist_ok=True)

#     save_invoice_json(invoice,base_path)

# def load_invoice_json(filepath):
#     try:
#         with open(filepath,"r") as file:
#             return json.load(file)
#     except FileNotFoundError as e:
#         raise FileNotFoundError(f"[ERROR] File not found: {filepath}")
#     except json.JSONDecodeError as e:
#         raise ValueError(f"[ERROR] Invalid JSON format: {e}")
    

# if __name__=="__main__":
#     base_path = Path(__file__).resolve().parent/"exported_json"
#     filepath = os.path.join(base_path,"INV_001_extracted.json")
#     invoice = load_invoice_json(filepath)
#     print(f'vendor : {invoice["vendor"]}')
#     print(f'amount : ${invoice["amount"]}')
#     print(f'status : {invoice["status"]}')


import json
import os
from datetime import datetime

def export_batch_summary(invoices, output_dir):
    """
    Exports full batch summary as JSON.
    Used for API responses and ERP integration.
    """
    total      = len(invoices)
    successful = sum(1 for inv in invoices if inv["status"] == "SUCCESS")
    failed     = total - successful

    summary = {
        "batch_date"  : datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "total"       : total,
        "successful"  : successful,
        "failed"      : failed,
        "success_rate": round((successful / total) * 100, 2),
        "invoices"    : invoices
    }

    filepath = os.path.join(output_dir, "batch_summary.json")

    with open(filepath, "w") as file:
        json.dump(summary, file, indent=4)

    print(f"[SUCCESS] Batch summary saved: {filepath}")
    return summary

