"""
seed_contactos_movimientos.py
Pobla clientes, proveedores y movimientos de la última semana.
Ejecutar desde la raíz del proyecto: python seed_contactos_movimientos.py
"""

from app import create_app
from app.extensions import db
from app.clienteproveedor.models import ClienteProveedor
from app.movimientos.models import Movimiento
from app.insumos.models import Insumo
from datetime import datetime, timedelta, date
import random

app = create_app()

# ── CLIENTES (25) ─────────────────────────────────────────────────────────────
CLIENTES = [
    {"nit": "1.000.000.001", "nombre": "Valentina Ríos Martínez",       "direccion": "Cra 15 #93-47, Bogotá",          "celular": "3005550001", "correo": "vrios@example.com",          "tipo_id": "CC"},
    {"nit": "1.000.000.002", "nombre": "Camila Ospina Herrera",          "direccion": "Cl 10 #43-25, Medellín",         "celular": "3005550002", "correo": "cospina@example.com",         "tipo_id": "CC"},
    {"nit": "1.000.000.003", "nombre": "Mariana Gómez Restrepo",         "direccion": "Av 6N #23-15, Cali",             "celular": "3005550003", "correo": "mgomez@example.com",        "tipo_id": "CC"},
    {"nit": "1.000.000.004", "nombre": "Daniela Vargas Suárez",          "direccion": "Cra 27 #57-12, Bucaramanga",     "celular": "3005550004", "correo": "dvargas@example.com",         "tipo_id": "CC"},
    {"nit": "1.000.000.005", "nombre": "Sofía Mendoza Peña",             "direccion": "Cl 72 #68-30, Barranquilla",     "celular": "3005550005", "correo": "smendoza@example.com",      "tipo_id": "CC"},
    {"nit": "1.000.000.006", "nombre": "Isabella Castro Mora",           "direccion": "Cra 11 #82-44, Bogotá",          "celular": "3005550006", "correo": "icastro@example.com",         "tipo_id": "CC"},
    {"nit": "1.000.000.007", "nombre": "Luciana Fernández Álvarez",      "direccion": "Cl 33 #76-20, Medellín",         "celular": "3005550007", "correo": "lfernandez@example.com",      "tipo_id": "CC"},
    {"nit": "1.000.000.008", "nombre": "Natalia Jiménez Torres",         "direccion": "Av 3N #12-08, Cali",             "celular": "3005550008", "correo": "njimenez@example.com",      "tipo_id": "CC"},
    {"nit": "1.000.000.009", "nombre": "Alejandra Ruiz Pinto",           "direccion": "Cra 33 #48-60, Bucaramanga",     "celular": "3005550009", "correo": "aruiz@example.com",           "tipo_id": "CC"},
    {"nit": "1.000.000.010", "nombre": "Gabriela Moreno Díaz",           "direccion": "Cl 84 #45-17, Barranquilla",     "celular": "3005550010", "correo": "gmoreno@example.com",         "tipo_id": "CC"},
    {"nit": "1.000.000.011", "nombre": "Paulina Salcedo Gómez",          "direccion": "Cra 7 #116-50, Bogotá",          "celular": "3005550011", "correo": "psalcedo@example.com",        "tipo_id": "CC"},
    {"nit": "1.000.000.012", "nombre": "Manuela Agudelo Ríos",           "direccion": "Cl 50 #52-36, Medellín",         "celular": "3005550012", "correo": "magudelo@example.com",      "tipo_id": "CC"},
    {"nit": "1.000.000.013", "nombre": "Catalina Prada Londoño",         "direccion": "Av 5N #34-22, Cali",             "celular": "3005550013", "correo": "cprada@example.com",          "tipo_id": "CC"},
    {"nit": "1.000.000.014", "nombre": "Verónica Pedraza Niño",          "direccion": "Cra 22 #35-14, Bucaramanga",     "celular": "3005550014", "correo": "vpedraza@example.com",        "tipo_id": "CC"},
    {"nit": "1.000.000.015", "nombre": "Juliana Ramos Espinosa",         "direccion": "Cl 53 #38-29, Barranquilla",     "celular": "3005550015", "correo": "jramos@example.com",          "tipo_id": "CC"},
    {"nit": "1.000.000.016", "nombre": "Andrea Muñoz Cardona",           "direccion": "Cra 9 #72-18, Bogotá",           "celular": "3005550016", "correo": "amunoz@example.com",        "tipo_id": "CC"},
    {"nit": "1.000.000.017", "nombre": "Valeria Quintero Betancur",      "direccion": "Cl 37 #65-41, Medellín",         "celular": "3005550017", "correo": "vquintero@example.com",       "tipo_id": "CC"},
    {"nit": "1.000.000.018", "nombre": "Simona Arango Vélez",            "direccion": "Av 8N #19-33, Cali",             "celular": "3005550018", "correo": "sarango@example.com",         "tipo_id": "CC"},
    {"nit": "1.000.000.019", "nombre": "Renata Serrano Blanco",          "direccion": "Cra 28 #42-55, Bucaramanga",     "celular": "3005550019", "correo": "rserrano@example.com",      "tipo_id": "CC"},
    {"nit": "1.000.000.020", "nombre": "Emilia Cárdenas Fuentes",        "direccion": "Cl 79 #41-26, Barranquilla",     "celular": "3005550020", "correo": "ecardenas@example.com",       "tipo_id": "CC"},
    {"nit": "1.000.000.021", "nombre": "Antonella Herrera Acosta",       "direccion": "Cra 13 #85-32, Bogotá",          "celular": "3005550021", "correo": "aherrera@example.com",        "tipo_id": "CC"},
    {"nit": "1.000.000.022", "nombre": "Luna Zapata Gutiérrez",          "direccion": "Cl 44 #80-15, Medellín",         "celular": "3005550022", "correo": "lzapata@example.com",         "tipo_id": "CC"},
    {"nit": "1.000.000.023", "nombre": "Sara Castaño Mejía",             "direccion": "Av 4N #27-19, Cali",             "celular": "3005550023", "correo": "scastano@example.com",      "tipo_id": "CC"},
    {"nit": "1.000.000.024", "nombre": "Alicia Bermúdez Ochoa",          "direccion": "Cra 35 #55-38, Bucaramanga",     "celular": "3005550024", "correo": "abermudez@example.com",       "tipo_id": "CC"},
    {"nit": "1.000.000.025", "nombre": "Regina Molina Cifuentes",        "direccion": "Cl 48 #32-47, Barranquilla",     "celular": "3005550025", "correo": "rmolina@example.com",         "tipo_id": "CC"},
]

