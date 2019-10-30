# Author: Alejandro M. Bernardis
# Email: alejandro.bernardis at gmail.com
# Created: 2019/10/12
# ~

__all__ = [
    '__title__',
    '__summary__',
    '__uri__',
    '__version__',
    '__author__',
    '__email__',
    '__license__',
    '__copyright__',
    '__commands__',
    'SEGMENT',
    'VERSION'
]

# version
SEGMENT = 'dev'
VERSION = (1, 0, 0, SEGMENT, 0)

# doc
__title__ = 'aysa-cli'
__summary__ = 'Marco de trabajo para el despliegue de contenedores.'
__uri__ = 'https://github.com/alejandrobernardis/aysa-cli/'
__issues__ = 'https://github.com/alejandrobernardis/aysa-cli/issues/'
__version__ = '.'.join([str(x) for x in VERSION])
__author__ = 'Alejandro M. BERNARDIS and individual contributors.'
__email__ = 'alejandro.bernardis@gmail.com'
__license__ = 'MTI License, Version 2.0'
__copyright__ = 'Copyright 2019-% {}'.format(__author__)
__commands__ = 'https://github.com/alejandrobernardis/aysa-commands/archive' \
               '/master.zip'