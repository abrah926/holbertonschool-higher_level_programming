#!/usr/bin/env python3
import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Converts a CSV file to JSON format and writes the result to data.json.
    Parameters:
    - csv_filename: The name of the CSV file to be converted.

    Returns:
    - True if the conversion is successful, False if an exception occurs.
    """
    try:
        with open(csv_filename, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)

            data = [row for row in csv_reader]

        if not data:
            print("No data found in the CSV file.")
            return False

        with open('data.json', mode='w') as json_file:
            json.dump(data, json_file, indent=4)

        return True

    except FileNotFoundError:
        print(f"The file {csv_filename} does not exist.")
        return False

    except Exception as e:
        print(f"An error occurred while processing the CSV file: {e}")
        return False
