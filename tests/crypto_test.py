from Cryptowebapp.crypto import format_usd, fetch_stocks_data

from pandas import DataFrame

def test_usd_formatting():


    assert format_usd(4.5) == "$4.50"

    assert format_usd(4.555555555) == "$4.56"

    assert format_usd(123456) == "$123,456"




def test_data_fetching():
    result = fetch_crypto_data("BTC")
    assert isinstance(result, DataFrame)

    assert "timestamp" in result.columns
    assert "volume" in result.columns
    assert "close (USD)" in result.columns