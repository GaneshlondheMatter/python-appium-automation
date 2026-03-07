import logging
import os

def get_logger(name):
    log_dir = "logs"
    os.makedirs(log_dir, exist_ok=True)

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # IMPORTANT: prevent duplicate logs
    logger.propagate = False

    if not logger.handlers:
        # File handler (optional – can keep detailed logs)
        file_handler = logging.FileHandler(f"{log_dir}/automation.log")
        file_formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
        )
        file_handler.setFormatter(file_formatter)

        # Console handler (SIMPLE step logs)
        console_handler = logging.StreamHandler()
        console_formatter = logging.Formatter("%(message)s")
        console_handler.setFormatter(console_formatter)

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger
