# Author: Alejandro M. Bernardis
# Email: alejandro.bernardis at gmail.com
# Created: 2019/10/12
# ~

import sys
import logging
from aysa_cli import __version__ as cli_v, __commands__ as cmd_u

try:
    from pip._internal.main import main as pip
except ImportError:
    from pip._internal import main as pip

log = logging.getLogger(__name__)


def upgrade(done=True):
    result = pip(['install', '--upgrade', cmd_u])
    if done is True:
        sys.exit(result)
    return result


def run(argv=None):
    cmd = __import__('aysa_commands')
    version = 'AySA Command Line Tool, client v{}, commands v{}'\
              .format(cli_v, cmd.__version__)
    top = cmd.TopLevelCommand('aysa', {'version': version})
    top.parse(argv)
    sys.exit(0)


def main():
    argv = sys.argv[1:]
    try:
        if argv and argv[0].lower() == 'upgrade':
            upgrade()
        else:
            run(argv)
    except ImportError:
        log.error('Commands not found.')
        upgrade(False) == 0 and main()
    except KeyboardInterrupt:
        log.error('Aborting.')
    except Exception as e:
        log.error(e)
    sys.exit(1)
