# Manipulando la hitoria

Comandos utilizados para manipular la hitoria del repositorio. Modifican la ecuencia de cambios en el historial de git

__Precaución__ estos comandos únicamente se pueden utilizar en repositorios donde solo trabaje una persona.

## __rebase__

Cambia el lugar de origen de la rama, e utiliza para actualziar cambio de nuestra rama a la ultima version de la rama padre.

![Image](img/rebase.png)

Otro uso es para unir, descartar, borrar commits, usando __git reverse --interactive__

## __amend__
Permie modificar el último commit 

```git
git commit --amend
```

