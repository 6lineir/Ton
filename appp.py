from pytonapi import Tonapi


def main():
    # Create a new Tonapi object with the provided API key
    tonapi = Tonapi(
        api_key="AG3QSHHGIDZ7NAAAAAAE7TCU2UBRU2DLBOOINDD3FCAUCKVMDI6OCM5SPLI5G3UWGXNLVUQ"
    )

    # Specify the account ID
    account_id = "UQAC-dODXrOtFwtsujnDCSYGh_-4ulP2CPsdLV_yNVml2NIR"  # noqa

    # Retrieve account information
    account = tonapi.accounts.get_info(account_id=account_id)

    # Print account details
    print(f"Account Address (raw): {account.address.to_raw()}")
    print(
        f"Account Address (userfriendly): {account.address.to_userfriendly(is_bounceable=True)}"
    )
    print(f"Account Balance (nanoton): {account.balance.to_nano()}")
    print(f"Account Balance (amount): {account.balance.to_amount()}")
    body = {"body": "Hi "}
    msg = tonapi.liteserver.send_message(body=body)
    print(msg)

if __name__ == "__main__":
    main()
