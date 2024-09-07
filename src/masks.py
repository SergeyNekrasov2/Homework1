import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s: %(filename)s: %(levelname)s: %(message)s",
    # filename="../logs/masks.log",
    filename='masks.log',
    filemode="w",
)
auth_logger = logging.getLogger("app.auth")


def get_mask_card_number(card_number: str) -> str:
    """Функция маскировки номера карты."""
    auth_logger.info(f"Маска карты{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}")
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(macc_number: str) -> str:
    """Функция маскировки номера счета."""
    mask_account = "**" + macc_number[-4:]
    auth_logger.info(f"Маска счета{mask_account}")
    return mask_account