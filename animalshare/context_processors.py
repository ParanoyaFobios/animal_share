from usertouser.models import usertouser

def unread_messages_count(request):
    if request.user.is_authenticated:
        count = usertouser.objects.filter(recipient=request.user, is_read=False).count()
        return {'unread_messages_count': count}
    return {}

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