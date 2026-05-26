"""1. Set up basic logging to console only
2. Loop through invoices
3. Log INFO for SUCCESS invoices
4. Log WARNING for confidence below 80
5. Log ERROR for FAILED invoices"""

import logging
logger = logging.getLogger("solution1")
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter(
    fmt="%(asctime)s | %(levelname)-8s | %(message)s",
    datefmt= "%Y-%m-%d %H:%M:%S"
)

console_handler= logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(formatter)

if not logger.handlers:
    logger.addHandler(console_handler)

invoices = [
    {"invoice_id": "INV_001", "status": "SUCCESS", "confidence": 95},
    {"invoice_id": "INV_002", "status": "FAILED",  "confidence": 40},
    {"invoice_id": "INV_003", "status": "SUCCESS", "confidence": 72},
]

for inv in invoices:
    is_failed = inv['status']!="SUCCESS"
    is_low_confidence = inv['confidence']<80
    if is_failed:
        logger.error(f"{inv['invoice_id']} processing failed")
    else:
        logger.info(f"{inv['invoice_id']} processed successfully")
    if is_low_confidence:
        logger.warning(f"{inv['invoice_id']} low confidence: {inv['confidence']}%")





