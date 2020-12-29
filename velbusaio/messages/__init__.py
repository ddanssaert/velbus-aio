"""
:author: Thomas Delaet <thomas@delaet.org>
"""
# pylint: disable-msg=C0301
from velbusaio.messages.bus_active import BusActiveMessage
from velbusaio.messages.bus_error_counter_status_request import (
    BusErrorStatusRequestMessage,
)
from velbusaio.messages.bus_error_counter_status import BusErrorCounterStatusMessage
from velbusaio.messages.bus_off import BusOffMessage
from velbusaio.messages.channel_name_part1 import (
    ChannelNamePart1Message,
    ChannelNamePart1Message2,
    ChannelNamePart1Message3,
)
from velbusaio.messages.channel_name_part2 import (
    ChannelNamePart2Message,
    ChannelNamePart2Message2,
    ChannelNamePart2Message3,
)
from velbusaio.messages.channel_name_part3 import (
    ChannelNamePart3Message,
    ChannelNamePart3Message2,
    ChannelNamePart3Message3,
)
from velbusaio.messages.channel_name_request import (
    ChannelNameRequestMessage,
    ChannelNameRequestMessage2,
)
from velbusaio.messages.clear_led import ClearLedMessage
from velbusaio.messages.fast_blinking_led import FastBlinkingLedMessage
from velbusaio.messages.interface_status_request import InterfaceStatusRequestMessage
from velbusaio.messages.memory_data_block import MemoryDataBlockMessage
from velbusaio.messages.memory_data import MemoryDataMessage
from velbusaio.messages.memory_dump_request import MemoryDumpRequestMessage
from velbusaio.messages.module_status_request import ModuleStatusRequestMessage
from velbusaio.messages.module_status import ModuleStatusMessage
from velbusaio.messages.module_status import ModuleStatusMessage2
from velbusaio.messages.module_type import ModuleTypeMessage
from velbusaio.messages.module_type_request import ModuleTypeRequestMessage
from velbusaio.messages.push_button_status import PushButtonStatusMessage
from velbusaio.messages.read_data_block_from_memory import (
    ReadDataBlockFromMemoryMessage,
)
from velbusaio.messages.read_data_from_memory import ReadDataFromMemoryMessage
from velbusaio.messages.receive_buffer_full import ReceiveBufferFullMessage
from velbusaio.messages.receive_ready import ReceiveReadyMessage
from velbusaio.messages.relay_status import RelayStatusMessage
from velbusaio.messages.set_led import SetLedMessage
from velbusaio.messages.slow_blinking_led import SlowBlinkingLedMessage
from velbusaio.messages.start_relay_blinking_timer import StartRelayBlinkingTimerMessage
from velbusaio.messages.start_relay_timer import StartRelayTimerMessage
from velbusaio.messages.switch_relay_off import SwitchRelayOffMessage
from velbusaio.messages.switch_relay_on import SwitchRelayOnMessage
from velbusaio.messages.switch_to_comfort import SwitchToComfortMessage
from velbusaio.messages.switch_to_day import SwitchToDayMessage
from velbusaio.messages.switch_to_night import SwitchToNightMessage
from velbusaio.messages.switch_to_safe import SwitchToSafeMessage
from velbusaio.messages.temp_sensor_status import TempSensorStatusMessage
from velbusaio.messages.temp_set_heating import TempSetHeatingMessage
from velbusaio.messages.temp_set_cooling import TempSetCoolingMessage
from velbusaio.messages.update_led_status import UpdateLedStatusMessage
from velbusaio.messages.very_fast_blinking_led import VeryFastBlinkingLedMessage
from velbusaio.messages.write_data_to_memory import WriteDataToMemoryMessage
from velbusaio.messages.write_memory_block import WriteMemoryBlockMessage
from velbusaio.messages.write_module_address_and_serial_number import (
    WriteModuleAddressAndSerialNumberMessage,
)
from velbusaio.messages.cover_down import CoverDownMessage, CoverDownMessage2
from velbusaio.messages.cover_up import CoverUpMessage, CoverUpMessage2
from velbusaio.messages.cover_off import CoverOffMessage, CoverOffMessage2
from velbusaio.messages.cover_position import CoverPosMessage
from velbusaio.messages.blind_status import BlindStatusMessage, BlindStatusNgMessage
from velbusaio.messages.sensor_temperature import SensorTemperatureMessage
from velbusaio.messages.kwh_status import KwhStatusMessage
from velbusaio.messages.counter_status import CounterStatusMessage
from velbusaio.messages.counter_status_request import CounterStatusRequestMessage
from velbusaio.messages.module_subtype import ModuleSubTypeMessage
from velbusaio.messages.set_temperature import SetTemperatureMessage
from velbusaio.messages.meteo_raw import MeteoRawMessage
from velbusaio.messages.set_realtime_clock import SetRealtimeClock
from velbusaio.messages.set_date import SetDate
from velbusaio.messages.set_daylight_saving import SetDaylightSaving
from velbusaio.messages.dimmer_channel_status import DimmerChannelStatusMessage
from velbusaio.messages.dimmer_status import DimmerStatusMessage
from velbusaio.messages.set_dimmer import SetDimmerMessage
from velbusaio.messages.restore_dimmer import RestoreDimmerMessage
from velbusaio.messages.slider_status import SliderStatusMessage
from velbusaio.messages.memo_text import MemoTextMessage
