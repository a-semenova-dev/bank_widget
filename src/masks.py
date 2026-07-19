"""
Module for masking card and account numbers.
"""

from src.logger_config import setup_logger

logger = setup_logger("masks", "masks.log")


def get_mask_card_number(card_number: str) -> str:
    logger.info("Request to mask card")
    try:
        if len(card_number) != 16 or not card_number.isdigit():
            logger.error(f"Invalid card: {card_number}")
            raise ValueError("Card number must contain exactly 16 digits")
        result = (
            f"{card_number[:4]} {card_number[4:6]}** **** "
            f"{card_number[-4:]}"
        )
        logger.info(f"Masked: {result}")
        return result
    except Exception as e:
        logger.error(f"Card error: {e}")
        raise


def get_mask_account(account_number: str) -> str:
    logger.info("Request to mask account")
    try:
        if len(account_number) < 4 or not account_number.isdigit():
            logger.error(f"Invalid account: {account_number}")
            raise ValueError("Account number must contain at least 4 digits")
        result = f"**{account_number[-4:]}"
        logger.info(f"Masked account: {result}")
        return result
    except Exception as e:
        logger.error(f"Account error: {e}")
        raise
