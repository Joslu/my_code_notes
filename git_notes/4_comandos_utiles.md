

__git status__
Nos permite conocer el status del repositorio, archivos nuevos, etc.

Cambiar colores de preferencia:

__git config color.status.branch magenta__

__git config color.status.added blue__

__git config color.status.untracked "141 bold"__

## Git log

Nos da información completa de cada uno de los commits

__git log__

__git log --oneline__ (Solo nos retorna una versión resumida de los cambios del reositorio)

__git log -n 2__ (Nos retorna el número de cambios que se quiera, en esta caso 2)

__git log --oneline -n 2__ (Se pueden combinar)

__git log --format=short full medium__ (Diferentes opciones, short, medium o full)

## Diff
Comando que nos es util para conocer las diferencias entre la área de trabajo y aré de repositorio

Ejemplo:

__diff --git a/index.html b/index.html__

## stash 

Git permite almacemar trozos de código sin hacer commit, se almacenan en una área guarde de git.
