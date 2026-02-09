# 🏠 CRM Imobiliário - Sistema Completo

Sistema de CRM completo para gestão imobiliária com cadastro de imóveis, leads, relatórios e IA para sugestão de preços.

## 📋 Funcionalidades

### ✅ Gerenciamento de Imóveis
- Cadastro completo de imóveis (casas, apartamentos, terrenos, comerciais)
- Filtros por tipo, preço, localização e status
- Upload de imagens e documentos
- Geolocalização com coordenadas
- Status: disponível, vendido, alugado

### 👥 Gestão de Leads
- Cadastro e acompanhamento de leads
- Múltiplas fontes: website, WhatsApp, indicação, redes sociais
- Status do funil de vendas: novo, contactado, interessado, negociando, convertido, perdido
- Atribuição de leads para agentes
- Histórico de interações

### 📊 Dashboard Inteligente
- Métricas em tempo real
- Novos leads do dia
- Imóveis ativos
- Receita do mês
- Gráficos de desempenho
- Atividades recentes

### 🤖 Inteligência Artificial
- **Sugestão de preço automatizada** baseada em:
  - Área do imóvel
  - Número de quartos e banheiros
  - Localização (cidade e bairro)
  - Tipo de imóvel
  - Vagas de garagem
  - Tendências de mercado
- Análise de mercado por região
- Recomendação de imóveis para leads

### 📈 Relatórios e Analytics
- Visão geral do negócio
- Imóveis por tipo e localização
- Leads por fonte e status
- Taxa de conversão
- Receita por período
- Análise de vendas

### 🔗 Integrações

#### WhatsApp Business
- Envio de mensagens automáticas
- Templates personalizados
- Notificações de novos imóveis
- Follow-up automatizado

#### Pagamentos
- **Pix**: Geração de QR Code e copia-e-cola
- **Cartão**: Processamento via Stripe
- Confirmação automática de pagamentos
- Webhooks para notificações

### 🔐 Sistema de Autenticação
- Login seguro com usuário e senha
- Níveis de acesso: admin, manager, agent
- Sessões persistentes
- Logout seguro

## 🚀 Tecnologias Utilizadas

### Backend
- **Python 3.8+**
- **Flask** - Framework web
- **Flask-SQLAlchemy** - ORM para banco de dados
- **Flask-Login** - Gerenciamento de autenticação
- **scikit-learn** - Machine Learning para IA
- **pandas & numpy** - Análise de dados

### Frontend
- **HTML5 / CSS3**
- **JavaScript (Vanilla)**
- Design responsivo
- Interface moderna e intuitiva

### Banco de Dados
- **SQLite** (desenvolvimento)
- Suporte para **PostgreSQL** (produção)

### Integrações
- WhatsApp Business API
- Stripe (pagamentos com cartão)
- APIs de pagamento Pix

## 📦 Instalação

### Pré-requisitos
- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)
- Navegador web moderno

### Passos para instalação

1. **Clone o repositório**
```bash
git clone https://github.com/Murilolimaveloso/CRM.git
cd CRM
```

