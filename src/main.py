from typing import Callable, Set, Tuple

from src.io import *
from src.wrangler import *
from src.types import FilePath, SteelSectionClassification


if __name__ == '__main__':

    def wrangle_xlsx_files(s: SteelSectionClassification, f: Callable[[FilePath], SectionDefinitions]) -> None:
        print(f'Processing {s.upper()} section data.')
        save_section_data_to_json(
            config[s]['outFile'],
            coerce_section_def_values_to_float(
                f(FilePath(config[s]['inputFile']))
            )
        )

    args: Set[Tuple[SteelSectionClassification, Callable[[FilePath], SectionDefinitions]]] = {
        ('ub', wrangle_universal_sections),
        ('uc', wrangle_universal_sections)
    }

    print('Loading configuration file.')
    config = load_config(FilePath('config.json'))
    for sections_cat, wrangle in args:
        wrangle_xlsx_files(sections_cat, wrangle)
