def bankacc_details(account_number, name, type):
    result = (
        f"Account Number: {number}\n"
        f"Account Name: {name}\n"
        f"Account Type: {type(savings/current)}\n"
    )
    return result


if __name__ == "__main__":
    account_number = "A101"
    name = "Varsha"
    type = Savings

    print(bankacc_details(account_number, name, type))