def bankacc_details(account_number, name, acc_type):
    result = (
        f"Account Number: {account_number}\n"
        f"Account Name: {name}\n"
        f"Account Type: {acc_type}\n"
    )
    return result


if __name__ == "__main__":
    account_number = "A101"
    name = "Varsha"
    acc_type = "Savings"

    print(bankacc_details(account_number, name, acc_type))