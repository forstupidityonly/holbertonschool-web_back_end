#!/usr/bin/env python3
"""fixing annotations"""
from typing import Sequence, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """commint"""
    if lst:
        return lst[0]
    return None
