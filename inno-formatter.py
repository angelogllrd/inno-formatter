#! python3
# Formatea el script de creación del instalador de Inno Setup para solucionar
# el problema de las carpetas, y lo copia al portapapeles.

# By Angelo Gallardi

import re, pyperclip

# Obtengo el texto del portapapeles
script = pyperclip.paste()

# Separo el texto en lineas
lineas = script.splitlines()

# Formateo las lineas de carpetas
salida = []
for linea in lineas:
	if 'recursesubdirs createallsubdirs' in linea: # Las lineas de carpetas contienen las 2 palabras
		# Busco el nombre de la carpeta
		mo = re.search(r'\\([^\\]+)\\\*";', linea) # Regex para detectar el patrón "\nombre_carpeta\*"
		carpeta = mo.group(1)

		# Formateo la linea reemplazando "{app}" por "{app}/nombre_carpeta" y la agrego a las demás
		salida.append(linea.replace('{app}', '{app}/' + carpeta))
	else:
		salida.append(linea)

# Formo nuevamente el script y lo copio al portapapeles
script = '\n'.join(salida)
print('Script formateado copiado al portapapeles.')
pyperclip.copy(script)