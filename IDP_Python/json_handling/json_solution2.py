"""1. Convert json_string to a Python dictionary
2. Print each field on a separate line"""

import json

def to_python_dictionary(json_string):
    try:
        return json.loads(json_string)
    except json.JSONDecodeError as e:
        raise ValueError(f"[ERROR] Invalid json format : {e}")

json_string = '{"invoice_id": "INV_002", "vendor": "Beta Ltd", "amount": 2000.0, "status": "FAILED", "confidence": 40}'

if __name__=="__main__":
    invoice = to_python_dictionary(json_string)
    print(
        f"{'Invoice ID':<11}: {invoice['invoice_id']}\n"
        f"{'Vendor':<11}: {invoice['vendor']}\n"
        f"{'Amount':<11}: ${invoice['amount']}\n"
        f"{'Status':<11}: {invoice['status']}\n"
        f"{'Confidence':<11}: {invoice['confidence']}%"
    )