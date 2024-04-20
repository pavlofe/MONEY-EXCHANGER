from PyQt5.QtWidgets import* 

from forex_python.converter import CurrencyRates


class CurrencyConverter(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Currency converter: GeeksForGeeks")
        self.setFixedSize(700, 400)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.setup_ui()

    def setup_ui(self):
        self.layout = QVBoxLayout(self.central_widget)

        # Top label
        self.top_label = QLabel("Обмінник Валют")
        self.top_label.setFont(QFont("Lato Black", 19, weight=QFont.Bold))
        self.layout.addWidget(self.top_label)

        # Input fields and labels
        self.amount_label = QLabel("Amount: ")
        self.amount_label.setFont(QFont("Lato Black", 15, weight=QFont.Bold))
        self.amount_field = QLineEdit()

        self.from_currency_label = QLabel("From Currency: ")
        self.from_currency_label.setFont(QFont("Lato Black", 15, weight=QFont.Bold))
        self.from_currency_combo = QComboBox()
        self.from_currency_combo.addItems(["INR", "USD", "CAD", "CNY", "DKK", "EUR", "UAH"])

        self.to_currency_label = QLabel("To Currency: ")
        self.to_currency_label.setFont(QFont("Lato Black", 15, weight=QFont.Bold))
        self.to_currency_combo = QComboBox()
        self.to_currency_combo.addItems(["INR", "USD", "CAD", "CNY", "DKK", "EUR", "UAH"])

        self.converted_label = QLabel("Converted Amount: ")
        self.converted_label.setFont(QFont("Lato Black", 15, weight=QFont.Bold))
        self.converted_field = QLineEdit()
        self.converted_field.setReadOnly(True)

        # Layout for input fields and labels
        input_layout = QHBoxLayout()
        input_layout.addWidget(self.amount_label)
        input_layout.addWidget(self.amount_field)
        input_layout.addWidget(self.from_currency_label)
        input_layout.addWidget(self.from_currency_combo)
        input_layout.addWidget(self.to_currency_label)
        input_layout.addWidget(self.to_currency_combo)
        self.layout.addLayout(input_layout)

        # Spacer
        self.layout.addWidget(QLabel())

        # Convert and Clear buttons
        self.convert_button = QPushButton("Convert")
        self.convert_button.clicked.connect(self.convert_currency)
        self.clear_button = QPushButton("Clear All")
        self.clear_button.clicked.connect(self.clear_all)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.convert_button)
        button_layout.addWidget(self.clear_button)
        self.layout.addLayout(button_layout)

        # Spacer
        self.layout.addWidget(QLabel())

        # Add converted amount label and field
        converted_layout = QHBoxLayout()
        converted_layout.addWidget(self.converted_label)
        converted_layout.addWidget(self.converted_field)
        self.layout.addLayout(converted_layout)

    def convert_currency(self):
        from_currency = self.from_currency_combo.currentText()
        to_currency = self.to_currency_combo.currentText()
        amount = self.amount_field.text()

        if not amount:
            QMessageBox.warning(self, "Error", "Amount Not Entered.\n Please enter a valid amount.")
            return

        if from_currency == "currency" or to_currency == "currency":
            QMessageBox.warning(
                self,
                "Error",
                "Currency Not Selected.\n Please select FROM and TO Currency from
