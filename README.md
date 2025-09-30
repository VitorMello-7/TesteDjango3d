# TesteDjango3d

Projeto Django usando AdminLTE (via npm) e PostgreSQL.

## Como configurar (Windows / PowerShell)

1) Clonar o repositório e entrar na pasta

2) Criar e ativar um ambiente virtual Python

```powershell
python -m venv venv
./venv/Scripts/Activate.ps1
```

3) Instalar dependências Python

```powershell
pip install -r requirements.txt
```

4) Instalar dependências JavaScript (AdminLTE, Bootstrap, etc.)

```powershell
npm install
```

5) Criar o arquivo `.env` (copie do exemplo e ajuste valores)

```powershell
Copy-Item .env.example .env
# Edite .env e defina DJANGO_SECRET_KEY e dados de DB (DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT)
```

6) Rodar migrações e iniciar o servidor

```powershell
python manage.py migrate
python manage.py runserver
```

Aplicação por padrão estará disponível em http://127.0.0.1:8000/ (ex.: rota `/sample3d/`).

## Notas

- Os assets do AdminLTE/Bootstrap/jQuery são servidos diretamente do `node_modules` em desenvolvimento (ver `STATICFILES_DIRS` em `mysite/settings.py`).
- Em produção, configure `collectstatic` e um servidor de arquivos estáticos, ou use um pipeline para copiar somente o necessário.
- O arquivo `.env` é ignorado pelo Git; não suba segredos. Mantenha apenas um `.env.example` com placeholders, se preferir.
