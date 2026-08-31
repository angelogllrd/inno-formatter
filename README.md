# inno-formatter

[Inno Setup](https://jrsoftware.org/isinfo.php) genera un script previo a la compilación **para obtener el instalador de nuestro programa Python**, pero antes de compilar suele ser necesario realizar varias modificaciones manuales para que el instalador funcione correctamente y sea más amigable.

`inno-formatter.py` es un script que automatiza este proceso, ahorrándonos hacerlo línea por línea. Al ejecutarlo, analiza el script en el portapapeles y aplica de forma **automática** las siguientes tres mejoras:

1. **Soluciona el problema de las carpetas:** Modifica las líneas correspondientes a las subcarpetas de nuestro proyecto, corrigiendo la ruta de destino (reemplaza `{app}` por `{app}/nombre_carpeta`).
   ![image](https://github.com/user-attachments/assets/3a29a25c-db91-4085-8dd2-6148b408c1f8)
2. **Ícono en el escritorio por defecto:** Elimina el flag `unchecked` para que la opción de crear un acceso directo en el escritorio ya venga marcada (util para instalación con `/SILENT`).
3. **Ejecución en modo silencioso:** Quita la restricción `skipifsilent` para que el programa se inicie automáticamente al terminar la instalación si fué ejecutado con el parámetro `/SILENT`).

### Requisitos
* pyperclip (https://pypi.org/project/pyperclip/)

### Pasos para usarlo
1. Copiar el script generado por Inno Setup al finalizar el Script Wizard.

   ![image](https://github.com/user-attachments/assets/6cc2bac5-4047-45ce-8f01-03efff674a21)
   
2. Abrir la consola en la carpeta de `inno-formatter.py` y ejecutar:
   ```bash
   $ python inno-formatter.py

3. Pegar el script formateado que se copió al portapapeles en Inno Setup, reemplazando el original.

   ![image](https://github.com/user-attachments/assets/a82bae10-2e2d-4298-a616-c3b2d36e35dd)

