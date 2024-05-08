from __future__ import annotations


import builtins
from typing import Any, Callable, Literal, NamedTuple, Optional, Sequence, TypeVar, Union, overload

from jax._src import core as _core
from jax._src import dtypes as _dtypes
from jax._src.lax.lax import PrecisionLike
from jax._src.lax.slicing import GatherScatterMode
from jax._src.lib import Device
from jax._src.numpy.index_tricks import _Mgrid, _Ogrid, CClass as _CClass, RClass as _RClass
from jax._src.typing import (
    Array, ArrayLike, DType, DTypeLike,
    DimSize, DuckTypedArray, Shape, DeprecatedArg
)
from jax.numpy import fft as fft, linalg as linalg
from jax.sharding import Sharding as _Sharding
import numpy as _np

_T = TypeVar('_T')

_Axis = Union[None, int, Sequence[int]]

_Device = Device

ComplexWarning: type

_deprecations: dict[str, tuple[str, Any]]
def abs(x: ArrayLike, /) -> Array: ...
def absolute(x: ArrayLike, /) -> Array: ...
def acos(x: ArrayLike, /) -> Array: ...
def acosh(x: ArrayLike, /) -> Array: ...
def add(x: ArrayLike, y: ArrayLike, /) -> Array: ...
def amax(a: ArrayLike, axis: _Axis = ..., out: None = ...,
        keepdims: builtins.bool = ..., initial: Optional[ArrayLike] = ...,
        where: Optional[ArrayLike] = ...) -> Array: ...
def amin(a: ArrayLike, axis: _Axis = ..., out: None = ...,
        keepdims: builtins.bool = ..., initial: Optional[ArrayLike] = ...,
        where: Optional[ArrayLike] = ...) -> Array: ...
def all(a: ArrayLike, axis: _Axis = ..., out: None = ...,
        keepdims: builtins.bool = ..., *, where: Optional[ArrayLike] = ...) -> Array: ...
def allclose(a: ArrayLike, b: ArrayLike, rtol: ArrayLike = ...,
             atol: ArrayLike = ..., equal_nan: builtins.bool = ...) -> Array: ...
alltrue = all
def angle(z: ArrayLike, deg: builtins.bool = ...) -> Array: ...
def any(a: ArrayLike, axis: _Axis = ..., out: None = ...,
        keepdims: builtins.bool = ..., *, where: Optional[ArrayLike] = ...) -> Array: ...
def append(
    arr: ArrayLike, values: ArrayLike, axis: Optional[int] = ...
) -> Array: ...
def apply_along_axis(func1d: Callable, axis: int, arr: ArrayLike, *args,
                     **kwargs) -> Array: ...
def apply_over_axes(
    func: Callable, a: ArrayLike, axes: Sequence[int]
) -> Array: ...
def arange(
    start: DimSize,
    stop: Optional[DimSize] = ...,
    step: Optional[DimSize] = ...,
    dtype: Optional[DTypeLike] = ...,
) -> Array: ...
def arccos(x: ArrayLike, /) -> Array: ...
def arccosh(x: ArrayLike, /) -> Array: ...
def arcsin(x: ArrayLike, /) -> Array: ...
def arcsinh(x: ArrayLike, /) -> Array: ...
def arctan(x: ArrayLike, /) -> Array: ...
def arctan2(x: ArrayLike, y: ArrayLike, /) -> Array: ...
def arctanh(x: ArrayLike, /) -> Array: ...
def argmax(
    a: ArrayLike,
    axis: Optional[int] = ...,
    out: None = ...,
    keepdims: Optional[builtins.bool] = ...,
) -> Array: ...
def argmin(
    a: ArrayLike,
    axis: Optional[int] = ...,
    out: None = ...,
    keepdims: Optional[builtins.bool] = ...,
) -> Array: ...
def argpartition(a: ArrayLike, kth: int, axis: int = ...) -> Array: ...
def argsort(
    a: ArrayLike,
    axis: Optional[int] = ...,
    *,
    stable: builtins.bool = ...,
    descending: builtins.bool = ...,
    kind: str | None = ...,
    order: None = ...,
) -> Array: ...
def argwhere(
    a: ArrayLike,
    *,
    size: Optional[int] = ...,
    fill_value: Optional[ArrayLike] = ...,
) -> Array: ...
around = round
def array(object: Any, dtype: DTypeLike | None = ..., copy: builtins.bool = True,
          order: str | None = ..., ndmin: int = ...) -> Array: ...
def array_equal(
    a1: ArrayLike, a2: ArrayLike, equal_nan: builtins.bool = ...
) -> Array: ...
def array_equiv(a1: ArrayLike, a2: ArrayLike) -> Array: ...
array_repr = _np.array_repr
def array_split(
    ary: ArrayLike,
    indices_or_sections: Union[int, Sequence[int], ArrayLike],
    axis: int = ...,
) -> list[Array]: ...
array_str = _np.array_str
def asarray(
    a: Any, dtype: Optional[DTypeLike] = ..., order: Optional[str] = ...,
    *, copy: Optional[builtins.bool] = ...
) -> Array: ...
def asin(x: ArrayLike, /) -> Array: ...
def asinh(x: ArrayLike, /) -> Array: ...
def astype(a: ArrayLike, dtype: Optional[DTypeLike], /, *, copy: builtins.bool = ..., device: _Device | _Sharding | None = ...) -> Array: ...
def atan(x: ArrayLike, /) -> Array: ...
def atan2(x: ArrayLike, y: ArrayLike, /) -> Array: ...
def atanh(x: ArrayLike, /) -> Array: ...
@overload
def atleast_1d() -> list[Array]: ...
@overload
def atleast_1d(x: ArrayLike, /) -> Array: ...
@overload
def atleast_1d(x: ArrayLike, y: ArrayLike, /, *arys: ArrayLike) -> list[Array]: ...

@overload
def atleast_2d() -> list[Array]: ...
@overload
def atleast_2d(x: ArrayLike, /) -> Array: ...
@overload
def atleast_2d(x: ArrayLike, y: ArrayLike, /, *arys: ArrayLike) -> list[Array]: ...

