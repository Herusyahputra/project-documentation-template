#########################################################################
#   MoilApp (Applications for sophisticated fisheye image processing)   #
#   Written by Haryanto (haryanto@o3635.mcut.edu.tw)                    #
#   Based on Moil-Lab (Ming Chi University of Technology)               #
#########################################################################
# try:
import sys
from PyQt5 import QtWidgets
from Moilapp_Controller import Controller


def main():
    """
    Create instance Main window to create the main window of Application.

    Returns:
        None.
    """

    apps = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Controller(MainWindow)
    MainWindow.show()
    sys.exit(apps.exec_())


if __name__ == '__main__':
    main()

# except ImportError as err:
#     print("\nThe environment not match requirement, "
#           "\nPlease install all the library, or read the Readme doc to do it.")
#     print("-----------------------------------------------------------------")
#     print(err)
