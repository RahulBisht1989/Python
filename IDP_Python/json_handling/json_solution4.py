"""1. Save all invoices as one batch_summary.json file
2. Include total, successful, failed, success_rate in the file
3. Read batch_summary.json back
4. Print the summary"""
import json
from pathlib import Path

def summary_process(invoices):
    try:
        total = len(invoices)
        failed = sum(1 for inv in invoices if inv["status"]!="SUCCESS")
        successful = total - failed
        success_rate = round((successful/total)*100,2) if total > 0 else 0.0

        summary={
            "total" : total,
            "successful" : successful,
            "failed" : failed,
            "success_rate" : success_rate,
            "invoices" : invoices
        }
        return summary
    except ValueError as e:
        raise ValueError(f"[ERROR] Invalid data {e}")

def summary_report(filepath,summary):
    try:
        with open(filepath, "w") as file:
            json.dump(summary, file, indent= 4)
    except IOError as e:
        raise IOError(f"[ERROR] Could not save file {filepath}")
    
    
def summary_read(filepath):
    try:
        with open(filepath, "r") as file:
            summary_invoices = json.load(file)
            line = (
                "===== BATCH SUMMARY =====\n"
                f"{'Total':<10} : {summary_invoices['total']}\n"
                f"{'Successful':<10} : {summary_invoices['successful']}\n"
                f"{'Failed':<10} : {summary_invoices['failed']}\n"
                f"{'Rate':<10} : {summary_invoices['success_rate']}%\n"
                "========================="
            )
            return line
    except FileNotFoundError as e:
        raise FileNotFoundError(f"[ERROR] FILE NOTFOUND : {filepath}")
    except json.JSONDecodeError as e:
        raise ValueError(f"[ERROR] Invalid json {e}")
        
invoices = [
    {"invoice_id": "INV_001", "vendor": "Acme Corp", "amount": 1500.0, "status": "SUCCESS", "confidence": 95},
    {"invoice_id": "INV_002", "vendor": "Beta Ltd",  "amount": 2000.0, "status": "FAILED",  "confidence": 40},
    {"invoice_id": "INV_003", "vendor": "Gamma Inc", "amount": 750.0,  "status": "SUCCESS", "confidence": 85},
    {"invoice_id": "INV_004", "vendor": "Delta Co",  "amount": 1200.0, "status": "FAILED",  "confidence": 60},
    {"invoice_id": "INV_005", "vendor": "Echo Ltd",  "amount": 900.0,  "status": "SUCCESS", "confidence": 72},
]

if __name__=="__main__":
    from json_solution3 import basedir
    filename = "batch_summary.json"
    filepath = basedir/filename
    summary = summary_process(invoices)
    summary_report(filepath,summary)
    if filepath.exists():
           status = summary_read(filepath)
           print(status)
