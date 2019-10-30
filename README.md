# AySA Cli

Marco de trabajo para el despliegue de contenedores.

## Instalación

Se requiere la versión de `python` **>=3.6**, en adelante.

### Con entorno virtual

```bash
# creamos el entorno virtual
> virtualenv --python=python37 aysa

# ingresamos al directorio del entorno
> cd aysa

# iniciamos el entorno
> source ./bin/activate

# instalamos dentro del entorno
> pip install https://github.com/alejandrobernardis/aysa-cli/archive/master.zip

# test
> aysa -v
... 1.0.0.dev.0
```

### Sin entorno virtual

```bash
> pip install https://github.com/alejandrobernardis/aysa-cli/archive/master.zip
```

### Desde el código fuente

```bash
# clonamos el repositorio
> git clone https://github.com/alejandrobernardis/aysa-cli.git

# ingresamos al directorio del repositorio
> cd aysa-cli

# instalamos
> python setup.py install
```
