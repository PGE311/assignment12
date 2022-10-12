#!/usr/bin/env python

# Copyright 2020-2021 John T. Foster
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import unittest
import nbconvert

import numpy as np



with open("assignment12.ipynb") as f:
    exporter = nbconvert.PythonExporter()
    python_file, _ = exporter.from_file(f)

with open("assignment12.py", "w") as f:
    f.write(python_file)

from assignment12 import Matrix 

class TestSolution(unittest.TestCase):

    def test_row_swap(self):

        x = [[1, 2], [3, 4]]
        A = Matrix(x)
        A.row_swap(0, 1)
        np.testing.assert_equal(A(), np.array([[3, 4], [1, 2]]))

    def test_row_multiply(self):

        x = [[1, 2], [3, 4]]
        A = Matrix(x)
        A.row_multiply(0, 10)
        np.testing.assert_equal(A(), np.array([[10, 20], [3, 4]]))

    def test_row_combine(self):

        x = [[1, 2], [3, 4]]
        A = Matrix(x)
        A.row_combine(0, 1, -10)
        np.testing.assert_equal(A(), np.array([[31, 42], [3, 4]]))

    def test_row_swap_private(self):

        x = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
        A = Matrix(x)
        A.row_swap(1, 2)
        np.testing.assert_equal(A(), np.array([[0, 1, 2], [6, 7, 8], [3, 4, 5]]))

    def test_row_multiply_private(self):

        x = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
        A = Matrix(x)
        A.row_multiply(1, 20)
        np.testing.assert_equal(A(), np.array([[0, 1, 2], [60, 80, 100], [6, 7, 8]]))

    def test_row_combine_private(self):

        x = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
        A = Matrix(x)
        A.row_combine(2, 1, -12)
        np.testing.assert_equal(A(), np.array([[ 0,  1,  2], [ 3,  4,  5], [42, 55, 68]]))


if __name__ == '__main__':
    unittest.main()
