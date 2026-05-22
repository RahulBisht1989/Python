# file: report_writer.py

def write_batch_report(invoices, report_file="batch_report.txt"):
    """
    Processes invoices and writes summary report to file.
    """
    output_file = os.path.join(FILE_DIR,report_file)
    total = len(invoices)
    successful = sum(1 for inv in invoices if inv["status"]=="SUCCESS")
    failed = total-successful
    review = sum(1 for inv in invoices if inv["confidence"]<80)

    try:
        with open(output_file, "w", encoding= "utf-8") as file:
            file.write("===== DAILY BATCH REPORT =====\n")
            file.write(f"{'Total Documents':<18}: {total}\n")
            file.write(f"{'Successful':<18}: {successful}\n")
            file.write(f"{'Failed':<18}: {failed}\n")
            file.write(f"{'Needs Review':<18}: {review}\n")
            file.write("==============================\n\n")

            for inv in invoices:
                flag = "⚠️  Review" if inv["confidence"]<80 else "✅ OK"
                line = (f"{inv['id']:<12} | "
                         f"{inv['vendor']:<12} | "
                         f"{inv['amount']:<12} | "
                         f"{inv['status']:<8} | "
                         f"{inv['confidence']:<4} | "
                         f"{flag}\n"
                         )

                file.write(line)
            print(f"[SUCCESS] Report written to {report_file}")
    except IOError as e:
        print(f"[ERROR] Could not write report: {e}")        
        
if __name__=="__main__":
    import os
    from invoice_reader import read_invoices
    from create_sample_filehandling import Full_file_path,FILE_DIR
    invoices = read_invoices(Full_file_path)
    write_batch_report(invoices)


