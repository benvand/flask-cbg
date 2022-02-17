from flask import Flask, render_template, request, session, redirect, url_for

from forms import ProvideBankAccountDetails
from config import Config


app = Flask(__name__)
app.config.from_object(Config)


@app.route('/home')
def home():
    print('foo')
    return render_template('home.html')

@app.route('/children')
def children():
    return render_template('children.html')

@app.route('/bank-account-details')
def bank_account_details():
    return render_template('bank-account-details.html')

@app.route('/provide-bank-account-details')
def provide_bank_account_details():
    form=ProvideBankAccountDetails()
    if form.validate_on_submit():
        session['iban'] = request.form['iban']
        # session.pop('iban', default=None)
        return redirect(url_for('bank_account_details'))
    return render_template('provide-bank-account-details.html', form=form)