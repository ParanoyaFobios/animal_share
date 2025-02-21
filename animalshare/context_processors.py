from usertouser.models import usertouser
from django.db.models import Sum
from goods.models import Categories
from carts.models import Carts


def unread_messages_count(request):
    if request.user.is_authenticated:
        count = usertouser.objects.filter(recipient=request.user, is_read=False).count()
        return {'unread_messages_count': count}
    return {}


def cart_total_quantity(request):
    total_quantity = 0
    if request.user.is_authenticated:
        user = request.user
        total_quantity = Carts.objects.filter(user=user).aggregate(total_quantity=Sum('quantity'))['total_quantity'] or 0
    else:
        session_key = request.session.session_key
        total_quantity = Carts.objects.filter(session_key=session_key).aggregate(total_quantity=Sum('quantity'))['total_quantity'] or 0
    return {'total_quantity': total_quantity}


def categories(request):
    categories = Categories.objects.all()  # Получаем все категории
    return {'categories': categories}

#контекстные процессоры используются для добавления переменных, доступных в любом месте шаблонов.
#требует добавления в файл настроек TEMPLATES = [
#     {
#         ...
#         'OPTIONS': {
#             'context_processors': [
#                 ...
#                 'your_app.context_processors.unread_messages_count',
#             ],
#         },
#     },
# ]