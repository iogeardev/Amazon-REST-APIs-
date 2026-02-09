"""Simple rate limiter (token bucket) placeholder."""

import time

class TokenBucket:
    def __init__(self, rate_per_sec: float, burst: int):
        self.rate = rate_per_sec
        self.capacity = burst
        self.tokens = burst
        self.last = time.time()

    def consume(self, amount: int = 1):
        while True:
            now = time.time()
            delta = now - self.last
            self.last = now
            self.tokens = min(self.capacity, self.tokens + delta * self.rate)
            if self.tokens >= amount:
                self.tokens -= amount
                return
            time.sleep(max(0.05, (amount - self.tokens) / max(self.rate, 1e-6)))
