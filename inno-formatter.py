#! python3
# Formatea el script de creación del instalador de Inno Setup para:
#   * solucionar el problema de las carpetas
#   * tildar el checkbox de ícono en escritorio
#   * iniciar automáticamente si la instalación es /SILENT
# y lo copia al portapapeles.

# By Angelo Gallardi

import re, pyperclip

# Obtengo el texto del portapapeles
script = pyperclip.paste()

# Separo el texto en lineas
lineas = script.splitlines()

salida = []
for linea in lineas:
	# 1. Verifico "Flags: unchecked"
	if 'Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}";' in linea:
		salida.append(linea.replace(' Flags: unchecked', ''))

	# 2. Verifico linea de carpeta
	elif 'recursesubdirs createallsubdirs' in linea:
		# Busco el nombre de la carpeta
		mo = re.search(r'\\([^\\]+)\\\*";', linea) # Regex para detectar el patrón "\nombre_carpeta\*"
		carpeta = mo.group(1)

		# Formateo la linea reemplazando "{app}" por "{app}/nombre_carpeta" y la agrego a las demás
		salida.append(linea.replace('{app}', '{app}/' + carpeta))

	# 3. Verifico linea de ejecución al terminar instalación
	elif 'Flags: nowait postinstall skipifsilent' in linea:
		salida.append(linea.replace(' skipifsilent', ''))

	# 4. No debo modificar nada, copio tal cual
	else:
		salida.append(linea)

# Formo nuevamente el script y lo copio al portapapeles
script = '\n'.join(salida)
pyperclip.copy(script)
print('Script formateado copiado al portapapeles.')