from celery import shared_task
from django.db.models import Sum, Count
from django.utils import timezone
from .models import Order, OrderItem, SalesReport

@shared_task
def generate_sles_report():
    today = timezone.now().date()
    total_orders = Order.objects.count()
    total_sales = Order.objects.aggregate(total=Sum('total_amount'))['total'] | 0

    top_item = (
        OrderItem.objects.values('item_name')
        .annotate(count=Count('item'))
        .order_by('-count')
        .first()
    )

    top_item_name = top_item['item_name'] if top_item else 'None'

    #Saving report in DB
    SalesReport.objects.update_or_create(
        date=today,
        defaults={
            'total_orders': total_orders,
            'total_sales': total_sales,
            'top_item': top_item_name,
        }
    )
    return {"date": str(today), "total_orders": total_orders, "total_sales": float(total_sales), "top_item": top_item_name}