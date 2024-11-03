import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from ui_main_window import Ui_MainWindow


class MainWindow:
    def __init__(self):
        """
        Initialise game window
        """
        # --- setup GUI elements
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)
        
        # --- initialise variables
        
        
        # --- initialise GUI
        self.signals()
        

    def show(self):
        """
        Displays main window
        """
        self.main_win.show()
        
        
    def signals(self):
        """
        Connects the UI buttons to the corresponding functions (see slots)
        """
        pass
    
    
    # ---- SLOTS ---- #
    """
    functions that are called from the signals go below here
    """
    


if __name__ == '__main__':
    # starts application
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())