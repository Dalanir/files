import pandas as pd
import numpy as np

from pydantic import BaseModel
from typing import List

from .utils.data_bit import Label, Value
from .utils.generator_utils import generate_breakdown_column, generate_numeric_column


class Barchart(BaseModel):
    domain: str
    label: Label
    value: Value
    groups: Label = None
    filters: List[Label] = []
    report: Label

    def generateFakeData(self):
        # init
        data = pd.DataFrame({self.label.column_name: self.label.values_list})

        # groups
        if self.groups:
            data = generate_breakdown_column(data, self.groups)

        for filter_ in self.filters:
            data = generate_breakdown_column(data, filter_)

        # add numerics values
        data = generate_numeric_column(data, self.value)

        return data

