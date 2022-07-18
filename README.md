# mo_technologies
### Los commits recientes son agregados por la rama master
### Para hacer el despliegue se necesita que la maquina anfitrión tenga instalado y configurado docker y docker-compose
## Clonar repositorio
- git clone https://github.com/softkra/mo_technologies.git
#### *No deberia presentar problemas al momento de clonarlo ya que el repositorio es publico*
## Iniciar despliegue del proyecto mediante docker
- Una vez clonado el repositorio, se ingresa al directorio 'mo_technologies'
- Con `docker-compose up --build -d` se iniciará la construccion de los contenedores docker que estan configurados para trabajar con la version de Python 3.9 y la ultima de Django soportada por la version de python
- Una vez se creen los contenedores se puede hacer seguimiento a los logs con el comando `docker-compose logs -f` y en este apartado nos debe mostrar lo siguiente:
```
mo-backend-1  | System check identified no issues (0 silenced).
mo-backend-1  | July 18, 2022 - 01:11:23
mo-backend-1  | Django version 4.0.6, using settings 'mo_technologies.settings'
mo-backend-1  | Starting development server at http://0.0.0.0:8000/
mo-backend-1  | Quit the server with CONTROL-C.
```
## Colección de postman [AQUI](https://github.com/softkra/mo_technologies/blob/master/mo-technologies.postman_collection.json)
##### _El código almacenado en este GitHub fue desarrollado por Christian David Porres_
