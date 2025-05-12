import time
from loguru import logger
from pathlib import Path
import os
 

log_path = ".//log/"
t = time.strftime("%Y_%m_%d")
 
 
# class Loggings:
 
#     def __new__(cls, *args, **kwargs):
#         logger = loguru.logger
#         logger.add(log_path = log_path, encoding="utf-8",
#                    enqueue=True, retention="10 days")
#         return logger
 

class Loggings:
    logger.add(f"{log_path}/file_{t}.log", rotation="500MB", encoding="utf-8", enqueue=True,
               retention="10 days")
    def get_hande(self):
        return logger
