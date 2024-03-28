import os
import logging
from datetime import datetime

from exception import CustomException

LOG_FOLDER = f'{datetime.now().strftime("%m_%d_%Y")}'
LOG_FILE = f'{datetime.now().strftime("%m_%d_%Y_%H_%M_%S")}.log'

logs_path = os.path.join(os.getcwd(), "logs",LOG_FOLDER)
os.makedirs(logs_path, exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# print("logs_path", logs_path)
# print("LOG_FILE", LOG_FILE)
# print("LOG_FILE_PATH", LOG_FILE_PATH)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format='%(asctime)s - %(levelname)s - %(message)s', 
    level=logging.INFO
)

# if __name__ == "__main__":
#     logging.info("Logging has started")