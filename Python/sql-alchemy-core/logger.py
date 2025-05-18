import logging
from rich.logging import RichHandler
from rich.traceback import install
from rich.console import Console
from rich.theme import Theme

install(show_locals=True)

theme = Theme({"info": "bold green", "error": "bold red", "warrning": "bold yellow"})

console = Console(theme=theme)

logging.basicConfig(
    level="NOTSET",
    format="%(message)s",
    datefmt="[%X]",
    handlers=[RichHandler(rich_tracebacks=True)],
)

logger = logging.getLogger("rich")
