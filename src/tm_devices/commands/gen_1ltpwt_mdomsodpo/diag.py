"""The diag commands module.

These commands are used in the following models:
DPO4K, DPO4KB, MDO3, MDO3K, MDO4K, MDO4KB, MDO4KC, MSO4K, MSO4KB

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - DIAg:INDIvidual:TESTnumber
    - DIAg:INDIvidual:TESTnumber?
    - DIAg:LOOP:OPTion {ALWAYS|FAIL|ONFAIL|ONCE|NTIMES}
    - DIAg:LOOP:OPTion:NTIMes <NR1>
    - DIAg:LOOP:OPTion:NTIMes?
    - DIAg:LOOP:STOP
    - DIAg:RESUlt:FLAg?
    - DIAg:RESUlt:LOG?
    - DIAg:SELect {ALL|APPKey|CPU|DISplay|FPAnel|IO|ROM|ACQ|RF|AFG}
    - DIAg:STATE {EXECute|ABORt}
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite, SCPICmdWriteNoArguments

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class DiagState(SCPICmdWrite):
    """The ``DIAg:STATE`` command.

    Description:
        - This command starts or stops the oscilloscope diagnostic self-tests. Which self-test is
          run is specified by the ``DIAg:SELect``: or ``DIAg:SELect:<function>`` commands.

    Usage:
        - Using the ``.write(value)`` method will send the ``DIAg:STATE value`` command.

    SCPI Syntax:
        ```
        - DIAg:STATE {EXECute|ABORt}
        ```

    Info:
        - ``EXECute`` starts diagnostics.
        - ``ABORt`` stops diagnostics at the end of the current loop.
    """


class DiagSelect(SCPICmdWrite):
    """The ``DIAg:SELect`` command.

    Description:
        - This command specifies which of the diagnostic groups will be tested when the
          ``DIAg:STATE EXECute`` command is run.

    Usage:
        - Using the ``.write(value)`` method will send the ``DIAg:SELect value`` command.

    SCPI Syntax:
        ```
        - DIAg:SELect {ALL|APPKey|CPU|DISplay|FPAnel|IO|ROM|ACQ|RF|AFG}
        ```

    Info:
        - ``ALL`` runs all diagnostic groups.
        - ``APPKey`` runs just the application key diagnostic group.
        - ``CPU`` runs just the CPU diagnostic group.
        - ``DISplay`` runs just the display circuit diagnostic group.
        - ``FPAnel`` runs just the front panel diagnostic group.
        - ``IO`` runs just the IO board diagnostic group.
        - ``ROM`` runs just the ROM board diagnostic group.
        - ``ACQ`` runs just the acquisition system diagnostic group.
        - ``RF`` runs just the RF system diagnostic group (SA option enabled).
        - ``AFG`` runs just the AFG system diagnostic group (models with AFG hardware).
    """


class DiagResultLog(SCPICmdRead):
    """The ``DIAg:RESUlt:LOG`` command.

    Description:
        - This query returns the test Pass/Fail status of each diagnostic area. It does not return
          the overall status.

    Usage:
        - Using the ``.query()`` method will send the ``DIAg:RESUlt:LOG?`` query.
        - Using the ``.verify(value)`` method will send the ``DIAg:RESUlt:LOG?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DIAg:RESUlt:LOG?
        ```
    """


class DiagResultFlag(SCPICmdRead):
    """The ``DIAg:RESUlt:FLAg`` command.

    Description:
        - This query returns the status of the diagnostic test area that has been selected.

    Usage:
        - Using the ``.query()`` method will send the ``DIAg:RESUlt:FLAg?`` query.
        - Using the ``.verify(value)`` method will send the ``DIAg:RESUlt:FLAg?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DIAg:RESUlt:FLAg?
        ```
    """


class DiagResult(SCPICmdRead):
    """The ``DIAg:RESUlt`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DIAg:RESUlt?`` query.
        - Using the ``.verify(value)`` method will send the ``DIAg:RESUlt?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.flag``: The ``DIAg:RESUlt:FLAg`` command.
        - ``.log``: The ``DIAg:RESUlt:LOG`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._flag = DiagResultFlag(device, f"{self._cmd_syntax}:FLAg")
        self._log = DiagResultLog(device, f"{self._cmd_syntax}:LOG")

    @property
    def flag(self) -> DiagResultFlag:
        """Return the ``DIAg:RESUlt:FLAg`` command.

        Description:
            - This query returns the status of the diagnostic test area that has been selected.

        Usage:
            - Using the ``.query()`` method will send the ``DIAg:RESUlt:FLAg?`` query.
            - Using the ``.verify(value)`` method will send the ``DIAg:RESUlt:FLAg?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DIAg:RESUlt:FLAg?
            ```
        """
        return self._flag

    @property
    def log(self) -> DiagResultLog:
        """Return the ``DIAg:RESUlt:LOG`` command.

        Description:
            - This query returns the test Pass/Fail status of each diagnostic area. It does not
              return the overall status.

        Usage:
            - Using the ``.query()`` method will send the ``DIAg:RESUlt:LOG?`` query.
            - Using the ``.verify(value)`` method will send the ``DIAg:RESUlt:LOG?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DIAg:RESUlt:LOG?
            ```
        """
        return self._log