@overload
def atleast_3d() -> list[Array]: ...
@overload
def atleast_3d(x: ArrayLike, /) -> Array: ...
@overload
def atleast_3d(x: ArrayLike, y: ArrayLike, /, *arys: ArrayLike) -> list[Array]: ...

@overload
def average(a: ArrayLike, axis: _Axis = ..., weights: Optional[ArrayLike] = ...,
            returned: Literal[False] = False, keepdims: builtins.bool = False) -> Array: ...
@overload
def average(a: ArrayLike, axis: _Axis = ..., weights: Optional[ArrayLike] = ..., *,
            returned: Literal[True], keepdims: builtins.bool = False) -> tuple[Array, Array]: ...
@overload
def average(a: ArrayLike, axis: _Axis = ..., weights: Optional[ArrayLike] = ...,
            returned: builtins.bool = False, keepdims: builtins.bool = False) -> Union[Array, tuple[Array, Array]]: ...

def bartlett(M: int) -> Array: ...
bfloat16: Any
def bincount(x: ArrayLike, weights: Optional[ArrayLike] = ...,
             minlength: int = ..., *, length: Optional[int] = ...) -> Array: ...
def bitwise_and(x: ArrayLike, y: ArrayLike, /) -> Array: ...
def bitwise_count(x: ArrayLike, /) -> Array: ...
def bitwise_invert(x: ArrayLike, /) -> Array: ...
def bitwise_left_shift(x: ArrayLike, y: ArrayLike, /) -> Array: ...
def bitwise_not(x: ArrayLike, /) -> Array: ...
def bitwise_or(x: ArrayLike, y: ArrayLike, /) -> Array: ...
def bitwise_right_shift(x: ArrayLike, y: ArrayLike, /) -> Array: ...
def bitwise_xor(x: ArrayLike, y: ArrayLike, /) -> Array: ...
def blackman(M: int) -> Array: ...
def block(arrays: Union[ArrayLike, Sequence[ArrayLike], Sequence[Sequence[ArrayLike]]]) -> Array: ...
bool: Any
bool_: Any
def broadcast_arrays(*args: ArrayLike) -> list[Array]: ...

@overload
def broadcast_shapes(*shapes: Sequence[int]) -> tuple[int, ...]: ...

@overload
def broadcast_shapes(*shapes: Sequence[Union[int, _core.Tracer]]
                     ) -> tuple[Union[int, _core.Tracer], ...]: ...

def broadcast_to(array: ArrayLike, shape: DimSize | Shape) -> Array: ...
c_: _CClass
can_cast = _np.can_cast
def cbrt(x: ArrayLike, /) -> Array: ...
cdouble: Any
def ceil(x: ArrayLike, /) -> Array: ...
character = _np.character
def choose(a: ArrayLike, choices: Sequence[ArrayLike],
           out: None = ..., mode: str = ...) -> Array: ...
def clip(
    x: ArrayLike | None = ...,
    /,
    min: Optional[ArrayLike] = ...,
    max: Optional[ArrayLike] = ...,
    a: ArrayLike | DeprecatedArg | None = ...,
    a_min: ArrayLike | DeprecatedArg | None = ...,
    a_max: ArrayLike | DeprecatedArg | None = ...
) -> Array: ...
def column_stack(
    tup: Union[_np.ndarray, Array, Sequence[ArrayLike]]
) -> Array: ...
complex128: Any
complex64: Any
complex_: Any
complexfloating = _np.complexfloating
def compress(condition: ArrayLike, a: ArrayLike, axis: Optional[int] = ...,
             out: None = ...) -> Array: ...
def concat(arrays: Sequence[ArrayLike], /, *, axis: int | None = 0) -> Array: ...
def concatenate(
    arrays: Union[_np.ndarray, Array, Sequence[ArrayLike]],
    axis: Optional[int] = ...,
    dtype: Optional[DTypeLike] = ...,
) -> Array: ...
def conjugate(x: ArrayLike, /) -> Array: ...
conj = conjugate
def convolve(a: ArrayLike, v: ArrayLike, mode: str = ..., *,
             precision: PrecisionLike = ...,
             preferred_element_type: Optional[DTypeLike] = ...) -> Array: ...
def copy(a: ArrayLike, order: Optional[str] = ...) -> Array: ...
def copysign(x: ArrayLike, y: ArrayLike, /) -> Array: ...
def corrcoef(x: ArrayLike, y: Optional[ArrayLike] = ..., rowvar: builtins.bool = ...) -> Array: ...
def correlate(a: ArrayLike, v: ArrayLike, mode: str = ..., *,
              precision: PrecisionLike = ...,
              preferred_element_type: Optional[DTypeLike] = ...) -> Array: ...
def cos(x: ArrayLike, /) -> Array: ...
def cosh(x: ArrayLike, /) -> Array: ...
def count_nonzero(a: ArrayLike, axis: _Axis = ...,
                  keepdims: builtins.bool = ...) -> Array: ...
def cov(m: ArrayLike, y: Optional[ArrayLike] = ..., rowvar: builtins.bool = ...,
        bias: builtins.bool = ..., ddof: Optional[int] = ...,
        fweights: Optional[ArrayLike] = ...,
        aweights: Optional[ArrayLike] = ...) -> Array: ...
def cross(
    a: ArrayLike,
    b: ArrayLike,
    axisa: int = -1,
    axisb: int = -1,
    axisc: int = -1,
    axis: Optional[int] = ...,
) -> Array: ...
csingle: Any
def cumprod(a: ArrayLike, axis: _Axis = ..., dtype: DTypeLike = ...,
            out: None = ...) -> Array: ...
cumproduct = cumprod
def cumsum(a: ArrayLike, axis: _Axis = ..., dtype: DTypeLike = ...,
           out: None = ...) -> Array: ...
def cumulative_sum(x: ArrayLike, /, *, axis: int | None = ...,
                   dtype: DTypeLike | None = ...,
                   include_initial: bool = ...) -> Array: ...

