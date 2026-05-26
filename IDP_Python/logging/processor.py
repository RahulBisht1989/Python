import logging
processor_logger = logging.getLogger(f"idp_system.{__name__}")

def process_invoices(invoices):
    failed_item = 0
    success_item = 0
    for inv in invoices:
        is_failed = inv['status'] != "SUCCESS"
        is_low_confidence = inv['confidence'] < 80
        processor_logger.debug(f"Starting processing: {inv['invoice_id']}")
        if is_low_confidence:
            processor_logger.warning(f"{inv['invoice_id']} low confidence: {inv['confidence']}%")
        if is_failed:
            processor_logger.error(f"{inv['invoice_id']} processing failed")
            failed_item += 1
        else:
            processor_logger.info(f"{inv['invoice_id']} processed successfully")
            success_item += 1

    return {
        "failed" : failed_item,
        "success" : success_item
    }

        
    