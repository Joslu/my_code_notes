# Comandos escenciales
## Creando nuevo repo

__Git Init__
Genera una carpeta .git donde se almacena el historial de las versiones del repositorio.

## Agregar cambios
Agregar los cambios al stage de git

__git add file.txt__ (Archivo especfico)

__git add *.txt__ (Agrega todos los archivos txt)

__git add src/component*__ (Agregar un path)

__git add .__ (Agrega todos los archivos que se hayan modificado)

__git add -A__ ( Agrega todos los archivos con cambios ene l proyecto)

__git add -u__ (Agrega todos los archivos modifiados o eliminados)

__git reset__ (Devuelve cambios en archivos a la zona de trabajo)

## Guardar cambios

__commit__ 
Comando para mover los cambios de stage al área de repositorio

__git commit -m 'mensaje commit'__

Estrategias de commits:
- commit pequeños y frecuentes
- cambios significativos, relacionados una funcionalidad

Buenas practicas:
- titulo debe tener maximo 50
- verbos imperativos (fix, add, delete, update)
- espacio entre titulo y descripcion
- en qué y porqué
- sigue las convenencias de tu equipo

## Sincronizar cambios

__git push__

enviar cambios del repositorio local al remoto

repositorio remoto

__git remote add origin git@github.com:youremail/mireporemoto.git__

__git branch -M main__

__git push -u origin main__

__git pull__
traer los cambios del repositorio remoto al local
