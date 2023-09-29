import argparse
import os
import shutil
import time
import logging

DIR_BACKUP = "replica"
LOG_FILE = "log_file.log"


def log_setup(log_file):
    # setup log file
    logging.basicConfig(
        format='%(asctime)s %(levelname)5s: %(message)s',
        level=logging.INFO,
        handlers=[logging.FileHandler(log_file), logging.StreamHandler()]
                        )


def p_args():
    # parser args from bash
    parser = argparse.ArgumentParser(
        description="Folder synchronization"
        )
    parser.add_argument(
        "dir_source", help="Source folder path"
        )
    parser.add_argument(
        "interval", type=int, help="Synchronization interval in seconds"
        )
    return parser.parse_args()


def copy_folders(dir_source, DIR_BACKUP):
    # make copy form source directory to backup
    try:
        # Check if source folder exists
        if not os.path.exists(dir_source):
            logging.error(
                f"Source folder '{os.path.abspath(dir_source)}' don´t exist."
                         )
            return

        # Sync folder
        if os.path.exists(DIR_BACKUP):
            shutil.rmtree(DIR_BACKUP)
        shutil.copytree(dir_source, DIR_BACKUP)

        logging.info(
            f"Copy successful:"
            f"'{os.path.abspath(dir_source)},"
            f" to '{os.path.abspath(DIR_BACKUP)}'")

    except Exception as e:
        logging.error(f"Copy error: {e}")


def run():
    # run copy dir process
    logging.info(
        ('Folder sync is starting copy data from'
         ' %s folder to %s folder. Path log file: %s'),
        (os.path.abspath(args.dir_source)),
        (os.path.abspath(DIR_BACKUP)),
        (os.path.abspath(LOG_FILE))
                )
    while True:
        copy_folders(args.dir_source, DIR_BACKUP)
        time.sleep(args.interval)


args = p_args()
log_setup(LOG_FILE)
run()