def deg2rad(x: ArrayLike, /) -> Array: ...
degrees = rad2deg
def delete(
    arr: ArrayLike,
    obj: Union[ArrayLike, slice],
    axis: Optional[int] = ...,
    *,
    assume_unique_indices: builtins.bool = ...,
) -> Array: ...
def diag(v: ArrayLike, k: int = 0) -> Array: ...
def diag_indices(n: int, ndim: int = ...) -> tuple[Array, ...]: ...
def diag_indices_from(arr: ArrayLike) -> tuple[Array, ...]: ...
def diagflat(v: ArrayLike, k: int = 0) -> Array: ...
def diagonal(
    a: ArrayLike, offset: ArrayLike = ..., axis1: int = ..., axis2: int = ...
): ...
def diff(a: ArrayLike, n: int = ..., axis: int = ...,
         prepend: Optional[ArrayLike] = ...,
         append: Optional[ArrayLike] = ...) -> Array: ...
def digitize(x: ArrayLike, bins: ArrayLike, right: builtins.bool = ...) -> Array: ...
divide = true_divide
def divmod(x: ArrayLike, y: ArrayLike, /) -> tuple[Array, Array]: ...
def dot(
    a: ArrayLike, b: ArrayLike, *, precision: PrecisionLike = ...,
    preferred_element_type: Optional[DTypeLike] = ...) -> Array: ...
double: Any
def dsplit(
    ary: ArrayLike, indices_or_sections: Union[int, ArrayLike]
) -> list[Array]: ...

def dstack(tup: Union[_np.ndarray, Array, Sequence[ArrayLike]],
           dtype: Optional[DTypeLike] = ...) -> Array: ...
dtype = _np.dtype
e: float
def ediff1d(ary: ArrayLike, to_end: Optional[ArrayLike] = ...,
            to_begin: Optional[ArrayLike] = ...) -> Array: ...
@overload
def einsum(
    subscript: str, /,
    *operands: ArrayLike,
    out: None = ...,
    optimize: Union[str, builtins.bool] = "optimal",
    precision: PrecisionLike = ...,
    preferred_element_type: Optional[DTypeLike] = ...,
    _use_xeinsum: builtins.bool = False,
    _dot_general: Callable[..., Array] = ...,
) -> Array: ...

@overload
def einsum(
    arr: ArrayLike,
    axes: Sequence[Any], /,
    *operands: Union[ArrayLike, Sequence[Any]],
    out: None = ...,
    optimize: Union[str, builtins.bool] = "optimal",
    precision: PrecisionLike = ...,
    preferred_element_type: Optional[DTypeLike] = ...,
    _use_xeinsum: builtins.bool = False,
    _dot_general: Callable[..., Array] = ...,
) -> Array: ...
@overload
def einsum(
    subscripts, /,
    *operands,
    out: None = ...,
    optimize: Union[str, builtins.bool] = ...,
    precision: PrecisionLike = ...,
    preferred_element_type: Optional[DTypeLike] = ...,
    _use_xeinsum: builtins.bool = ...,
    _dot_general: Callable[..., Array] = ...,
) -> Array: ...

def einsum_path(subscripts, *operands, optimize =  ...): ...
def empty(shape: Any, dtype: Optional[DTypeLike] = ...,
          device: Optional[Union[_Device, _Sharding]] = ...) -> Array: ...
def empty_like(prototype: Union[ArrayLike, DuckTypedArray],
               dtype: Optional[DTypeLike] = ...,
               shape: Any = ..., *,
               device: Optional[Union[_Device, _Sharding]] = ...) -> Array: ...
def equal(x: ArrayLike, y: ArrayLike, /) -> Array: ...
euler_gamma: float
def exp(x: ArrayLike, /) -> Array: ...
def exp2(x: ArrayLike, /) -> Array: ...
def expand_dims(a: ArrayLike, axis: Union[int, Sequence[int]]) -> Array: ...
def expm1(x: ArrayLike, /) -> Array: ...
def extract(condition: ArrayLike, arr: ArrayLike) -> Array: ...
def eye(N: DimSize, M: Optional[DimSize] = ..., k: int = ...,
        dtype: Optional[DTypeLike] = ...) -> Array: ...
def fabs(x: ArrayLike, /) -> Array: ...
finfo = _dtypes.finfo
def fix(x: ArrayLike, out: None = ...) -> Array: ...
def flatnonzero(
    a: ArrayLike,
    *,
    size: Optional[int] = ...,
    fill_value: Union[None, ArrayLike, tuple[ArrayLike]] = ...,
) -> Array: ...
flexible = _np.flexible
def flip(
    m: ArrayLike, axis: Optional[Union[int, Sequence[int]]] = ...
) -> Array: ...

def fliplr(m: ArrayLike) -> Array: ...
def flipud(m: ArrayLike) -> Array: ...
float16: Any
float32: Any
float64: Any
float8_e4m3b11fnuz: Any
float8_e4m3fn: Any
float8_e4m3fnuz: Any
float8_e5m2: Any
float8_e5m2fnuz: Any
float_: Any
def float_power(x: ArrayLike, y: ArrayLike, /) -> Array: ...
floating = _np.floating
def floor(x: ArrayLike, /) -> Array: ...
def floor_divide(x: ArrayLike, y: ArrayLike, /) -> Array: ...
def fmax(x: ArrayLike, y: ArrayLike, /) -> Array: ...
def fmin(x: ArrayLike, y: ArrayLike, /) -> Array: ...
def fmod(x: ArrayLike, y: ArrayLike, /) -> Array: ...
def frexp(x: ArrayLike, /) -> tuple[Array, Array]: ...
def from_dlpack(x: Any, /, *, device: _Device | _Sharding | None = None,
                copy: builtins.bool | None = None) -> Array: ...
def frombuffer(buffer: Union[bytes, Any], dtype: DTypeLike = ...,
               count: int = ..., offset: int = ...) -> Array: ...
def fromfile(*args, **kwargs): ...
def fromfunction(function: Callable[..., Array], shape: Any,
                 *, dtype: DTypeLike = ..., **kwargs) -> Array: ...
