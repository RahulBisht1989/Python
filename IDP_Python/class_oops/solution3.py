"""Task:
Create a Document parent class with:
→ doc_id, filename

Create Invoice and PurchaseOrder child classes:
→ Invoice adds vendor, amount
→ PurchaseOrder adds supplier, quantity
→ Both override display() method"""


class Document:
    
    def __init__(self, doc_id, filename):
        self.doc_id = doc_id
        self.filename = filename

    def display(self):
        return f"Document: {self.doc_id} | {self.filename}"
    
class Invoice(Document):

    def __init__(self,doc_id, filename, vendor, amount):
        super().__init__(doc_id, filename)
        self.vendor = vendor
        self.amount = amount

    def display(self):
        return f"{'Invoice':<14}: {self.doc_id:<7} | {self.vendor:<9} | ${self.amount}"
    
class PurchaseOrder(Document):

    def __init__(self, doc_id, filename, supplier, quantity):
        super().__init__(doc_id, filename)
        self.supplier = supplier
        self.quantity = quantity

    def display(self):
        return f"{'PurchaseOrder':<14}: {self.doc_id:<7} | {self.supplier:<9} | Qty: {self.quantity}"
    


if __name__ == "__main__":
    inv = Invoice("INV_001", "invoice.pdf", "Acme Corp", 1500.0)
    po  = PurchaseOrder("PO_001", "po.pdf", "Beta Ltd", 100)

    print(inv.display())
    print(po.display())