"""Retry with exponential backoff placeholder."""

import time
import random

def with_retry(fn, max_attempts: int = 5, base_delay: float = 1.0):
    attempt = 0
    while True:
        attempt += 1
        try:
            return fn()
        except Exception:
            if attempt >= max_attempts:
                raise
            sleep = base_delay * (2 ** (attempt - 1)) + random.random()
            time.sleep(sleep)
