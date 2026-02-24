import requests

class WaveMoney:
    def pay(self, item_name, amount, ref_command, success_url, cancel_url, ipn_url):
        payload = {
            "amount": amount,
            "currency": "XOF",
            "merchant_id": "TON_ID_MARCHAND",
            "ref_command": ref_command,
            "success_url": success_url,
            "cancel_url": cancel_url,
            "ipn_url": ipn_url
        }

        # Exemple d’appel API Wave (à adapter selon leur documentation)
        response = requests.post("https://api.wave.com/payment", json=payload)
        return response.json()
