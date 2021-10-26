from area_codes.data_types import AreaCode, AreaCodes, UsState, UsStateAbbreviation
from area_codes.state_data import area_codes_to_state, state_to_area_code, abbrev_to_state, state_to_abbrev


def _is_abbreviation(state) -> bool:
    return len(state) == 2


def get_area_codes_for_state(state: UsState) -> AreaCodes:
    return state_to_area_code.get(state)


def get_area_codes_for_state_abbreviation(state: UsStateAbbreviation) -> AreaCodes:
    return state_to_area_code.get(abbrev_to_state.get(state))


def get_state_for_area_code(area_code: AreaCode) -> UsState:
    return area_codes_to_state.get(area_code)


def get_state_abbreviation_for_area_code(area_code: AreaCode) -> UsStateAbbreviation:
    return get_state_abbreviation(get_state_for_area_code(area_code))


def get_state_abbreviation(state: UsState) -> UsStateAbbreviation:
    return state_to_abbrev.get(state)


def get_state_from_abbreviation(state: UsStateAbbreviation) -> UsState:
    return abbrev_to_state.get(state)
