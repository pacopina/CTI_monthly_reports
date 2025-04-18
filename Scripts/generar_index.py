import os

def agrupar_por_directorio(root_dir="."):
    estructura = {}
    for carpeta_actual, _, archivos in os.walk(root_dir):
        for archivo in archivos:
            if archivo.endswith(".html") and archivo != "index.html":
                ruta_relativa = os.path.relpath(os.path.join(carpeta_actual, archivo), root_dir)
                ruta_relativa = ruta_relativa.replace("\\", "/")  # Windows friendly
                carpeta = os.path.dirname(ruta_relativa)
                if carpeta not in estructura:
                    estructura[carpeta] = []
                estructura[carpeta].append((archivo, ruta_relativa))
    return estructura

def generar_index(estructura):
    with open("index.html", "w", encoding="utf-8") as f:
        f.write("""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Índice de Reportes CTI</title>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap" rel="stylesheet">
  <style>
    body {
      font-family: 'Inter', sans-serif;
      background-color: #f9fafb;
      color: #111827;
      margin: 0;
      padding: 2rem;
    }
    h1 {
      text-align: center;
      color: #1f2937;
      margin-bottom: 3rem;
    }
    .carpeta {
      max-width: 800px;
      margin: 2rem auto;
      background: #fff;
      border-radius: 8px;
      padding: 1.5rem 2rem;
      box-shadow: 0 2px 6px rgba(0,0,0,0.05);
    }
    .carpeta h2 {
      font-size: 1.2rem;
      color: #2563eb;
      margin-bottom: 1rem;
      border-bottom: 1px solid #e5e7eb;
      padding-bottom: 0.5rem;
    }
    ul {
      list-style: none;
      padding-left: 1rem;
    }
    li {
      margin: 0.4rem 0;
    }
    a {
      color: #111827;
      text-decoration: none;
      font-weight: 500;
      transition: color 0.2s ease;
    }
    a:hover {
      color: #2563eb;
    }
  </style>
</head>
<body>
  <h1>📊 Índice de Reportes CTI</h1>
""")
        for carpeta, archivos in sorted(estructura.items()):
            f.write(f'  <div class="carpeta">\n')
            f.write(f'    <h2>📁 {carpeta}</h2>\n')
            f.write('    <ul>\n')
            for nombre, ruta in sorted(archivos):
                f.write(f'      <li><a href="{ruta}">{nombre}</a></li>\n')
            f.write('    </ul>\n')
            f.write('  </div>\n')
        f.write("</body>\n</html>")

if __name__ == "__main__":
    estructura = agrupar_por_directorio()
    generar_index(estructura)
