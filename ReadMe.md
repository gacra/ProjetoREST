#Projeto REST

Guilherme José Acra

##Pré-requisitos

###Linguagem

[Python 3](https://www.python.org/) (versão usada: 3.6.2)

### Pacotes

[Django](https://www.djangoproject.com/) (versão usada: 1.11.7)<br>
[Django REST framework](http://www.django-rest-framework.org/) (versão usada: 3.7.3)

Que podem ser baixados da seguinte maneira:
```sh
$ pip install django
$ pip install djangorestframework
```

### Ambiente de teste usado:

Windowns 10 Pro 64 bits

##Execução

Execute:
```sh
$ python manage.py makemigrations appREST
$ python manage.py migrate
$ python manage.py loaddata plans_seed.json
$ python manage.py runserver
```
Os dois primeiros comandos criam o banco de dados.<br>
O segundo insere no banco os produtos padrões.<br>
Por fim, o último inicia o servidor.

##Uso

###Segunda Etapa

Com o servidor rodando, basta entrar na url `http://127.0.0.1:8000/pages/` em algum navegador.

A primeira página mostra todos os planos disponíveis. 

A página de pagamento se encontra em `http://127.0.0.1:8000/pages/new_payment/`, entretanto é possível chegar nela através da página inicial.

Exemplos de como as páginas deveriam ser renderizadas se encontram na pasta `Exemplos` deste projeto.

Ambas as páginas foram desenvolvidas para serem responsivas.

O navegador usado para o desenvolvimento foi o *Google Chrome (v62.0)*, sendo onde as páginas apresentam melhor resposta. Testes também foram feitos no *Mozilla Firefox (v57.0)* e no *Microsoft Edge (v40)*. Nesses navegadores, há apenas algumas pequenas alterações de aparência, não prejudicando a usabilidade.

###Primeira Etapa

####GET: 

Usar a rota `http://127.0.0.1:8000/plans/`

#### POST: 

Usar a rota `http://127.0.0.1:8000/payment/`

Exemplo do body:

```
{  
  "payment_date": "2017-11-14",  
  "payment_type": "BL",  
  "product": 1,  
  "product_price": "59.90",  
  "discount": "30.00",  
  "transaction_id": 1  
}
```

Em que:

| Campo | Valor |
|-------|-------|
| payment_date    | Data no formato AAAA-MM-DD |
| payment_type:   | Tipo do pagamento ("CT" para cartão, ou "BL" para boleto) |
| product:        | ID do produto (pode ser obtido pelo GET anterior) |
| product_price:  | Preço do produto (deve ser correspondente ao produto do campo anterior) |
| discount:       | Desconto (não deve ser superior a 50%) |
| transaction_id: | ID da transação (deve ser único) |

**Obs1:** O campo price é calculado automaticamente<br>
**Obs2:** Caso o body do POST não esteja correto é retornado um código de erro HTTP 400 (Bad Request) e um JSON com os erros cometidos<br>
**Obs3:** Para fins de teste foi implementado também um GET para a rota /payment

####Extras

- Ambiente administrativo do Django:

Para criar um usuário administrador: `python manage.py createsuperuser`.<br>
Após acessar no navegador: `http://127.0.0.1:8000/admin/`<br>
Usuário: adm<br>
Senha: adm12345

-  Interface do Django REST:

Acessar as rotas `/plans` e `/payment` por meio de um navegador

##Arquivos relevantes do projeto Django

- Segunda Etapa:
	- pages/templates/
	- pages/static/
	- pages/urls.py
	- pages/views.py

- Primeira Etapa:
  - appRest/models.py  
  - appRest/serializers.py  
  - appRest/urls.py  
  - appRest/views.py  