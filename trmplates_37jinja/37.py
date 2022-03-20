# from jinja2 import Template

# name = "Игорь"
# age = 28

# tm =Template("Привет {{ n }}. Мне {{ a*2 }} лет")
# msg = tm.render(n=name, a=age)
# print(msg)


# или

# per = {'name': 'Игорь', 'age': 28}
# tm =Template("Привет {{ p.name }}. Мне {{ p.age }} лет")
# msg = tm.render(p=per)
# print(msg)

# или

# per = {'name': 'Игорь', 'age': 28}
# tm =Template("Привет {{ p['name'] }}. Мне {{ p['age'] }} лет")
# msg = tm.render(p=per)
# print(msg)


# class Person:
#     def __init__(self, name, age):
#         self.name= name
#         self.age=age
#
# per=Person("Игорь", 28)
# tm =Template("Привет {{ p.name }}. Мне {{ p.age }} лет")
# msg = tm.render(p=per)
# print(msg)

# class Person:
#     def __init__(self, name, age):
#         self.name= name
#         self.age=age
#
#     def get_name(self):
#         return self.name
#
#     def get_age(self):
#         return self.age
#
# per=Person("Игорь", 28)
# tm =Template("Привет {{ p.get_name() }}. Мне {{ p.get_age() }} лет")
# msg = tm.render(p=per)
# print(msg)


# data="""Модуль Jinja вместо определения {{ name }}
# посдствит соответсвующее
# значение
# """
# tm=Template(data)
# msg = tm.render(name="Игорь")
# print(msg)

# или
# data="""{%raw%}Модуль Jinja вместо определения {{ name }}
# посдствит соответсвующее
# значение{% endraw%}
# """
# tm=Template(data)
# msg = tm.render(name="Игорь")
# print(msg)

# link = "<a href = '#> Ссылка</a>"
# tm=Template('{{link | e}}')
# msg = tm.render(link=link)
# print(msg)

# cites =[
#     {"id": 1, "city": "Москва"},
#     {"id": 2, "city": "Смоленск"},
#     {"id": 3, "city": "Минск"},
#     {"id": 4, "city": "Житомир"},
#     {"id": 5, "city": "Ярославль"}
# ]
#
# link ="""<select name="cites">
# {% for c in cites -%}
#     {% if c.id>3 -%}
#         <option value = "{{c['id']}}">{{c['city'] }}</option>
#     {% elif c.city == "Москва" -%}
#         <option >{{ c['city'] }}</option>
#     {% else -%}
#         {{ c['city'] }}
#     {% endif -%}
# {% endfor -%}
# </select>
# """
# tm=Template(link)
# msg = tm.render(cites=cites)
#
# print(msg)



from jinja2 import Template

menu=[
    {'href': '/index', 'link': 'Главная'},
    {'href': '/news', 'link': 'Новости'},
    {'href': '/about', 'link': 'О компании'},
    {'href': '/shop', 'link': 'Магазин'},
    {'href': '/contacts', 'link': 'Контакты'},
]

link="""<ul> 
<li><a href="/index" class="active">Глвная</a></li>
{% for m in menu[1:]-%}
    <li><a href="{{ m['href'] }}">{{ m['link'] }}</a></li>
{% endfor -%}
</ul>
"""

tm=Template(link)
msg = tm.render(menu=menu)

print(msg)


# from jinja2 import Template

# cars=[
#     {'model': 'AUDI', 'price': 23000},
#     {'model': 'Skoda', 'price': 17000},
#     {'model': 'Renult', 'price': 44000},
#     {'model': 'Wolkvagen', 'price': 21000},
# ]
#
# tpl="Суммарная цена автомобилей {{ sc | sum(attribute='price')}}"
#
# tm=Template(tpl)
# msg = tm.render(sc=cars)
#
# print(msg)


# from jinja2 import Template
#
# cars=[
#     {'model': 'AUDI', 'price': 23000},
#     {'model': 'Skoda', 'price': 17000},
#     {'model': 'Renult', 'price': 44000},
#     {'model': 'Wolkvagen', 'price': 21000},
# ]
# lst=[1, 2, 3, 4, 5, 6]
#
# tpl="Суммарная цена автомобилей {{ sc | sum()}}"
#
# tm=Template(tpl)
# msg = tm.render(sc=lst)

# print(msg)

# from jinja2 import Template
#
# cars=[
#     {'model': 'AUDI', 'price': 23000},
#     {'model': 'Skoda', 'price': 17000},
#     {'model': 'Renult', 'price': 44000},
#     {'model': 'Wolkvagen', 'price': 21000},
# ]
# # lst=[1, 2, 3, 4, 5, 6]
#
# tpl="Суммарная цена автомобилей {{ (sc | min(attribute='price')).model}}"
#
# tm=Template(tpl)
# msg = tm.render(sc=cars)
# print(msg)

# from jinja2 import Template
#
# cars=[
#     {'model': 'AUDI', 'price': 23000},
#     {'model': 'Skoda', 'price': 17000},
#     {'model': 'Renult', 'price': 44000},
#     {'model': 'Wolkvagen', 'price': 21000},
# ]
# # lst=[1, 2, 3, 4, 5, 6]
#
# tpl="Суммарная цена автомобилей {{ sc | random}}" # случаный выбор
#
# tm=Template(tpl)
# msg = tm.render(sc=cars)
# print(msg)

# from jinja2 import Template
#
# cars=[
#     {'model': 'AUDI', 'price': 23000},
#     {'model': 'Skoda', 'price': 17000},
#     {'model': 'Renult', 'price': 44000},
#     {'model': 'Wolkvagen', 'price': 21000},
# ]
# # lst=[1, 2, 3, 4, 5, 6]
#
# tpl="Суммарная цена автомобилей {{ sc | replace('model', 'brand') }}"
#
# tm=Template(tpl)
# msg = tm.render(sc=cars)
# print(msg)