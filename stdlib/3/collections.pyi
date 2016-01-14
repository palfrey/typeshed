# Stubs for collections

# Based on http://docs.python.org/3.2/library/collections.html

# TODO UserDict
# TODO UserList
# TODO UserString
# TODO more abstract base classes (interfaces in mypy)

# These are not exported.
from typing import (
    TypeVar, Iterable, Generic, Iterator, Dict, overload,
    Mapping, List, Tuple, Callable, Sized,
    Optional, Union
)
# These are exported.
# TODO reexport more.
from typing import (
    MutableMapping as MutableMapping,
    Sequence as Sequence,
    MutableSequence as MutableSequence,
    AbstractSet as Set,
)

_T = TypeVar('_T')
_KT = TypeVar('_KT')
_VT = TypeVar('_VT')


# namedtuple is special-cased in the type checker; the initializer is ignored.
namedtuple = object()


# Technically, deque only derives from MutableSequence in 3.5.
# But in practice it's not worth losing sleep over.
class deque(MutableSequence[_T], Generic[_T]):
    maxlen = 0 # type: Optional[int] # TODO readonly
    def __init__(self, iterable: Iterable[_T] = ...,
                 maxlen: int = ...) -> None: ...
    def append(self, x: _T) -> None: ...
    def appendleft(self, x: _T) -> None: ...
    def insert(self, i: int, x: _T) -> None: ...
    def clear(self) -> None: ...
    def count(self, x: _T) -> int: ...
    def extend(self, iterable: Iterable[_T]) -> None: ...
    def extendleft(self, iterable: Iterable[_T]) -> None: ...
    def pop(self, i: int = ...) -> _T: ...
    def popleft(self) -> _T: ...
    def remove(self, value: _T) -> None: ...
    def reverse(self) -> None: ...
    def rotate(self, n: int) -> None: ...

    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[_T]: ...
    def __str__(self) -> str: ...
    def __hash__(self) -> int: ...

    # These methods of deque don't really take slices, but we need to
    # define them as taking a slice to satisfy MutableSequence.
    @overload
    def __getitem__(self, index: int) -> _T: ...
    @overload
    def __getitem__(self, s: slice) -> Sequence[_T]: raise TypeError
    @overload
    def __setitem__(self, i: int, x: _T) -> None: ...
    @overload
    def __setitem__(self, s: slice, o: Sequence[_T]) -> None: raise TypeError
    @overload
    def __delitem__(self, i: int) -> None: ...
    @overload
    def __delitem__(self, s: slice) -> None: raise TypeError

    def __contains__(self, o: object) -> bool: ...

    # TODO __reversed__


class Counter(Dict[_T, int], Generic[_T]):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, Mapping: Mapping[_T, int]) -> None: ...
    @overload
    def __init__(self, iterable: Iterable[_T]) -> None: ...
    # TODO keyword arguments

    def elements(self) -> Iterator[_T]: ...

    @overload
    def most_common(self) -> List[_T]: ...
    @overload
    def most_common(self, n: int) -> List[_T]: ...

    @overload
    def subtract(self, Mapping: Mapping[_T, int]) -> None: ...
    @overload
    def subtract(self, iterable: Iterable[_T]) -> None: ...

    # The Iterable[Tuple[...]] argument type is not actually desirable
    # (the tuples will be added as keys, breaking type safety) but
    # it's included so that the signature is compatible with
    # Dict.update. Not sure if we should use '# type: ignore' instead
    # and omit the type from the union.
    def update(self, m: Union[Mapping[_T, int],
                              Iterable[Tuple[_T, int]],
                              Iterable[_T]]) -> None: ...

class OrderedDict(Dict[_KT, _VT], Generic[_KT, _VT]):
    def popitem(self, last: bool = ...) -> Tuple[_KT, _VT]: ...
    def move_to_end(self, key: _KT, last: bool = ...) -> None: ...


class defaultdict(Dict[_KT, _VT], Generic[_KT, _VT]):
    default_factory = ...  # type: Callable[[], _VT]

    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, map: Mapping[_KT, _VT]) -> None: ...
    @overload
    def __init__(self, iterable: Iterable[Tuple[_KT, _VT]]) -> None: ...
    @overload
    def __init__(self, default_factory: Callable[[], _VT]) -> None: ...
    @overload
    def __init__(self, default_factory: Callable[[], _VT],
                 map: Mapping[_KT, _VT]) -> None: ...
    @overload
    def __init__(self, default_factory: Callable[[], _VT],
                 iterable: Iterable[Tuple[_KT, _VT]]) -> None: ...
    # TODO __init__ keyword args

    def __missing__(self, key: _KT) -> _VT: ...
    # TODO __reversed__