class DiagLoopStop(SCPICmdWriteNoArguments):
    """The ``DIAg:LOOP:STOP`` command.

    Description:
        - Request that diagnostics stop looping.

    Usage:
        - Using the ``.write()`` method will send the ``DIAg:LOOP:STOP`` command.

    SCPI Syntax:
        ```
        - DIAg:LOOP:STOP
        ```
    """


class DiagLoopOptionNtimes(SCPICmdWrite, SCPICmdRead):
    """The ``DIAg:LOOP:OPTion:NTIMes`` command.

    Description:
        - This command sets or queries how many loops to run, if N-times is being used.

    Usage:
        - Using the ``.query()`` method will send the ``DIAg:LOOP:OPTion:NTIMes?`` query.
        - Using the ``.verify(value)`` method will send the ``DIAg:LOOP:OPTion:NTIMes?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DIAg:LOOP:OPTion:NTIMes value``
          command.

    SCPI Syntax:
        ```
        - DIAg:LOOP:OPTion:NTIMes <NR1>
        - DIAg:LOOP:OPTion:NTIMes?
        ```

    Info:
        - ``<NR1>`` is how many loops to run.
    """


class DiagLoopOption(SCPICmdWrite, SCPICmdRead):
    """The ``DIAg:LOOP:OPTion`` command.

    Description:
        - Sets the self-test loop option.

    Usage:
        - Using the ``.write(value)`` method will send the ``DIAg:LOOP:OPTion value`` command.

    SCPI Syntax:
        ```
        - DIAg:LOOP:OPTion {ALWAYS|FAIL|ONFAIL|ONCE|NTIMES}
        ```

    Info:
        - ``ALWAYS`` continues looping until the self tests (diagnostics) are stopped via the front
          panel or by an oscilloscope command.
        - ``FAIL`` causes looping until the first self test (diagnostic) failure or until self tests
          (diagnostics) are stopped.
        - ``ONFAIL`` causes looping on a specific test group as long as a FAIL status is returned
          from the test.
        - ``ONCE`` executes self test (diagnostics test) sequence once.
        - ``NTIMES`` runs 'n' number of loops.

    Properties:
        - ``.ntimes``: The ``DIAg:LOOP:OPTion:NTIMes`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._ntimes = DiagLoopOptionNtimes(device, f"{self._cmd_syntax}:NTIMes")

    @property
    def ntimes(self) -> DiagLoopOptionNtimes:
        """Return the ``DIAg:LOOP:OPTion:NTIMes`` command.

        Description:
            - This command sets or queries how many loops to run, if N-times is being used.

        Usage:
            - Using the ``.query()`` method will send the ``DIAg:LOOP:OPTion:NTIMes?`` query.
            - Using the ``.verify(value)`` method will send the ``DIAg:LOOP:OPTion:NTIMes?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DIAg:LOOP:OPTion:NTIMes value``
              command.

        SCPI Syntax:
            ```
            - DIAg:LOOP:OPTion:NTIMes <NR1>
            - DIAg:LOOP:OPTion:NTIMes?
            ```

        Info:
            - ``<NR1>`` is how many loops to run.
        """
        return self._ntimes


class DiagLoop(SCPICmdRead):
    """The ``DIAg:LOOP`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DIAg:LOOP?`` query.
        - Using the ``.verify(value)`` method will send the ``DIAg:LOOP?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.option``: The ``DIAg:LOOP:OPTion`` command.
        - ``.stop``: The ``DIAg:LOOP:STOP`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._option = DiagLoopOption(device, f"{self._cmd_syntax}:OPTion")
        self._stop = DiagLoopStop(device, f"{self._cmd_syntax}:STOP")

    @property
    def option(self) -> DiagLoopOption:
        """Return the ``DIAg:LOOP:OPTion`` command.

        Description:
            - Sets the self-test loop option.

        Usage:
            - Using the ``.write(value)`` method will send the ``DIAg:LOOP:OPTion value`` command.

        SCPI Syntax:
            ```
            - DIAg:LOOP:OPTion {ALWAYS|FAIL|ONFAIL|ONCE|NTIMES}
            ```

        Info:
            - ``ALWAYS`` continues looping until the self tests (diagnostics) are stopped via the
              front panel or by an oscilloscope command.
            - ``FAIL`` causes looping until the first self test (diagnostic) failure or until self
              tests (diagnostics) are stopped.
            - ``ONFAIL`` causes looping on a specific test group as long as a FAIL status is
              returned from the test.
            - ``ONCE`` executes self test (diagnostics test) sequence once.
            - ``NTIMES`` runs 'n' number of loops.

        Sub-properties:
            - ``.ntimes``: The ``DIAg:LOOP:OPTion:NTIMes`` command.
        """
        return self._option

    @property
    def stop(self) -> DiagLoopStop:
        """Return the ``DIAg:LOOP:STOP`` command.

        Description:
            - Request that diagnostics stop looping.

        Usage:
            - Using the ``.write()`` method will send the ``DIAg:LOOP:STOP`` command.

        SCPI Syntax:
            ```
            - DIAg:LOOP:STOP
            ```
        """
        return self._stop


