VERSION_TUPLE = (0, 4, 1)
VERSION = ".".join(map(str, VERSION_TUPLE))

from .chain import Chain
from .text import Text, NewlineText
from .splitters import split_into_sentences
from .utils import combine
