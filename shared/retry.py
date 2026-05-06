import time
from typing import Callable


def retry(
    func: Callable,
    retries: int = 3,
    delay: int = 2,
):
    """
    Retry wrapper for transient failures.
    """

    last_exception = None

    for attempt in range(1, retries + 1):

        try:
            return func()

        except Exception as exc:

            last_exception = exc

            print(
                f"[Retry {attempt}/{retries}] "
                f"Request failed: {exc}"
            )

            time.sleep(delay)

    raise last_exception