# ruff: noqa: D402,PLR0913
# pyright: reportConstantRedefinition=none
"""The digio commands module.

These commands are used in the following models:
SS3706A

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Attributes and Functions:

::

    - digio.readbit()
    - digio.readport()
    - digio.trigger[N].assert()
    - digio.trigger[N].clear()
    - digio.trigger[N].mode
    - digio.trigger[N].overrun
    - digio.trigger[N].pulsewidth
    - digio.trigger[N].release()
    - digio.trigger[N].reset()
    - digio.trigger[N].stimulus
    - digio.trigger[N].wait()
    - digio.writebit()
    - digio.writeport()
    - digio.writeprotect
"""

from typing import Dict, Optional, TYPE_CHECKING, Union

from .._helpers import (
    BaseTSPCmd,
    DefaultDictPassKeyToFactory,
    NoDeviceProvidedError,
    ValidatedDynamicNumberCmd,
)

if TYPE_CHECKING:
    from tm_devices.drivers.pi.tsp_device import TSPDevice


class DigioTriggerItem(ValidatedDynamicNumberCmd, BaseTSPCmd):
    """The ``digio.trigger[N]`` command tree.

    **Info:**
        - ``N``, the digital I/O trigger line (1 to 14).

    Constants:
        - ``.EVENT_ID``: The trigger event generated by the digital I/O line N.

    Properties/methods:
        - ``.assert()``: The ``digio.trigger[N].assert()`` function.
        - ``.clear()``: The ``digio.trigger[N].clear()`` function.
        - ``.mode``: The ``digio.trigger[N].mode`` attribute.
        - ``.overrun``: The ``digio.trigger[N].overrun`` attribute.
        - ``.pulsewidth``: The ``digio.trigger[N].pulsewidth`` attribute.
        - ``.release()``: The ``digio.trigger[N].release()`` function.
        - ``.reset()``: The ``digio.trigger[N].reset()`` function.
        - ``.stimulus``: The ``digio.trigger[N].stimulus`` attribute.
        - ``.wait()``: The ``digio.trigger[N].wait()`` function.
    """

    EVENT_ID = "digio.trigger[N].EVENT_ID"
    """str: The trigger event generated by the digital I/O line N."""

    def __init__(self, device: Optional["TSPDevice"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        # pylint: disable=invalid-name
        self.EVENT_ID = self.EVENT_ID.replace(
            "[N]", f"[{self._cmd_syntax.rsplit('[', maxsplit=1)[-1].split(']', maxsplit=1)[0]}]"
        )

    @property
    def mode(self) -> str:
        """Access the ``digio.trigger[N].mode`` attribute.

        **Description:**
            - This attribute sets the mode in which the trigger event detector and the output
              trigger generator operate on the given trigger line.

        **Usage:**
            - Accessing this property will send the ``print(digio.trigger[N].mode)`` query.
            - Setting this property to a value will send the ``digio.trigger[N].mode = value``
              command.

        **TSP Syntax:**

        ::

            - digio.trigger[N].mode = value
            - print(digio.trigger[N].mode)

        **Info:**
            - ``N``, the digital I/O trigger line (1 to 14).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".mode"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.mode)"
            )
        except AttributeError as error:
            msg = f"No TSPDevice object was provided, unable to access the ``{self._cmd_syntax}.mode`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @mode.setter
    def mode(self, value: Union[str, float]) -> None:
        """Access the ``digio.trigger[N].mode`` attribute.

        **Description:**
            - This attribute sets the mode in which the trigger event detector and the output
              trigger generator operate on the given trigger line.

        **Usage:**
            - Accessing this property will send the ``print(digio.trigger[N].mode)`` query.
            - Setting this property to a value will send the ``digio.trigger[N].mode = value``
              command.

        **TSP Syntax:**

        ::

            - digio.trigger[N].mode = value
            - print(digio.trigger[N].mode)

        **Info:**
            - ``N``, the digital I/O trigger line (1 to 14).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".mode", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.mode = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPDevice object was provided, unable to access the ``{self._cmd_syntax}.mode`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def overrun(self) -> str:
        """Access the ``digio.trigger[N].overrun`` attribute.

        **Description:**
            - This attribute returns the event detector overrun status.

        **Usage:**
            - Accessing this property will send the ``print(digio.trigger[N].overrun)`` query.

        **TSP Syntax:**

        ::

            - print(digio.trigger[N].overrun)

        **Info:**
            - ``N``, the digital I/O trigger line (1 to 14).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".overrun"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.overrun)"
            )
        except AttributeError as error:
            msg = f"No TSPDevice object was provided, unable to access the ``{self._cmd_syntax}.overrun`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def pulsewidth(self) -> str:
        """Access the ``digio.trigger[N].pulsewidth`` attribute.

        **Description:**
            - This attribute describes the length of time that the trigger line is asserted for
              output triggers.

        **Usage:**
            - Accessing this property will send the ``print(digio.trigger[N].pulsewidth)`` query.
            - Setting this property to a value will send the ``digio.trigger[N].pulsewidth = value``
              command.

        **TSP Syntax:**

        ::

            - digio.trigger[N].pulsewidth = value
            - print(digio.trigger[N].pulsewidth)

        **Info:**
            - ``width``, the pulse width (seconds).
            - ``N``, the digital I/O trigger line (1 to 14).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".pulsewidth"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.pulsewidth)"
            )
        except AttributeError as error:
            msg = f"No TSPDevice object was provided, unable to access the ``{self._cmd_syntax}.pulsewidth`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @pulsewidth.setter
    def pulsewidth(self, value: Union[str, float]) -> None:
        """Access the ``digio.trigger[N].pulsewidth`` attribute.

        **Description:**
            - This attribute describes the length of time that the trigger line is asserted for
              output triggers.

        **Usage:**
            - Accessing this property will send the ``print(digio.trigger[N].pulsewidth)`` query.
            - Setting this property to a value will send the ``digio.trigger[N].pulsewidth = value``
              command.

        **TSP Syntax:**

        ::

            - digio.trigger[N].pulsewidth = value
            - print(digio.trigger[N].pulsewidth)

        **Info:**
            - ``width``, the pulse width (seconds).
            - ``N``, the digital I/O trigger line (1 to 14).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".pulsewidth", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.pulsewidth = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPDevice object was provided, unable to access the ``{self._cmd_syntax}.pulsewidth`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def stimulus(self) -> str:
        """Access the ``digio.trigger[N].stimulus`` attribute.

        **Description:**
            - This attribute selects the event that causes a trigger to be asserted on the digital
              output line.

        **Usage:**
            - Accessing this property will send the ``print(digio.trigger[N].stimulus)`` query.
            - Setting this property to a value will send the ``digio.trigger[N].stimulus = value``
              command.

        **TSP Syntax:**

        ::

            - digio.trigger[N].stimulus = value
            - print(digio.trigger[N].stimulus)

        **Info:**
            - ``N``, the digital I/O trigger line (1 to 14).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".stimulus"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.stimulus)"
            )
        except AttributeError as error:
            msg = f"No TSPDevice object was provided, unable to access the ``{self._cmd_syntax}.stimulus`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @stimulus.setter
    def stimulus(self, value: Union[str, float]) -> None:
        """Access the ``digio.trigger[N].stimulus`` attribute.

        **Description:**
            - This attribute selects the event that causes a trigger to be asserted on the digital
              output line.

        **Usage:**
            - Accessing this property will send the ``print(digio.trigger[N].stimulus)`` query.
            - Setting this property to a value will send the ``digio.trigger[N].stimulus = value``
              command.

        **TSP Syntax:**

        ::

            - digio.trigger[N].stimulus = value
            - print(digio.trigger[N].stimulus)

        **Info:**
            - ``N``, the digital I/O trigger line (1 to 14).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".stimulus", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.stimulus = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPDevice object was provided, unable to access the ``{self._cmd_syntax}.stimulus`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def assert_(self) -> None:
        """Run the ``digio.trigger[N].assert()`` function.

        **Description:**
            - This function asserts a trigger pulse on one of the digital I/O lines.

        **TSP Syntax:**

        ::

            - digio.trigger[N].assert()

        **Info:**
            - ``N``, the digital I/O trigger line (1 to 14).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.assert()"
            )
        except AttributeError as error:
            msg = f"No TSPDevice object was provided, unable to run the ``{self._cmd_syntax}.assert()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def clear(self) -> None:
        """Run the ``digio.trigger[N].clear()`` function.

        **Description:**
            - This function clears the trigger event on a digital I/O line.

        **TSP Syntax:**

        ::

            - digio.trigger[N].clear()

        **Info:**
            - ``N``, the digital I/O trigger line (1 to 14).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.clear()"
            )
        except AttributeError as error:
            msg = f"No TSPDevice object was provided, unable to run the ``{self._cmd_syntax}.clear()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def release(self) -> None:
        """Run the ``digio.trigger[N].release()`` function.

        **Description:**
            - This function releases an indefinite length or latched trigger.

        **TSP Syntax:**

        ::

            - digio.trigger[N].release()

        **Info:**
            - ``N``, the digital I/O trigger line (1 to 14).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.release()"
            )
        except AttributeError as error:
            msg = f"No TSPDevice object was provided, unable to run the ``{self._cmd_syntax}.release()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def reset(self) -> None:
        """Run the ``digio.trigger[N].reset()`` function.

        **Description:**
            - This function resets trigger values to their factory defaults.

        **TSP Syntax:**

        ::

            - digio.trigger[N].reset()

        **Info:**
            - ``N``, the digital I/O trigger line (1 to 14).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.reset()"
            )
        except AttributeError as error:
            msg = f"No TSPDevice object was provided, unable to run the ``{self._cmd_syntax}.reset()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def wait(self, timeout: float) -> str:
        """Run the ``digio.trigger[N].wait()`` function.

        **Description:**
            - This function waits for a trigger.

        **TSP Syntax:**

        ::

            - digio.trigger[N].wait()

        Args:
            timeout: Timeout in seconds.

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.wait({timeout}))"
            )
        except AttributeError as error:
            msg = f"No TSPDevice object was provided, unable to run the ``{self._cmd_syntax}.wait()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class Digio(BaseTSPCmd):
    """The ``digio`` command tree.

    Properties/methods:
        - ``.readbit()``: The ``digio.readbit()`` function.
        - ``.readport()``: The ``digio.readport()`` function.
        - ``.trigger``: The ``digio.trigger[N]`` command tree.
        - ``.writebit()``: The ``digio.writebit()`` function.
        - ``.writeport()``: The ``digio.writeport()`` function.
        - ``.writeprotect``: The ``digio.writeprotect`` attribute.
    """

    def __init__(self, device: Optional["TSPDevice"] = None, cmd_syntax: str = "digio") -> None:
        super().__init__(device, cmd_syntax)
        self._trigger: Dict[int, DigioTriggerItem] = DefaultDictPassKeyToFactory(
            lambda x: DigioTriggerItem(device, f"{self._cmd_syntax}.trigger[{x}]")
        )

    @property
    def trigger(self) -> Dict[int, DigioTriggerItem]:
        """Return the ``digio.trigger[N]`` command tree.

        **Info:**
            - ``N``, the digital I/O trigger line (1 to 14).

        Constants:
            - ``.EVENT_ID``: The trigger event generated by the digital I/O line N.

        Sub-properties/methods:
            - ``.assert()``: The ``digio.trigger[N].assert()`` function.
            - ``.clear()``: The ``digio.trigger[N].clear()`` function.
            - ``.mode``: The ``digio.trigger[N].mode`` attribute.
            - ``.overrun``: The ``digio.trigger[N].overrun`` attribute.
            - ``.pulsewidth``: The ``digio.trigger[N].pulsewidth`` attribute.
            - ``.release()``: The ``digio.trigger[N].release()`` function.
            - ``.reset()``: The ``digio.trigger[N].reset()`` function.
            - ``.stimulus``: The ``digio.trigger[N].stimulus`` attribute.
            - ``.wait()``: The ``digio.trigger[N].wait()`` function.
        """
        return self._trigger

    @property
    def writeprotect(self) -> str:
        """Access the ``digio.writeprotect`` attribute.

        **Description:**
            - This attribute contains the write-protect mask that protects bits from changes from
              the digio.writebit() and digio.writeport() functions.

        **Usage:**
            - Accessing this property will send the ``print(digio.writeprotect)`` query.
            - Setting this property to a value will send the ``digio.writeprotect = value`` command.

        **TSP Syntax:**

        ::

            - digio.writeprotect = value
            - print(digio.writeprotect)

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".writeprotect"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.writeprotect)"
            )
        except AttributeError as error:
            msg = f"No TSPDevice object was provided, unable to access the ``{self._cmd_syntax}.writeprotect`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @writeprotect.setter
    def writeprotect(self, value: Union[str, float]) -> None:
        """Access the ``digio.writeprotect`` attribute.

        **Description:**
            - This attribute contains the write-protect mask that protects bits from changes from
              the digio.writebit() and digio.writeport() functions.

        **Usage:**
            - Accessing this property will send the ``print(digio.writeprotect)`` query.
            - Setting this property to a value will send the ``digio.writeprotect = value`` command.

        **TSP Syntax:**

        ::

            - digio.writeprotect = value
            - print(digio.writeprotect)

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".writeprotect", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.writeprotect = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPDevice object was provided, unable to access the ``{self._cmd_syntax}.writeprotect`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def readbit(self, n: int) -> str:
        """Run the ``digio.readbit()`` function.

        **Description:**
            - This function reads one digital I/O line.

        **TSP Syntax:**

        ::

            - digio.readbit()

        Args:
            n: Digital I/O line number to be read (1 to 14).

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.readbit({n}))"
            )
        except AttributeError as error:
            msg = f"No TSPDevice object was provided, unable to run the ``{self._cmd_syntax}.readbit()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def readport(self) -> str:
        """Run the ``digio.readport()`` function.

        **Description:**
            - This function reads the digital I/O port.

        **TSP Syntax:**

        ::

            - digio.readport()

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.readport())"
            )
        except AttributeError as error:
            msg = f"No TSPDevice object was provided, unable to run the ``{self._cmd_syntax}.readport()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def writebit(self, n: int, data: int) -> None:
        """Run the ``digio.writebit()`` function.

        **Description:**
            - This function sets a digital I/O line high or low.

        **TSP Syntax:**

        ::

            - digio.writebit()

        Args:
            n: Digital I/O trigger line (1 to 14).
            data: The value to write to the bit.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.writebit({n}, {data})"
            )
        except AttributeError as error:
            msg = f"No TSPDevice object was provided, unable to run the ``{self._cmd_syntax}.writebit()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def writeport(self, data: int) -> None:
        """Run the ``digio.writeport()`` function.

        **Description:**
            - This function writes to all digital I/O lines.

        **TSP Syntax:**

        ::

            - digio.writeport()

        Args:
            data: Value to write to the port (0 to 16383).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.writeport({data})"
            )
        except AttributeError as error:
            msg = f"No TSPDevice object was provided, unable to run the ``{self._cmd_syntax}.writeport()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error
