import builtins, collections, functools, itertools, math, re, string, sys, time

__all__ = [
    "cache",
    "chr",
    "collections",
    "Counter",
    "defaultdict",
    "deque",
    "enumerate",
    "filter",
    "findall",
    "functools",
    "identity",
    "it",
    "itertools",
    "L1",
    "L2",
    "list",
    "map",
    "math",
    "partial",
    "range",
    "re",
    "read",
    "reduce",
    "reversed",
    "s_hi",
    "s_lo",
    "s_num",
    "set",
    "sleep",
    "sorted",
    "str",
    "string",
    "sys",
    "time",
    "zip",
    "zip_longest"
]


def chr(i, /):
    return str(builtins.chr(i))


def findall(pattern, string, flags=0):
    return PaivList(re.findall(pattern, string, flags))


def identity(x):
    return x


def read(file):
    if hasattr(file, 'read'):
        return str(file.read())
    with open(file) as fp:
        return str(fp.read())


def reversed(sequence, /):
    if not hasattr(sequence, '__reversed__'):
        sequence = list(sequence)
    return list(builtins.reversed(sequence))


def sorted(iterable, /, *args, key=None, reverse=False):
    return PaivList(builtins.sorted(iterable, *args, key=key, reverse=reverse))


_noarg = object()

def reduce(func, iterable, initial=_noarg):
    if initial is _noarg:
        return functools.reduce(func, iterable)
    return functools.reduce(func, iterable, initial)


def L1(v):
    return builtins.abs(v.real) + builtins.abs(v.imag)


def L2(v):
    return math.sqrt(v.real * v.real + v.imag * v.imag)


class _Sequence:
    
    def all(self):
        return builtins.all(self)
    
    def any(self):
        return builtins.any(self)

    def batched(self, size):
        it = iter(self)
        def inner():
            while x := tuple(itertools.islice(it, size)):
                yield x
        return map(identity, inner())

    def enumerate(self):
        return enumerate(self)
            
    def filter(self, func):
        return filter(func, self)

    def join(self, separator):
        return str(separator.join(self))

    def len(self):
        return builtins.len(self)

    def list(self):
        return list(self)
    
    def map(self, func):
        return map(func, self)
    
    def mapl(self, func):
        return list(map(func, self))

    def max(self):
        return builtins.max(self)
    
    def min(self):
        return builtins.min(self)

    def prod(self):
        return math.prod(self)
    
    def reduce(self, func, initial=_noarg):
        return reduce(func, self, initial)

    def reversed(self):
        return reversed(self)

    def set(self):
        return set(self)
    
    def sorted(self, /, *, key=None, reverse=False):
        return sorted(self, key=key, reverse=reverse)

    def str(self):
        return builtins.str(self)
    
    def sum(self):
        return builtins.sum(self)

    def tuple(self):
        return builtins.tuple(self)

    def zip(self, *iterables, strict=False):
        return zip(self, *iterables, strict=strict)
    
    def zip_longest(self, *iterables, fillvalue=None):
        return zip_longest(self, *iterables, fillvalue=fillvalue)


class PaivEnumerate (builtins.enumerate, _Sequence):
    pass


class PaivFilter (builtins.filter, _Sequence):
    pass


class PaivList (builtins.list, _Sequence):
    pass


class PaivMap (builtins.map, _Sequence):
    pass


class PaivSet (builtins.set, _Sequence):
    pass


class PaivString (builtins.str, _Sequence):

    def __add__(self, value, /):
        return str(super().__add__(value))
    
    def __mul__(self, value, /):
        return str(super().__mul__(value))

    def add(self, value):
        return self + value

    def lower(self):
        return str(super().lower())

    def mul(self, value):
        return self * value

    def sorted(self):
        return sorted(self).join('')

    def split(self, /, sep=None, maxsplit=-1):
        return map(str, super().split(sep=sep, maxsplit=maxsplit)).list()

    def splitlines(self, /, keepends=False):
        return map(str, super().splitlines(keepends=keepends)).list()

    def strip(self, chars=None, /):
        return str(super().strip(chars))

    def upper(self):
        return str(super().upper())


class PaivRange (_Sequence):

    def __init__(self, start, stop=None, step=1, /):
        r = builtins.range(start) if stop is None else builtins.range(start, stop, step)
        self.start = r.start
        self.stop = r.stop
        self.step = r.step
        self._r = r

    def __bool__(self, /):
        return self._r.__bool__()

    def __contains__(self, key, /):
        return self._r.__contains__(key)

    def __eq__(self, value, /):
        if isinstance(value, PaivRange):
            return self._r.__eq__(value._r)
        return self._r.__eq__(value)

    def __getitem__(self, key, /):
        return self._r.__getitem__(key)

    def __hash__(self, /):
        return self._r.__hash__()
    
    def __iter__(self, /):
        return self._r.__iter__()

    def __len__(self, /):
        return self._r.__len__()

    def __ne__(self, value, /):
        if isinstance(value, PaivRange):
            return self._r.__ne__(value._r)
        return self._r.__ne__(value)

    def __repr__(self, /):
        return self._r.__repr__()

    def __reversed__(self, /):
        return self._r.__reversed__()

    def __str__(self, /):
        return self._r.__str__()

    def count(self, key, /):
        return self._r.count(key)

    def index(self, key, /):
        return self._r.index(key)

    def isdisjoint(self, value, /):
        assert self.step == 1 == value.step
        return self.stop <= value.start or self.start >= value.stop

    def issubset(self, value, /):
        assert self.step == 1 == value.step
        return self.start >= value.start and self.stop <= value.stop

    def issuperset(self, value, /):
        assert self.step == 1 == value.step
        return self.start <= value.start and self.stop >= value.stop

    def intersection(self, value, /):
        if self.isdisjoint(value):
            return None
        return range(max(self.start, value.start), min(self.stop, value.stop))

    def intersect(self, value, /):
        return self.intersection(value)

    def difference(self, value, /):
        if self.start <= value.start:
            if self.stop <= value.start:
                return (self, value)
            return (range(self.start, value.start), range(value.stop, self.stop))
        else:
            if value.stop <= self.start:
                return (value, self)
            return (range(value.start, self.start), range(self.stop, value.stop))

    def union(self, value, /):
        assert self.step == 1 == value.step
        if self.stop < value.start or self.start > value.stop:
            return None
        return range(min(self.start, value.start), max(self.stop, value.stop))


class PaivZip (builtins.zip, _Sequence):
    pass


class PaivZipLongest (itertools.zip_longest, _Sequence):
    pass


cache = functools.cache
Counter = collections.Counter
defaultdict = collections.defaultdict
deque = collections.deque
enumerate = PaivEnumerate
filter = PaivFilter
it = itertools
list = PaivList
map = PaivMap
partial = functools.partial
range = PaivRange
set = PaivSet
str = PaivString
sleep = time.sleep
zip = PaivZip
zip_longest = PaivZipLongest
s_hi = str(string.ascii_uppercase)
s_lo = str(string.ascii_lowercase)
s_num = str(string.digits)