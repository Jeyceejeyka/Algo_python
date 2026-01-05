"""
Unit 8 Assignment: Dictionary Inversion with Files and Exception Handling
"""

def read_dictionary(filename):
    data = {}

    try:
        with open(filename, "r") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue

                key, values = line.split(":")
                value_list = values.split(",")

                data[key] = value_list

    except FileNotFoundError:
        print("Error: Input file not found.")
    except Exception as e:
        print("Unexpected error:", e)

    return data


def invert_dictionary(original_dict):
    inverted = {}

    for key, values in original_dict.items():
        for value in values:
            if value not in inverted:
                inverted[value] = []
            inverted[value].append(key)

    return inverted


def write_dictionary(filename, dictionary):
    with open(filename, "w") as file:
        for key, values in dictionary.items():
            line = "%s:%s\n" % (key, ",".join(values))
            file.write(line)


def main():
    input_file = "original_dict.txt"
    output_file = "inverted_dict.txt"

    original = read_dictionary(input_file)
    inverted = invert_dictionary(original)

    print("Original Dictionary:")
    print(original)

    print("\nInverted Dictionary:")
    print(inverted)

    write_dictionary(output_file, inverted)


if __name__ == "__main__":
    main()
