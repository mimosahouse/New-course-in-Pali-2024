# python3.10 "6. Vault/scripts/update_properties_time_format.py" "2. Track"

import os
import re
import argparse
from datetime import datetime


class MarkdownDateTimeUpdater:
    """
    A class to update datetime formats in Markdown files within a given directory.
    
    Attributes
    ----------
    directory : str
        The root directory to search for Markdown files.
    datetime_pattern : re.Pattern
        A regex pattern to match datetime strings in the format 'dd-mm-yyyy hh:mm:ss'.
    
    Methods
    -------
    process_markdown_files():
        Processes all Markdown files in the given directory (including subdirectories)
        and updates the datetime format.
    convert_datetime_format(match: re.Match) -> str:
        Converts the matched datetime to the new desired format.
    """

    def __init__(self, directory):
        """
        Constructs the necessary attributes for the MarkdownDateTimeUpdater object.

        Parameters
        ----------
        directory : str
            The root directory to search for Markdown files.
        """
        self.directory = directory
        # Regex to match datetime in the format '29-09-2024 22:09:43'
        self.datetime_pattern = re.compile(r'\b(\d{2})-(\d{2})-(\d{4}) (\d{2}:\d{2}:\d{2})\b')

    def process_markdown_files(self):
        """
        Processes all Markdown files in the given directory (including subdirectories)
        and updates the datetime format from 'dd-mm-yyyy hh:mm:ss' to 'yyyy-mm-dd hh:mm:ss'.
        """
        for root, _, files in os.walk(self.directory):
            for file in files:
                if file.endswith('.md'):
                    file_path = os.path.join(root, file)
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()

                    # Replace all matches of the datetime format
                    updated_content = self.datetime_pattern.sub(lambda m: self.convert_datetime_format(m), content)

                    # Write updated content back to file if changes were made
                    if content != updated_content:
                        with open(file_path, 'w', encoding='utf-8') as f:
                            f.write(updated_content)
                        print(f"Updated datetime format in: {file_path}")

    @staticmethod
    def convert_datetime_format(match):
        """
        Converts the matched datetime to the new desired format 'yyyy-mm-dd hh:mm:ss'.

        Parameters
        ----------
        match : re.Match
            A regex match object containing the datetime components.

        Returns
        -------
        str
            The datetime string in the new format 'yyyy-mm-dd hh:mm:ss' if valid, otherwise returns the original string.
        """
        try:
            day, month, year, time = match.groups()
            hours, minutes, seconds = map(int, time.split(':'))

            # Validate time components
            if not (0 <= hours < 24 and 0 <= minutes < 60 and 0 <= seconds < 60):
                raise ValueError("Invalid time component(s)")

            # Convert to new format 'yyyy-mm-dd hh:mm:ss'
            new_datetime = datetime.strptime(f"{day}-{month}-{year} {time}", "%d-%m-%Y %H:%M:%S")
            return new_datetime.strftime("%Y-%m-%d %H:%M:%S")
        except ValueError as e:
            print(f"Error parsing datetime: {match.group(0)}")
            print(f"Error details: {e}")
            # Return the original matched string if there is an error
            return match.group(0)


def main():
    """
    Main function to run the MarkdownDateTimeUpdater via command-line interface.
    """
    parser = argparse.ArgumentParser(description="Update datetime formats in Markdown files within a specified directory.")
    parser.add_argument('directory', type=str, help="The root directory to search for Markdown files.")
    args = parser.parse_args()

    # Create an instance of MarkdownDateTimeUpdater and process the files
    updater = MarkdownDateTimeUpdater(args.directory)
    updater.process_markdown_files()


if __name__ == "__main__":
    main()
