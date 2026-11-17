# Nuée — Skincare Inventory System

> *From the French "nuée", a cloud — inspired by aerial photography of clouds.*

Full-stack inventory management web app for skincare businesses, built with **Python and Flask**. It tracks products, batches and expiration dates, records every stock movement, issues invoices in Colombian pesos (COP) and shows the state of the business on a dashboard.

Built by Ana Melo during the Software Development program at INDECAP (Envigado, Colombia).

---

## Features

- **Authentication**: sign in, sign up and password recovery with a 6-digit code sent by email, limited to 5 attempts and valid for 15 minutes.
- **Roles**: administrators and standard users. Editing or deleting products and movements, changing invoice status and managing users are restricted to administrators and checked on the server.
- **Products**: full CRUD with minimum stock, batch, health registry (INVIMA), VAT and expiration date.
- **Batches**: each product keeps its batches with supplier, purchase cost and expiration.
- **Inventory movements**: inbound, outbound, returns and write-offs (damage or expiration), with automatic receipt numbers.
- **Quick movement**: register a sale for an occasional customer without creating a contact first.
- **Invoicing**: invoices in COP with VAT, status (pending, paid, voided), PDF export and email delivery.
- **Clients and suppliers**: contact directory with ID type, search and quick lookup by ID number.
- **Dashboard**: totals, low-stock and expiration alerts, inbound vs outbound chart for the last 7 days and top 5 best sellers.
- **Light and dark mode** with a calm, cloud-inspired visual identity.
- **Four languages**: Spanish, English, French and Portuguese (Flask-Babel).

---

## Tech stack

| Layer | Technology |
|---|---|
| Backend | Python 3, Flask (application factory and blueprints), SQLAlchemy |
| Database | SQL Server (pyodbc, ODBC Driver 17); any SQLAlchemy URL works through `DATABASE_URL` |
| Migrations | Flask-Migrate / Alembic |
| Frontend | HTML5, CSS3, Jinja2, Bootstrap 5, Bootstrap Icons, Chart.js, JavaScript |
| Forms and security | Flask-WTF with CSRF protection, hashed passwords (Werkzeug) |
| Email | Flask-Mail (SMTP) |
| PDF | ReportLab |
| i18n | Flask-Babel |
| Configuration | python-dotenv |

---

## Project structure

```
nuee-inventory/
├── app/
│   ├── auth/                      # Sign in, sign up, password recovery, profile and users
│   ├── clienteproveedor/          # Clients and suppliers
│   ├── facturas/                  # Invoices, PDF generation and email delivery
│   ├── insumos/                   # Product catalog and inventory
│   ├── lotes/                     # Batches and expiration dates
│   ├── main/                      # Dashboard
│   ├── movimientos/               # Inbound and outbound movements
│   ├── static/                    # CSS
│   ├── templates/                 # Jinja2 templates per module
│   ├── translations/              # .po/.mo catalogs (en, fr, pt; Spanish is the source)
│   ├── extensions.py              # Flask extensions
│   └── __init__.py                # Application factory (create_app)
├── migrations/                    # Alembic history
├── app.py                         # Entry point
├── config.py                      # Development and production settings
├── babel.cfg                      # i18n extraction settings
├── requirements.txt
├── crear_usuario.py               # Creates the first administrator (asks for the password)
├── seed_nuee.py                   # Sample product catalog
└── seed_contactos_movimientos.py  # Sample contacts and movements (fictitious data)
```

---

## Running locally

### Requirements

- Python 3.10 or later
- SQL Server with ODBC Driver 17 (or another database through `DATABASE_URL`)
- An SMTP account for password recovery and invoice emails (optional in development)

### Steps

```bash
git clone https://github.com/anaxmmm/nuee-inventory.git
cd nuee-inventory

python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # macOS / Linux

pip install -r requirements.txt
```

Create a `.env` file in the project root:

```env
SECRET_KEY=a-long-random-secret-key
MAIL_USERNAME=your-email@gmail.com
MAIL_PASSWORD=your-app-password
```

```bash
# Apply migrations (the NueeDB database must exist in SQL Server)
flask db upgrade

# Optional: sample products, contacts and movements
python seed_nuee.py
python seed_contactos_movimientos.py

# Create the first administrator (asks for the password in the console)
python crear_usuario.py

# Run the app
python app.py
```

Open `http://127.0.0.1:5000`.

In development, if sending the recovery email fails, the code is printed only in the server console.

---

## Environment variables

| Variable | Description |
|---|---|
| `SECRET_KEY` | Signs sessions and CSRF tokens. Required in production. |
| `FLASK_ENV` | `development` (default) or `production` |
| `DATABASE_URL` | Full database URL. Optional in development; overrides the default SQL Server connection |
| `MAIL_USERNAME` | Email account used to send emails |
| `MAIL_PASSWORD` | App password for that account (not the main password) |
| `MAIL_DEBUG` | `True` to log SMTP traffic while debugging |
| `SESSION_COOKIE_SECURE` | `True` when the app is served over HTTPS |

The `.env` file is never committed.

---

## Translations

```bash
pybabel extract -F babel.cfg -k _l -k lazy_gettext -o app/translations/messages.pot .
pybabel update -i app/translations/messages.pot -d app/translations
pybabel compile -d app/translations
```

Available languages: `es` (Spanish, source), `en` (English), `fr` (French), `pt` (Portuguese).

---

## Design system

Nuée uses a calm, cloud-inspired identity:

| Token | Value |
|---|---|
| Sky deep (primary) | `#7B8FC7` |
| Sky mid | `#A3B2D9` |
| Sky light | `#C7D2E8` |
| Sky pale | `#EEF1F8` |
| Text | `#111111` |
| Background | `#FAFAFA` |
| UI typeface | DM Sans |
| Brand typeface | Tenor Sans |

---

## Author

**Ana Melo** — Software developer and UX/UI designer, Medellín, Colombia

- [LinkedIn](https://www.linkedin.com/in/anamelomarin/)
- [GitHub](https://github.com/anaxmmm)

---

## License

All rights reserved © 2026 Ana María Melo Marín.
