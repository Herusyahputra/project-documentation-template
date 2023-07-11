#######################################################
# the application for implementation MoilSDK
# writen by Haryanto
# email: M07158031@o365.mcut.edu.tw
#######################################################
from Ui_Controler import *


def main():
    apps = QtWidgets.QApplication(sys.argv)
    window = Controller()
    window.show()
    sys.exit(apps.exec_())


if __name__ == '__main__':
    main()
