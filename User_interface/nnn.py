from __future__ import print_function
import ctypes, sys
ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
from automatminer import MatPipe
print('ok')