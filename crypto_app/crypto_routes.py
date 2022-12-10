from flask import Blueprint, request, render_template, redirect, flash

from Cryptowebapp.crypto import 

crypto_routes = Blueprint("crypto_routes", __name__)

@stocks_routes.route("/stocks/form")
def crypto_form():
    print("STOCKS FORM...")
    return render_template("stocks_form.html")

@crypto_routes.route("/stocks/dashboard", methods=["GET", "POST"])
def crypto_dashboard():
    print("CRYPTO DASHBOARD...")

    if request.method == "POST":
        # for data sent via POST request, form inputs are in request.form:
        request_data = dict(request.form)
        print("FORM DATA:", request_data)
    else:
        # for data sent via GET request, url params are in request.args
        request_data = dict(request.args)
        print("URL PARAMS:", request_data)

    symbol = request_data.get("symbol") or "BTC"

    try:
        df = fetch_crypto_data(symbol=symbol)
        latest_close_usd = format_usd(df.iloc[0]["adjusted_close"])
        latest_date = df.iloc[0]["timestamp"]
        data = df.to_dict("records")

        #flash("Fetched Real-time Market Data!", "success")
        return render_template("crypto_dashboard.html",
            symbol=symbol,
            latest_close_usd=latest_close_usd,
            latest_date=latest_date,
            data=data
        )
    except Exception as err:
        print('OOPS', err)

        #flash("Market Data Error. Please check your symbol and try again!", "danger")
        return redirect("/crypto/form")

#
# API ROUTES
#

@crypto_routes.route("/api/crypto.json")
def crypto_api():
    print("CRYPTO DATA (API)...")

    # for data supplied via GET request, url params are in request.args:
    url_params = dict(request.args)
    print("URL PARAMS:", url_params)
    symbol = url_params.get("symbol") or "BTC"

    try:
        df = fetch_crypto_data(symbol=symbol)
        data = df.to_dict("records")
        return {"symbol": symbol, "data": data }
    except Exception as err:
        print('OOPS', err)
        return {"message":"Market Data Error. Please try again."}, 404