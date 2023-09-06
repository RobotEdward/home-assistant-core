# Home Assistant Integration Dev Notes

## Config / Data Entry Flow

https://developers.home-assistant.io/docs/data_entry_flow_index/

## Config Entries
https://developers.home-assistant.io/docs/config_entries_index/


## DataUpdateCoordinator

[Use CoordinatorEntity when using the DataUpdateCoordinator](https://aarongodfrey.dev/home%20automation/use-coordinatorentity-with-the-dataupdatecoordinator/)

https://developers.home-assistant.io/docs/integration_fetching_data

## Examples
This one has more comments https://github.com/home-assistant/example-custom-config/blob/master/custom_components/detailed_hello_world_push/__init__.py

Tutorial using config yaml: https://aarongodfrey.dev/home%20automation/building_a_home_assistant_custom_component_part_1/

## Entities
Generic properties are in here: https://developers.home-assistant.io/docs/core/entity

fine to use the _attr_xxx versions rather than re-implementing properties: https://developers.home-assistant.io/docs/core/entity#entity-class-or-instance-attributes

## TO DO
- [ ] make async
- [ ] Device Info https://developers.home-assistant.io/docs/device_registry_index/
- [ ] Translation friendly: https://developers.home-assistant.io/docs/internationalization/core/#name-of-entities
