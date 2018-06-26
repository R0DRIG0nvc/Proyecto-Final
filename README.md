# Proyecto final - Topico 2 - Desarrollo Web

## Descripción de la solución del problema que se resolvió.

El problema está centrado en la mala compra y gestión de productos por parte de una empresa, en donde es necesario generar un mantenedor de ventas y de productos, donde las ventas depende 100% del inventario actual. El actual sistema satisface las necesidades del cliente, en donde se contemplan dos perfiles de usuarios:

Administrador: El administrador es el encargado de poblar el sistema con categorías y productos, en donde especifica la cantidad y el stock.

Cliente: El cliente tiene acceso al carro de compra, en donde él elije los productos que desea encargar al sistema, en donde procederá a administra sus carros de compras.

### Instrucciones necesarias para poder desplegar el proyecto (SO Linux).

* Instalar git.
```
sudo apt-get install git
```

* Instalar virtualenv para poder generar nuestro entorno de trabajo.
```
sudo apt-get install python-virtualenv virtualenv
```

* Clonar nuestro repositorio git.
```
git clone git@github.com:R0DRIG0nvc/Proyecto-Final.git
```

* Crear nuestro ambiente virtual utilizando el nombre de nuestro repositorio git.
```
virtualenv -p python3 "nombre repositorio"
```

* Activar ambiente virtual (Posicionarse donde se encuentra nuestro archivo 'bin')
```
source bin/activate
```

* Instalar el archivo requirements.
```
pip install -r requirements.txt
```

* Una vez instalados los requerimientos procedemos a levantar nuestro proyecto. Debemos ubicarnos donde se encuentre nuestro archivo 'manage.py' y realizar el siguiente comando.
```
python manage.py runserver
```
* Finalmente se procede a conectarse al servidor utilizando la siguiente url.
```
http://localhost:8080/
```
#### Usuarios de prueba.
* Administrador.
```
username: root
password: hola12345
```

* Cliente.
```
Es necesario registrarse
```
