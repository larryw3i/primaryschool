import importlib
import os
import sys
import argparse
from pathlib import *

project_path = str(Path(__file__).parent.parent.absolute())

if not project_path in sys.path:
    sys.path.append(project_path)
