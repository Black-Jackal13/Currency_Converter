from PyQt5.QtWidgets import *
from PyQt5 import uic
from converter import get_currencies, convert


class Converter(QMainWindow):
    def __init__(self):
        super(Converter, self).__init__()
        uic.loadUi('gui.ui', self)
        self.setWindowTitle('Currency Converter')
        self.show()

        # Update Currencies Window
        currencies = get_currencies()
        for name, currency in currencies:
            name = currency['currencyName']
            _id = currency['id']
            symbol = currency.get("currencySymbol", "NO SYMBOL")
            self.currencies_view.append(f"{_id}: {name} - {symbol}")

        # Convert Functionality
        self.convert_button.clicked.connect(self._convert)

    def _convert(self):
        original = self.original_currency.text()
        target = self.target_currency.text()

        try:
            amount = int(self.amount.text())
        except ValueError:
            amount = 1

        converted = convert(original, target, amount)

        self.result.setText(f"{target} {converted:.2f}")

def main():
    app = QApplication([])
    window = Converter()
    app.exec_()

if __name__ == '__main__':
    main()