import random
import time
import logging
import sys
import traceback


def retry_with_backoff(
    retries: int = 5,
    backoff_in_millis: int = 50,
    exception: Exception = Exception(),
    log=logging,
    log_level="debug",
):
    """Decorator to retry a function multiple times, applying an exponential
    backoff strategy.
    Note that the function will be potentially called retries + 1 times. In
    otherwords, "retries" refers to the number of retries the function is to
    perform. Values < zero have no effect and result in no retries, but one
    single execution.
    The decorated function is expected to raise an exception on failure and
    will be retried for `retries` times, using an exponential backoff with an
    interval of `backoff_seconds`. If `backoff_seconds is `0`, no backoff will
    be applied and the function retries immediately.
    If the retry loop exhausts the number of retries, the wrapped functions
    exception will be reraised, so the original exception needs to be handled
    in the parent code tree.
    Usage:
    ```python
    from shared.retry import retry_with_backoff
    @retry_with_backoff(retries=3)
    def foo(a, b=1):
        return connect(a, raise_exception=True)
    ```
    Parameters
    ----------
    retries : int
        The max number of retries to do before failing the function.
    backoff_in_millis : int
        An interval to sleep between retries (this is exponentially increased)
        in milliseconds. The time between retries is further randomized with
        an additional interval between 0 and 250ms.
        If this parameter is set to `0`, no sleep will be applied and the
        function retries immediately.
    exception: Exception
        Exception to be raised when the maximum number of retries is reached.
    log : logging.Logger
        The logger to use for this retry loop.
    log_level : str
        The log level to use for failed attempts, everything else is logged
        as `debug`.
    Returns
    -------
    callable(callable(...)) :
        A decorator function applicable to other functions.
    """
    dbg_log = log.debug
    flr_log = getattr(log, log_level.lower(), dbg_log)

    def rwb(f):
        """Retry decorator configured to the retry count and backoff times."""

        def wrapper(*args, **kwargs):
            x = 0
            while True:
                dbg_log(f"Trying '{f.__name__}' attempt={x + 1} retries={retries}")
                try:
                    return f(*args, **kwargs)
                except:  # noqa: 722
                    _, exc, _ = sys.exc_info()
                    flr_log(f"Failed '{f.__name__}' error={exc}")
                    flr_log(traceback.format_exc())
                    if x == retries:
                        raise exception
                    else:
                        sleep = (
                            (backoff_in_millis * 2**x + random.uniform(0, 250)) if backoff_in_millis > 0 else 0
                        ) / 1000
                        flr_log(f"Retrying '{f.__name__}' sleep={sleep}ms")
                        time.sleep(sleep)
                        x += 1

        return wrapper

    return rwb
