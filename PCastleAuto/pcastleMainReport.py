import os
import subprocess
from datetime import datetime
from dotenv import load_dotenv
from PCastleAuto.file_operations import get_latest_report_directory, rename_report_file
from PCastleAuto.run import run_pingcastle_process
from PCastleAuto.data_processing import filter_computers

load_dotenv()

# Fetch paths
START_DIRECTORY = os.getenv('START_DIRECTORY')
PINGCASTLE_PATH = os.getenv('PINGCASTLE_PATH')
DOMAIN = os.getenv('DOMAIN')
CREATION_FLAGS = subprocess.CREATE_NEW_CONSOLE

def get_datetime_folder_name():
    return datetime.now().strftime("PCastle_%Y%m%d_%H%M%S")

def main():
    current_folder_name = get_datetime_folder_name()
    report_directory = os.path.join(START_DIRECTORY, current_folder_name)

    previous_report_directory = get_latest_report_directory(START_DIRECTORY, exclude=current_folder_name)

    if not os.path.exists(report_directory):
        os.makedirs(report_directory)

    os.chdir(report_directory)

    run_pingcastle_process([PINGCASTLE_PATH, "--scanner", "share", "--scmode-server", "--datefile"], CREATION_FLAGS)
    new_report_path = rename_report_file(report_directory, "ad_scanner_share_autuni.aut.ac.nz.txt", "ad_scanner_share_autuni.aut.ac.nz.csv")

    prev_report_path = os.path.join(previous_report_directory, "ad_scanner_share_autuni.aut.ac.nz.csv")

    if os.path.exists(prev_report_path):
        filter_computers(prev_report_path, new_report_path, os.path.join(START_DIRECTORY, "different_rows.csv"))
    else:
        print(f"Previous report not found: {prev_report_path}")

if __name__ == "__main__":
    main()