# -*- coding: utf-8 -*-
import re
import sys
from enterprise_gateway import launch_instance
if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw|\.exe)?$', '', sys.argv[0])
    sys.exit(launch_instance())