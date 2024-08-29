import widgets as widg
if __name__ == "__main__":
    import sys
    app = widg.QtWidgets.QApplication(sys.argv)
    w = widg.Window()
    w.show()
    sys.exit(app.exec_())