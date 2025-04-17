import os

EXCLUDE = {"index.html"}

def generar_index():
    archivos = [f for f in os.listdir(".") if f.endswith(".html") and f not in EXCLUDE]

    html = """<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Índice del Sitio</title>
  <style>
    body {
      font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
      background: #f0f2f5;
      color: #333;
      padding: 2rem;
    }
    h1 {
      text-align: center;
      color: #2c3e50;
    }
    ul {
      max-width: 600px;
      margin: 2rem auto;
      padding: 0;
      list-style: none;
    }
    li {
      background: white;
      margin: 0.5rem 0;
      padding: 1rem;
      border-radius: 8px;
      box-shadow: 0 2px 4px rgba(0,0,0,0.1);
      transition: transform 0.2s ease;
    }
    li:hover {
      transform: scale(1.02);
    }
    a {
      text-decoration: none;
      color: #2980b9;
      font-weight: bold;
    }
  </style>
</head>
<body>
  <h1>📄 Páginas del Sitio</h1>
  <ul>
"""

    for archivo in sorted(archivos):
        nombre = archivo.replace(".html", "").capitalize()
        html += f'    <li><a href="{archivo}">{nombre}</a></li>\n'

    html += """  </ul>
</body>
</html>"""

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html)

    print("✨ index.html generado con estilo.")

if __name__ == "__main__":
    generar_index()
