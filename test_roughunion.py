# test_roughunion.py
"""
Tests for RoughUnion module.
"""

import unittest
from roughunion import RoughUnion

class TestRoughUnion(unittest.TestCase):
    """Test cases for RoughUnion class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = RoughUnion()
        self.assertIsInstance(instance, RoughUnion)
        
    def test_run_method(self):
        """Test the run method."""
        instance = RoughUnion()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
