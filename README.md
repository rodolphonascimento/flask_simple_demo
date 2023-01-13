
## API documentation

#### Authenticate and get valid token

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



#### Insert a Provider

```sh
  POST /api/providers/insert
```

Payload:
```json
{
    "id": "BRCRD0028MG2RHMZ",
    "name": "Alice Chains",
    "company": "Apple",
    "amount_products": 150
}
```
