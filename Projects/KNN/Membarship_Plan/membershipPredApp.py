# GUI Application Code Base
import tkinter as tk
from tkinter import ttk
import logging


logging.basicConfig(
    format='%(asctime)s %(levelname)-8s [%(filename)s : %(lineno)d] %(message)s',
    datefmt='%d-%m-%Y %H:%M:%S',
    level='DEBUG',
    filename='telecom_membership_pred_log.txt'
)

logger = logging.getLogger('test_logger')



if __name__ == '__main__':
    root = tk.Tk()
    root.title("Membership Plan Prediction")

    # gui window dimension
    root.geometry("500x250")

    # Create Panedwindow
    panedwindow = ttk.Panedwindow(root, orient=tk.HORIZONTAL)
    panedwindow.pack(fill=tk.BOTH, expand=True)

    # Create Frames to panedwindow
    frame1 = ttk.Frame(panedwindow, width=250, height=250, relief=tk.SUNKEN)
    frame2 = ttk.Frame(panedwindow, width=250, height=250, relief=tk.SUNKEN)
    panedwindow.add(frame1, weight=1)
    panedwindow.add(frame2, weight=1)

    root.mainloop()
