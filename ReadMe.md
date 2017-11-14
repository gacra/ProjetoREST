---------------
Pré-requisitos
---------------

* Linguagem:

Python 3 (versão usada: 3.6.2)

* Pacotes:

Django (versão usada: 1.11.7)
djangorestframework (versão usada: 3.7.3)

* Ambiente de teste usado:

Windowns 10 Pro 64 bits

---------
Execução
---------

Na pasta do projeto:
python manage.py runserver

----
Uso
----

* GET: http://127.0.0.1:8000/plans/

* POST: http://127.0.0.1:8000/payment/
Exemplo do body:

{  
    "payment_date": "2017-11-14",  
    "payment_type": "BL",  
    "product": 1,  
    "product_price": "59.90",  
    "discount": "30.00",  
    "transaction_id": 1  
}

Em que:

- payment_date: Data no formato AAAA-MM-DD
- payment_type: Tipo do pagamento ("CT" para cartão, ou "BL" para boleto)
- product: ID do produto (pode ser obtido pelo GET anterior)
- product_price: Preço do produto (deve ser correspondente ao produto do campo anterior)
- discount: Desconto (não deve ser superior a 50%)
- transaction_id: ID da transação (deve ser único)

Obs1: O campo price é calculado automaticamente  
Obs2: Caso o body do POST não esteja correto é retornado um código de erro HTTP 400 (Bad Request) e um JSON com os erros cometidos
Obs3: Para fins de teste foi implementado também um GET para a rota /payment

-------
Extras
-------

* Ambiente administrativo do Django:
http://127.0.0.1:8000/admin/
Usuário: adm
Senha: adm12345

* Interface do Django REST:
Acessar as rotas /plans e /payment por meio de um navegador

--------------------------------------
Arquivos relevantes do projeto Django
--------------------------------------

appRest/models.py  
appRest/serializers.py  
appRest/urls.py  
appRest/views.py  