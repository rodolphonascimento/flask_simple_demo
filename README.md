# flask_simple_demo


A simple API Flask demo project for maintanance Providers local database 



## How to run it

First, install python libraries used:
```bash
  pip install -r requirements.txt
```

Seconde, run the app:
```bash
  python3 app.py
```




## API documentation

#### 1) Authenticate and get valid token

```sh
  POST /api/auth
```

Payload:
```json
  {
    "username": "scott",
    "password": "cat"
  }
```
Response:
```json
{
    "access_token": <received-token>
}
```

After that, to use in HTTP header auth attributes for all request, as following:
```header
  Authentication: JWT <you token>
```


#### 2) Insert a Provider

```sh
  POST /api/providers/insert
```

Payload:
```json
{
    "id": "BRCRD0128MG2RHMZ",
    "name": "Geddy Lee",
    "company": "Rush",
    "amount_products": 2112
}
```
Response:
```sh
HTTP status code: 201 or 400
```



#### 3) Returns one or more providers

```sh
  GET /api/providers/list/<id>
```

| Param     | Type         | Description                                 |
| :---------- | :--------- | :------------------------------------------ |
| `id`      | `string` | *Optional*. Provider ID |

Response:
```sh
HTTP status code: 200, 400 or 404
```
```json
[
    {
        "amount_products": "200",
        "company": "Microsoft",
        "created_at": "Wed, 11 Jan 2023 20:49:29 GMT",
        "id": "BRCRD0028MG2ROMU",
        "name": "Bill Gates"
    },
    {
        "amount_products": "2112",
        "company": "Rush",
        "created_at": "Fri, 13 Jan 2023 15:46:34 GMT",
        "id": "BRCRD0128MG2RHMZ",
        "name": "Geddy Lee"
    } 
```

#### 4) Update one provider

```sh
  PUT /api/providers/update/<id>
```
| Param     | Type         | Description                                 |
| :---------- | :--------- | :------------------------------------------ |
| `id`      | `string` | ***Required***. Provider ID |


Payload (send only informations that you want to change):
```json
{
    "name": "Geddy Lee",
    "amount_products": 211
}
```
Response:
```sh
HTTP status code: 200, 400 or 404
```
```json
{
    "amount_products": "211",
    "company": "Rush",
    "created_at": "Fri, 13 Jan 2023 15:46:34 GMT",
    "id": "BRCRD0128MG2RHMZ",
    "name": "Geddy Lee"
}
```

#### 5) Delete one provider

```sh
  DELETE /api/providers/delete/<id>
```
| Param     | Type         | Description                                 |
| :---------- | :--------- | :------------------------------------------ |
| `id`      | `string` | ***Required***. Provider ID |

Response:
```sh
HTTP status code 200, 400 or 404
```

