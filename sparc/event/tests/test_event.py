import unittest
from doctest import DocTestSuite
from doctest import DocFileSuite

import sparc.event

def test_suite():
    return unittest.TestSuite((
        DocFileSuite('event.txt',
                     package=sparc.event),))

if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')