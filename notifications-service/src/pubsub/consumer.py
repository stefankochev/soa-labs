from typing import Union

from fastapi.logger import logger

from aiokafka import AIOKafkaConsumer

from src.settings import KAFKA_BROKER_HOST, KAFKA_BROKER_PORT, KAFKA_CONSUMER_GROUP, ITEMS_TOPIC
from src.pubsub.handlers.new_items_handler import new_items_handler

TOPICS = [ITEMS_TOPIC]

kafka_consumer: Union[AIOKafkaConsumer, None] = None

HANDLERS = {
    ITEMS_TOPIC: new_items_handler
}


def get_consumer() -> AIOKafkaConsumer:
    global kafka_consumer
    if not kafka_consumer:
        kafka_consumer = AIOKafkaConsumer(
            *TOPICS,
            bootstrap_servers=f"{KAFKA_BROKER_HOST}:{str(KAFKA_BROKER_PORT)}",
            group_id=KAFKA_CONSUMER_GROUP,
        )
    return kafka_consumer


async def consume():
    consumer = get_consumer()
    await consumer.start()
    try:
        # Consume messages
        logger.info("Waiting for messages...")
        async for msg in consumer:
            print(
                "Consumed: ",
                msg.topic,
                msg.partition,
                msg.offset,
                msg.key,
                msg.value,
                msg.timestamp,
            )

            if msg.topic not in HANDLERS:
                # we don't have a handler for this topic, just continue
                continue

            # process the message with the corresponding handler function
            HANDLERS[msg.topic](msg.value)
    finally:
        await consumer.stop()
