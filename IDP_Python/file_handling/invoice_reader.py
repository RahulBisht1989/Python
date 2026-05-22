from create_sample_filehandling import Full_file_path

def read_invoices(filepath):
    """
    Reads invoice file and returns list of invoice dictionaries.
    """
    invoices =[]

    try:
        with open(filepath,"r") as file:
                for line in file:
                    line = line.strip()    # remove \n

                    if not line:          # skip empty lines
                            continue
                    
                    parts = line.split(",")

                    if len(parts)!=5:
                            print(f"[WARN] Skipping the malformed line {line}")
                            continue
                    
                    invoice = {
                            "id" : parts[0],
                            "vendor" : parts[1],
                            "amount" : float(parts[2]),
                            "status" : parts[3],
                            "confidence" : int(parts[4])
                    }

                    invoices.append(invoice)
    except FileNotFoundError:
          print(f"[ERROR] File not found: {filepath}")
          return []
    
    except ValueError as e:
          print(f"[ERROR] Invalid data in file: {e}")
          return []
    
    return invoices

def main():
      invoices = read_invoices(Full_file_path)
      for inv in invoices:
           print(inv)

if __name__=="__main__":
        main()


