"""this is a test"""
import unittest
from unittest.mock import mock_open, patch
from jvpm.class_file import ClassFile
class TestClassFile(unittest.TestCase):
    """this class tests the ClassFileClass"""
    def setUp(self):
        """set up the test"""
        mock_object = mock_open(read_data=b'\xca\xfe\xba\xbe\x00\x00\x00\x34\x00\x0f\x0a\x00\x03\x00\x0c\x07' +
                                              b'\x00\x0d\x07\x00\x0e\x01\x00\x06\x3c\x69\x6e\x69\x74\x3e\x01\x00' +
                                              b'\x03\x28\x29\x56\x01\x00\x04\x43\x6f\x64\x65\x01\x00\x0f\x4c\x69' +
                                              b'\x6d\x61\x69\x6e\x01\x00\x16\x28\x5b\x4c\x6a\x61\x76\x61\x2f\x6c' +
                                              b'\x61\x6e\x67\x2f\x53\x74\x72\x69\x6e\x67\x3b\x29\x56\x01\x00\x0a' +
                                              b'\x53\x6f\x75\x72\x63\x65\x46\x69\x6c\x65\x01\x00\x0b\x73\x69\x6d' +
                                              b'\x53\x6f\x75\x72\x63\x65\x46\x69\x6c\x65\x01\x00\x0b\x73\x69\x6d' +
                                              b'\x70\x6c\x65\x2e\x6a\x61\x76\x61\x0c\x00\x04\x00\x05\x01\x00\x04' +
                                              b'\x74\x65\x73\x74\x01\x00\x10\x6a\x61\x76\x61\x2f\x6c\x61\x6e\x67' +
                                              b'\x2f\x4f\x62\x6a\x65\x63\x74\x00\x20\x00\x02\x00\x03\x00\x00\x00' +
                                              b'\x00\x00\x02\x00\x00\x00\x04\x00\x05\x00\x01\x00\x06\x00\x00\x00' +
                                              b'\x1d\x00\x01\x00\x01\x00\x00\x00\x05\x2a\xb7\x00\x01\xb1\x00\x00' +
                                              b'\x00\x01\x00\x07\x00\x00\x00\x06\x00\x01\x00\x00\x00\x01\x00\x08' +
                                              b'\x00\x08\x00\x09\x00\x01\x00\x06\x00\x00\x00\x1e\x00\x01\x00\x02' +
                                              b'\x00\x00\x00\x06\x04\x3c\x84\x01\x01\xb1\x00\x00\x00\x01\x00\x07' +
                                              b'\x00\x00\x00\x06\x00\x01\x00\x00\x00\x01\x00\x01\x00\x0a\x00\x00' +
                                              b'\x00\x02\x00\x0b')
        with patch('builtins.open', mock_object):
            self.class_file = ClassFile('jvpm/Test.class')

    def test_magic(self):
        """tests the get_magic method"""
        self.assertEqual(self.class_file.get_magic(), b'\xCA\xFE\xBA\xBE')

    def test_minor(self):
        """tests the get_minor method"""
        self.assertEqual(self.class_file.get_minor(), b"\x00\x00")

    def test_major(self):
        """tests the get_major method"""
        self.assertEqual(self.class_file.get_major(), b'\x004')

    def test_constant_pool_count(self):
        """tests the get_constant_pool_count method"""
        self.assertEqual(self.class_file.get_constant_pool_count(), b"\x00\x0f")
