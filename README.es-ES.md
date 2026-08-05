

# Plantilla de Nuevo Proyecto de Python de Alex

![GitHub tag (latest by date)](https://img.shields.io/github/v/tag/alexfayers/new_python_project?label=version)
![Lines of code](https://img.shields.io/tokei/lines/github/alexfayers/new_python_project)
![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/alexfayers/new_python_project/CI.yml?label=tests)
![GitHub last commit](https://img.shields.io/github/last-commit/alexfayers/new_python_project)

Este repositorio te permite iniciar un nuevo proyecto de Python más rápido. Configura algunas cosas después de que [crees un nuevo repositorio a partir de esta plantilla](https://github.com/alexfayers/new_python_project/generate), para que puedas comenzar con tu nueva idea antes.

## Instalación

Puedes usar este repositorio de varias maneras:

- [Crear un nuevo repositorio a partir de esta plantilla](https://github.com/alexfayers/new_python_project/generate) (este es el método más fácil)
- [Usar el script auxiliar](#using-the-helper-script) (este es el método que uso)
- [Usar cookiecutter](#using-cookiecutter) (ideal si ya usas cookiecutter)
- [Usar cruft](#using-cruft) (útil para mantener tu proyecto actualizado)

Después de crear tu nuevo repositorio, espera a que se complete el flujo de trabajo [rename_templates](.github/workflows/rename_templates.yml). Esto moverá algunos archivos, renombrará ciertos elementos y restablecerá la versión del proyecto para que todo esté listo para que comiences.

Luego puedes clonar el repositorio localmente y comenzar a programar.

*Recomiendo usar [Visual Studio Code](https://code.visualstudio.com) con mi paquete de extensiones ([Alex's New Python Project Template - Extensions](https://marketplace.visualstudio.com/items?itemName=alexfayers.alexs-nppt-extensions))*

### Usando cookiecutter

Puedes usar [cookiecutter](https://cookiecutter.readthedocs.io/en/1.7.2/) para crear un nuevo proyecto a partir de esta plantilla. Puedes usar este método de la siguiente manera:

```bash
$ pip install cookiecutter
$ cookiecutter gh:alexfayers/new_python_project
```

### Usando el script auxiliar

También puedes instalar este repositorio como un módulo de Python y usarlo para crear un nuevo proyecto. Instala un nuevo script llamado `anppt` (Alex's New Python Project Template), que simplemente envuelve a cookiecutter. Este método es útil si creas muchos proyectos con esta plantilla (¡como yo!). Puedes usar este método de la siguiente manera:

```bash
$ pip install git+https://github.com/alexfayers/new_python_project.git
$ anppt
```

# Usando cruft

Puedes usar [cruft](https://cruft.github.io/cruft/) para crear un nuevo proyecto a partir de esta plantilla, lo que significa que podrás mantenerte al día con cualquier cambio en la plantilla original. Puedes usar este método de la siguiente manera:

```bash
$ pip install cruft
$ cruft create https://github.com/alexfayers/new_python_project.git
```

Y luego puedes actualizar tu proyecto a la última versión de la plantilla con cruft de la siguiente manera:

```bash
$ cruft update
```

¡Fácil!

## Desarrollo

La plantilla incluye algunas de mis preferencias para escribir en Python:

- Todos los parámetros de las funciones y los valores de retorno deben tener tipado.
- Todas las funciones, clases y módulos deben contener docstrings (en el formato de Google).
- Los ganchos de pre-commit están disponibles para habilitar la ejecución de linting y formateo antes de hacer un commit. Puedes instalarlos usando `pre-commit install` o simplemente ejecutarlos una vez con `tox -e lint`.
- También se incluyen algunas clases y funciones útiles que uso mucho como submódulos de tu módulo. En el futuro crearé un sistema para gestionarlas, pero por ahora puedes eliminarlas si no las necesitas.
- El proyecto es instalable como un módulo de Python, lo que te permite incluso subirlo a PyPI, si lo deseas.

## Tox

La [configuración de tox](tox.ini) también proporciona muchos atajos útiles. Por ejemplo:

---

Puedes ejecutar tus pruebas unitarias usando:

```bash
tox
```

---

Puedes validar y formatear tu código y documentación usando:

```bash
tox -e lint
```

---

Puedes regenerar tu documentación localmente usando:

```bash
tox -e docs
```

_(Aunque la documentación se genera y actualiza automáticamente si es necesario, como último paso del [flujo de trabajo de CI](.github/workflows/CI.yml))_

---

Puedes construir el proyecto en archivos `.whl` y `.tar.gz` usando:

```bash
tox -e build
```

---

Y hasta puedes crear un nuevo lanzamiento en GitHub usando:

```bash
tox -e release patch  # for a small fix
tox -e release minor  # for a small improvement
tox -e release patch  # for a big change or feature addition
```

_El comando de lanzamiento también actualizará automáticamente tu [changelog](CHANGELOG.md) mediante el uso de [gitchangelog](https://github.com/vaab/gitchangelog)._

---

## Documentación, reiterada

Toda la documentación se genera usando pdoc. De todos modos, cada función y cada clase necesitan un docstring: es una [buena práctica](https://peps.python.org/pep-0257/#what-is-a-docstring).

Las pruebas de CI no pasarán hasta que todos los docstrings estén escritos y formateados correctamente. Esto puede resultar molesto para algunas personas al principio, pero en realidad es muy útil a largo plazo, ya que te obliga a documentar a medida que avanzas.

## Obtener cambios del repositorio upstream

Si lo deseas, puedes agregar este repositorio como un remoto upstream, y luego podrás extraer cualquier actualización de la plantilla a tu propio repositorio:

```bash
# Add the upstream remote:
git remote add upstream https://github.com/alexfayers/new_python_project
# Make sure we can't push to it:
git remote set-url --push upstream no_push
```

Luego, cuando quieras actualizar, puedes hacer algo como esto:

```bash
# pull from upstream, ignoring the fact that our new repo isn't technically the same repo as the upstream
git pull upstream main --allow-unrelated-histories
# Only accept our changes if there are merge issues - these might happen because of the rename script
git checkout --ours .
# Stage all of the new changes to stop merge issue warnings popping up everywhere
git add .
# commit all of that
git commit -m 'Merge upstream'

# ???
# profit
```
