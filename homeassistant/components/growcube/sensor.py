"""Support for GrowCube smart plant watering sensors."""
from __future__ import annotations

import logging

from pygrowcube import pygrowcube

from homeassistant.components.sensor import SensorDeviceClass, SensorEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import UnitOfTemperature
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(
    hass: HomeAssistant,
    config_entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Add sensor entities for this GrowCube config entry."""
    status = hass.data[DOMAIN][config_entry.entry_id]
    new_devices = [RoomTemperature(status), Humidity(status)]
    for i in range(4):
        new_devices.append(Moisture(i, status))
    if new_devices:
        async_add_entities(new_devices)


class RoomTemperature(SensorEntity):
    """GrowCube room temperature sensor entity."""

    def __init__(self, status: pygrowcube.Status) -> None:
        """Initialise the sensor from GrowCube status object."""
        self._attr_native_value = int(status.temperature)
        self._attr_unique_id = f"{status.id}+_temperature"
        self._attr_name = "GrowCube Temperature"
        self._attr_native_unit_of_measurement = UnitOfTemperature.CELSIUS
        self._attr_device_class = SensorDeviceClass.TEMPERATURE

    def update(self) -> None:
        """Fetch new state data for the sensor.

        This is the only method that should fetch new data for Home Assistant.
        """
        _LOGGER.info("Update RoomTemp")


class Humidity(SensorEntity):
    """GrowCube humidity sensor entity."""

    def __init__(self, status: pygrowcube.Status) -> None:
        """Initialise the sensor from GrowCube status object."""
        self._attr_native_value = int(status.humidity)
        self._attr_unique_id = f"{status.id}+_humidity"
        self._attr_name = "GrowCube Humidity"
        self._attr_native_unit_of_measurement = "%"
        self._attr_device_class = SensorDeviceClass.HUMIDITY

    def update(self) -> None:
        """Fetch new state data for the sensor.

        This is the only method that should fetch new data for Home Assistant.
        """
        _LOGGER.info("Update RoomTemp")


class Moisture(SensorEntity):
    """GrowCube moisture sensor entity - one per channel."""

    def __init__(self, channel: int, status: pygrowcube.Status) -> None:
        """Initialise the sensor from GrowCube status object and a channel number."""
        outlet = ["A", "B", "C", "D"][channel]
        self._attr_native_value = int(status.moistures[channel])
        self._attr_unique_id = f"{status.id}_plant_{outlet}"
        self._attr_name = f"GrowCube Plant {outlet}"
        self._attr_native_unit_of_measurement = "%"
        self._attr_device_class = SensorDeviceClass.MOISTURE
        self._channel = channel

    def update(self) -> None:
        """Fetch new state data for the sensor.

        This is the only method that should fetch new data for Home Assistant.
        """
        _LOGGER.info("Update RoomTemp")
