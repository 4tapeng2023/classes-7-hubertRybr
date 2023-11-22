import unittest
from unittest.mock import patch, Mock
from xml_file_processor import FileProcessor


class TestFileProcessor(unittest.TestCase):

    @patch("xml_file_processor.ET.parse")
    def test_read_file(self, mock_parse):
        processor = FileProcessor()
        mock_tree = mock_parse.return_value
        mock_root = mock_tree.getroot.return_value

        result = processor.read_file("test.xml")

        mock_parse.assert_called_once_with("test.xml")
        self.assertEqual(result, mock_root)

    @patch("xml_file_processor.ET.parse")
    @patch("xml_file_processor.FileProcessor._write_to_file")
    def test_add_record(self, mock_write_to_file, mock_parse):
        processor = FileProcessor()
        mock_tree = mock_parse.return_value
        mock_root = mock_tree.getroot.return_value

        record = {"id": "1", "name": "John Doe", "age": "30", "city": "New York"}
        processor.add_record("test.xml", record)

        mock_parse.assert_called_once_with("test.xml")
        mock_write_to_file.assert_called_once_with("test.xml", mock_root)

    @patch("xml_file_processor.ET.parse")
    @patch("xml_file_processor.FileProcessor._write_to_file")
    def test_delete_record(self, mock_write_to_file, mock_parse):
        processor = FileProcessor()
        mock_tree = mock_parse.return_value
        mock_root = mock_tree.getroot.return_value

        processor.delete_record("test.xml", "1")

        mock_parse.assert_called_once_with("test.xml")
        mock_write_to_file.assert_called_once_with("test.xml", mock_root)

    @patch("xml_file_processor.ET.parse")
    @patch("xml_file_processor.FileProcessor._write_to_file")
    def test_update_record(self, mock_write_to_file, mock_parse):
        processor = FileProcessor()
        mock_tree = mock_parse.return_value
        mock_root = mock_tree.getroot.return_value

        new_record = {"age": "31", "city": "Chicago"}
        processor.update_record("test.xml", "1", new_record)

        mock_parse.assert_called_once_with("test.xml")
        mock_write_to_file.assert_called_once_with("test.xml", mock_root)

    @patch("builtins.print")
    @patch("xml_file_processor.ET.parse")
    def test_display_records(self, mock_parse, mock_print):
        processor = FileProcessor()
        mock_tree = mock_parse.return_value
        mock_root = mock_tree.getroot.return_value
        mock_records = [Mock(tag='record', findall=Mock(return_value=["record_data"]))]

        mock_root.findall.return_value = mock_records

        processor.display_records("test.xml")

        


if __name__ == "__main__":
    unittest.main()
