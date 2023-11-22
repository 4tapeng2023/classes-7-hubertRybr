from xml_file_processor import FileProcessor

def main():
    processor = FileProcessor()
    filename = "data.xml"

    while True:
        print("\nMenu:")
        print("1. Read File")
        print("2. Add Record")
        print("3. Delete Record")
        print("4. Update Record")
        print("5. Display Records")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            processor.read_file(filename)
        elif choice == "2":
            record = {
                "id": input("Enter ID: "),
                "name": input("Enter Name: "),
                "age": input("Enter Age: "),
                "city": input("Enter City: ")
            }
            processor.add_record(filename, record)
        elif choice == "3":
            record_id = input("Enter ID of the record to delete: ")
            processor.delete_record(filename, record_id)
        elif choice == "4":
            record_id = input("Enter ID of the record to update: ")
            new_record = {
                "age": input("Enter New Age: "),
                "city": input("Enter New City: ")
            }
            processor.update_record(filename, record_id, new_record)
        elif choice == "5":
            processor.display_records(filename)
        elif choice == "6":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()
