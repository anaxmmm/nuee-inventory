"""Crea la primera cuenta de administrador.

Uso: python crear_usuario.py
Pide el usuario, el correo y la contraseña en la consola; la contraseña no se muestra.
"""
from getpass import getpass

from app import create_app
from app.extensions import db
from app.auth.models import Usuario


def pedir_password():
    while True:
        password = getpass("Contraseña (mínimo 8 caracteres): ")
        if len(password) < 8:
            print("La contraseña es muy corta.")
            continue
        if password != getpass("Repite la contraseña: "):
            print("Las contraseñas no coinciden.")
            continue
        return password


def main():
    app = create_app()
    with app.app_context():
        username = input("Usuario administrador: ").strip()
        if not username:
            print("El usuario no puede estar vacío.")
            return
        if Usuario.query.filter_by(username=username).first():
            print(f"El usuario '{username}' ya existe.")
            return
        nombre = input("Nombre completo: ").strip() or username
        email = input("Correo (opcional): ").strip() or None

        usuario = Usuario(username=username, nombre=nombre, email=email, rol="admin", activo=True)
        usuario.set_password(pedir_password())
        db.session.add(usuario)
        db.session.commit()
        print(f"Administrador '{username}' creado.")


if __name__ == "__main__":
    main()
