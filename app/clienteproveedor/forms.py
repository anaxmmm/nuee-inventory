from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, EmailField
from wtforms.validators import DataRequired, Optional, Length, Email
from flask_babel import lazy_gettext as _l


class ClienteProveedorForm(FlaskForm):

    tipo_identificacion = SelectField(
        _l('Tipo de Identificación'),
        choices=[
            ('NIT', 'NIT'),
            ('CC', _l('Cédula de Ciudadanía (CC)')),
            ('CE', _l('Cédula de Extranjería (CE)')),
            ('PP', _l('Pasaporte (PP)')),
        ],
        default='NIT'
    )

    nit = StringField(
        _l('Número de Identificación'),
        validators=[DataRequired(message=_l('El número de identificación es obligatorio')),
                    Length(max=20)]
    )

    nombre = StringField(
        _l('Nombre / Razón Social'),
        validators=[DataRequired(message=_l('El nombre es obligatorio')),
                    Length(max=150)]
    )

    direccion = StringField(
        _l('Dirección'),
        validators=[Optional(), Length(max=150)]
    )

    celular = StringField(
        _l('Celular'),
        validators=[Optional(), Length(max=20)]
    )

    correo = EmailField(
        _l('Correo Electrónico'),
        validators=[Optional(), Email(message=_l('Ingresa un correo válido')), Length(max=120)]
    )

    tipo = SelectField(
        _l('Tipo de Contacto'),
        choices=[('C', _l('Cliente')), ('P', _l('Proveedor'))],
        default='C'
    )