def fromiter(*args, **kwargs): ...
def fromstring(
    string: str, dtype: DTypeLike = ..., count: int = ..., *, sep: str
) -> Array: ...
def full(shape: Any, fill_value: ArrayLike,
         dtype: Optional[DTypeLike] = ..., *,
         device: Optional[Union[_Device, _Sharding]] = ...) -> Array: ...
def full_like(a: Union[ArrayLike, DuckTypedArray],
              fill_value: ArrayLike, dtype: Optional[DTypeLike] = ...,
              shape: Any = ..., *,
              device: Optional[Union[_Device, _Sharding]] = ...) -> Array: ...
def gcd(x1: ArrayLike, x2: ArrayLike) -> Array: ...
generic = _np.generic
def geomspace(
    start: ArrayLike,
    stop: ArrayLike,
    num: int = ...,
    endpoint: builtins.bool = ...,
    dtype: Optional[DTypeLike] = ...,
    axis: int = ...,
) -> Array: ...
get_printoptions = _np.get_printoptions
def gradient(f: ArrayLike, *varargs: ArrayLike,
             axis: Optional[Union[int, Sequence[int]]] = ...,
             edge_order: Optional[int] = ...) -> Union[Array, list[Array]]: ...
def greater(x: ArrayLike, y: ArrayLike, /) -> Array: ...
def greater_equal(x: ArrayLike, y: ArrayLike, /) -> Array: ...
def hamming(M: int) -> Array: ...
def hanning(M: int) -> Array: ...
def heaviside(x: ArrayLike, y: ArrayLike, /) -> Array: ...
def histogram(a: ArrayLike, bins: ArrayLike = ...,
              range: Optional[Sequence[ArrayLike]] = ...,
              weights: Optional[ArrayLike] = ...,
              density: Optional[builtins.bool] = ...) -> tuple[Array, Array]: ...
def histogram2d(
    x: ArrayLike,
    y: ArrayLike,
    bins: Union[ArrayLike, Sequence[ArrayLike]] = ...,
    range: Optional[Sequence[Union[None, Array, Sequence[ArrayLike]]]] = ...,
    weights: Optional[ArrayLike] = ...,
    density: Optional[builtins.bool] = ...,
) -> tuple[Array, Array, Array]: ...
def histogram_bin_edges(a: ArrayLike, bins: ArrayLike = ...,
                        range: Union[None, Array, Sequence[ArrayLike]] = ...,
                        weights: Optional[ArrayLike] = ...) -> Array: ...
def histogramdd(
    sample: ArrayLike,
    bins: Union[ArrayLike, Sequence[ArrayLike]] = ...,
    range: Optional[Sequence[Union[None, Array, Sequence[ArrayLike]]]] = ...,
    weights: Optional[ArrayLike] = ...,
    density: Optional[builtins.bool] = ...,
) -> tuple[Array, list[Array]]: ...
def hsplit(
    ary: ArrayLike, indices_or_sections: Union[int, ArrayLike]
) -> list[Array]: ...
def hstack(tup: Union[_np.ndarray, Array, Sequence[ArrayLike]],
           dtype: Optional[DTypeLike] = ...) -> Array: ...
def hypot(x: ArrayLike, y: ArrayLike, /) -> Array: ...
def i0(x: ArrayLike) -> Array: ...
def identity(n: DimSize, dtype: Optional[DTypeLike] = ...) -> Array: ...
iinfo = _dtypes.iinfo
def imag(x: ArrayLike, /) -> Array: ...
index_exp = _np.index_exp

@overload
def indices(dimensions: Sequence[int], dtype: DTypeLike = int32,
            sparse: Literal[False] = False) -> Array: ...
@overload
def indices(dimensions: Sequence[int], dtype: DTypeLike = int32,
            *, sparse: Literal[True]) -> tuple[Array, ...]: ...
@overload
def indices(dimensions: Sequence[int], dtype: DTypeLike = int32,
            sparse: builtins.bool = False) -> Union[Array, tuple[Array, ...]]: ...

inexact = _np.inexact
inf: float
def inner(
    a: ArrayLike, b: ArrayLike, *, precision: PrecisionLike = ...,
    preferred_element_type: Optional[DTypeLike] = ...) -> Array: ...
def insert(arr: ArrayLike, obj: Union[ArrayLike, slice], values: ArrayLike,
           axis: Optional[int] = ...) -> Array: ...
int16: Any
int32: Any
int4: Any
int64: Any
int8: Any
int_: Any
integer = _np.integer
def interp(x: ArrayLike, xp: ArrayLike, fp: ArrayLike,
           left: Union[ArrayLike, str, None] = ...,
           right: Union[ArrayLike, str, None] = ...,
           period: Optional[ArrayLike] = ...) -> Array: ...
def intersect1d(ar1: ArrayLike, ar2: ArrayLike, assume_unique: builtins.bool = ...,
                return_indices: builtins.bool = ...) -> Union[Array, tuple[Array, Array, Array]]: ...
def invert(x: ArrayLike, /) -> Array: ...
def isclose(a: ArrayLike, b: ArrayLike, rtol: ArrayLike = ...,
            atol: ArrayLike = ..., equal_nan: builtins.bool = ...) -> Array: ...
def iscomplex(m: ArrayLike) -> Array: ...
def iscomplexobj(x: Any) -> builtins.bool: ...
def isdtype(dtype: DTypeLike, kind: Union[DType, str, tuple[Union[DType, str], ...]]) -> builtins.bool: ...
def isfinite(x: ArrayLike, /) -> Array: ...
def isin(element: ArrayLike, test_elements: ArrayLike,
         assume_unique: builtins.bool = ..., invert: builtins.bool = ...) -> Array: ...
