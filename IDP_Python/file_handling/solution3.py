"""
1. Read invoices.txt
2. Calculate total number of invoices
3. Calculate total amount of all invoices
4. Calculate average amount
5. Write results to summary.txt"""

def summary(dataset,summaryfile="summary.txt"):
    total_invoices=0
    all_amount=[]
    total_amount=0
    average_amount = 0
    try:
        with open(dataset,"r") as file:
            for line in file:
                line = line.strip()
                
                if not line:
                    continue

                total_invoices+=1
                
                parts= line.split(",")

                if len(parts)!=5:
                    print(f"[ERROR] Skipping malform line {line}")
                    continue

                all_amount.append(float(parts[2]))

            total_amount=sum(all_amount)
            average_amount = total_amount/total_invoices

            line = ("===== INVOICE SUMMARY =====\n"
                    f"Total Invoices : {total_invoices}\n"
                    f"Total Amount   : ${total_amount}\n"
                    f"Average Amount : ${average_amount}\n"
                    "==========================="
                    )
    except FileNotFoundError:
        raise FileNotFoundError(f"[ERROR] File not found : {dataset}")
    except ValueError as e:
        raise ValueError(f"[ERROR] Invalid data in file: {e}")
    
    try:
        with open(summaryfile, "w") as file:
            file.write(line)
    except IOError as e:
        raise IOError(f"[ERROR] Could not write report: {e}")
    
if __name__=="__main__":
    import os
    from datafile import file_path,base_dir
    summaryfile = os.path.join(base_dir,"summary.txt")
    line = summary(file_path,summaryfile)
