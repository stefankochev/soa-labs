import asyncio
from typing import Union
from aiokafka import AIOKafkaProducer

from src.settings import KAFKA_BROKER_HOST, KAFKA_BROKER_PORT

kafka_producer: Union[AIOKafkaProducer, None] = None


def get_producer() -> AIOKafkaProducer:
    global kafka_producer
    if not kafka_producer:
        loop = asyncio.get_event_loop()
        kafka_producer = AIOKafkaProducer(
            loop=loop,
            bootstrap_servers=f"{KAFKA_BROKER_HOST}:{KAFKA_BROKER_PORT}",
        )
    return kafka_producer
