# providers/wave.py
from paytech_provider import PayTechProvider

class WaveMoney:
    def pay(self, item_name, amount, ref_command, success_url, cancel_url, ipn_url):
        provider = PayTechProvider()
        return provider.pay(item_name, amount, ref_command, success_url, cancel_url, ipn_url, "Wave")
