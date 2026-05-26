import logging
from pathlib import Path

def setup_logger(log_file="logs/idp_system.log", level=logging.DEBUG):
    file_path = Path(__file__).resolve().parent / log_file

    Path(file_path).parent.mkdir(parents=True, exist_ok=True)

    root_logger= logging.getLogger("idp_system")
    root_logger.setLevel(level)

    formatter = logging.Formatter(
        fmt= "%(asctime)s | %(levelname)-8s | %(name)-20s | %(message)s",
        datefmt= "%Y-%m-%d %H:%M:%S" 
    )

    file_handler = logging.FileHandler(
        file_path,
        mode= "a",
        encoding= "utf-8"
    )
    file_handler.setLevel(level)
    file_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)

    if not root_logger.handlers:
        root_logger.addHandler(file_handler)
        root_logger.addHandler(console_handler)



