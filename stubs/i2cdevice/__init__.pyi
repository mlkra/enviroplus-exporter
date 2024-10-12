import types

from _typeshed import Incomplete

__version__: str

class MockSMBus:
    regs: Incomplete
    def __init__(
        self, i2c_bus, default_registers: Incomplete | None = None
    ) -> None: ...
    def write_i2c_block_data(self, i2c_address, register, values) -> None: ...
    def read_i2c_block_data(self, i2c_address, register, length): ...

class _RegisterProxy:
    device: Incomplete
    register: Incomplete
    def __init__(self, device, register) -> None: ...
    def __getattribute__(self, name): ...
    def write(self): ...
    def read(self): ...
    def __enter__(self): ...
    def __exit__(
        self,
        exception_type: type[BaseException] | None,
        exception_value: BaseException | None,
        exception_traceback: types.TracebackType | None,
    ) -> None: ...

class Register:
    name: Incomplete
    address: Incomplete
    bit_width: Incomplete
    read_only: Incomplete
    volatile: Incomplete
    is_read: bool
    fields: Incomplete
    namedtuple: Incomplete
    def __init__(
        self,
        name,
        address,
        fields: Incomplete | None = None,
        bit_width: int = 8,
        read_only: bool = False,
        volatile: bool = True,
    ) -> None: ...

class BitField:
    name: Incomplete
    mask: Incomplete
    adapter: Incomplete
    bit_width: Incomplete
    read_only: Incomplete
    def __init__(
        self,
        name,
        mask,
        adapter: Incomplete | None = None,
        bit_width: int = 8,
        read_only: bool = False,
    ) -> None: ...

class BitFlag(BitField):
    def __init__(self, name, bit, read_only: bool = False) -> None: ...

class Device:
    locked: Incomplete
    registers: Incomplete
    values: Incomplete
    def __init__(
        self,
        i2c_address,
        i2c_dev: Incomplete | None = None,
        bit_width: int = 8,
        registers: Incomplete | None = None,
    ) -> None: ...
    def lock_register(self, name) -> None: ...
    def unlock_register(self, name) -> None: ...
    def read_register(self, name): ...
    def write_register(self, name): ...
    def get_addresses(self): ...
    def select_address(self, address): ...
    def next_address(self): ...
    def set(self, register, **kwargs) -> None: ...
    def get(self, register): ...
    def get_field(self, register, field): ...
    def set_field(self, register, field, value) -> None: ...
    def get_register(self, register): ...
