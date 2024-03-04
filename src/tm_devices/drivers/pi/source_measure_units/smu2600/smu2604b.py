"""SMU Model 2604B device driver module."""

from tm_devices.commands import SMU2604BMixin
from tm_devices.drivers.pi.source_measure_units.smu2600.smu2600b import SMU2600B


class SMU2604B(SMU2604BMixin, SMU2600B):
    """SMU2604B device driver."""
