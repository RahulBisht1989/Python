"""
Create an Invoice class with:
→ invoice_id, vendor, amount, status, confidence
→ is_successful() method
→ is_low_confidence() method — threshold 80
→ __str__ method

Create two invoice objects and print them.
"""

class Invoice:
    confidence_threshold = 80
    def __init__(self, invoice_id, vendor, amount, status, confidence):
        self.invoice_id = invoice_id
        self.vendor = vendor
        self.amount = amount
        self.status = status
        self.confidence = confidence

    def is_successful(self):
        return self.status == "SUCCESS"

    def is_low_confidence(self):
        return self.confidence < Invoice.confidence_threshold

    def __str__(self):
        return  (
            f"Invoice({self.invoice_id} | "
            f"{self.vendor:<9} | "
            f"${self.amount} | "
            f"{self.status})"
        )

inv1 = Invoice("INV_001", "Acme Corp", 1500.0, "SUCCESS", 95)
inv2 = Invoice("INV_002", "Beta Ltd",  2000.0, "FAILED",  40)
print(inv1, inv2, sep= "\n")
print(f"{inv1.invoice_id} successful: {inv1.is_successful()}")
print(f"{inv2.invoice_id} successful: {inv2.is_successful()}")
print(f"{inv1.invoice_id} low confidence: {inv1.is_low_confidence()}")
print(f"{inv2.invoice_id} low confidence: {inv2.is_low_confidence()}")