class DiagIndividualTestnumber(SCPICmdWriteNoArguments, SCPICmdRead):
    """The ``DIAg:INDIvidual:TESTnumber`` command.

    Description:
        - This command specifies the number of the diagnostics test to run.

    Usage:
        - Using the ``.query()`` method will send the ``DIAg:INDIvidual:TESTnumber?`` query.
        - Using the ``.verify(value)`` method will send the ``DIAg:INDIvidual:TESTnumber?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write()`` method will send the ``DIAg:INDIvidual:TESTnumber`` command.

    SCPI Syntax:
        ```
        - DIAg:INDIvidual:TESTnumber
        - DIAg:INDIvidual:TESTnumber?
        ```

    Info:
        - ``<NR1>`` is the test number to run.
    """


class DiagIndividual(SCPICmdRead):
    """The ``DIAg:INDIvidual`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DIAg:INDIvidual?`` query.
        - Using the ``.verify(value)`` method will send the ``DIAg:INDIvidual?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.testnumber``: The ``DIAg:INDIvidual:TESTnumber`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._testnumber = DiagIndividualTestnumber(device, f"{self._cmd_syntax}:TESTnumber")

    @property
    def testnumber(self) -> DiagIndividualTestnumber:
        """Return the ``DIAg:INDIvidual:TESTnumber`` command.

        Description:
            - This command specifies the number of the diagnostics test to run.

        Usage:
            - Using the ``.query()`` method will send the ``DIAg:INDIvidual:TESTnumber?`` query.
            - Using the ``.verify(value)`` method will send the ``DIAg:INDIvidual:TESTnumber?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write()`` method will send the ``DIAg:INDIvidual:TESTnumber`` command.

        SCPI Syntax:
            ```
            - DIAg:INDIvidual:TESTnumber
            - DIAg:INDIvidual:TESTnumber?
            ```

        Info:
            - ``<NR1>`` is the test number to run.
        """
        return self._testnumber


class Diag(SCPICmdRead):
    """The ``DIAg`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DIAg?`` query.
        - Using the ``.verify(value)`` method will send the ``DIAg?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.individual``: The ``DIAg:INDIvidual`` command tree.
        - ``.loop``: The ``DIAg:LOOP`` command tree.
        - ``.result``: The ``DIAg:RESUlt`` command tree.
        - ``.select``: The ``DIAg:SELect`` command.
        - ``.state``: The ``DIAg:STATE`` command.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "DIAg") -> None:
        super().__init__(device, cmd_syntax)
        self._individual = DiagIndividual(device, f"{self._cmd_syntax}:INDIvidual")
        self._loop = DiagLoop(device, f"{self._cmd_syntax}:LOOP")
        self._result = DiagResult(device, f"{self._cmd_syntax}:RESUlt")
        self._select = DiagSelect(device, f"{self._cmd_syntax}:SELect")
        self._state = DiagState(device, f"{self._cmd_syntax}:STATE")

    @property
    def individual(self) -> DiagIndividual:
        """Return the ``DIAg:INDIvidual`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DIAg:INDIvidual?`` query.
            - Using the ``.verify(value)`` method will send the ``DIAg:INDIvidual?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.testnumber``: The ``DIAg:INDIvidual:TESTnumber`` command.
        """
        return self._individual

    @property
    def loop(self) -> DiagLoop:
        """Return the ``DIAg:LOOP`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DIAg:LOOP?`` query.
            - Using the ``.verify(value)`` method will send the ``DIAg:LOOP?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.option``: The ``DIAg:LOOP:OPTion`` command.
            - ``.stop``: The ``DIAg:LOOP:STOP`` command.
        """
        return self._loop

    @property
    def result(self) -> DiagResult:
        """Return the ``DIAg:RESUlt`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DIAg:RESUlt?`` query.
            - Using the ``.verify(value)`` method will send the ``DIAg:RESUlt?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.flag``: The ``DIAg:RESUlt:FLAg`` command.
            - ``.log``: The ``DIAg:RESUlt:LOG`` command.
        """
        return self._result

    @property
    def select(self) -> DiagSelect:
        """Return the ``DIAg:SELect`` command.

        Description:
            - This command specifies which of the diagnostic groups will be tested when the
              ``DIAg:STATE EXECute`` command is run.

        Usage:
            - Using the ``.write(value)`` method will send the ``DIAg:SELect value`` command.

        SCPI Syntax:
            ```
            - DIAg:SELect {ALL|APPKey|CPU|DISplay|FPAnel|IO|ROM|ACQ|RF|AFG}
            ```

        Info:
            - ``ALL`` runs all diagnostic groups.
            - ``APPKey`` runs just the application key diagnostic group.
            - ``CPU`` runs just the CPU diagnostic group.
            - ``DISplay`` runs just the display circuit diagnostic group.
            - ``FPAnel`` runs just the front panel diagnostic group.
            - ``IO`` runs just the IO board diagnostic group.
            - ``ROM`` runs just the ROM board diagnostic group.
            - ``ACQ`` runs just the acquisition system diagnostic group.
            - ``RF`` runs just the RF system diagnostic group (SA option enabled).
            - ``AFG`` runs just the AFG system diagnostic group (models with AFG hardware).
        """
        return self._select

    @property
    def state(self) -> DiagState:
        """Return the ``DIAg:STATE`` command.

        Description:
            - This command starts or stops the oscilloscope diagnostic self-tests. Which self-test
              is run is specified by the ``DIAg:SELect``: or ``DIAg:SELect:<function>`` commands.

        Usage:
            - Using the ``.write(value)`` method will send the ``DIAg:STATE value`` command.

        SCPI Syntax:
            ```
            - DIAg:STATE {EXECute|ABORt}
            ```

        Info:
            - ``EXECute`` starts diagnostics.
            - ``ABORt`` stops diagnostics at the end of the current loop.
        """
        return self._state
