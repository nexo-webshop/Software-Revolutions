# gui.py
# External libraries needed: pip install PySide6
# NO MAIL SENDER WITHOUT THIS! THIS IS THE GUI FOR THE SYSTEM! the screen where you are looking at.
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLineEdit, QListWidget, QVBoxLayout, QWidget, QTextEdit
from config import APP_NAME

class NexoMailGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(APP_NAME)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        
        self.search_bar = QLineEdit()
        self.search_bar.setPlaceholderText("Doorzoek je mails met natuurlijke taal...")
        
        self.mail_list = QListWidget()
        self.mail_viewer = QTextEdit()
        self.mail_viewer.setReadOnly(True)

        layout.addWidget(self.search_bar)
        layout.addWidget(self.mail_list)
        layout.addWidget(self.mail_viewer)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def display_mail_list(self, mails):
        """Update de lijst met mail headers."""
        pass

    def show_mail_content(self, mail_id):
        """Haalt mail op, decrypteert deze en toont de tekst."""
        pass

def launch_gui():
    app = QApplication(sys.argv)
    window = NexoMailGUI()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    launch_gui()
