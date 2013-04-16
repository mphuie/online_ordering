from flask.ext.wtf import Form, TextField, Required, SelectField, DateField


class MyForm(Form):
	name = TextField('Name', validators=[Required()])
	business_unit = SelectField('Business unit', choices=[
        ('SB', 'SB'),
        ('ENT', 'ENT'),
        ('PDES', 'PDES')
    ])