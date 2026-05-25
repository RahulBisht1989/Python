"""1. Convert invoice dictionary to JSON string
2. Print the JSON string with indent=4"""

import json

def converter_jsonstring(invoice):
    return json.dumps(invoice,indent=4)

invoice = {
    "invoice_id" : "INV_001",
    "vendor"     : "Acme Corp",
    "amount"     : 1500.0,
    "status"     : "SUCCESS",
    "confidence" : 95
}

if __name__== "__main__":
    jsonstring = converter_jsonstring(invoice)
    print(jsonstring)