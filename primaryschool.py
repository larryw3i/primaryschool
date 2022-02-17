import getopt
import os
import sys

argv = sys.argv[1:]

for arg in argv:

    if arg == 'req_dev':
        from primaryschool.settings import install_requirements_dev
        install_requirements_dev()

    if arg == 'req_dev_u':
        from primaryschool.settings import install_requirements_dev_u
        install_requirements_dev_u()

    if arg == 'test':
        import tests

if len(argv) == 0:
    import re
    import sys

    import tests
    from primaryschool import victory
    if __name__ == '__main__':
        sys.argv[0] = re.sub(r'(-script\.pyw|\.exe)?$', '', sys.argv[0])
        sys.exit(victory())
