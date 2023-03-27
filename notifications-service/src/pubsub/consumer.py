from typing import Union

from fastapi.logger import logger

from aiokafka import AIOKafkaConsumer

from src.settings import (
    KAFKA_BROKER_HOST,
    KAFKA_BROKER_PORT,
    KAFKA_CONSUMER_GROUP,
    ITEMS_TOPIC,
)
from src.pubsub.handlers.new_items_handler import new_items_handler

TOPICS = [ITEMS_TOPIC]

kafka_consumer: Union[AIOKafkaConsumer, None] = None

# map of events handler (per topic)
HANDLERS_MAP = {ITEMS_TOPIC: new_items_handler}


def get_consumer() -> AIOKafkaConsumer:
    global kafka_consumer
    if not kafka_consumer:
        kafka_consumer = AIOKafkaConsumer(
            *TOPICS,  # subscribe to all topics in the TOPICS list
            bootstrap_servers=f"{KAFKA_BROKER_HOST}:{KAFKA_BROKER_PORT}",
            # consumer group - one message delivered per group
            # in our case all instances of a service are part of the same group,
            # i.e. only one instance will consumer the event
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
            logger.info(
                f"New message - Topic: {msg.topic} Partition: {msg.partition} Offset: {msg.offset} "
                f"Key: {msg.key} Value: {msg.value} Timestamp: {msg.timestamp}",
            )

            if msg.topic not in HANDLERS_MAP:
                # we don't have a handler for this topic, just continue
                continue

            # process the message with the corresponding handler function
            await HANDLERS_MAP[msg.topic](msg.value)
    finally:
        await consumer.stop()
