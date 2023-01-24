from importlib import import_module
from pathlib import Path
import logging

__all__ = [
    import_module(f".{f.stem}", __package__)
    for f in Path(__file__).parent.glob("*.py")
    if "__" not in f.stem
]

for m in __all__:
    m.logger = logging.getLogger(m.__name__)

del import_module, Path, logging