# ── PROVEEDORES (25) ──────────────────────────────────────────────────────────
PROVEEDORES = [
    {"nit": "900.000.001-1", "nombre": "Belleza & Cosmética S.A.S",          "direccion": "Cra 68 #22-31, Bogotá",          "celular": "6045550001", "correo": "ventas@bellezacosmetica.example.com",     "tipo_id": "NIT"},
    {"nit": "900.000.002-2", "nombre": "Distribuciones Derma Colombia",       "direccion": "Cl 80 #45-12, Medellín",         "celular": "6045550002", "correo": "pedidos@dermacolombia.example.com",       "tipo_id": "NIT"},
    {"nit": "900.000.003-3", "nombre": "Importadora Skin Care Andina",        "direccion": "Av 6N #14-55, Cali",             "celular": "6045550003", "correo": "contacto@skinandina.example.com",        "tipo_id": "NIT"},
    {"nit": "900.000.004-4", "nombre": "Laboratorios Natura Vital Ltda",      "direccion": "Cra 15 #63-20, Bucaramanga",     "celular": "6045550004", "correo": "lab@naturavital.example.com",             "tipo_id": "NIT"},
    {"nit": "900.000.005-5", "nombre": "Cosméticos del Caribe S.A",           "direccion": "Cl 72 #43-18, Barranquilla",     "celular": "6045550005", "correo": "info@cosmeticoscaribe.example.com",      "tipo_id": "NIT"},
    {"nit": "900.000.006-6", "nombre": "Global Beauty Solutions Colombia",     "direccion": "Cra 7 #127-60, Bogotá",          "celular": "6045550006", "correo": "ventas@globalbeauty.example.com",         "tipo_id": "NIT"},
    {"nit": "900.000.007-7", "nombre": "Dermocosméticos Antioquia S.A.S",     "direccion": "Cl 10 #38-44, Medellín",         "celular": "6045550007", "correo": "contacto@dermoantioquia.example.com",     "tipo_id": "NIT"},
    {"nit": "900.000.008-8", "nombre": "Proveedora Nacional de Skincare",      "direccion": "Av 3N #28-19, Cali",             "celular": "6045550008", "correo": "pedidos@skincarenacional.example.com",    "tipo_id": "NIT"},
    {"nit": "900.000.009-9", "nombre": "Industrias Cosméticas del Sur",        "direccion": "Cra 40 #52-35, Bucaramanga",     "celular": "6045550009", "correo": "ventas@cosmeticosdelsur.example.com",     "tipo_id": "NIT"},
    {"nit": "900.000.010-0", "nombre": "Biocosmética Premium Colombia",        "direccion": "Cl 53 #31-27, Barranquilla",     "celular": "6045550010", "correo": "info@biocosmetica.example.com",           "tipo_id": "NIT"},
    {"nit": "900.000.011-1", "nombre": "Peptide Lab Distribuciones",           "direccion": "Cra 11 #90-14, Bogotá",          "celular": "6045550011", "correo": "lab@peptidelab.example.com",              "tipo_id": "NIT"},
    {"nit": "900.000.012-2", "nombre": "Ceramide & Co Importaciones",          "direccion": "Cl 45 #70-22, Medellín",         "celular": "6045550012", "correo": "imports@ceramideco.example.com",         "tipo_id": "NIT"},
    {"nit": "900.000.013-3", "nombre": "Dermaline Colombia S.A.S",             "direccion": "Av 5N #40-33, Cali",             "celular": "6045550013", "correo": "ventas@dermalineco.example.com",          "tipo_id": "NIT"},
    {"nit": "900.000.014-4", "nombre": "Wellness Cosmetics Distribuidora",     "direccion": "Cra 30 #48-17, Bucaramanga",     "celular": "6045550014", "correo": "contacto@wellnessco.example.com",         "tipo_id": "NIT"},
    {"nit": "900.000.015-5", "nombre": "Atlántico Beauty Mayorista",           "direccion": "Cl 84 #52-41, Barranquilla",     "celular": "6045550015", "correo": "mayorista@atlanticobeauty.example.com",   "tipo_id": "NIT"},
    {"nit": "900.000.016-6", "nombre": "Skinlab Bogotá Proveedores",           "direccion": "Cra 9 #65-28, Bogotá",           "celular": "6045550016", "correo": "lab@skinlabbogota.example.com",           "tipo_id": "NIT"},
    {"nit": "900.000.017-7", "nombre": "Medellín Glow Distribuciones",         "direccion": "Cl 30 #80-55, Medellín",         "celular": "6045550017", "correo": "glow@medellinglow.example.com",           "tipo_id": "NIT"},
    {"nit": "900.000.018-8", "nombre": "Valle Cosmético S.A",                  "direccion": "Av 9N #15-44, Cali",             "celular": "6045550018", "correo": "ventas@vallecosmetico.example.com",       "tipo_id": "NIT"},
    {"nit": "900.000.019-9", "nombre": "Provitalia Skincare Colombia",          "direccion": "Cra 25 #60-39, Bucaramanga",     "celular": "6045550019", "correo": "info@provitalia.example.com",             "tipo_id": "NIT"},
    {"nit": "900.000.020-0", "nombre": "Cosmética Sostenible del Norte",        "direccion": "Cl 63 #38-26, Barranquilla",     "celular": "6045550020", "correo": "eco@cosmeticanorte.example.com",          "tipo_id": "NIT"},
    {"nit": "900.000.021-1", "nombre": "Glaze Import Export S.A.S",            "direccion": "Cra 13 #100-17, Bogotá",         "celular": "6045550021", "correo": "imports@glazeco.example.com",            "tipo_id": "NIT"},
    {"nit": "900.000.022-2", "nombre": "Antioquia Dermis Laboratorio",          "direccion": "Cl 55 #62-14, Medellín",         "celular": "6045550022", "correo": "lab@antioquiadermis.example.com",         "tipo_id": "NIT"},
    {"nit": "900.000.023-3", "nombre": "Pacific Skin Distribuciones",           "direccion": "Av 2N #50-21, Cali",             "celular": "6045550023", "correo": "ventas@pacificskin.example.com",          "tipo_id": "NIT"},
    {"nit": "900.000.024-4", "nombre": "Santander Beauty Mayorista",            "direccion": "Cra 18 #72-43, Bucaramanga",     "celular": "6045550024", "correo": "mayorista@santanderbeauty.example.com",   "tipo_id": "NIT"},
    {"nit": "900.000.025-5", "nombre": "Caribe Glow Importaciones Ltda",        "direccion": "Cl 45 #27-38, Barranquilla",     "celular": "6045550025", "correo": "imports@caribeglow.example.com",          "tipo_id": "NIT"},
]


