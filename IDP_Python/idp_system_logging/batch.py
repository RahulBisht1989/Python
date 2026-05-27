import logging
from idp_system_logging.processor import process_invoices

batch_logger = logging.getLogger(__name__)


def process_batch(invoices):
    total = len(invoices)
    batch_logger.info(f"Batch started — {total} invoices")
    item_status = process_invoices(invoices)
    batch_logger.info(f"Batch complete — Success: {item_status['success']} | Failed: {item_status['failed']}")
