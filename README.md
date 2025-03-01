# inno-formatter

[Inno Setup](https://jrsoftware.org/isinfo.php) genera un script previo a la compilación **para obtener el instalador de nuestro programa Python**, pero antes de compilar es necesario **modificar las líneas correspondientes a las carpetas de nuestro proyecto** de la siguiente forma, carpeta por carpeta:

![image](https://github.com/user-attachments/assets/3a29a25c-db91-4085-8dd2-6148b408c1f8)

`inno-formater.py` es un script que hace las modificaciones de forma **automática**, ahorrándonos hacerlo línea por línea.

### Requisitos
* pyperclip (https://pypi.org/project/pyperclip/)

### Pasos para usarlo
1. Copiar el script generado por Inno Setup al finalizar el Script Wizard.

   ![image](https://github.com/user-attachments/assets/6cc2bac5-4047-45ce-8f01-03efff674a21)
   
2. Abrir la consola en la carpeta de `inno-formatter.py` y ejecutar:
   ```
   $ python inno-formatter.py
   ```   
3. Pegar el script formateado que se copió al portapapeles en Inno Setup, reemplazando el original.
   
   ![image](https://github.com/user-attachments/assets/a82bae10-2e2d-4298-a616-c3b2d36e35dd)

