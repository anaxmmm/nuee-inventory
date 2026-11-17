from flask_wtf import FlaskForm
from wtforms import IntegerField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Optional
from flask_babel import lazy_gettext as _l


class FacturaForm(FlaskForm):
    id_cliente = IntegerField(
        _l("Cliente"),
        validators=[DataRequired(message=_l("Seleccione un cliente"))]
    )
    observaciones = TextAreaField(
        _l("Observaciones"),
        validators=[Optional()]
    )
    submit = SubmitField(_l("Crear Factura"))