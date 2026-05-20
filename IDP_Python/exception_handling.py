# """Problem 1 — Easy
# Write a function safe_divide(a, b) that returns a / b but handles division by zero gracefully."""
# def safe_divide(a, b):
#     try:
#         r= a/b
#         print(r)
#     except ZeroDivisionError as z:
#         print("value cannot divide by 0")
#     finally:
#         print("Division attempted")

# safe_divide(10, 2)
# safe_divide(10, 0)
# safe_divide(0, 5)


# """Problem 2 — Easy
# Write a function get_field(doc, field) that safely gets a field from a document dictionary. 
# If the field is missing return "FIELD NOT FOUND"."""
# # Test documents
# doc1 = {"doc": "INV_001.pdf", "status": "SUCCESS", "confidence": 95}
# doc2 = {"doc": "INV_002.pdf", "status": "FAILED"}       # missing confidence
# doc3 = {"doc": "INV_003.pdf"}                            # missing status and confidence

# def get_field(doc, field):
#         try:    
#             return(f"{doc[field]}")
#         except KeyError as k:
#             return("FIELD NOT FOUND")

# output1= get_field(doc1,"confidence")
# output2=get_field(doc2,"confidence")
# output3=get_field(doc3,"confidence")

# print(output1,output2,output3, sep="\n")


"""Problem 3 — Medium
Write a function validate_invoice(doc) that checks:
amount exists and is a number
amount is greater than zero
vendor exists and is not empty
Raise a ValueError for each violation."""

# def validate_invoice(doc):
#     try:
#         if not isinstance(doc["amount"],(int,float)):
#             raise TypeError("amount must be a number")
#         if doc["vendor"]=="":
#             raise ValueError("vendor cannot be empty")
#         if doc["amount"]<=0:
#             raise ValueError("amount must be greater than zero")

#         return "✅ Valid"
        
#     except KeyError as e:
#         return (f"❌ Error: Missing field: {e}")
#     except TypeError as e:
#         return (f"❌ Error: {e}")
#     except ValueError as e:
#         return (f"❌ Error: {e}")
           
# # Test invoices — some valid, some broken
# invoice1 = {"vendor": "Acme Corp",  "amount": 1500}     # valid
# invoice2 = {"vendor": "Acme Corp",  "amount": -500}     # invalid amount
# invoice3 = {"vendor": "",           "amount": 1000}     # empty vendor
# invoice4 = {"vendor": "Acme Corp"}                      # missing amount
# invoice5 = {"amount": "lots"}   # wrong type

# output1 = "invoice1 → "+ validate_invoice(invoice1)
# output2 = "invoice2 → "+ validate_invoice(invoice2)
# output3 = "invoice3 → "+ validate_invoice(invoice3)
# output4 = "invoice4 → "+ validate_invoice(invoice4)
# output5 = "invoice5 → "+ validate_invoice(invoice5)
# print(output1,output2,output3,output4,output5, sep="\n" )
# print(__name__)

"""Problem 4 — Hard
Extend your process_batch() from the functions lesson to handle exceptions per document 
without crashing the entire batch."""

# def process_batch(batch,threshold=80):
#     list=[]
#     required_keys = ["doc", "status", "confidence"]
#     for item in batch:
#         for key in required_keys:
#             if key not in item:
#                 list.append(f"{'[ERROR]':<8} {item['doc']} → Missing field: {key}")
#         if "confidence" in item:
#             if not isinstance(item["confidence"],(int,float)):
#                 list.append(f"{'[ERROR]':<8} {item['doc']} → confidence must be a number")
#             elif not 0<=item["confidence"]<=100:
#                 list.append(f"{'[ERROR]':<8} {item['doc']} → confidence must be between 0 and 100")
#             else:
#                 if item["confidence"]>=threshold:
#                     status = f"{'[OK]':<8} {item['doc']} → ✅ OK"
#                 else:
#                     status = f"{'[OK]':<8} {item['doc']} → ⚠️  Needs Review"
#                 list.append(status)
#     return list

def validate_invoice(item):
    try:
        if not isinstance(item["confidence"],(int,float)):
            raise ValueError (f"{'[ERROR]':<8} {item['doc']} → confidence must be a number")
        elif not 0<=item["confidence"]<=100:
            raise ValueError(f"{'[ERROR]':<8} {item['doc']} → confidence must be between 0 and 100")
    except ValueError as e:
        return f"{e}"
    except TypeError as e:
        return f"{e}"
    except KeyError as e:
        return (f"{'[ERROR]':<8} {item['doc']} → Missing field: {e}")
    else:
       return None 
    
def is_low_confidence(score,threshold):
        return score<threshold

def process_batch(batch,threshold=80):
    summary = []
    for item in batch:
        error = validate_invoice(item)
        if error is not None:
            status = error
        elif not is_low_confidence(item["confidence"],threshold):
            status = f"{'[OK]':<8} {item['doc']} → ✅ OK"
        else:
            status = f"{'[OK]':<8} {item['doc']} → ⚠️  Needs Review" 
        summary.append(status)
    return summary
batch = [
    {"doc": "INV_001.pdf", "status": "SUCCESS", "confidence": 95},
    {"doc": "INV_002.pdf", "status": "FAILED",  "confidence": 40},
    {"doc": "INV_003.pdf", "status": "SUCCESS"},                        # missing confidence
    {"doc": "INV_004.pdf", "status": "SUCCESS", "confidence": "high"},  # wrong type
    {"doc": "INV_005.pdf", "status": "SUCCESS", "confidence": 150},     # out of range
    {"doc": "INV_006.pdf", "status": "SUCCESS", "confidence": 72},
]

batch_summary= process_batch(batch,80)
for i in batch_summary:
    print(i)