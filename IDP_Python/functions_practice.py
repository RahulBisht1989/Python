"""Problem 1 — Easy
Write a function is_low_confidence(score) that returns True if score is below 80, else False."""

# def is_low_confidence(score):
#     if score<80:
#         return True
#     else:
#         return False

# score= int(input("provide confidence:\n"))

# if __name__=="__main__":
#     if is_low_confidence(score):
#         print(f"{score}% - ⚠️ LOW CONFIDENCE - Needs Review")
#     else:
#         print(f"{score}% - ✅ OK")
"""Problem 2 — Easy
Write a function format_document_log(filename, status) that prints:[LOG] INV_001.pdf → SUCCESS"""

# def format_document_log(filename,status="PENDING"):
#     return(f"[LOG] {filename} → {status}")

# file_status= format_document_log("789797", "SUCCESS")
# print(file_status)

"""Problem 3 — Medium
Write a function calculate_invoice_total(amount, tax_rate=0.18) 
that returns the total amount including tax."""

# def calculate_invoice_total(amount, tax_rate=0.18):
#      amount+=(amount*tax_rate)
#      return amount

# total_amount= calculate_invoice_total(768)
# print(total_amount)

"""Problem 4 — Medium
Write a function count_failed(batch) that takes a list of documents 
and returns only the count of failed ones."""

# def count_failed(batch):
#     count=0
#     for i in batch:
#         if i["status"]!="SUCCESS":
#             count+=1
#     return count

# batch = [
#     {"doc": "INV_001.pdf", "status": "SUCCESS"},
#     {"doc": "INV_002.pdf", "status": "FAILED"},
#     {"doc": "PO_010.pdf",  "status": "SUCCESS"},
#     {"doc": "KYC_003.pdf", "status": "FAILED"},
#     {"doc": "INV_005.pdf", "status": "SUCCESS"},
# ]

# failed_doc = count_failed(batch)

# print("Failed Documents: ", failed_doc)

"""Problem 5 — Hard
Write a function process_batch(batch, threshold=80) that loops through documents, checks confidence, 
and prints a full report using the patterns you already know."""
def summary_report(batch):
    total=0
    success= 0
    failed=0
    review=0
    for i in batch:
        total+=1
        if i["status"]!="SUCCESS":
            failed+=1
        else:
            success+=1
        if i["confidence"]<80:
            review+=1
    
    return total,success,failed,review


def process_batch(batch, threshold=80):
    lines=[]
    for i in batch:
        flag =  i["confidence"]<threshold
        if flag:
            status = "⚠️ LOW CONFIDENCE - Needs Review"
        else:
            status = "✅ OK"
        
        line = (f"doc: {i['doc']:<12} | status: {i['status']:<8} | Score: {i['confidence']} | {status}") 
        lines.append(line)
    return lines

batch = [
    {"doc": "INV_001.pdf", "status": "SUCCESS", "confidence": 95},
    {"doc": "INV_002.pdf", "status": "FAILED",  "confidence": 40},
    {"doc": "PO_010.pdf",  "status": "SUCCESS", "confidence": 85},
    {"doc": "KYC_003.pdf", "status": "FAILED",  "confidence": 60},
    {"doc": "INV_005.pdf", "status": "SUCCESS", "confidence": 72},
]

total,success,failed,review = summary_report(batch)
print(f"========== BATCH PROCESSING REPORT ==========")
for i in process_batch(batch):
    print(i)
print(
    f"=============================================\n"
    f"Total: {total} | Success: {success} | Failed: {failed} | Needs Review: {review}"
    )

