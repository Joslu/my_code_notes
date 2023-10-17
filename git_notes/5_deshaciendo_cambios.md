# Deshaciendo cambios

## __revert__

```git

git revert <hash-del-commit>

```

En lugar de modificar la hitoria, nos genera un nuevo commit que revierta los cambios que queremos deshacer.

## __reset__

No permite mover el apuntador del estado actual a un commit anterior. Util si deseas deshacer mas commits y volver a un estado anterior 

```git
git reset --soft HEAD~1
```

__--mixed__
- Deshace el commit
- Mantiene los cmabios en el área de trabajo

__--hard__
- Dehace el commit
- Deshace los cambios
- Cambios no recuperables
- 