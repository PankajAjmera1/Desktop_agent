import os
import sys
import logging

class InstanceManager:
    @staticmethod
    def check_instance(lock_file='agent.lock'):
        try:
            if os.path.exists(lock_file):
                print(f"Instance already running. Lock file found: {lock_file}")
                logging.info(f"Instance already running. Lock file found: {lock_file}")
                sys.exit(1)  # Exit with a non-zero status to indicate an issue
            else:
                # Create the lock file and write the current process ID
                with open(lock_file, 'w') as f:
                    f.write(str(os.getpid()))
                print(f"Lock file created: {lock_file}")
                logging.info(f"Lock file created: {lock_file}")
        except OSError as e:
            print(f"Failed to create lock file: {e}")
            logging.error(f"Failed to create lock file: {e}")
            sys.exit(1)  # Exit with a non-zero status to indicate an issue

    @staticmethod
    def release_instance(lock_file='agent.lock'):
        try:
            if os.path.exists(lock_file):
                os.remove(lock_file)
                print(f"Lock file removed: {lock_file}")
                logging.info(f"Lock file removed: {lock_file}")
            else:
                print(f"No lock file found to remove: {lock_file}")
                logging.warning(f"No lock file found to remove: {lock_file}")
        except OSError as e:
            print(f"Failed to remove lock file: {e}")
            logging.error(f"Failed to remove lock file: {e}")
