from errbot import BotPlugin, arg_botcmd
import requests


class Charlotte(BotPlugin):
    """
    Personal bot for many operations
    """

    @arg_botcmd('ip', type=str)
    def graynoise(self, _, ip):
        """
        Run Graynoise on the target IP address
        """
        resp = requests.get(f'https://api.greynoise.io/v3/community/{ip}')
        result = resp.json()
        return f"{ip} is considered as {result['classification']} ({result['name']}, last seen: {result['last_seen'])} - more: {result['link']}"
