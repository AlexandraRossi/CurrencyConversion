import sys
import datetime as dt
from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon, QDoubleValidator
from PyQt5.QtWidgets import *
from  PyQt5 import *
import currency_ingester as ci







class CurrencyGui(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "currency_converter"
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.source_country_list = None
        self.target_country_list = None
        self.target_currency_field = None
        self.target_currency_symbol = None
        self.initUI()
        self.show()
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.source_country_list = QListWidget()
        self.target_country_list = QListWidget()
        self.source_country_list.itemClicked.connect(self.country_clicked)
        self.target_country_list.itemClicked.connect(self.country_clicked)



        #get country list
        ingester = ci.ingester()
        countries = ingester.get_countries()

        country_string_list = []
        for country in countries:
            country_string_list.append(f"{country['name']} {country['currencySymbol']} [{country['currencyId']})")
            country_string_list.sort()

        for country_string in country_string_list:
            self.source_country_list.addItem(country_string)
            self.target_country_list.addItem(country_string)







        # Target currency symbols


        #Currency input


        #Currency output

        country_list_layout = QHBoxLayout()
        country_list_layout.addWidget(self.source_country_list)
        country_list_layout.addWidget(self.target_country_list)

        self.source_currency_field = QLineEdit()
        self.source_currency_symbol = QLabel()
        self.target_currency_field = QLineEdit()
        self.target_currency_symbol = QLabel()
        convert_button = QPushButton("Convert ➡︎")
        convert_button.pressed.connect(self.convert_button_pressed)



        currency_layout = QHBoxLayout()
        currency_layout.setAlignment(Qt.AlignVCenter)
        currency_layout.addWidget(self.source_currency_field)
        currency_layout.addWidget(self.source_currency_symbol)
        currency_layout.addWidget(convert_button)
        currency_layout.addWidget(self.target_currency_field)
        currency_layout.addWidget(self.target_currency_symbol)

        layout = QVBoxLayout()
        layout.addLayout(country_list_layout)
        layout.addLayout(currency_layout)


        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def country_clicked (self, item):
        selected_string = item.text()
        selection_list = selected_string.split()
        symbol = selection_list[-2]
        if item.listWidget() is self.source_country_list:
            self.source_currency_symbol.setText(symbol)

        print(symbol)
    def get_currency_id(self, list_widget) -> str:
        # determine target and source currency

        selected_items = self.list_widget.selectedItems()

        if len(selected_items) == 0:
            print("select a source currency")
        item_text = selected_items[0].text()
        currency_id = item_text.split()[-1]
        currency_id = currency_id[1:-1]
        return currency_id


        # retrieve the source currency amount
        # call the ingester for the conversion rate
        # multiply conversion rate by source currency
        # put the results in target currency

    def convert_button_pressed(self):
        source_currency_id = self.get_currency_id(self.source_country_list)
        target_currency_id = self.get_currency_id(self.target_country_list)

        if source_currency_id is None or target_currency_id is None:
            self.statusBar().showMessage("source and target country must be selected", 3000)

        print(source_currency_id)
        print(target_currency_id)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CurrencyGui()
    sys.exit(app.exec_())
