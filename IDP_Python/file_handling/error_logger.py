# file: error_logger.py
def log_error(message, log_file="error.log"):
        """
    Appends error message to log file with timestamp.
    Never overwrites existing logs.
    """
        from datetime import datetime
        timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

        with open(log_file, "a") as file:
                file.write(f"[{timestamp}]- {message}\n")
                


if __name__=="__main__":
        from create_sample_filehandling import FILE_DIR
        import os
        log_file = os.path.join(FILE_DIR,"error.log")
        log_error("INV_003 missing confidence field",log_file)
        log_error("INV_004 invalid confidence type",log_file)