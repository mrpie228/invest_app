from .models import DealHistory, Asset




def create_history(deal_type, deal_owner, dealers, price):
    deal_hist = DealHistory.objects.create(deal_type=deal_type,
                                           deal_owner=deal_owner,
                                           dealers=dealers, price=price)
    deal_hist.save()
