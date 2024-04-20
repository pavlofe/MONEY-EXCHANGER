from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QLabel, QLineEdit, QPushButton, QComboBox, QMessageBox
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from forex_python.converter import CurrencyRates


class CurrencyConverter(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Currency Converter: GeeksForGeeks")
        self.setGeometry(100, 100, 400, 300)
        
        # Layouts
        main_layout = QVBoxLayout()
        
        # Top Label
        top_label = QLabel("ОБМІННИК ВАЛЮТ")
        top_label.setFont(QFont('lato black', 19, QFont.Bold))
        top_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(top_label)
        
        # Input Layout
        input_layout = QGridLayout()
        main_layout.addLayout(input_layout)
        
        # Labels
        labels = ["Сума:", "З Валюти:", "В Валюту:", "Конвертована Сума:"]
        for i, text in enumerate(labels):
            label = QLabel(text)
            label.setFont(QFont('lato black', 15, QFont.Bold))
            input_layout.addWidget(label, i, 0)
        
        # Input fields
        self.amount_input = QLineEdit()
        input_layout.addWidget(self.amount_input, 0, 1)
        
        self.from_currency_combo = QComboBox()
        self.from_currency_combo.addItems(["INR", "USD", "CAD", "CNY", "DKK", "EUR", "UAH"])
        input_layout.addWidget(self.from_currency_combo, 1, 1)
        
        self.to_currency_combo = QComboBox()
        self.to_currency_combo.addItems(["INR", "USD", "CAD", "CNY", "DKK", "EUR", "UAH"])
        input_layout.addWidget(self.to_currency_combo, 2, 1)
        
        self.converted_amount = QLineEdit()
        self.converted_amount.setReadOnly(True)
        input_layout.addWidget(self.converted_amount, 3, 1)
        
        # Button Layout
        button_layout = QHBoxLayout()
        main_layout.addLayout(button_layout)
        
        # Buttons
        convert_button = QPushButton("Convert")
        convert_button.clicked.connect(self.convert_currency)
        button_layout.addWidget(convert_button)
        
        clear_button = QPushButton("Clear All")
        clear_button.clicked.connect(self.clear_all)
        button_layout.addWidget(clear_button)
        
        self.setLayout(main_layout)
    
    def convert_currency(self):
        c = CurrencyRates()
        
        from_currency = self.from_currency_combo.currentText()
        to_currency = self.to_currency_combo.currentText()
        
        amount_text = self.amount_input.text()
        if not amount_text:
            QMessageBox.warning(self, "Error", "Amount Not Entered.\nPlease enter a valid amount.")
            return
        
        try:
            amount = float(amount_text)
        except ValueError:
            QMessageBox.warning(self, "Error", "Invalid amount.\nPlease enter a valid number.")
            return
        
        converted_amount = c.convert(from_currency, to_currency, amount)
        self.converted_amount.setText(f"{converted_amount:.4f}")
    
    def clear_all(self):
        self.amount_input.clear()
        self.converted_amount.clear()

if __name__ == '__main__':
    import sys
    
    app = QApplication(sys.argv)
    
    window = CurrencyConverter()
    window.show()
    
    sys.exit(app.exec_())
