import sys
from PyQt5.QtWidgets import QApplication
from ui import EmployeeUI
from employee import EmployeeManager

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = EmployeeUI()
    manager = EmployeeManager(ui)
    
    ui.add_btn.clicked.connect(manager.add_employee)
    ui.update_btn.clicked.connect(manager.update_employee)
    ui.delete_btn.clicked.connect(manager.delete_employee)
    ui.clear_btn.clicked.connect(ui.clear_inputs)
    ui.search_btn.clicked.connect(manager.search_employee)
    ui.export_btn.clicked.connect(manager.export_to_csv)
    ui.import_btn.clicked.connect(manager.import_from_csv)
    ui.table.itemClicked.connect(manager.get_selected_row)
    
    ui.show()
    sys.exit(app.exec_())