import functools

from collections import OrderedDict
from collections.abc import Awaitable, Callable
from typing import ParamSpec, TypeAlias, TypeVar


__all__ = ("async_lru_cache",)


P = ParamSpec("P")
T = TypeVar("T")
AsyncFn: TypeAlias = Callable[P, Awaitable[T]]


def async_lru_cache[FN: AsyncFn](maxsize: int = 128) -> Callable[[FN], FN]:
    def decorator(fn: FN) -> FN:
        cache = OrderedDict()

        @functools.wraps(fn)
        async def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
            key = (args, frozenset(kwargs.items()))

            if key in cache:
                # Move the item to the end to show that it was recently used
                cache.move_to_end(key)
                return cache[key]

            # Call the original function and cache the result
            result = await fn(*args, **kwargs)
            cache[key] = result
            # Ensure the cache doesn't exceed the maxsize
            if len(cache) > maxsize:
                # Pop the first item since it is the least recently used
                cache.popitem(last=False)
            return result

        return wrapper

    return decorator
