# test_portalyarn.py
"""
Tests for PortalYarn module.
"""

import unittest
from portalyarn import PortalYarn

class TestPortalYarn(unittest.TestCase):
    """Test cases for PortalYarn class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = PortalYarn()
        self.assertIsInstance(instance, PortalYarn)
        
    def test_run_method(self):
        """Test the run method."""
        instance = PortalYarn()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
