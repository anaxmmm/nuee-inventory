from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField
from wtforms.validators import DataRequired, Length, Email, EqualTo, Optional
from flask_babel import lazy_gettext as _l


class LoginForm(FlaskForm):
    username = StringField(_l("Usuario"), validators=[DataRequired()])
    password = PasswordField(_l("Contraseña"), validators=[DataRequired()])
    submit   = SubmitField(_l("Ingresar"))


class RegisterForm(FlaskForm):
    nombre           = StringField(_l("Nombre completo"),
                                   validators=[DataRequired(), Length(max=100)])
    email            = EmailField(_l("Correo electrónico"),
                                  validators=[DataRequired(), Email()])
    username         = StringField(_l("Nombre de usuario"),
                                   validators=[DataRequired(), Length(min=3, max=50)])
    password         = PasswordField(_l("Contraseña"),
                                     validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField(_l("Confirmar contraseña"),
                                     validators=[DataRequired(),
                                                 EqualTo("password",
                                                         message=_l("Las contraseñas no coinciden"))])
    submit           = SubmitField(_l("Crear usuario"))


class PerfilForm(FlaskForm):
    nombre   = StringField(_l("Nombre completo"),
                           validators=[DataRequired(), Length(max=100)])
    email    = EmailField(_l("Correo electrónico"),
                          validators=[DataRequired(), Email()])
    password = PasswordField(_l("Nueva contraseña (opcional)"),
                             validators=[Optional(), Length(min=6)])
    confirm_password = PasswordField(_l("Confirmar nueva contraseña"),
                                     validators=[Optional(),
                                                 EqualTo("password",
                                                         message=_l("Las contraseñas no coinciden"))])
    submit   = SubmitField(_l("Guardar cambios"))