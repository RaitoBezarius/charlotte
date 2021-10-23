from errbot import BotPlugin, arg_botcmd
import requests


class Charlotte(BotPlugin):
    """
    Personal bot for many operations
    """

    @arg_botcmd('ip', type=str)
    def graynoise(self, _, args):
        """
        Run Graynoise on the target IP address
        """
        resp = requests.get(f'https://api.greynoise.io/v3/community/{args.ip}')
        result = resp.json()
        return f"{args.ip} is considered as {result['classification']} (result['name'], last seen: result['last_seen']) - result['link']"
