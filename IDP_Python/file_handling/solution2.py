"""Read invoices.txt and print only FAILED invoices."""

def failed_invoice(filepath):
    documents=[]
    try:
        with open(filepath,"r") as file:
            for line in file:
                line= line.strip()

                if not line:
                    continue

                parts = line.split(",")

                if parts[3]!= "SUCCESS":
                    status = (f"FAILED Invoice: {parts[0]:<8} | "
                            f"Vendor: {parts[1]:<8} | "
                            f"Amount: ${float(parts[2])}")
                    documents.append(status)
    except FileNotFoundError:
        raise FileNotFoundError(f"[ERROR] File not found : {filepath}")
    except ValueError as e:
        raise ValueError(f"[ERROR] Invalid data in file: {e}")
        
    return documents


if __name__=="__main__":
    from datafile import file_path
    documents = failed_invoice(file_path)
    for doc in documents:
        print(doc)