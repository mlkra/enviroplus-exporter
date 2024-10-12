from _typeshed import Incomplete

class Adapter: ...

class LookupAdapter(Adapter):
    lookup_table: Incomplete
    snap: Incomplete
    def __init__(self, lookup_table, snap: bool = True) -> None: ...

class U16ByteSwapAdapter(Adapter): ...
