import pandas as pd
import json

UB_XLSX_FILE = 'xlsx/UB-Section-Properties-And-Dimensions.xlsx'
SECTION_DESIGNATION = 'Unnamed: 0'
SECTION_MASS_PER_M = 'Unnamed: 1'
FIRST_THREE_COLS = [0, 1, 2]
EMPTY_COL = 'Unnamed: 2'
HEADER_ROWS = 6
FOOTER_ROWS = -6

COLUMN_LABELS = {
  'Mass per metre'            :   'Mass Per Metre (kg/m)',
  'Depth of section'          :   'Depth of Section, h (mm)',
  'Width of section'          :   'Width of Section, b (mm)',
  'Thickness'                 :   'Web Thickness, tw (mm)',
  'Unnamed: 7'                :   'Flange Thickness, tf (mm)',
  'Root radius'               :   'Root Radius, r (mm)',
  'Depth between fillets'     :   'Depth Between Fillets, d (mm)',
  'Ratios for local buckling' :   'Ratios for Local Web Buckling, cw/tw',
  'Unnamed: 11'               :   'Ratios for Local Flange Buckling, cf/tf',
  'Dimensions for detailing'  :   'End Clearance Dimension for Detailing, C (mm)',
  'Unnamed: 13'               :   'Longitudinal Notch Dimension, N (mm)',
  'Unnamed: 14'               :   'Vertical Notch Dimension, n (mm)',
  'Surface area'              :   'Surface Area Per Metre (m2)',
  'Unnamed: 16'               :   'Surface Area Per Tonne (m2)',
  'Second moment of area'     :   'Second Moment of Area, Y-Y (cm4)',
  'Unnamed: 18'               :   'Second Moment of Area, Z-Z (cm4)',
  'Radius of gyration'        :   'Radius of Gyration, Y-Y (cm)',
  'Unnamed: 20'               :   'Radius of Gyration, Z-Z (cm)',
  'Elastic modulus'           :   'Elastic Modulus, Y-Y (cm3)',
  'Unnamed: 22'               :   'Elastic Modulus, Z-Z (cm3)',
  'Plastic modulus'           :   'Plastic Modulus, Y-Y (cm3)',
  'Unnamed: 24'               :   'Plastic Modulus, Z-Z (cm3)',
  'Buckling parameter'        :   'Buckling Parameter, U',
  'Torsional index'           :   'Torsional Index, X',
  'Warping constant'          :   'Warping Constant, Iw (dm6)',
  'Torsional constant'        :   'Torsional Constant, IT (cm4)',
  'Area of section'           :   'Area of Section, A (cm2)'
}

df = pd.read_excel(UB_XLSX_FILE, skiprows=HEADER_ROWS)
df = df.iloc[:FOOTER_ROWS]
df.drop(EMPTY_COL, axis=1, inplace=True)
df.drop(FIRST_THREE_COLS, axis=0, inplace=True)
df.fillna(method='ffill', inplace=True)
df['UB Section Designation'] = (df[SECTION_DESIGNATION] + ' ' + df[SECTION_MASS_PER_M]).str.strip()
df.drop([SECTION_DESIGNATION, SECTION_MASS_PER_M], axis=1, inplace=True)
df.rename(columns=COLUMN_LABELS, inplace=True)
df.set_index('UB Section Designation', inplace=True)
dict = df.transpose().to_dict()

for section, properties in dict.items():
    for k, v in properties.items(): 
        properties[k] = float(v)

with open('UB-Sections.json', mode='w', encoding='utf-8') as f:
    json.dump(dict, f)
    