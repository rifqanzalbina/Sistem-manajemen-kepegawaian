from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QFormLayout, QLabel, QLineEdit,
    QPushButton, QTableWidget, QTableWidgetItem, QHBoxLayout, QHeaderView
)

class EmployeeUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sistem Manajemen Kepegawaian")
        self.setGeometry(100, 100, 800, 600)
        
        layout = QVBoxLayout()
        
        # Input fields
        form_layout = QFormLayout()
        self.id_input = QLineEdit()
        self.name_input = QLineEdit()
        self.position_input = QLineEdit()
        self.salary_input = QLineEdit()
        self.address_input = QLineEdit()
        self.phone_input = QLineEdit()
        
        form_layout.addRow("ID:", self.id_input)
        form_layout.addRow("Nama:", self.name_input)
        form_layout.addRow("Jabatan:", self.position_input)
        form_layout.addRow("Gaji:", self.salary_input)
        form_layout.addRow("Alamat:", self.address_input)
        form_layout.addRow("Telepon:", self.phone_input)
        
        # Tombol
        btn_layout = QHBoxLayout()
        self.add_btn = QPushButton("Tambah")
        self.update_btn = QPushButton("Ubah")
        self.delete_btn = QPushButton("Hapus")
        self.clear_btn = QPushButton("Bersihkan")
        self.export_btn = QPushButton("Ekspor ke CSV")
        self.import_btn = QPushButton("Impor dari CSV")
        
        btn_layout.addWidget(self.add_btn)
        btn_layout.addWidget(self.update_btn)
        btn_layout.addWidget(self.delete_btn)
        btn_layout.addWidget(self.clear_btn)
        btn_layout.addWidget(self.export_btn)
        btn_layout.addWidget(self.import_btn)
        
        # Pencarian
        search_layout = QHBoxLayout()
        self.search_input = QLineEdit()
        self.search_btn = QPushButton("Cari")
        search_layout.addWidget(QLabel("Cari:"))
        search_layout.addWidget(self.search_input)
        search_layout.addWidget(self.search_btn)
        
        # Tabel
        self.table = QTableWidget()
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels(["ID", "Nama", "Jabatan", "Gaji", "Alamat", "Telepon"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        
        # Tambahkan ke layout utama
        layout.addLayout(form_layout)
        layout.addLayout(btn_layout)
        layout.addLayout(search_layout)
        layout.addWidget(self.table)
        self.setLayout(layout)
        
    def clear_inputs(self):
        self.id_input.clear()
        self.name_input.clear()
        self.position_input.clear()
        self.salary_input.clear()
        self.address_input.clear()
        self.phone_input.clear()
        
    def create_table_item(self, text):
        return QTableWidgetItem(str(text))