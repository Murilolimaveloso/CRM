# 📋 Referência Rápida - CRM Imobiliário

## Comandos Essenciais

### Iniciar o Sistema
```bash
# Linux/Mac
./start.sh

# Windows
start.bat

# Manual
source venv/bin/activate
python backend/app.py
```

### Reiniciar Banco de Dados
```bash
rm crm.db
python init_db.py
```

## Credenciais Padrão

| Usuário | Senha | Perfil |
|---------|-------|--------|
| admin | admin123 | Administrador |
| joao | senha123 | Agente |
| maria | senha123 | Agente |

## Endpoints Principais

### Autenticação
- `POST /api/auth/login` - Login
- `POST /api/auth/logout` - Logout
- `GET /api/auth/me` - Usuário atual

### Imóveis
- `GET /api/properties` - Listar
- `POST /api/properties` - Criar
- `PUT /api/properties/:id` - Atualizar
- `DELETE /api/properties/:id` - Deletar

### Leads
- `GET /api/leads` - Listar
- `POST /api/leads` - Criar
- `PUT /api/leads/:id` - Atualizar
- `DELETE /api/leads/:id` - Deletar

### IA
- `POST /api/ai/suggest-price` - Sugerir preço
- `GET /api/ai/market-analysis` - Análise de mercado
- `GET /api/ai/property-recommendations/:lead_id` - Recomendações

### Dashboard
- `GET /api/dashboard/stats` - Estatísticas
- `GET /api/dashboard/charts/leads-trend` - Tendência de leads
- `GET /api/dashboard/charts/revenue-trend` - Tendência de receita

### Relatórios
- `GET /api/reports/overview` - Visão geral
- `GET /api/reports/properties` - Relatório de imóveis
- `GET /api/reports/leads` - Relatório de leads
- `GET /api/reports/sales` - Relatório de vendas

### Integrações
- `POST /api/integrations/whatsapp/send` - WhatsApp
- `POST /api/integrations/payment/pix/create` - Pix
- `POST /api/integrations/payment/card/create` - Cartão

## Tipos e Status

### Tipos de Imóvel
- `apartamento`
- `casa`
- `terreno`
- `comercial`

### Status do Imóvel
- `disponível`
- `vendido`
- `alugado`

### Status do Lead
- `novo`
- `contactado`
- `interessado`
- `negociando`
- `convertido`
- `perdido`

### Fontes de Lead
- `website`
- `whatsapp`
- `indicação`
- `redes sociais`

### Perfis de Usuário
- `admin` - Acesso total
- `manager` - Gerenciamento
- `agent` - Agente de vendas

## Estrutura de Dados

### Criar Imóvel (JSON)
```json
{
  "title": "Apartamento 3 Quartos",
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

### Criar Lead (JSON)
```json
{
  "name": "João Silva",
  "email": "joao@email.com",
  "phone": "(11) 98765-4321",
  "whatsapp": "5511987654321",
  "budget": 400000,
  "property_interest": "Apartamento",
  "location_preference": "São Paulo",
  "source": "website"
}
```

### Sugerir Preço (JSON)
```json
{
  "property_type": "apartamento",
  "area": 120,
  "bedrooms": 3,
  "bathrooms": 2,
  "parking_spaces": 2,
  "city": "São Paulo"
}
```

## Variáveis de Ambiente

```env
# Aplicação
SECRET_KEY=sua-chave-secreta
DATABASE_URL=sqlite:///crm.db

# WhatsApp
WHATSAPP_API_KEY=seu-token
WHATSAPP_PHONE_ID=seu-phone-id

# Pagamentos
PIX_API_KEY=sua-chave-pix
STRIPE_API_KEY=sk_test_sua_chave_stripe
```

## Portas Padrão

- Backend API: `http://localhost:5000`
- Frontend: Abrir `frontend/index.html`

## Atalhos do Sistema

### Dashboard
- Ver estatísticas em tempo real
- Monitorar novos leads
- Acompanhar receita

### Imóveis
- Cadastrar propriedades
- Filtrar por tipo/preço/cidade
- Ver preço sugerido pela IA

### Leads
- Gerenciar pipeline de vendas
- Atribuir para agentes
- Acompanhar status

### IA
- Calcular preço ideal
- Analisar mercado
- Recomendar imóveis

### Relatórios
- Análise completa do negócio
- Métricas de conversão
- Desempenho de vendas

### Integrações
- Enviar WhatsApp automático
- Processar pagamentos
- Gerar Pix

## Comandos de Debug

### Verificar Instalação
```bash
python --version
pip --version
```

### Testar Dependências
```bash
pip list
```

### Ver Logs
```bash
# No modo debug, veja logs no terminal
python backend/app.py
```

### Testar API
```bash
# Verificar saúde
curl http://localhost:5000/api/auth/me

# Login (exemplo)
curl -X POST http://localhost:5000/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{"username":"admin","password":"admin123"}'
```

## Solução Rápida de Problemas

| Problema | Solução |
|----------|---------|
| Porta ocupada | Mude para porta 8000 |
| Módulo não encontrado | `pip install -r requirements.txt` |
| Banco bloqueado | `rm crm.db && python init_db.py` |
| Sem permissão | `chmod +x start.sh` |
| API não responde | Verifique se backend está rodando |

## Recursos Úteis

- 📖 README completo: `README.md`
- 🔌 Documentação API: `API_DOCUMENTATION.md`
- 📚 Guia de instalação: `INSTALLATION_GUIDE.md`
- 🐛 Reportar bugs: GitHub Issues

## Exemplos de Uso

### Exemplo 1: Cadastrar imóvel e calcular preço
```python
# Via API
import requests

# Login
session = requests.Session()
session.post('http://localhost:5000/api/auth/login', 
    json={'username': 'admin', 'password': 'admin123'})

# Criar imóvel (IA calculará preço automaticamente)
response = session.post('http://localhost:5000/api/properties',
    json={
        'title': 'Apartamento Novo',
        'property_type': 'apartamento',
        'area': 100,
        'bedrooms': 2,
        'bathrooms': 1,
        'city': 'São Paulo',
        'price': 350000
    })

print(response.json())
# Verá ai_suggested_price calculado pela IA
```

### Exemplo 2: Listar leads e filtrar
```python
# Listar todos os leads
response = session.get('http://localhost:5000/api/leads')
leads = response.json()

# Filtrar leads novos
response = session.get('http://localhost:5000/api/leads?status=novo')
new_leads = response.json()
```

### Exemplo 3: Enviar WhatsApp
```python
# Enviar mensagem
response = session.post('http://localhost:5000/api/integrations/whatsapp/send',
    json={
        'to': '+5511987654321',
        'message': 'Olá! Temos um novo imóvel para você!'
    })
```

## Dicas de Produção

✅ **Sempre:**
- Use HTTPS em produção
- Configure SECRET_KEY forte
- Use PostgreSQL ao invés de SQLite
- Ative logs apropriados
- Faça backup do banco regularmente
- Configure as integrações reais

❌ **Nunca:**
- Comite o arquivo .env
- Use credenciais padrão
- Execute em modo debug em produção
- Exponha a API sem autenticação

---

**Para mais detalhes, consulte a documentação completa.**
