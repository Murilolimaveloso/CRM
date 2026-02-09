# 📚 Documentação da API - CRM Imobiliário

## Visão Geral

API RESTful para gerenciamento de CRM imobiliário com suporte para propriedades, leads, relatórios, IA e integrações.

**Base URL:** `http://localhost:5000/api`

**Formato:** JSON

**Autenticação:** Session-based (Flask-Login)

---

## 🔐 Autenticação

### Registrar Usuário

```http
POST /api/auth/register
```

**Body:**
```json
{
  "username": "usuario123",
  "email": "usuario@email.com",
  "password": "senha123",
  "role": "agent"
}
```

**Response:** `201 Created`
```json
{
  "message": "User created successfully",
  "user": {
    "id": 1,
    "username": "usuario123",
    "email": "usuario@email.com",
    "role": "agent",
    "created_at": "2024-01-01T00:00:00"
  }
}
```

### Login

```http
POST /api/auth/login
```

**Body:**
```json
{
  "username": "admin",
  "password": "admin123"
}
```

**Response:** `200 OK`
```json
{
  "message": "Login successful",
  "user": {
    "id": 1,
    "username": "admin",
    "email": "admin@crm.com",
    "role": "admin"
  }
}
```

### Logout

```http
POST /api/auth/logout
```

**Response:** `200 OK`

### Obter Usuário Atual

```http
GET /api/auth/me
```

**Response:** `200 OK`

---

## 🏠 Imóveis (Properties)

### Listar Imóveis

```http
GET /api/properties?page=1&per_page=10&type=apartamento&status=disponível
```

**Parâmetros de Query:**
- `page` (int): Número da página
- `per_page` (int): Itens por página
- `type` (string): Tipo do imóvel
- `status` (string): Status do imóvel
- `min_price` (float): Preço mínimo
- `max_price` (float): Preço máximo
- `city` (string): Cidade

**Response:** `200 OK`
```json
{
  "properties": [...],
  "total": 45,
  "pages": 5,
  "current_page": 1
}
```

### Obter Imóvel

```http
GET /api/properties/1
```

**Response:** `200 OK`

### Criar Imóvel

```http
POST /api/properties
```

**Body:**
```json
{
  "title": "Apartamento Luxo 3 Quartos",
  "description": "Lindo apartamento...",
  "property_type": "apartamento",
  "price": 450000,
  "area": 120,
  "bedrooms": 3,
  "bathrooms": 2,
  "parking_spaces": 2,
  "address": "Rua das Flores, 123",
  "city": "São Paulo",
  "state": "SP",
  "zip_code": "01234-567"
}
```

**Response:** `201 Created`
```json
{
  "message": "Property created successfully",
  "property": {
    "id": 1,
    "title": "Apartamento Luxo 3 Quartos",
    "ai_suggested_price": 480000,
    ...
  }
}
```

### Atualizar Imóvel

```http
PUT /api/properties/1
```

**Response:** `200 OK`

### Deletar Imóvel

```http
DELETE /api/properties/1
```

**Response:** `200 OK`

---

## 👥 Leads

### Listar Leads

```http
GET /api/leads?page=1&per_page=10&status=novo
```

**Parâmetros:**
- `page`, `per_page`: Paginação
- `status`: Status do lead (novo, contactado, interessado, negociando, convertido, perdido)
- `source`: Fonte (website, whatsapp, indicação, redes sociais)

**Response:** `200 OK`

### Criar Lead

```http
POST /api/leads
```

**Body:**
```json
{
  "name": "João Silva",
  "email": "joao@email.com",
  "phone": "(11) 98765-4321",
  "whatsapp": "5511987654321",
  "status": "novo",
  "source": "website",
  "budget": 400000,
  "property_interest": "Apartamento",
  "location_preference": "São Paulo",
  "interested_property_id": 1
}
```

**Response:** `201 Created`

### Atualizar Lead

```http
PUT /api/leads/1
```

**Response:** `200 OK`

---

## 📊 Dashboard

### Obter Estatísticas

```http
GET /api/dashboard/stats
```

**Response:**
```json
{
  "new_leads_today": 12,
  "new_properties_today": 3,
  "active_properties": 45,
  "leads_by_status": {
    "novo": 23,
    "contactado": 15,
    "interessado": 12,
    "negociando": 8
  },
  "recent_leads": [...],
  "recent_properties": [...],
  "monthly_revenue": 125000
}
```

### Tendência de Leads

```http
GET /api/dashboard/charts/leads-trend?days=30
```

### Tendência de Receita

```http
GET /api/dashboard/charts/revenue-trend?months=12
```

---

## 📈 Relatórios

### Visão Geral

```http
GET /api/reports/overview
```

**Response:**
```json
{
  "total_properties": 45,
  "total_leads": 63,
  "total_transactions": 12,
  "total_revenue": 2250000,
  "properties_by_status": {...},
  "leads_by_status": {...},
  "monthly_revenue": [...]
}
```

### Relatório de Imóveis

```http
GET /api/reports/properties
```

### Relatório de Leads

```http
GET /api/reports/leads
```

