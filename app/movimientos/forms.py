from flask_wtf import FlaskForm
from wtforms import (IntegerField, DecimalField, SelectField,
                     TextAreaField, DateField, StringField, SubmitField)
from wtforms.validators import DataRequired, NumberRange, Optional
from flask_babel import lazy_gettext as _l


class MovimientoForm(FlaskForm):
    id_cliente = IntegerField(
        _l("Cliente"),
        validators=[DataRequired(message=_l("Seleccione un cliente"))]
    )
    id_insumo = IntegerField(
        _l("Insumo"),
        validators=[DataRequired(message=_l("Seleccione un insumo"))]
    )
    tipo = SelectField(
        _l("Tipo de operación"),
        choices=[
            ("salida", _l("Venta (Salida)")),
            ("entrada", _l("Compra (Entrada)")),
            ("devolucion", _l("Devolución"))
        ],
        validators=[DataRequired()]
    )
    precio = DecimalField(
        _l("Precio unitario"),
        validators=[DataRequired(), NumberRange(min=0)],
        places=2
    )
    cantidad = IntegerField(
        _l("Cantidad"),
        validators=[DataRequired(), NumberRange(min=1)],
        default=1
    )
    numero = StringField(
        _l("N° Comprobante"),
        validators=[Optional()]
    )
    fecha_vencimiento = DateField(
        _l("Vencimiento del lote"),
        validators=[Optional()],
        format="%Y-%m-%d"
    )
    observaciones = TextAreaField(
        _l("Observaciones"),
        validators=[Optional()]
    )
    submit = SubmitField(_l("Guardar Movimiento"))