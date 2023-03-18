import requests
from pybreaker import CircuitBreaker
from retry_decorator import retry_with_backoff


@retry_with_backoff(
    retries=5,
    backoff_in_millis=100,
    log_level="error",
    exception=Exception("Request retries exhausted"),
)
def request_with_retries(method: str, url: str, **kwargs):
    response = requests.request(method, url, **kwargs)
    response.raise_for_status()
    return response


# NOTE:
# Every instance of the service has an independent state of the circuit breaker;
# We can use a shared state storage for all the instances (e.g. Redis)
notifications_service_circuit_breaker = CircuitBreaker(fail_max=5, reset_timeout=20)


@notifications_service_circuit_breaker
def notifications_service_request(method: str, url: str, **kwargs):
    response = requests.request(method, url, **kwargs)
    response.raise_for_status()
    return response
