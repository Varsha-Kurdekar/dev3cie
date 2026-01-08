from bankacc import bankacc_details

def test_bankacc_details():
    expected_output = (
        "Account Number: A101\n"
        "Account Name: Varsha\n"
        "Account Type: Savings\n"
    )
    assert bankacc_details("A101", "Varsha", "Savings") == expected_output