def isinf(x: ArrayLike, /) -> Array: ...
def isnan(x: ArrayLike, /) -> Array: ...
def isneginf(x: ArrayLike, /) -> Array: ...
def isposinf(x: ArrayLike, /) -> Array: ...
def isreal(m: ArrayLike) -> Array: ...
def isrealobj(x: Any) -> builtins.bool: ...
def isscalar(element: Any) -> builtins.bool: ...
def issubdtype(arg1: DTypeLike, arg2: DTypeLike) -> builtins.bool: ...
iterable = _np.iterable
def ix_(*args: ArrayLike) -> tuple[Array, ...]: ...
def kaiser(M: int, beta: ArrayLike) -> Array: ...
def kron(a: ArrayLike, b: ArrayLike) -> Array: ...
def lcm(x1: ArrayLike, x2: ArrayLike) -> Array: ...
def ldexp(x: ArrayLike, y: ArrayLike, /) -> Array: ...
def left_shift(x: ArrayLike, y: ArrayLike, /) -> Array: ...
def less(x: ArrayLike, y: ArrayLike, /) -> Array: ...
def less_equal(x: ArrayLike, y: ArrayLike, /) -> Array: ...
def lexsort(keys: Sequence[ArrayLike], axis: int = ...) -> Array: ...

@overload
def linspace(start: ArrayLike, stop: ArrayLike, num: int = 50,
             endpoint: builtins.bool = True, retstep: Literal[False] = False,
             dtype: Optional[DTypeLike] = ...,
             axis: int = 0) -> Array: ...
@overload
def linspace(start: ArrayLike, stop: ArrayLike, num: int,
             endpoint: builtins.bool, retstep: Literal[True],
             dtype: Optional[DTypeLike] = ...,
             axis: int = 0) -> tuple[Array, Array]: ...
@overload
def linspace(start: ArrayLike, stop: ArrayLike, num: int = 50,
             endpoint: builtins.bool = True, *, retstep: Literal[True],
             dtype: Optional[DTypeLike] = ...,
             axis: int = 0) -> tuple[Array, Array]: ...
@overload
def linspace(start: ArrayLike, stop: ArrayLike, num: int = 50,
             endpoint: builtins.bool = True, retstep: builtins.bool = False,
             dtype: Optional[DTypeLike] = ...,
             axis: int = 0) -> Union[Array, tuple[Array, Array]]: ...

def load(*args: Any, **kwargs: Any) -> Array: ...
def log(x: ArrayLike, /) -> Array: ...
def log10(x: ArrayLike, /) -> Array: ...
def log1p(x: ArrayLike, /) -> Array: ...
def log2(x: ArrayLike, /) -> Array: ...
def logaddexp(x: ArrayLike, y: ArrayLike, /) -> Array: ...
def logaddexp2(x: ArrayLike, y: ArrayLike, /) -> Array: ...
def logical_and(x: ArrayLike, y: ArrayLike, /) -> Array: ...
def logical_not(x: ArrayLike, /) -> Array: ...
def logical_or(x: ArrayLike, y: ArrayLike, /) -> Array: ...
def logical_xor(x: ArrayLike, y: ArrayLike, /) -> Array: ...
def logspace(start: ArrayLike, stop: ArrayLike, num: int = ...,
             endpoint: builtins.bool = ..., base: ArrayLike = ...,
             dtype: Optional[DTypeLike] = ..., axis: int = ...) -> Array: ...
def mask_indices(
    n: int, mask_func: Callable, k: int = ...
) -> tuple[Array, ...]: ...
def matmul(
    a: ArrayLike, b: ArrayLike, *, precision: PrecisionLike = ...,
    preferred_element_type: Optional[DTypeLike] = ...) -> Array: ...
def matrix_transpose(x: ArrayLike, /) -> Array: ...
max = amax
def maximum(x: ArrayLike, y: ArrayLike, /) -> Array: ...
def mean(a: ArrayLike, axis: _Axis = ..., dtype: DTypeLike = ...,
         out: None = ..., keepdims: builtins.bool = ..., *,
         where: Optional[ArrayLike] = ...) -> Array: ...
def median(a: ArrayLike, axis: Optional[Union[int, tuple[int, ...]]] = ...,
           out: None = ..., overwrite_input: builtins.bool = ...,
           keepdims: builtins.bool = ...) -> Array: ...
def meshgrid(*xi: ArrayLike, copy: builtins.bool = ..., sparse: builtins.bool = ...,
             indexing: str = ...) -> list[Array]: ...
mgrid: _Mgrid
min = amin
def minimum(x: ArrayLike, y: ArrayLike, /) -> Array: ...
def mod(x: ArrayLike, y: ArrayLike, /) -> Array: ...
def modf(x: ArrayLike, /, out=None) -> tuple[Array, Array]: ...
def moveaxis(a: ArrayLike, source: Union[int, Sequence[int]],
             destination: Union[int, Sequence[int]]) -> Array: ...
def multiply(x: ArrayLike, y: ArrayLike, /) -> Array: ...
nan: float
def nan_to_num(x: ArrayLike, copy: builtins.bool = ..., nan: ArrayLike = ...,
               posinf: Optional[ArrayLike] = ...,
               neginf: Optional[ArrayLike] = ...) -> Array: ...
def nanargmax(
    a: ArrayLike,
    axis: Optional[int] = ...,
    out: None = ...,
    keepdims: Optional[builtins.bool] = ...,
) -> Array: ...
def nanargmin(
    a: ArrayLike,
    axis: Optional[int] = ...,
    out: None = ...,
    keepdims: Optional[builtins.bool] = ...,
) -> Array: ...
def nancumprod(a: ArrayLike, axis: _Axis = ..., dtype: DTypeLike = ...,
               out: None = ...) -> Array: ...
def nancumsum(a: ArrayLike, axis: _Axis = ..., dtype: DTypeLike = ...,
               out: None = ...) -> Array: ...
def nanmax(a: ArrayLike, axis: _Axis = ..., out: None = ...,
           keepdims: builtins.bool = ..., initial: Optional[ArrayLike] = ...,
           where: Optional[ArrayLike] = ...) -> Array: ...
def nanmean(a: ArrayLike, axis: _Axis = ..., dtype: DTypeLike = ...,
            out: None = ...,
            keepdims: builtins.bool = ...,
            where: Optional[ArrayLike] = ...) -> Array: ...
