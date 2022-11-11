import json

from src.types import FilePath, ConfigFile, SectionDefinitions


def load_config(filepath: FilePath) -> ConfigFile:
    """
    Load the local configuration file into memory
    that is used to determine how each raw Excel
    file should be parsed and processed.
    """

    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)


def save_section_data_to_json(fp: FilePath, data: SectionDefinitions) -> None:
    """Saves the given section definitions export to JSON."""

    with open(fp, mode='w', encoding='utf-8') as f:
        json.dump(data, f)
