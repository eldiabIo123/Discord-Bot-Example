#########################################################
### IMPORTS                                           ###
#########################################################
import os
from dotenv import load_dotenv
from dhooks import Webhook as DHWebhook

#########################################################
### Klasy                                             ###
#########################################################
class WebhookManager:
    def __init__(self):
        load_dotenv("../.env")
        self._hooks = {
            "log": DHWebhook(str(os.getenv("Webhook_logi"))),
            "error": DHWebhook(str(os.getenv("Webhook_error"))),
        }

    def __getattr__(self, name):
        if name in self._hooks:
            def sender(**kwargs):
                self._hooks[name].send(**kwargs)
            return sender
        raise AttributeError(f"Webhook '{name}' nie istnieje.")

#########################################################
### VARIABLE                                          ###
#########################################################
Webhook = WebhookManager()