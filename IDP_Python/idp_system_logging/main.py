from idp_system_logging.logger import setup_logger
setup_logger()
from idp_system_logging.batch import process_batch


if __name__ == "__main__":
    invoices = [
        {"invoice_id": "INV_001", "status": "SUCCESS", "confidence": 95},
        {"invoice_id": "INV_002", "status": "FAILED",  "confidence": 40},
        {"invoice_id": "INV_003", "status": "SUCCESS", "confidence": 72},
    ]

    process_batch(invoices)

