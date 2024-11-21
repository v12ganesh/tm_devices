"""MSO4K device driver module."""

from tm_devices.commands import MSO4KMixin
from tm_devices.drivers.scopes.tekscope_3k_4k.tekscope_3k_4k import TekScope3k4k


class MSO4K(MSO4KMixin, TekScope3k4k):
    """MSO4K device driver."""

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