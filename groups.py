def get_group(customer_id):
    '''
    Вычисляет сумму цифр в id клиента
    
    Args:
        customer_id: id клиента
    Return:
        s: сумма цифр
    '''
    s = 0
    while customer_id != 0:
        s += customer_id % 10
        customer_id = customer_id // 10
    
    return s


def first(n_customers):
    '''
    Проходится по всем клиентам с id от 0 до n_customers и вычисляет для каждого группу.
    Количество найденных групп сохраняется в словаре groups
    
    Args:
        n_customers: количество клиентов
    Return:
        groups: словарь, в котором ключ - номер группы, значение - количество клиентов в группе
    '''
    groups = dict()
    
    for i in range(n_customers):
        group = get_group(i)
        if group in groups:
            groups[group] += 1
        else:
            groups[group] = 1
    
    return groups


def second(n_customers, n_first_id):
    '''
    Все как в функции first, но проходимся от n_first_id до n_first_id + n_customers
    
    Args:
        n_customers: количество клиентов
    Return:
        groups: словарь, в котором ключ - номер группы, значение - количество клиентов в группе
    '''
    groups = dict()
    
    for i in range(n_first_id, n_first_id + n_customers):
        group = get_group(i)
        if group in groups:
            groups[group] += 1
        else:
            groups[group] = 1
    
    return groups