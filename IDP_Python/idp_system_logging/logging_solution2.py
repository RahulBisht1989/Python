"""
1. Set up logger that writes to BOTH console and log file
2. Console shows INFO and above
3. Log file saves DEBUG and above
4. Add a DEBUG log at start of each invoice processing
5. Process invoices and log appropriate levels
"""
import logging
from pathlib import Path
def setup_logger():
    log_path = "logs/solution2.log"

    log_file = Path(__file__).resolve().parent / log_path

    log_file.parent.mkdir(parents=True ,exist_ok= True)

    logger = logging.getLogger("solution2")
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        fmt= "%(asctime)s | %(levelname)-8s | %(message)s",
        datefmt= "%Y-%m-%d %H:%M:%S"  
    )

    file_handler= logging.FileHandler(
        log_file,
        mode="a",
        encoding="utf-8"
        )
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    console_handler= logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)

    if not logger.handlers:
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger

invoices = [
    {"invoice_id": "INV_001", "status": "SUCCESS", "confidence": 95},
    {"invoice_id": "INV_002", "status": "FAILED",  "confidence": 40},
    {"invoice_id": "INV_003", "status": "SUCCESS", "confidence": 72},
]

logger = setup_logger()

failed = 0
success = 0
logger.info(f"Batch started — {len(invoices)} invoices")
for inv in invoices:
    is_failed = inv['status'] != "SUCCESS"
    is_low_confidence = inv['confidence'] < 80
    logger.debug(f"Starting processing: {inv['invoice_id']}")
    if is_failed:
        logger.error(f"{inv['invoice_id']} processing failed")
        failed += 1
    else:
        logger.info(f"{inv['invoice_id']} processed successfully")
        success += 1
    if is_low_confidence:
        logger.warning(f"{inv['invoice_id']} low confidence: {inv['confidence']}%")
logger.info(f"Batch complete — Success: {success} | Failed: {failed}")