**Response:**
```json
{
  "by_source": {
    "website": 28,
    "whatsapp": 18,
    "indicação": 10
  },
  "conversion_rate": 7.9,
  "avg_response_time": 2.5
}
```

### Relatório de Vendas

```http
GET /api/reports/sales
```

---

## 🤖 IA - Inteligência Artificial

### Sugerir Preço

```http
POST /api/ai/suggest-price
```

**Body:**
```json
{
  "property_type": "apartamento",
  "area": 120,
  "bedrooms": 3,
  "bathrooms": 2,
  "parking_spaces": 2,
  "city": "São Paulo",
  "state": "SP"
}
```

**Response:**
```json
{
  "suggested_price": 480000,
  "confidence": 0.85,
  "factors": {
    "area": "Área total do imóvel",
    "location": "Localização (cidade e bairro)",
    "bedrooms": "Número de quartos",
    ...
  }
}
```

### Análise de Mercado

```http
GET /api/ai/market-analysis?city=São Paulo&type=apartamento
```

**Response:**
```json
{
  "average_price": 450000,
  "median_price": 420000,
  "min_price": 250000,
  "max_price": 1200000,
  "total_properties": 25,
  "trend": "growing",
  "price_per_m2": 3750
}
```

### Recomendações de Imóveis

```http
GET /api/ai/property-recommendations/1
```

**Response:**
```json
{
  "recommendations": [
    {
      "property": {...},
      "match_score": 0.85,
      "reason": "Dentro do orçamento, Localizado em São Paulo"
    }
  ]
}
```

---

## 🔗 Integrações

### Enviar WhatsApp

```http
POST /api/integrations/whatsapp/send
```

**Body:**
```json
{
  "to": "5511987654321",
  "message": "Olá! Temos um novo imóvel..."
}
```

**Response:**
```json
{
  "success": true,
  "message_id": "wamid.xxx",
  "demo_mode": true
}
```

### Enviar Template WhatsApp

```http
POST /api/integrations/whatsapp/send-template
```

**Body:**
```json
{
  "to": "5511987654321",
  "template_name": "new_property",
  "parameters": ["João", "Apartamento 3 quartos"]
}
```

### Criar Pagamento Pix

```http
POST /api/integrations/payment/pix/create
```

**Body:**
```json
{
  "amount": 450000,
  "description": "Entrada apartamento",
  "customer_info": {
    "name": "João Silva",
    "email": "joao@email.com"
  }
}
```

**Response:**
```json
{
  "success": true,
  "payment_id": "pix_123",
  "qr_code": "00020126580014br.gov.bcb.pix...",
  "qr_code_url": "https://...",
  "copy_paste_code": "00020126580014br.gov.bcb.pix...",
  "amount": 450000,
  "status": "pending"
}
```

### Criar Pagamento com Cartão

```http
POST /api/integrations/payment/card/create
```

**Body:**
```json
{
  "amount": 450000,
  "card_token": "tok_xxx",
  "installments": 1,
  "description": "Pagamento imóvel"
}
```

### Verificar Status do Pagamento

```http
GET /api/integrations/payment/status/pix_123
```

**Response:**
```json
{
  "payment_id": "pix_123",
  "status": "approved"
}
```

---

## 📋 Status Codes

- `200 OK` - Requisição bem-sucedida
- `201 Created` - Recurso criado com sucesso
- `400 Bad Request` - Dados inválidos
- `401 Unauthorized` - Não autenticado
- `403 Forbidden` - Sem permissão
- `404 Not Found` - Recurso não encontrado
- `500 Internal Server Error` - Erro no servidor

---

## 🔒 Autenticação

A API utiliza autenticação baseada em sessão. Após o login, o cookie de sessão é enviado automaticamente em todas as requisições.

**Headers necessários:**
```
Content-Type: application/json
```

---

## 📝 Tipos de Dados

### Property Types
- `apartamento`
- `casa`
- `terreno`
- `comercial`

### Property Status
- `disponível`
- `vendido`
- `alugado`

### Lead Status
- `novo`
- `contactado`
- `interessado`
- `negociando`
- `convertido`
- `perdido`

### Lead Sources
- `website`
- `whatsapp`
- `indicação`
- `redes sociais`

### User Roles
- `admin`
- `manager`
- `agent`

---

## 🚀 Exemplos de Uso

### Exemplo completo: Criar imóvel e sugerir preço

```javascript
// 1. Login
const loginResponse = await fetch('http://localhost:5000/api/auth/login', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    username: 'admin',
    password: 'admin123'
  }),
  credentials: 'include'
});

// 2. Criar imóvel
const propertyResponse = await fetch('http://localhost:5000/api/properties', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    title: 'Apartamento Novo',
    property_type: 'apartamento',
    price: 450000,
    area: 120,
    bedrooms: 3,
    bathrooms: 2,
    city: 'São Paulo'
  }),
  credentials: 'include'
});

const property = await propertyResponse.json();
console.log('Preço sugerido pela IA:', property.property.ai_suggested_price);
```

---

Para mais informações, consulte o README.md principal do projeto.
