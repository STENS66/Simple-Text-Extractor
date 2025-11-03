# -*- coding: utf-8 -*-
"""
Simple Text Extractor - Version 1.0

Copyright © Gaëtan Sencie 2025
Tous droits réservés.
"""

import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import os
import sys
import shutil
import multiprocessing
import threading
import logging
import queue
import re
import time
import tempfile
import subprocess
from pathlib import Path
import contextlib
import traceback 
import webbrowser


# NOUVEAUX IMPORTS REQUIS
try:
    import pypdfium2 as pdfium
except ImportError:
    pdfium = None



CODE SOUS LICENCE 






if __name__ == "__main__":
    multiprocessing.freeze_support() 
    app = OCRApp()
    app.mainloop()
