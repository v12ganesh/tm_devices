"""DMM7510 device driver module."""
from tm_devices.commands import DMM7510Mixin
from tm_devices.drivers.pi.digital_multimeters.dmm7500.dmm7500 import DMM7500


class DMM7510(DMM7510Mixin, DMM7500):
    """DMM7510 device driver."""

    ################################################################################################
    # Magic Methods
    ################################################################################################

    ################################################################################################
    # Properties
    ################################################################################################

    ################################################################################################
    # Public Methods
    ################################################################################################

    ################################################################################################
    # Private Methods
    ################################################################################################