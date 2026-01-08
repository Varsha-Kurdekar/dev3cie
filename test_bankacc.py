from bankacc import bankacc_details

def test_bankacc_details():
    expected_output = (
        "Account Number: A101\n"
        "Accont Name: Varsha\n"
        "Type: (Savings/current)"
    )
    assert bankacc_details("A101", "Varsha", "Savings") == expected_output