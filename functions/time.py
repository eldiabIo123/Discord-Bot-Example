#########################################################
### IMPORTS                                           ###
#########################################################
import pytz
from datetime import datetime

#########################################################
### Klasa                                             ###
#########################################################
class Date:
    def __init__(self, timezone: str = "Europe/Warsaw"):
        self.timezone = pytz.timezone(timezone)

    def now(self, format: str) -> str:
        return datetime.now(self.timezone).strftime(format)
