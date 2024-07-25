#! /usr/bin/env python3.6

"""
server.py
Stripe Sample.
Python 3.6 or newer required.
"""
import os
from flask import Flask, jsonify, redirect, request, send_from_directory

import stripe
# This is your test secret API key.
stripe.api_key = 'sk_test_51OuCCXK0g9v1y00EpCFyL6nA88JOA37L0oxnThLmebp3o5WyFQQuSRRil4Ljqm05CtaoNEJDyx00GypoEulDYGTY00v2yA1cy8'

app = Flask(__name__,
            static_url_path='',
            static_folder='public')

YOUR_DOMAIN = 'http://localhost:4242'

@app.route('/.well-known/apple-developer-merchantid-domain-association')
def apple_pay_verification():
    return send_from_directory('.well-known', 'apple-developer-merchantid-domain-association')

@app.route('/create-checkout-session', methods=['POST'])
def create_checkout_session():
    try:
        session = stripe.checkout.Session.create(
            ui_mode = 'embedded',
            line_items=[
                {
                    # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                    "price_data": {
                        "currency": "usd",
                        "product_data": {
                            "name": "TESTING THIS CHECKOUT FUNCTION",
                        },
                        "unit_amount": 20900,
                    },
                    "quantity": 1,
                },
            ],
            mode='payment',
            return_url=YOUR_DOMAIN + '/return.html?session_id={CHECKOUT_SESSION_ID}',
            # redirect_on_completion="never",
        )
    except Exception as e:
        return str(e)

    return jsonify(clientSecret=session.client_secret)

@app.route('/session-status', methods=['GET'])
def session_status():
  session = stripe.checkout.Session.retrieve(request.args.get('session_id'))

  return jsonify(status=session.status, customer_email=session.customer_details.email)

if __name__ == '__main__':
    app.run(port=4242)