import pandas as pd
import numpy as np
from numpy.random import rand
from mutils.pandas import Processor as p
import unittest


class TestProcessor(unittest.TestCase):
    def test_exclude_cols(self):
        df = pd.DataFrame({"A": rand(10), "B": rand(10), "C": rand(10), "D": rand(10)})

        df = p(df).exclude_cols(["B", "D"]).get()
        self.assertTrue((df.columns == ["A", "C"]).all())

    def test_exclude_cols_regex(self):
        cols = ["fooA", "barB", "fooC", "foobarD", "barfooZ"]
        df = pd.DataFrame({col: rand(15) for col in cols})
        df = p(df).exclude_cols(["foo.*"]).get()
        
        self.assertTrue((df.columns == ["barB", "barfooZ"]).all())

    def test_keep_dtypes(self):
        df = pd.DataFrame({
            "A": rand(10),
            "B": rand(10).astype("int64"),
            "C": rand(10).astype("int64"),
            "D": rand(10),
            "E": rand(10).astype("str"),
            "F": rand(10).astype("str")
        })

        df1 = p(df).keep_dtypes(["int64"]).get()
        self.assertTrue((df1.columns == ["B", "C"]).all())

        df2 = p(df).keep_dtypes(["object", "float64"]).get()
        self.assertTrue((df2.columns == ["A", "D", "E", "F"]).all())


if __name__ == "__main__":
    unittest.main()
