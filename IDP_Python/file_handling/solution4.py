"""1. Read invoices.txt
2. Write all SUCCESS invoices to successful.txt
3. Write all FAILED invoices to failed.txt
4. Each file must include a header, all matching invoices, a divider, and total count"""

def invoice_data(dataset_path):
    invoices=[]
    try:
        with open(dataset_path,"r") as f:
            for line in f:
                line = line.strip()

                if not line:
                    continue

                invoices.append(line)
    except FileNotFoundError:
        raise FileNotFoundError(f"[ERROR] FIle not found :{file_path}")
    return invoices

def check_status():
    invoices = invoice_data(file_path)
    sucess_status = []
    fail_status =[]
    try:
        for inv in invoices :
            parts = inv.split(",")
            if len(parts)!=5:
                print(f"[ERROR] Skipping malform line {inv}")
                continue
            if parts[3]!="SUCCESS":
                fail_status.append(f"{parts[0]:<8} | {parts[1]:<11} | ${float(parts[2]):<8} | Confidence: {parts[4]}%")
            else:
                sucess_status.append(f"{parts[0]:<8} | {parts[1]:<11} | ${float(parts[2]):<8} | Confidence: {parts[4]}%")
        total_pass = len(sucess_status)
        total_fail = len(fail_status)
    except ValueError as e:
        raise ValueError(f"[ERROR] Invalid data in file: {e}")

    return total_pass, total_fail, fail_status,sucess_status

def report_writer(successful_path,failed_path):
    total_pass, total_fail, fail_status,sucess_status = check_status()
    try:
        with open(successful_path,"w") as file:
            file.write("===== SUCCESSFUL INVOICES =====\n")
            for inv in sucess_status:
                file.write(f"{inv}\n")
            file.write("===============================\n")
            file.write(f"Total Successful: {total_pass}")
        
        with open(failed_path,"w") as f:
            f.write("===== FAILED INVOICES =====\n")
            for inv in fail_status:
                f.write(f"{inv}\n")
            f.write("===========================\n")
            f.write(f"Total Failed: {total_fail}")

    except IOError as e:
        raise IOError(f"[ERROR] Could not write report: {e}")
        

if __name__=="__main__":
    import os
    from datafile import base_dir, file_path
    successful_path = os.path.join(base_dir,"successful.txt")
    failed_path = os.path.join(base_dir,"failed.txt")
    report_writer(successful_path,failed_path)
