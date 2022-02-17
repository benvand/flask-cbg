from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class ProvideBankAccountDetails(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    bank = StringField('Bank', validators=[DataRequired()])
    iban = StringField('IBAN', validators=[DataRequired()])
    submit = SubmitField('Next')