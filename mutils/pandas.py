from typing import Tuple, List
import pandas as pd 
import time 
import re 
import functools

class Processor:
    def __init__(self, dataframe: pd.DataFrame):
        self._df = dataframe
    
    def get(self):
        return self._df.copy()

    def __repr__(self) -> str:
        return self._df.__repr__
    
    def __str__(self) -> str:
        return self._df.__str__
    
    def keep_dtypes(self, keep_dt: List[str]):
        df = self._df.copy()

        keep_cols = []
        dtypes = df.dtypes

        for col in df.columns:
            if dtypes[col] in keep_dt:
                keep_cols.append(col)
        
        df = df[keep_cols]

        return Processor(df)

    def exclude_cols(self, exclude_cols: List[str]):
        df = self._df.copy()
        keep_cols = []

        for col in df.columns:
            keep = True 
            for pattern in exclude_cols:
                if re.match(pattern, col):
                    keep = False
                    break
            if keep:
                keep_cols.append(col)
        
        df = df[keep_cols]

        return Processor(df)