import sys
import os
from PyQt6.QtWidgets import QApplication

from src.ui.main_window import MainWindow
from src.utils.backup_manager import BackupManager

def main():
    app = QApplication(sys.path)
    
    # Modern style fusion
    app.setStyle("Fusion")
    
    window = MainWindow()
    window.show()
    
    exit_code = app.exec()
    
    # Run backup when window closes
    BackupManager.create_backup()
    print("Otomatik yedek alındı.")
    
    sys.exit(exit_code)

if __name__ == "__main__":
    main()

