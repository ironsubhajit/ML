# GUI Application Code Base
import tkinter as tk
import logging


logging.basicConfig(
    format='%(asctime)s %(levelname)-8s [%(filename)s : %(lineno)d] %(message)s',
    datefmt='%d-%m-%Y %H:%M:%S',
    level='DEBUG',
    filename='telecom_membership_pred_log.txt'
)

logger = logging.getLogger('test_logger')
