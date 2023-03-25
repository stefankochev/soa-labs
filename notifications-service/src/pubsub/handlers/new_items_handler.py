from fastapi.logger import logger


def new_items_handler(message: dict):
    """Handler of new_item messages.

    :param message: the messaging containing the new_item event
    :return: None
    """
    # Here we could be sending mobile push notifications, email notifications or notify users
    # using other communication channels (here we just mock/log this action, not implemented)
    logger.info("Sending notifications")
    print("Handling message")
    print(message)
