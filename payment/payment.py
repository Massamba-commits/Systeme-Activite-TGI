import datetime
from orange import OrangeMoney
from wave import WaveMoney

class Payment:
    def __init__(self):
        self.orange = OrangeMoney()
        self.wave = WaveMoney()
    
    def create_payment(self, user_id, item_name, amount, method, success_url, cancel_url, ipn_url):
        """Créer un paiement via Orange Money ou Wave.
        method: nom du moyen (par ex. 'Orange Money' ou 'Wave')."""
        ref_command = f"CMD{user_id}{int(datetime.datetime.now().timestamp())}"
        m = (method or "").strip().lower()

        try:
            if m in ("orange money", "orange", "orange_money", "orange-money"):
                return self.orange.pay(item_name, amount, ref_command, success_url, cancel_url, ipn_url)
            if m in ("wave", "wave money", "wave_money", "wave-money"):
                return self.wave.pay(item_name, amount, ref_command, success_url, cancel_url, ipn_url)

            return {"error": "Méthode de paiement invalide"}
        except Exception as e:
            return {"error": "Erreur lors de la création du paiement", "details": str(e)}
