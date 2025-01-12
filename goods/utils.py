from goods.models import Products
from django.db.models import Q


def q_search(query): #этой функцие сортировки (если бы мы указалаи Products.objects.get(id=int(query)) на выходе получили бы обьект), мы получает qwert set при условии ввода 5ти цифр(айди товара)
    if query.isdigit() and len(query) <= 5:
        return Products.objects.filter(id=int(query))
    
    keywords = [word for word in query.split() if len(word) > 3] #создал генератор списков с условием, разделять запрос если введые строки больше 3ех символов
    q_objects = Q() #создал отдельную переменную т.к. оператор Q имеет специальный синтаксис
    for token in keywords:
        q_objects |= Q(description__icontains=token) #|= это форма записи, операторы или, равно ( x = x + 1; x+=1] )
        q_objects |= Q(name__icontains=token) #|= это форма записи, операторы или, равно ( x = x + 1; x+=1] )
    return Products.objects.filter(q_objects)