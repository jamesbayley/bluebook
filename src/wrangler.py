import pandas as pd

from src.types import FilePath, SectionDefinitions


def wrangle_section_data(excel_file: FilePath, config) -> SectionDefinitions:
    df = pd.read_excel(excel_file)
    df = df.iloc[config['headerRowCount']:-config['footerRowCount']]
    df[df.columns[2]] = df.iloc[:, 2].apply(lambda x: x == '+' or x == '#')
    df.fillna(method='ffill', inplace=True)
    df[df.columns[1]] = df.iloc[:, 1].apply(lambda s: s if 'x' in str(s) else f'x{s}')
    df['Section'] = df.iloc[:, 0] + ' ' + df.iloc[:, 1]
    df.drop(df.columns[[0, 1]], axis=1, inplace=True)
    df.rename(columns=config['columnLabels'], inplace=True)
    df.set_index('Section', inplace=True)
    data = df.transpose().to_dict()
    data = {k.translate({32: None}): v for k, v in data.items()}

    for properties in data.values():
        for k, v in properties.items():
            if not isinstance(v, bool):
                try:
                    properties[k] = float(v)
                except ValueError:
                    pass

    return data