
# Parse specified cats information from a file.
# Each line in the file contains a cat's id, name and age separated by a comma.
# parameters:
#   path: the path to the cat data file.
# The function returns a list of dictionaries containing cat information ("id", "name", "age"), 
# or raises an exception if an error occurs.
def get_cats_info(path: str) -> list[dict[str, str]]:
    cats = []

    with open(path, "r", encoding='utf-8') as cats_file:
        for line_number, line in enumerate(cats_file, start=1):
            line = line.rstrip("\r\n")
            try:
                cat_id, cat_name, cat_age = line.split(',')
                cats.append({"id": cat_id, "name": cat_name, "age": cat_age})
            except ValueError as e:
                raise ValueError(f"Could not parse cat record at line {line_number}: {line}") from e

    return cats


# Example usage:
def main():
    try:

        cats_info = get_cats_info("assets/cats.txt")
        print(cats_info)

    except FileNotFoundError as e:
        print(f"Cats file not found: {e}")

    except PermissionError as e:
        print(f"Access denied to cats file: {e}")

    except ValueError as e:
        print(f"Invalid cat record: {e}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
