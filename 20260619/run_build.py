#!/usr/bin/env python3
"""Lance le build du jour — fonctionne depuis n'importe quel sous-dossier de 20260619/."""

import os
import subprocess
import sys

build_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "build")
raise SystemExit(subprocess.run([sys.executable, "main.py"], cwd=build_dir).returncode)
