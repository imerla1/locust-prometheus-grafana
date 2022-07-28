import logging
from rich.logging import RichHandler
import requests

FORMAT = "%(message)s"
logging.basicConfig(
    level="NOTSET", format=FORMAT, datefmt="[%X]", handlers=[RichHandler()]
)

log = logging.getLogger("rich")
log.info("Hello, World!")
log.error("[bold red blink]Server is shutting down![/]")

url = "http://localhost:8000"
resp = requests.get(url)
log.debug(f"resp from {url} code: {resp.status_code}")