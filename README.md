# flask_simple_demo


A simple API Flask demo project








## API documentation

#### Authenticate and get valid token

```http
  POST /api/auth

  Payload:
  {
    "username": "scott",
    "password": "cat"
  }
```



#### Returns one or more providers

```http
  GET /api/providers/list/<id>
```

| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `id`      | `string` | *Optional*. Provider ID |

#### add(num1, num2)

Recebe dois números e retorna a sua soma.