2. **Crie e ative um ambiente virtual**
```bash
# Linux/Mac
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

3. **Instale as dependências**
```bash
pip install -r requirements.txt
```

4. **Configure as variáveis de ambiente**
```bash
cp .env.example .env
# Edite o arquivo .env com suas configurações
```

5. **Inicie o servidor**
```bash
cd backend
python app.py
```

6. **Acesse a aplicação**
```
Abra o navegador e acesse: http://localhost:5000
```

Para acessar o frontend diretamente, abra o arquivo:
```
frontend/index.html
```

## 🔧 Configuração

### Variáveis de Ambiente

Edite o arquivo `.env` com suas configurações:

```env
SECRET_KEY=sua-chave-secreta-aqui
DATABASE_URL=sqlite:///crm.db
WHATSAPP_API_KEY=sua-chave-whatsapp
WHATSAPP_PHONE_ID=seu-phone-id
PIX_API_KEY=sua-chave-pix
STRIPE_API_KEY=sua-chave-stripe
```

### Banco de Dados

O banco de dados é criado automaticamente na primeira execução. Para recriá-lo:

```bash
rm crm.db
python app.py
```

## 📱 API Endpoints

### Autenticação
- `POST /api/auth/register` - Registrar novo usuário
- `POST /api/auth/login` - Login
- `POST /api/auth/logout` - Logout
- `GET /api/auth/me` - Dados do usuário atual

### Imóveis
- `GET /api/properties` - Listar imóveis
- `GET /api/properties/:id` - Detalhes do imóvel
- `POST /api/properties` - Criar imóvel
- `PUT /api/properties/:id` - Atualizar imóvel
- `DELETE /api/properties/:id` - Deletar imóvel

### Leads
- `GET /api/leads` - Listar leads
- `GET /api/leads/:id` - Detalhes do lead
- `POST /api/leads` - Criar lead
- `PUT /api/leads/:id` - Atualizar lead
- `DELETE /api/leads/:id` - Deletar lead

### Dashboard
- `GET /api/dashboard/stats` - Estatísticas do dashboard
- `GET /api/dashboard/charts/leads-trend` - Tendência de leads
- `GET /api/dashboard/charts/revenue-trend` - Tendência de receita

### Relatórios
- `GET /api/reports/overview` - Visão geral
- `GET /api/reports/properties` - Relatório de imóveis
- `GET /api/reports/leads` - Relatório de leads
- `GET /api/reports/sales` - Relatório de vendas

### IA
- `POST /api/ai/suggest-price` - Sugerir preço
- `GET /api/ai/market-analysis` - Análise de mercado
- `GET /api/ai/property-recommendations/:lead_id` - Recomendar imóveis

### Integrações
- `POST /api/integrations/whatsapp/send` - Enviar WhatsApp
- `POST /api/integrations/whatsapp/send-template` - Enviar template
- `POST /api/integrations/payment/pix/create` - Criar pagamento Pix
- `POST /api/integrations/payment/card/create` - Criar pagamento cartão
- `GET /api/integrations/payment/status/:id` - Status do pagamento

## 👨‍💻 Modo Demonstração

O sistema funciona em **modo demonstração** sem necessidade de configurar as integrações externas. 

**Credenciais de teste:**
- Usuário: `admin`
- Senha: `admin123`

Todas as funcionalidades estão disponíveis com dados fictícios para demonstração.

## 🎨 Interface

A interface foi desenvolvida com foco em:
- **Usabilidade**: Navegação intuitiva e clara
- **Responsividade**: Funciona em desktop, tablet e mobile
- **Performance**: Carregamento rápido e operações fluidas
- **Acessibilidade**: Design acessível para todos os usuários

## 📊 Estrutura do Projeto

```
CRM/
├── backend/
│   ├── app.py                 # Aplicação principal
│   ├── models/                # Modelos de dados
│   │   ├── user.py
│   │   ├── property.py
│   │   ├── lead.py
│   │   └── transaction.py
│   ├── routes/                # Rotas da API
│   │   ├── auth.py
│   │   ├── properties.py
│   │   ├── leads.py
│   │   ├── reports.py
│   │   ├── ai_price.py
│   │   ├── dashboard.py
│   │   └── integrations.py
│   └── services/              # Serviços
│       ├── ai_service.py
│       ├── whatsapp_service.py
│       └── payment_service.py
├── frontend/
│   ├── index.html             # Interface principal
│   ├── styles.css             # Estilos
│   └── app.js                 # Lógica do frontend
├── requirements.txt           # Dependências Python
├── .env.example              # Exemplo de configuração
├── .gitignore                # Arquivos ignorados
└── README.md                 # Este arquivo
```

## 🔒 Segurança

- Senhas criptografadas com hash seguro
- Proteção contra CSRF
- Validação de entrada de dados
- Sessões seguras
- CORS configurável

## 🚀 Deploy em Produção

### Heroku
```bash
heroku create seu-app-crm
git push heroku main
```

### Docker
```bash
docker build -t crm-imobiliario .
docker run -p 5000:5000 crm-imobiliario
```

### VPS/Cloud
1. Configure um servidor com Python 3.8+
2. Instale as dependências
3. Configure nginx como proxy reverso
4. Use gunicorn como servidor WSGI
5. Configure SSL com Let's Encrypt

## 📝 Roadmap Futuro

- [ ] App mobile nativo (React Native)
- [ ] Sistema de agendamento de visitas
- [ ] Assinatura de contratos digital
- [ ] Chat interno entre agentes
- [ ] Integração com portais imobiliários
- [ ] Sistema de avaliação de imóveis
- [ ] Tour virtual 360°
- [ ] Reconhecimento de imagens com IA
- [ ] Chatbot com IA para atendimento

## 🤝 Contribuindo

Contribuições são bem-vindas! Por favor:

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/MinhaFeature`)
3. Commit suas mudanças (`git commit -m 'Adiciona MinhaFeature'`)
4. Push para a branch (`git push origin feature/MinhaFeature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

## 👤 Autor

**Murilo Lima Veloso**

## 📞 Suporte

Para suporte, abra uma issue no GitHub ou entre em contato.

---

**Desenvolvido com ❤️ para revolucionar a gestão imobiliária** 