def nanmedian(a: ArrayLike, axis: Optional[Union[int, tuple[int, ...]]] = ...,
              out: None = ..., overwrite_input: builtins.bool = ...,
              keepdims: builtins.bool = ...) -> Array: ...
def nanmin(a: ArrayLike, axis: _Axis = ..., out: None = ...,
           keepdims: builtins.bool = ..., initial: Optional[ArrayLike] = ...,
           where: Optional[ArrayLike] = ...) -> Array: ...
def nanpercentile(a: ArrayLike, q: ArrayLike,
                  axis: Optional[Union[int, tuple[int, ...]]] = ...,
                  out: None = ..., overwrite_input: builtins.bool = ..., method: str = ...,
                  keepdims: builtins.bool = ..., interpolation: None = ...) -> Array: ...
def nanprod(a: ArrayLike, axis: _Axis = ..., dtype: DTypeLike = ...,
            out: None = ...,
            keepdims: builtins.bool = ..., initial: Optional[ArrayLike] = ...,
            where: Optional[ArrayLike] = ...) -> Array: ...
def nanquantile(a: ArrayLike, q: ArrayLike, axis: Optional[Union[int, tuple[int, ...]]] = ...,
                out: None = ..., overwrite_input: builtins.bool = ..., method: str = ...,
                keepdims: builtins.bool = ..., interpolation: None = ...) -> Array: ...
def nanstd(a: ArrayLike, axis: _Axis = ..., dtype: DTypeLike = ..., out: None = ...,
           ddof: int = ..., keepdims: builtins.bool = ...,
           where: Optional[ArrayLike] = ...) -> Array: ...
def nansum(a: ArrayLike, axis: _Axis = ..., dtype: DTypeLike = ...,
           out: None = ..., keepdims: builtins.bool = ...,
           initial: Optional[ArrayLike] = ...,
           where: Optional[ArrayLike] = ...) -> Array: ...
def nanvar(a: ArrayLike, axis: _Axis = ..., dtype: DTypeLike = ...,
           out: None = ...,
           ddof: int = 0, keepdims: builtins.bool = False,
           where: Optional[ArrayLike] = ...) -> Array: ...
ndarray = Array
ndim = _np.ndim
def negative(x: ArrayLike, /) -> Array: ...
newaxis = ...
def nextafter(x: ArrayLike, y: ArrayLike, /) -> Array: ...
def nonzero(a: ArrayLike, *, size: Optional[int] = ...,
            fill_value: Union[None, ArrayLike, tuple[ArrayLike, ...]] = ...
    ) -> tuple[Array, ...]: ...
def not_equal(x: ArrayLike, y: ArrayLike, /) -> Array: ...
number = _np.number
object_ = _np.object_
ogrid: _Ogrid
def ones(shape: Any, dtype: Optional[DTypeLike] = ...,
         device: Optional[Union[_Device, _Sharding]] = ...) -> Array: ...
def ones_like(a: Union[ArrayLike, DuckTypedArray],
              dtype: Optional[DTypeLike] = ...,
              shape: Any = ..., *,
              device: Optional[Union[_Device, _Sharding]] = ...) -> Array: ...
def outer(a: ArrayLike, b: Array, out: None = ...) -> Array: ...
def packbits(
    a: ArrayLike, axis: Optional[int] = ..., bitorder: str = ...
) -> Array: ...

PadValueLike = Union[_T, Sequence[_T], Sequence[Sequence[_T]]]
def pad(array: ArrayLike, pad_width: PadValueLike[int | Array | _np.ndarray],
        mode: Union[str, Callable[..., Any]] = ..., **kwargs) -> Array: ...

def partition(a: ArrayLike, kth: int, axis: int = ...) -> Array: ...
def percentile(a: ArrayLike, q: ArrayLike,
               axis: Optional[Union[int, tuple[int, ...]]] = ...,
               out: None = ..., overwrite_input: builtins.bool = ..., method: str = ...,
               keepdims: builtins.bool = ..., interpolation: None = ...) -> Array: ...
def permute_dims(x: ArrayLike, /, axes: tuple[int, ...]) -> Array: ...
pi: float
def piecewise(x: ArrayLike, condlist: Union[Array, Sequence[ArrayLike]],
              funclist: Sequence[Union[ArrayLike, Callable[..., Array]]],
              *args, **kw) -> Array: ...
def place(arr: ArrayLike, mask: ArrayLike, vals: ArrayLike, *,
          inplace: builtins.bool = ...) -> Array: ...
def poly(seq_of_zeros: Array) -> Array: ...
def polyadd(a1: Array, a2: Array) -> Array: ...
def polyder(p: Array, m: int = ...) -> Array: ...
def polydiv(u: ArrayLike, v: ArrayLike, *, trim_leading_zeros: builtins.bool = ...) -> tuple[Array, Array]: ...
def polyfit(x: Array, y: Array, deg: int, rcond: Optional[float] = ...,
            full: builtins.bool = ..., w: Optional[Array] = ..., cov: builtins.bool = ...
            ) -> Union[Array, tuple[Array, ...]]: ...
def polyint(p: Array, m: int = ..., k: Optional[int] = ...) -> Array: ...
def polymul(a1: ArrayLike, a2: ArrayLike, *, trim_leading_zeros: builtins.bool = ...) -> Array: ...
def polysub(a1: Array, a2: Array) -> Array: ...
def polyval(p: Array, x: Array, *, unroll: int = ...) -> Array: ...
def positive(x: ArrayLike, /) -> Array: ...
def pow(x: ArrayLike, y: ArrayLike, /) -> Array: ...
def power(x: ArrayLike, y: ArrayLike, /) -> Array: ...
printoptions = _np.printoptions
def prod(a: ArrayLike, axis: _Axis = ..., dtype: DTypeLike = ...,
         out: None = ..., keepdims: builtins.bool = ...,
         initial: Optional[ArrayLike] = ..., where: Optional[ArrayLike] = ...,
         promote_integers: builtins.bool = ...) -> Array: ...
