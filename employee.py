import csv
from PyQt5.QtWidgets import QMessageBox, QFileDialog
import database

class EmployeeManager:
    def __init__(self, ui):
        self.ui = ui
        database.create_database()
        self.load_data()

    def load_data(self):
        employees = database.fetch_all_employees()
        self.ui.table.setRowCount(0)
        for row_number, row_data in enumerate(employees):
            self.ui.table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                if column_number == 3:  # Kolom gaji
                    data = f"Rp {int(data):,}".replace(",", ".")
                self.ui.table.setItem(row_number, column_number, self.ui.create_table_item(data))

    def add_employee(self):
        id = self.ui.id_input.text()
        name = self.ui.name_input.text()
        position = self.ui.position_input.text()
        salary = self.ui.salary_input.text().replace(".", "")
        address = self.ui.address_input.text()
        phone = self.ui.phone_input.text()

        if id and name and position and salary:
            try:
                # Check if employee already exists
                existing_employee = database.fetch_employee_by_id(id)
                if existing_employee:
                    QMessageBox.warning(self.ui, "Error", "ID Pegawai sudah ada!")
                else:
                    database.add_employee(id, name, position, salary, address, phone)
                    self.load_data()
                    self.ui.clear_inputs()
                    QMessageBox.information(self.ui, "Sukses", "Pegawai berhasil ditambahkan!")
            except Exception as e:
                QMessageBox.warning(self.ui, "Error", f"Terjadi kesalahan: {e}")
        else:
            QMessageBox.warning(self.ui, "Error", "Harap isi semua field!")

    def update_employee(self):
        id = self.ui.id_input.text()
        name = self.ui.name_input.text()
        position = self.ui.position_input.text()
        salary = self.ui.salary_input.text().replace(".", "")
        address = self.ui.address_input.text()
        phone = self.ui.phone_input.text()

        if id and name and position and salary:
            try:
                database.update_employee(id, name, position, salary, address, phone)
                self.load_data()
                self.ui.clear_inputs()
                QMessageBox.information(self.ui, "Sukses", "Pegawai berhasil diubah!")
            except Exception as e:
                QMessageBox.warning(self.ui, "Error", f"Terjadi kesalahan: {e}")
        else:
            QMessageBox.warning(self.ui, "Error", "Harap isi semua field!")

    def delete_employee(self):
        id = self.ui.id_input.text()
        if id:
            database.delete_employee(id)
            self.load_data()
            self.ui.clear_inputs()
            QMessageBox.information(self.ui, "Sukses", "Pegawai berhasil dihapus!")
        else:
            QMessageBox.warning(self.ui, "Error", "Pilih pegawai yang akan dihapus!")

    def get_selected_row(self):
        selected_row = self.ui.table.currentRow()
        self.ui.id_input.setText(self.ui.table.item(selected_row, 0).text())
        self.ui.name_input.setText(self.ui.table.item(selected_row, 1).text())
        self.ui.position_input.setText(self.ui.table.item(selected_row, 2).text())
        salary = self.ui.table.item(selected_row, 3).text().replace("Rp ", "").replace(".", "")
        self.ui.salary_input.setText(salary)
        self.ui.address_input.setText(self.ui.table.item(selected_row, 4).text())
        self.ui.phone_input.setText(self.ui.table.item(selected_row, 5).text())

    def search_employee(self):
        query = self.ui.search_input.text()
        employees = database.search_employees(query)
        self.ui.table.setRowCount(0)
        for row_number, row_data in enumerate(employees):
            self.ui.table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                if column_number == 3:  # Kolom gaji
                    data = f"Rp {int(data):,}".replace(",", ".")
                self.ui.table.setItem(row_number, column_number, self.ui.create_table_item(data))

    def export_to_csv(self):
        path, _ = QFileDialog.getSaveFileName(self.ui, "Simpan File", "", "CSV Files (*.csv)")
        if path:
            employees = database.fetch_all_employees()
            with open(path, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["ID", "Nama", "Jabatan", "Gaji", "Alamat", "Telepon"])
                for employee in employees:
                    writer.writerow(employee)
            QMessageBox.information(self.ui, "Sukses", "Data berhasil diekspor ke CSV!")

    def import_from_csv(self):
        path, _ = QFileDialog.getOpenFileName(self.ui, "Buka File", "", "CSV Files (*.csv)")
        if path:
            with open(path, mode='r') as file:
                reader = csv.reader(file)
                next(reader)  # Skip header
                for row in reader:
                    try:
                        database.add_employee(row[0], row[1], row[2], row[3], row[4], row[5])
                    except Exception as e:
                        QMessageBox.warning(self.ui, "Error", f"Terjadi kesalahan saat mengimpor data: {e}")
            self.load_data()
            QMessageBox.information(self.ui, "Sukses", "Data berhasil diimpor dari CSV!")