from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, DateField, IntegerField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, NumberRange, Optional, InputRequired
from flask_babel import lazy_gettext as _l


class InsumoForm(FlaskForm):
    codigo = StringField(
        _l('Código'),
        validators=[
            DataRequired(message=_l("El código es obligatorio")),
            Length(max=15)
        ]
    )

    descripcion = StringField(
        _l('Descripción'),
        validators=[
            DataRequired(message=_l("La descripción es obligatoria")),
            Length(max=150)
        ]
    )

    lote = StringField(
        _l('Lote'),
        validators=[
            DataRequired(message=_l("El lote es obligatorio")),
            Length(max=12)
        ]
    )

    invima = StringField(
        _l('Registro INVIMA'),
        validators=[
            Optional(),
            Length(max=15)
        ]
    )

    valor = DecimalField(
        _l('Valor'),
        validators=[
            DataRequired(message=_l("El valor es obligatorio")),
            NumberRange(min=0)
        ],
        places=2
    )

    iva = DecimalField(
        _l('IVA %%'),
        validators=[
            Optional(),
            NumberRange(min=0, max=100)
        ],
        places=2,
        default=0
    )

    cantidad = IntegerField(
        _l('Cantidad'),
        validators=[
            InputRequired(message=_l("La cantidad es obligatoria")),
            NumberRange(min=0, message=_l("La cantidad no puede ser negativa"))
        ],
        default=0
    )

    stock_minimo = IntegerField(
        _l('Stock Mínimo'),
        validators=[
            InputRequired(message=_l("El stock mínimo es obligatorio")),
            NumberRange(min=0, message=_l("El stock mínimo no puede ser negativo"))
        ],
        default=5
    )

    fecha_vencimiento = DateField(
        _l('Fecha de Vencimiento'),
        validators=[Optional()],
        format='%Y-%m-%d'
    )

    activo = BooleanField(_l('Activo'), default=True)

    submit = SubmitField(_l('Guardar'))