product = prod
promote_types = _np.promote_types
def ptp(a: ArrayLike, axis: _Axis = ..., out: None = ...,
        keepdims: builtins.bool = ...) -> Array: ...
def put(a: ArrayLike, ind: ArrayLike, v: ArrayLike,
        mode: str | None = ..., *, inplace: builtins.bool = ...) -> Array: ...
def quantile(a: ArrayLike, q: ArrayLike, axis: Optional[Union[int, tuple[int, ...]]] = ...,
             out: None = ..., overwrite_input: builtins.bool = ..., method: str = ...,
             keepdims: builtins.bool = ..., interpolation: None = ...) -> Array: ...
r_: _RClass
def rad2deg(x: ArrayLike, /) -> Array: ...
radians = deg2rad
def ravel(a: ArrayLike, order: str = ...) -> Array: ...
def ravel_multi_index(multi_index: Sequence[ArrayLike], dims: Sequence[int],
                      mode: str = ..., order: str = ...) -> Array: ...
def real(x: ArrayLike, /) -> Array: ...
def reciprocal(x: ArrayLike, /) -> Array: ...
register_jax_array_methods: Any
def remainder(x: ArrayLike, y: ArrayLike, /) -> Array: ...
def repeat(a: ArrayLike, repeats: ArrayLike, axis: Optional[int] = ..., *,
           total_repeat_length: Optional[int] = ...) -> Array: ...
def reshape(
    a: ArrayLike, newshape: Union[DimSize, Shape], order: str = ...
) -> Array: ...

def resize(a: ArrayLike, new_shape: Shape) -> Array: ...
def result_type(*args: Any) -> DType: ...
def right_shift(x: ArrayLike, y: ArrayLike, /) -> Array: ...
def rint(x: ArrayLike, /) -> Array: ...
def roll(a: ArrayLike, shift: Union[ArrayLike, Sequence[int]],
         axis: Optional[Union[int, Sequence[int]]] = ...) -> Array: ...
def rollaxis(a: ArrayLike, axis: int, start: int = 0) -> Array: ...
def roots(p: ArrayLike, *, strip_zeros: builtins.bool = ...) -> Array: ...
def rot90(m: ArrayLike, k: int = ..., axes: tuple[int, int] = ...) -> Array: ...
def round(a: ArrayLike, decimals: int = ..., out: None = ...) -> Array: ...
round_ = round
s_ = _np.s_
save = _np.save
savez = _np.savez
def searchsorted(a: ArrayLike, v: ArrayLike, side: str = ...,
                 sorter: None = ..., *, method: str = ...) -> Array: ...
def select(
    condlist: Sequence[ArrayLike],
    choicelist: Sequence[ArrayLike],
    default: ArrayLike = ...,
) -> Array: ...
set_printoptions = _np.set_printoptions
def setdiff1d(
    ar1: ArrayLike,
    ar2: ArrayLike,
    assume_unique: builtins.bool = ...,
    *,
    size: Optional[int] = ...,
    fill_value: Optional[ArrayLike] = ...,
) -> Array: ...
def setxor1d(ar1: ArrayLike, ar2: ArrayLike, assume_unique: builtins.bool = ...) -> Array: ...
shape = _np.shape
def sign(x: ArrayLike, /) -> Array: ...
def signbit(x: ArrayLike, /) -> Array: ...
signedinteger = _np.signedinteger
def sin(x: ArrayLike, /) -> Array: ...
def sinc(x: ArrayLike, /) -> Array: ...
single: Any
def sinh(x: ArrayLike, /) -> Array: ...
size = _np.size
sometrue = any
def sort(
    a: ArrayLike,
    axis: Optional[int] = ...,
    *,
    stable: builtins.bool = ...,
    descending: builtins.bool = ...,
    kind: str | None = ...,
    order: None = ...,
) -> Array: ...
def sort_complex(a: ArrayLike) -> Array: ...
def split(
    ary: ArrayLike,
    indices_or_sections: Union[int, Sequence[int], ArrayLike],
    axis: int = ...,
) -> list[Array]: ...

def sqrt(x: ArrayLike, /) -> Array: ...
def square(x: ArrayLike, /) -> Array: ...
def squeeze(
    a: ArrayLike, axis: Optional[Union[int, Sequence[int]]] = ...
) -> Array: ...
def stack(
    arrays: Union[_np.ndarray, Array, Sequence[ArrayLike]],
    axis: int = ...,
    out: None = ...,
    dtype: Optional[DTypeLike] = ...,
) -> Array: ...
def std(a: ArrayLike, axis: _Axis = ..., dtype: DTypeLike = ...,
        out: None = ..., ddof: int = ..., keepdims: builtins.bool = ..., *,
        where: Optional[ArrayLike] = ...) -> Array: ...
def subtract(x: ArrayLike, y: ArrayLike, /) -> Array: ...
def sum(
    a: ArrayLike,
    axis: _Axis = ...,
    dtype: DTypeLike = ...,
    out: None = ...,
    keepdims: builtins.bool = ...,
    initial: Optional[ArrayLike] = ...,
    where: Optional[ArrayLike] = ...,
    promote_integers: builtins.bool = ...,
) -> Array: ...
def swapaxes(a: ArrayLike, axis1: int, axis2: int) -> Array: ...
def take(
    a: ArrayLike,
    indices: ArrayLike,
    axis: Optional[int] = ...,
    out: None = ...,
    mode: Optional[str] = ...,
    unique_indices: builtins.bool = ...,
    indices_are_sorted: builtins.bool = ...,
    fill_value: Optional[ArrayLike] = ...,
) -> Array: ...
def take_along_axis(
    arr: ArrayLike,
    indices: ArrayLike,
    axis: Optional[int],
    mode: Optional[Union[str, GatherScatterMode]] = ...,
) -> Array: ...
def tan(x: ArrayLike, /) -> Array: ...
def tanh(x: ArrayLike, /) -> Array: ...
def tensordot(a: ArrayLike, b: ArrayLike,
              axes: Union[int, Sequence[int], Sequence[Sequence[int]]] = ...,
              *, precision: PrecisionLike = ...,
              preferred_element_type: Optional[DTypeLike] = ...) -> Array: ...
