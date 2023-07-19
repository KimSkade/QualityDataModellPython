
import unittest.util

from aas2openapi.models.base import AAS, Submodel, SubmodelElementCollection
from typing import Optional, List, Union
from aas2openapi.models.base import qualityData
from txtEinlesen import getValuefromColumName

dateipfad = "C:\\Users\\kim0_\\Desktop\\Masterarbeit\\PruefplanValidierungsbauteil1_16.txt"
breakpoint = "END"

def createAASQualityDatafromKMG(dateipfad, breakpoint):
    i = 1
    while breakpoint != getValuefromColumName(dateipfad, "planid", i):
        result = qualityData.Result(
            id_short="result" + i,
            semantic_id="http://www.google.de/1",
            description="xyz",
            value=float(getValuefromColumName(dateipfad, "actual", i)),
            measureDate="Platzhalte Datum Uhrzeit",     #Quelle MeasureDate
            uppertol=float(getValuefromColumName(dateipfad, "uppertol", i)),
            lowertol=float(getValuefromColumName(dateipfad, "lowertol", i)),
            nominal=float(getValuefromColumName(dateipfad, "nominal", i)),
            resultCheck= True,  #Formel für ResultCheck anpassen
        )
        print(result)
        i += 1
