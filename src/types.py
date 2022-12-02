from typing import Dict, List, NewType, Union

"""
A standard string-based filepath representation.
"""
FilePath = NewType('FilePath', str)

"""
The standard section reference (i.e., identifier) used to
denote a specific structural section.
"""
SectionDesignation = NewType('SectionDesignation', str)

"""
The descriptive name given to a specific geometric dimension, material
property, or design characteristic associated with the section.
"""
SectionPropertyName = NewType('SectionPropertyName', str)

"""
The value for a given structural section property.
"""
SectionPropertyValue = NewType('SectionPropertyValue', Union[int, float])

"""
The collection of property names mapped against their respective
property values for a given structural section.
"""
SectionProperties = NewType('SectionProperty', dict[SectionPropertyName, SectionPropertyValue])

"""
Fully defines the given structural sections by mapping their unique
section designations against their respective collection of property
name-value mappings.
"""
SectionDefinitions = NewType('SectionDefinition', dict[SectionDesignation, SectionProperties])

"""
The available set of steel section classifications.
"""
SteelSectionClassification = NewType('SteelSectionClassification', str)

"""
The set of sheet-specific arguments to inject when processing a
specific Excel worksheet. The purpose of this type is to decouple
the wrangling steps from the specific worksheet being operated on.
"""
WranglerConfig = NewType('WranglingConfiguration', Dict[str, Union[str, int, List[str], Dict[str, str]]])

"""
The complete configuration file used by the wrangler to process
the various Excel worksheets that could potentially be injected.
"""
ConfigFile = NewType('ConfigurationFile', Dict[SteelSectionClassification, WranglerConfig])