def tile(A: ArrayLike, reps: Union[DimSize, Sequence[DimSize]]) -> Array: ...
def trace(a: ArrayLike, offset: int = ..., axis1: int = ..., axis2: int = ...,
          dtype: Optional[DTypeLike] = ..., out: None = ...) -> Array: ...
def transpose(a: ArrayLike, axes: Optional[Sequence[int]] = ...) -> Array: ...
def trapezoid(y: ArrayLike, x: ArrayLike | None = None, dx: ArrayLike = ...,
              axis: int = ...) -> Array: ...
def tri(
    N: int, M: Optional[int] = ..., k: int = ..., dtype: DTypeLike = ...
) -> Array: ...
def tril(m: ArrayLike, k: int = ...) -> Array: ...
def tril_indices(
    n: int, k: int = ..., m: Optional[int] = ...
) -> tuple[Array, Array]: ...
def tril_indices_from(arr: ArrayLike, k: int = ...) -> tuple[Array, Array]: ...
def fill_diagonal(a: ArrayLike, val: ArrayLike, wrap: builtins.bool = ..., *, inplace: builtins.bool = ...) -> Array: ...
def trim_zeros(filt: ArrayLike, trim: str = ...) -> Array: ...
def triu(m: ArrayLike, k: int = ...) -> Array: ...
def triu_indices(
    n: int, k: int = ..., m: Optional[int] = ...
) -> tuple[Array, Array]: ...
def triu_indices_from(arr: ArrayLike, k: int = ...) -> tuple[Array, Array]: ...
def true_divide(x: ArrayLike, y: ArrayLike, /) -> Array: ...
def trunc(x: ArrayLike, /) -> Array: ...
uint: Any
uint16: Any
uint32: Any
uint4: Any
uint64: Any
uint8: Any
def union1d(
    ar1: ArrayLike,
    ar2: ArrayLike,
    *,
    size: Optional[int] = ...,
    fill_value: Optional[ArrayLike] = ...,
) -> Array: ...
class _UniqueAllResult(NamedTuple):
  values: Array
  indices: Array
  inverse_indices: Array
  counts: Array
class _UniqueCountsResult(NamedTuple):
    values: Array
    counts: Array
class _UniqueInverseResult(NamedTuple):
    values: Array
    inverse_indices: Array
def unique(ar: ArrayLike, return_index: builtins.bool = ..., return_inverse: builtins.bool = ...,
           return_counts: builtins.bool = ..., axis: Optional[int] = ...,
           *, equal_nan: builtins.bool = ..., size: Optional[int] = ...,
           fill_value: Optional[ArrayLike] = ...
): ...
def unique_all(x: ArrayLike, /) -> _UniqueAllResult: ...
def unique_counts(x: ArrayLike, /) -> _UniqueCountsResult: ...
def unique_inverse(x: ArrayLike, /) -> _UniqueInverseResult: ...
def unique_values(x: ArrayLike, /) -> Array: ...
def unpackbits(
    a: ArrayLike,
    axis: Optional[int] = ...,
    count: Optional[ArrayLike] = ...,
    bitorder: str = ...,
) -> Array: ...
def unravel_index(indices: ArrayLike, shape: Shape) -> tuple[Array, ...]: ...
unsignedinteger = _np.unsignedinteger
def unstack(x: ArrayLike , /, *, axis: int = ...) -> tuple[Array, ...]: ...
def unwrap(p: ArrayLike, discont: Optional[ArrayLike] = ...,
           axis: int = ..., period: ArrayLike = ...) -> Array: ...
def vander(
    x: ArrayLike, N: Optional[int] = ..., increasing: builtins.bool = ...
) -> Array: ...
def var(a: ArrayLike, axis: _Axis = ..., dtype: DTypeLike = ...,
        out: None = ..., ddof: int = ..., keepdims: builtins.bool = ..., *,
        where: Optional[ArrayLike] = ...) -> Array: ...
def vdot(
    a: ArrayLike, b: ArrayLike, *, precision: PrecisionLike = ...,
    preferred_element_type: Optional[DTypeLike] = ...) -> Array: ...
def vecdot(x1: ArrayLike, x2: ArrayLike, /, *, axis: int = ...,
           precision: PrecisionLike = ...,
           preferred_element_type: Optional[DTypeLike] = ...) -> Array: ...
def vsplit(
    ary: ArrayLike, indices_or_sections: Union[int, ArrayLike]
) -> list[Array]: ...

def vstack(tup: Union[_np.ndarray, Array, Sequence[ArrayLike]],
           dtype: Optional[DTypeLike] = ...) -> Array: ...

@overload
def where(condition: ArrayLike, x: Literal[None] = ..., y: Literal[None] = ...,
          /, *, size: Optional[int] = ...,
          fill_value: Union[None, ArrayLike, tuple[ArrayLike, ...]] = ...
          ) -> tuple[Array, ...]: ...

@overload
def where(condition: ArrayLike, x: ArrayLike, y: ArrayLike, /, *,
          size: Optional[int] = ...,
          fill_value: Union[None, ArrayLike, tuple[ArrayLike, ...]] = ...
          ) -> Array: ...

@overload
def where(condition: ArrayLike, x: Optional[ArrayLike] = ...,
          y: Optional[ArrayLike] = ..., /, *, size: Optional[int] = ...,
          fill_value: Union[None, ArrayLike, tuple[ArrayLike, ...]] = ...
          ) -> Union[Array, tuple[Array, ...]]: ...

def zeros(shape: Any, dtype: Optional[DTypeLike] = ...,
          device: Optional[Union[_Device, _Sharding]] = ...) -> Array: ...
def zeros_like(a: Union[ArrayLike, DuckTypedArray],
               dtype: Optional[DTypeLike] = ...,
               shape: Any = ..., *,
               device: Optional[Union[_Device, _Sharding]] = ...) -> Array: ...

def vectorize(pyfunc, *, excluded = ..., signature = ...) -> Callable: ...
