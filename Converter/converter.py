from requests import get

# Constants
BASE_URL = "https://free.currconv.com/"

# Get API_KEY
with open("api_key.txt", "r") as file:
    # Get an API Key @ https://www.currencyconverterapi.com
    API_KEY = file.read()


def get_currencies():
    endpoint = f"api/v7/currencies?apiKey={API_KEY}"
    url = BASE_URL + endpoint
    data = get(url).json()['results']

    data = list(data.items())
    data.sort()

    return data


def exchange_rate(currency1, currency2):
    endpoint = f"api/v7/convert?q={currency1}_{currency2}&compact=ultra&apiKey={API_KEY}"
    url = BASE_URL + endpoint
    data = get(url).json()

    if len(data) == 0:
        print('INVALID CURRENCIES')
        return
    else:
        rate = list(data.values())[0]
        print(f"{currency1} --> {currency2} = {rate}")

        return rate


def convert(currency1, currency2, amount):
    rate = exchange_rate(currency1, currency2)
    if rate is None:
        return

    try:
        amount = float(amount)
    except ValueError:
        print("INVALID AMOUNT")
        return

    converted_amount = rate * amount
    print(f"{amount} {currency1}    ---->    {converted_amount:,.2f} {currency2}".replace(",", " "))
    return converted_amount


def print_currencies(currencies: dict):
    for name, currency in currencies:
        name = currency['currencyName']
        _id = currency['id']
        symbol = currency.get("currencySymbol", "NO SYMBOL")
        print(f"{_id}:  {name} - {symbol}")


def main():
    currencies = get_currencies()

    while True:
        # Home
        print("\n\n-------------[ Currency Converter ]-------------")
        print(" 1   List     - Display available currencies")
        print(" 2   Convert  - Convert a currencie to another")
        print(" 3   Rate     - Get exchange rate of a currency")
        print(" 4   Quit     - Quit Application\n")

        # Choose an Option
        command = int(input("Enter a Command:   "))

        # Handle tasks
        if command == 1:
            # List
            print_currencies(currencies)

        elif command == 2:
            # Convert
            currency1 = str(input("Enter Base Currency :       ")).upper()
            currency2 = str(input("Enter New Currency :        ")).upper()
            amount = input(f"Enter Amount in {currency1}:        ")
            print("")

            convert(currency1, currency2, amount)

        elif command == 3:
            # Rate
            currency1 = str(input("Enter Base Currency :       ")).upper()
            currency2 = str(input("Enter New Currency :        ")).upper()
            print("")

            exchange_rate(currency1, currency2)

        elif command == 4:
            # Quit
            break

        else:
            print("\n[ UNRECONIZED COMMAND ]\n")


if __name__ == "__main__":
    main()
