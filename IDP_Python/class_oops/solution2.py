"""Extend Invoice class with:
→ calculate_tax() method — 18% GST
→ calculate_total() method — amount + tax
→ to_dict() method

Print tax, total and dictionary for INV_001."""

class Invoice:
    """blueprint for sigle invoice document
    holds invoice data
    """
    
    CONFIDENCE_THRESHOLD = 80
    INVOICE_TAX = 0.18
    
    def __init__(self, invoice_id,vendor,amount,status,confidence):
        #initialized the instance attributes
        self.invoice_id = invoice_id
        self.vendor = vendor
        self.amount = amount
        self.status = status
        self.confidence = confidence

    def is_successful(self):
        #checks if invoice status is success
        return self.status == "SUCCESS"
    
    def is_low_confidence(self):
        #checks if invoice has low confidence
        return self.confidence< Invoice.CONFIDENCE_THRESHOLD
    
    def __str__(self):
        #prints in format
        return (f"Invoice({self.invoice_id} | "
                f"{self.vendor:<9} | "
                f"${self.amount} | "
                f"{self.status})"
                )
    
    def calculate_tax(self):
        #calculate 18% tax for the amount
        return round(self.amount * Invoice.INVOICE_TAX,2)
    
    def calculate_total(self):
        #calculate total after tax
        return self.amount + self.calculate_tax()
    
    def to_dict(self):
        #update the data in dictionary format
        return {
            'invoice_id' : self.invoice_id,
            'vendor' : self.vendor,
            'amount' : self.amount,
            'status' : self.status,
            'confidence' : self.confidence,
            'tax' : self.calculate_tax(),
            'total' : self.calculate_total()
        }

if __name__=="__main__":
    import json
    inv1 = Invoice("INV_001", "Acme Corp", 1500.0, "SUCCESS", 95)

    print(f"{'Tax':<5} : ${inv1.calculate_tax()}", f"Total : ${inv1.calculate_total()}", sep="\n")
    print(f"{'Dict':<5} :\n"
        f"{json.dumps(inv1.to_dict(), indent= 4)}")