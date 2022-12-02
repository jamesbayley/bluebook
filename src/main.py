from src.io import *
from src.wrangler import *
from src.types import FilePath


if __name__ == '__main__':

    section_categories = {
        'ub',
        'uc',
        'ubp',
        'pfc',
        't-split-from-ub',
        't-split-from-uc',
        'equal-l',
        'unequal-l',
        'hf-shs',
        'hf-rhs',
        'hf-chs',
        'hf-ehs',
        'cf-shs',
        'cf-rhs',
        'cf-chs'
    }

    print('Loading configuration file.')
    config = load_config(FilePath('../config.json'))

    for sc in section_categories:
        print(f'Processing {sc.upper()} section data.')
        filepath = FilePath('../' + config[sc]['inputFile'])
        save_section_data_to_json(
            '../' + config[sc]['outFile'],
            wrangle_section_data(filepath, config[sc])
        )