def seed_contactos():
    """Inserta clientes y proveedores si la tabla está vacía."""
    existentes = ClienteProveedor.query.count()
    if existentes > 0:
        print(f"  Ya existen {existentes} contactos. Omitiendo clientes/proveedores.")
        return

    for c in CLIENTES:
        registro = ClienteProveedor(
            nit                 = c["nit"],
            nombre              = c["nombre"],
            direccion           = c["direccion"],
            celular             = c["celular"],
            correo              = c["correo"],
            tipo                = "C",
            tipo_identificacion = c["tipo_id"],
        )
        db.session.add(registro)

    for p in PROVEEDORES:
        registro = ClienteProveedor(
            nit                 = p["nit"],
            nombre              = p["nombre"],
            direccion           = p["direccion"],
            celular             = p["celular"],
            correo              = p["correo"],
            tipo                = "P",
            tipo_identificacion = p["tipo_id"],
        )
        db.session.add(registro)

    db.session.commit()
    print(f"  25 clientes insertados")
    print(f"  25 proveedores insertados")


def seed_movimientos():
    """
    Genera movimientos de los últimos 7 días.
    - Salidas (ventas): vinculadas a clientes, reflejan demanda real
    - Entradas (reposición): vinculadas a proveedores
    Los productos más vendidos son labiales y esencias — productos de ticket
    rápido en el mercado colombiano de skincare.
    """
    existentes = Movimiento.query.count()
    if existentes > 0:
        print(f"  Ya existen {existentes} movimientos. Omitiendo movimientos.")
        return

    insumos = Insumo.query.filter_by(activo=True).all()
    if not insumos:
        print("  No hay insumos en la base de datos. Corre seed_nuee.py primero.")
        return

    clientes   = ClienteProveedor.query.filter_by(tipo="C").all()
    proveedores = ClienteProveedor.query.filter_by(tipo="P").all()

    if not clientes or not proveedores:
        print("  No hay clientes/proveedores. Algo falló en seed_contactos().")
        return

    hoy = datetime.utcnow()

    # Pesos de venta por producto — los labiales y esencias rotan más rápido
    pesos_venta = {
        "NUE-001": 18,   # Esencia Ceramida — hero product
        "NUE-002": 22,   # Tinte Labial — mayor rotación
        "NUE-003": 10,
        "NUE-004": 12,
        "NUE-005": 10,
        "NUE-006": 20,   # Mascarilla Labial — alta rotación
        "NUE-007": 14,
        "NUE-008": 9,
        "NUE-009": 18,   # Tratamiento Labial
        "NUE-010": 11,
        "NUE-011": 13,
        "NUE-012": 12,
        "NUE-013": 15,   # Mini Esencia — impulso por precio
        "NUE-014": 13,
        "NUE-015": 14,
        "NUE-016": 8,    # Kit — menor frecuencia, mayor ticket
        "NUE-017": 12,
        "NUE-018": 11,
    }

    insumo_map = {ins.codigo: ins for ins in insumos}
    codigos    = list(pesos_venta.keys())
    pesos      = [pesos_venta[c] for c in codigos]

    movimientos_generados = 0

    # ── Salidas (ventas) — 6 a 10 por día durante 7 días ──
    for dias_atras in range(7):
        fecha_dia = hoy - timedelta(days=dias_atras)
        ventas_del_dia = random.randint(6, 10)

        for _ in range(ventas_del_dia):
            codigo_elegido = random.choices(codigos, weights=pesos, k=1)[0]
            insumo = insumo_map.get(codigo_elegido)
            if not insumo:
                continue

            cliente = random.choice(clientes)
            cantidad = random.randint(1, 3)

            # Hora aleatoria dentro del día (9am - 7pm)
            hora = random.randint(9, 19)
            minuto = random.randint(0, 59)
            fecha_mov = fecha_dia.replace(hour=hora, minute=minuto, second=0, microsecond=0)

            mov = Movimiento(
                id_cliente     = cliente.id,
                id_insumo      = insumo.id,
                id_usuario     = 1,
                nombre_usuario = "admin",
                tipo           = "salida",
                precio         = float(insumo.valor),
                cantidad       = cantidad,
                fecha_creacion = fecha_mov,
                observaciones  = "Venta mostrador",
                fecha_vencimiento = insumo.fecha_vencimiento,
            )
            db.session.add(mov)
            movimientos_generados += 1

    # ── Entradas (reposición de inventario) — 2 a 3 por día ──
    for dias_atras in range(7):
        fecha_dia = hoy - timedelta(days=dias_atras)
        entradas_del_dia = random.randint(2, 3)

        for _ in range(entradas_del_dia):
            insumo = random.choice(insumos)
            proveedor = random.choice(proveedores)
            cantidad = random.randint(10, 30)

            hora = random.randint(8, 12)
            minuto = random.randint(0, 59)
            fecha_mov = fecha_dia.replace(hour=hora, minute=minuto, second=0, microsecond=0)

            # Costo de entrada es aprox 57% del precio de venta (inverso del margen 75%)
            costo_entrada = round(float(insumo.valor) / 1.75, 2)

            mov = Movimiento(
                id_cliente     = proveedor.id,
                id_insumo      = insumo.id,
                id_usuario     = 1,
                nombre_usuario = "admin",
                tipo           = "entrada",
                precio         = costo_entrada,
                cantidad       = cantidad,
                fecha_creacion = fecha_mov,
                observaciones  = "Reposición de inventario",
                fecha_vencimiento = insumo.fecha_vencimiento,
            )
            db.session.add(mov)
            movimientos_generados += 1

    db.session.commit()
    print(f"  {movimientos_generados} movimientos generados (últimos 7 días)")


def seed():
    with app.app_context():
        print("\nNuée — Seed de contactos y movimientos")
        print("─" * 45)

        print("\n[1/2] Clientes y proveedores...")
        seed_contactos()

        print("\n[2/2] Movimientos de la última semana...")
        seed_movimientos()

        print("\nSeed completado.")
        print("   El dashboard ahora mostrará estadísticas y top productos.\n")


if __name__ == "__main__":
    seed()