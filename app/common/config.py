import sys
from pathlib import Path

if getattr(sys, 'frozen', False):
    SYS_PATH = Path(sys.executable).parent
else:
    SYS_PATH = Path(__file__).resolve().parent.parent

THEME_PATH = ":/qss/dark/template_dark.qss"
QSS_PATH = SYS_PATH / 'resources' / 'qss'

TOP_FRAME = 'top_frame.qss'
BOTTOM_FRAME = 'bottom_frame.qss'
