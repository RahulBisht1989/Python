class IDPBaseException(Exception):
    pass

class InvalidInvoiceError(IDPBaseException):
    pass

class MissingFieldError(IDPBaseException):
    pass

class LowConfidenceError(IDPBaseException):
    pass

class InvoiceValidator:

    def __init__(self,invoice_dict):
        self.invoice_dict = invoice_dict
        self.invoice_id = self.invoice_dict.get("invoice_id","Unknown")
        self.vendor = self.invoice_dict.get("vendor","Unknown")
        self.amount = self.invoice_dict.get("amount",0)
        self.confidence = self.invoice_dict.get("confidence",0)

    def __str__(self):
        return (f"Invoice({self.invoice_id} | "
                f"{self.vendor} | "
                f"{self.amount} | "
                f"{self.confidence})"
                )
    
    def validate(self):
        if "vendor" not in self.invoice_dict:
            raise MissingFieldError(f"vendor missing in {self.invoice_id}")
        if not self.invoice_dict["vendor"].strip():
            raise MissingFieldError(f"vendor empty in {self.invoice_id}")
        if "amount" not in self.invoice_dict:
            raise MissingFieldError(f"amount missing in {self.invoice_id}")
        if not isinstance(self.invoice_dict["amount"], (int, float)):
            raise InvalidInvoiceError(f"amount must be a number in {self.invoice_id}")
        if self.invoice_dict["amount"]<=0:
            raise InvalidInvoiceError(f"amount must be greater than zero in {self.invoice_id}")
        if "confidence" not in self.invoice_dict:
            raise MissingFieldError(f"confidence empty in {self.invoice_id}")
        if not 0<=self.invoice_dict["confidence"]<=100:
            raise LowConfidenceError(f"confidence out of range in {self.invoice_id}")



invoices = [
    {"invoice_id": "INV_001", "vendor": "Acme Corp", "amount": 1500.0, "confidence": 95},
    {"invoice_id": "INV_002", "vendor": "Acme Corp", "confidence": 95},
    {"invoice_id": "INV_003", "vendor": "Acme Corp", "amount": -500.0, "confidence": 95},
    {"invoice_id": "INV_004", "vendor": "Acme Corp", "amount": 1500.0, "confidence": 150},
]

if __name__=="__main__":
    for doc in invoices:
        try:
            inv = InvoiceValidator(doc)
            inv.validate()
            print(inv)
            print(f"{inv.invoice_id} → ✅ Valid")
        except IDPBaseException as e:
            print(f"{inv.invoice_id} → ❌ {type(e).__name__}: {e}")
