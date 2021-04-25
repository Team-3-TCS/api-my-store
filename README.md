<p align="center">
<h2 align="center">MyStore Api - Taller de Construcción de Sistemas</h2>
<br>
</p>

<div align="center">
<img width=200px src="https://i.ibb.co/3TYg0qv/mystore.jpg" alt="Aurora Store"></a>
</div>

----

## Primeros pasos

- Instalar las dependencias del requirements

`pip install -r requirements.txt`


- Configurar la cadena de conexion dentro de **app\main\config.py**

`mysql_local_base = os.environ['DATABASE_URL'] = 'mysql://user:password@localhost:3306/dbMyStore'`

- Crear la base de datos **dbMyStore**

`create database dbMyStore`

- Para mapear la BD usar :

`python manage.py db upgrade`

- Para correr la aplicacion:

`python manage.py run`


## Consideraciones

- Cuando se genera un nuevo modelo o se quiere actualizar se usa que ya este en el **manage.py**:

`python manage.py db migrate`

`python manage.py db upgrade`

## Pre-requesitos
- Tener instalado **python**



