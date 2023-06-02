import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive",
]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPE_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPE_CREDS)
SHEET = GSPREAD_CLIENT.open("love_sandwiches")


def get_sales_data():
    """
    Get sales figures input from users
    """
    print("Please enter sales data from last market")
    print("Data should be six numbers, separated by commas")
    print("Example: 15,25,27,30,24,11\n")

    data_str = input("Enter sales data here:")

    sales_data = data_str.split(",")
    validate_data(sales_data)


def validate_data(values):
    """
    Validates data input by user, checks if there are 6 values and if
    strings can be converted into integers, Raises ValueError if eother fails
    """
    try:
        [int(value) for value in values]
        if len(values) != 6:
            raise ValueError(f"Exactly 6 values required, you provided {len(values)}")
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")


get_sales_data()
