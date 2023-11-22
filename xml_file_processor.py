import xml.etree.ElementTree as ET


class FileProcessor:
    def read_file(self, filename):
        try:
            tree = ET.parse(filename)
            root = tree.getroot()
            return root
        except FileNotFoundError:
            print(f"File {filename} not found.")
            return None
        except ET.ParseError:
            print(f"Error parsing XML file {filename}.")
            return None

    def add_record(self, filename, record):
        root = self.read_file(filename)
        if root is not None:
            record_element = ET.Element("record")
            for key, value in record.items():
                field = ET.SubElement(record_element, key)
                field.text = str(value)
            root.append(record_element)
            self._write_to_file(filename, root)
            print("Record added successfully.")

    def delete_record(self, filename, record_id):
        root = self.read_file(filename)
        if root is not None:
            record_to_delete = root.find(f"./record[id='{record_id}']")
            if record_to_delete is not None:
                root.remove(record_to_delete)
                self._write_to_file(filename, root)
                print(f"Record with ID {record_id} deleted successfully.")
            else:
                print(f"Record with ID {record_id} not found.")

    def update_record(self, filename, record_id, new_record):
        root = self.read_file(filename)
        if root is not None:
            record_to_update = root.find(f"./record[id='{record_id}']")
            if record_to_update is not None:
                for key, value in new_record.items():
                    field = record_to_update.find(key)
                    if field is not None:
                        field.text = str(value)
                    else:
                        new_field = ET.SubElement(record_to_update, key)
                        new_field.text = str(value)
                self._write_to_file(filename, root)
                print(f"Record with ID {record_id} updated successfully.")
            else:
                print(f"Record with ID {record_id} not found.")

    def display_records(self, filename):
        root = self.read_file(filename)
        if root is not None:
            pass

    def _write_to_file(self, filename, root):
        tree = ET.ElementTree(root)
        tree.write(filename)


