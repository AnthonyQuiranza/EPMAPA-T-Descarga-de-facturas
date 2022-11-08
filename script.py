#Importamos el módulo request, en caso de no tenerlo instalado usar "pip install request"
import requests as req
#Contador, número de pdf que se requiere instalar
cont = 184
while cont <= 231:
    name = f"FACTURA_001-015-000018{cont}.pdf"
    URL = f'http://192.168.0.8:8080/recursos_siim/FE/autorizados/{name}'
    file = req.get(URL, allow_redirects=True)
    open(f'docs2/{name}', 'wb').write(file.content)
    cont= cont + 1
