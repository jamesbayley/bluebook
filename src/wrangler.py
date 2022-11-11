import pandas as pd

from src.types import FilePath, SectionDefinitions


def wrangle_universal_sections(excel_file: FilePath) -> SectionDefinitions:
    """
    Wrangle universal beam/column (UB/UC) .xlsx files as the
    pre-processing step in the export engineering pipeline.
    """

    header_row_count = 9
    footer_row_count = 6

    column_labels = {
        'Eurocode 3 (in accordance with the UK National Annex) (BS EN 10365: 2017)': 'Section Designation',
        'Unnamed: 1': 'Section Mass Per Metre',
        'Unnamed: 2': 'Empty Column',
        'Unnamed: 3': 'Mass Per Metre (kg/m)',
        'Unnamed: 4': 'Depth of Section, h (mm)',
        'Unnamed: 5': 'Width of Section, b (mm)',
        'Unnamed: 6': 'Web Thickness, tw (mm)',
        'Unnamed: 7': 'Flange Thickness, tf (mm)',
        'Unnamed: 8': 'Root Radius, r (mm)',
        'Unnamed: 9': 'Depth Between Fillets, d (mm)',
        'Unnamed: 10': 'Ratios for Local Web Buckling, cw/tw',
        'Unnamed: 11': 'Ratios for Local Flange Buckling, cf/tf',
        'Unnamed: 12': 'End Clearance Dimension for Detailing, C (mm)',
        'Unnamed: 13': 'Longitudinal Notch Dimension, N (mm)',
        'Unnamed: 14': 'Vertical Notch Dimension, n (mm)',
        'Unnamed: 15': 'Surface Area Per Metre (m2)',
        'Unnamed: 16': 'Surface Area Per Tonne (m2)',
        'Unnamed: 17': 'Second Moment of Area, Y-Y (cm4)',
        'Unnamed: 18': 'Second Moment of Area, Z-Z (cm4)',
        'Unnamed: 19': 'Radius of Gyration, Y-Y (cm)',
        'Unnamed: 20': 'Radius of Gyration, Z-Z (cm)',
        'Unnamed: 21': 'Elastic Modulus, Y-Y (cm3)',
        'Unnamed: 22': 'Elastic Modulus, Z-Z (cm3)',
        'Unnamed: 23': 'Plastic Modulus, Y-Y (cm3)',
        'Unnamed: 24': 'Plastic Modulus, Z-Z (cm3)',
        'Unnamed: 25': 'Buckling Parameter, U',
        'Unnamed: 26': 'Torsional Index, X',
        'Unnamed: 27': 'Warping Constant, Iw (dm6)',
        'Unnamed: 28': 'Torsional Constant, IT (cm4)',
        'Unnamed: 29': 'Area of Section, A (cm2)'
    }

    df = pd.read_excel(excel_file, skiprows=0)
    df.rename(columns=column_labels, inplace=True)
    df = df.iloc[header_row_count:-footer_row_count]
    df.fillna(method='ffill', inplace=True)
    df['UB Section Designation'] = df['Section Designation'] + ' ' + df['Section Mass Per Metre']
    df.drop(['Section Designation', 'Section Mass Per Metre'], axis=1, inplace=True)
    df.drop('Empty Column', axis=1, inplace=True)
    df.set_index('UB Section Designation', inplace=True)
    data = df.transpose().to_dict()

    return data


def coerce_section_def_values_to_float(data: SectionDefinitions) -> SectionDefinitions:
    """
    Cycles through the steel section definition properties and casts
    all values to float. This is required because by default the
    Pandas DataFrame presumes all values to be strings.
    """

    for properties in data.values():
        for k, v in properties.items():
            properties[k] = float(v)

    return data
