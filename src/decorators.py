import functools 
from typing import Callable, Any, Optional 
 
def log(filename: Optional[str] = None) -
    def decorator(func: Callable) -
        @functools.wraps(func) 
        def wrapper(*args, **kwargs) -
            pass 
        return wrapper 
    return decorator 
