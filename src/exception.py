import sys
import logging
import os
from datetime import datetime

def error_message_detail(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occurred in python script name[{0}] line number [{1}] error message[{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message


class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message


if __name__ == "__main__":
    logs_folder = "logs"  # Specify the folder name where log files will be created

    # Create the logs folder if it doesn't exist
    os.makedirs(logs_folder, exist_ok=True)

    log_file = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
    log_file_path = os.path.join(logs_folder, log_file)

    logging.basicConfig(
        filename=log_file_path,
        format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
        level=logging.INFO,
    )

    try:
        a = 1 / 0
    except Exception as e:
        logging.info("Divide error")
        raise CustomException(str(e), sys)
