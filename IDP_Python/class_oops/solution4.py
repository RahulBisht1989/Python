"""Create custom exception classes:
→ IDPBaseException
→ InvalidInvoiceError
→ MissingFieldError
→ LowConfidenceError

Create InvoiceValidator class with validate() method:
→ vendor exists and not empty
→ amount exists, is number, greater than zero
→ confidence exists, between 0 and 100"""

class IDPBaseException(Exception):
    pass

class InvalidInvoiceError(IDPBaseException):
    pass

class MissingFieldError(IDPBaseException):
    pass

class LowConfidenceError(IDPBaseException):
    pass

class InvoiceValidator:
    required_fields =['invoice_id', 'vendor', 'amount', 'confidence']
    def __init__(self, **kwargs):
        for key,value in kwargs.items():
            setattr(self,key,value)


    def __str__(self):
        attributes = []
        for key,value in self.__dict__.items():
            attributes.append(f"{key} = {value}")
        return f"Invoice({', '.join(attributes)})"

    def validate(self):
        doc_id = getattr(self, 'invoice_id', 'UNKNOWN')
        for field in self.required_fields:
            value = getattr(self, field, None)
            if value is None:
                raise MissingFieldError(f"{field} missing in {doc_id}")
            if isinstance(value, str) and not value.strip():
                raise MissingFieldError(f"{field} empty in {doc_id}")
            
        amount = getattr(self , "amount", None)
        confidence = getattr(self , "confidence", None)
        if amount is not None and not isinstance(amount , (int,float)):
            raise InvalidInvoiceError(f"amount must be a number in {doc_id}")
        if amount is not None and amount<=0:
            raise InvalidInvoiceError(f"amount must be greater than zero in {doc_id}")
        if confidence is not None and not 0<=confidence<=100:
            raise LowConfidenceError(f"confidence out of range in {doc_id}")


invoices = [
    {"invoice_id": "INV_001", "vendor": "Acme Corp", "amount": 1500.0, "confidence": 95},
    {"invoice_id": "INV_002", "vendor": "Acme Corp", "confidence": 95},
    {"invoice_id": "INV_003", "vendor": "Acme Corp", "amount": -500.0, "confidence": 95},
    {"invoice_id": "INV_004", "vendor": "Acme Corp", "amount": 1500.0, "confidence": 150},
]



if __name__ == "__main__":
    
    for doc in invoices:
        try:
            inv = InvoiceValidator(**doc)
            inv.validate()
            print(f"{inv.invoice_id} → ✅ Valid")
        except IDPBaseException as e:
            print(f"{inv.invoice_id} → ❌ {type(e).__name__}: {e}")