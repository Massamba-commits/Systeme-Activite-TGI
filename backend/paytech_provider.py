class PayTechProvider:
    def pay(self, item_name, amount, ref_command, success_url, cancel_url, ipn_url, method=""):
        """
        Simulation d'un paiement via PayTechProvider.
        Cette classe sert de stub pour les tests locaux.
        En production, remplacer par un appel API réel (Wave, Orange Money, etc.).
        """

        # Log pour suivi
        print(f"[SIMULATION] Paiement via {method}: {amount} XOF - Réf {ref_command}")

        # Réponse simulée
        return {
            "payment_url": success_url,   # redirection simulée vers la page de succès
            "status": "PENDING",          # statut fictif
            "ref_command": ref_command,   # référence unique de la commande
            "method": method              # méthode utilisée
        }
