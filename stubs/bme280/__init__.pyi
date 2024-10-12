from _typeshed import Incomplete
from i2cdevice.adapter import Adapter

__version__: str
CHIP_ID: int
I2C_ADDRESS_GND: int
I2C_ADDRESS_VCC: int

class S8Adapter(Adapter): ...
class S16Adapter(Adapter): ...
class U16Adapter(Adapter): ...
class H5Adapter(S16Adapter): ...
class H4Adapter(S16Adapter): ...

class BME280Calibration:
    dig_t1: int
    dig_t2: int
    dig_t3: int
    dig_p1: int
    dig_p2: int
    dig_p3: int
    dig_p4: int
    dig_p5: int
    dig_p6: int
    dig_p7: int
    dig_p8: int
    dig_p9: int
    dig_h1: float
    dig_h2: float
    dig_h3: float
    dig_h4: float
    dig_h5: float
    dig_h6: float
    temperature_fine: int
    def __init__(self) -> None: ...
    def set_from_namedtuple(self, value) -> None: ...
    def compensate_temperature(self, raw_temperature): ...
    def compensate_pressure(self, raw_pressure): ...
    def compensate_humidity(self, raw_humidity): ...

class BME280:
    calibration: Incomplete
    def __init__(self, i2c_addr=..., i2c_dev: Incomplete | None = None) -> None: ...
    def setup(
        self,
        mode: str = "normal",
        temperature_oversampling: int = 16,
        pressure_oversampling: int = 16,
        humidity_oversampling: int = 16,
        temperature_standby: int = 500,
    ) -> None: ...
    temperature: Incomplete
    pressure: Incomplete
    humidity: Incomplete
    def update_sensor(self) -> None: ...
    def get_temperature(self): ...
    def get_pressure(self): ...
    def get_humidity(self): ...
    def get_altitude(self, qnh: float = 1013.25): ...
