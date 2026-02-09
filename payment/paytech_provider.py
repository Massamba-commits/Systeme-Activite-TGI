# providers/paytech_provider.py
class PayTechProvider:
    def pay(self, item_name, amount, ref_command, success_url, cancel_url, ipn_url, method=""):
        # Simulation pour tests locaux
        print(f"[SIMULATION] Paiement via {method}: {amount} XOF - Réf {ref_command}")
        return {
            "payment_url": success_url,  # redirection vers /success
            "status": "PENDING",
            "ref_command": ref_command
        }

     p