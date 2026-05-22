"""Create a file called documents.txt with 5 document names one per line. 
Read it and print each document name."""


def documents(dataset, filename="documents.txt"):
    document =[]
    with open(dataset,"r") as file:
        for line in file:
            line = line.strip()
            
            if not line:
                continue
            document.append(line)
    if not os.path.exists(filename):
        with open(filename, "w") as f:
            for line in document:
                line = line.strip()
                
                if not line:
                    continue
                
                parts = line.split(",")

                if len(parts)!=5:
                    print(f"[WARN] Skipping the incorrect line {line}")
                    continue

                line = (f"{parts[0]}.pdf\n")
                f.write(line)
            print("file created ✅")
    else:
        print("file already exist ✅")

if __name__=="__main__":
    import os
    from datafile import file_path, base_dir
    filename = os.path.join(base_dir,"documents.txt")
    documents(file_path,filename)