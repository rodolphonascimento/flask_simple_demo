
## API documentation

#### Authenticate and get valid token

```http
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

```http
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
