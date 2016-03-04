import unittest
from doctest import DocTestSuite
from doctest import DocFileSuite

import sparc.event.persistent

def test_suite():
    return unittest.TestSuite((
        DocFileSuite('alert.txt',
                     package=sparc.event.persistent),))

if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')