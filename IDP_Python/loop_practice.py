#P1 Your IDP system receives documents. Print the document number for the first 5 documents.
# invoices = int(input("how many invoices? \n"))
# for i in range(1, invoices+1):
#     print(f"Processing Document: {i}")

#P2 You have a list of invoice IDs. Loop through and print each one.
# YOUR TURN
# invoice_ids = ["INV-001", "INV-004", "INV-007", "INV-009"]
# for i in invoice_ids:
#     print(f"Invoice ID: {i}")

#P3 Problem 3 — Count Total Documents
# documents = ["Invoice_A.pdf", "Invoice_B.pdf", "PO_001.pdf", "KYC_Form.pdf"]
# count = 0
# for document in documents:
#     count+=1
# print(f"Total documents: {count}")

#Problem 4 — Flag Failed Documents
# documents = [
#     {"name": "Invoice_A.pdf", "status": "SUCCESS"},
#     {"name": "Invoice_C.pdf", "status": "FAILED"},
#     {"name": "PO_001.pdf",    "status": "SUCCESS"},
#     {"name": "PO_005.pdf",    "status": "FAILED"},
# ]

# for document in documents:
#     if document["status"]!= "SUCCESS":
#         print("FAILED document found:", document["name"])

#Problem 5 — Calculate Total Invoice Amount
# invoices = [500, 1200, 800, 750, 1250]
# total = 0
# for invoice in invoices:
#     total+=invoice
# print("Total Invoice Amount:", total)

#Problem 6 — While Loop: Retry Failed OCR
# import random
# success = False
# attempt = 0
# while True:
#     attempt+=1
#     success = random.choice([True,False])
#     if success!= True:
#         print(f"Attempt {attempt}: OCR Failed. Retrying...")
#     else:
#         print(f"Attempt {attempt}: OCR Success!")
#         break


#Problem 7 — Confidence Score Checker
# Field: vendor_name    | Score: 95% | ✅ OK
# Field: invoice_date   | Score: 72% | ⚠️  LOW CONFIDENCE - Needs Review
# extracted_fields = [
#     {"field": "vendor_name",  "confidence": 95},
#     {"field": "invoice_date", "confidence": 72},
#     {"field": "total_amount", "confidence": 88},
#     {"field": "po_number",    "confidence": 61},
# ]

# for field in extracted_fields:
#     if field["confidence"]<80:
#         status = "⚠️ LOW CONFIDENCE - Needs Review"
#     else:
#         status = "✅ OK"
        
#     print(f"Field: {field['field']:<12} | Score: {field['confidence']} | {status}")

#Problem 8 — Batch Document Summary Report
# ===== DAILY BATCH REPORT =====
# Total Documents : 5
# Successful      : 3
# Failed          : 2
# Success Rate    : 60.0%
# ==============================

def get_batch_report(batch):
    total = 0
    Successful= 0
    Failed=0
    for document in batch:
        total+=1
        if document["status"]=="SUCCESS":
            Successful+=1
        else:
            Failed+=1
    rate = (Successful/total)*100
    print(
        f"===== DAILY BATCH REPORT =====\n"
        f"{'Total Documents':<18}: {total}\n"
        f"{'Successful':<18}: {Successful}\n"
        f"{'Failed':<18}: {Failed}\n"
        f"{'Success Rate':<18}: {rate}%\n"
        f"=============================="
    )

batch = [
    {"doc": "INV_001.pdf", "status": "SUCCESS"},
    {"doc": "INV_002.pdf", "status": "FAILED"},
    {"doc": "PO_010.pdf",  "status": "SUCCESS"},
    {"doc": "KYC_003.pdf", "status": "FAILED"},
    {"doc": "INV_005.pdf", "status": "SUCCESS"},
]

get_batch_report(batch)