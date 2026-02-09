"""Pagination helper placeholder."""

from typing import Iterable, Callable, Any

def paginate(fetch_page: Callable[[str|None], tuple[list[Any], str|None]]) -> Iterable[Any]:
    token = None
    while True:
        items, token = fetch_page(token)
        for it in items:
            yield it
        if not token:
            break
