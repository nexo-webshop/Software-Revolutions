# config.py
import os

# Project Instellingen
APP_NAME = "Nexo Mail"
VERSION = "000.001"

# Paden
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "nexo_mail.db")
LOG_PATH = os.path.join(BASE_DIR, "logs")

# Beveiliging (Placeholders voor keys)
SECRET_KEY = "nexo-super-secret-key"
ENCRYPTION_LAYERS = ["AES", "RSA/ECC", "HMAC", "Obfuscation"]

# AI Instellingen
EMBEDDING_MODEL = "all-MiniLM-L6-v2"  # Voor sentence-transformers

# GUI Instellingen
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 800
