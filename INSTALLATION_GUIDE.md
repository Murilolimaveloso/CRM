# 🚀 Guia de Instalação e Uso - CRM Imobiliário

## Índice
1. [Instalação Rápida](#instalação-rápida)
2. [Instalação Detalhada](#instalação-detalhada)
3. [Primeiros Passos](#primeiros-passos)
4. [Usando o Sistema](#usando-o-sistema)
5. [Configuração das Integrações](#configuração-das-integrações)
6. [Solução de Problemas](#solução-de-problemas)

---

## Instalação Rápida

### Linux/Mac

```bash
# 1. Clone o repositório
git clone https://github.com/Murilolimaveloso/CRM.git
cd CRM

# 2. Execute o script de inicialização
chmod +x start.sh
./start.sh
```

### Windows

```batch
# 1. Clone o repositório
git clone https://github.com/Murilolimaveloso/CRM.git
cd CRM

# 2. Execute o script de inicialização
start.bat
```

O servidor estará disponível em: `http://localhost:5000`

---

## Instalação Detalhada

### Pré-requisitos

- **Python 3.8 ou superior**
  - Verifique: `python3 --version`
  - Download: https://www.python.org/downloads/

- **pip** (gerenciador de pacotes Python)
  - Geralmente instalado com Python
  - Verifique: `pip --version`

- **Git**
  - Verifique: `git --version`
  - Download: https://git-scm.com/downloads

### Passo a Passo

#### 1. Clone o Repositório

```bash
git clone https://github.com/Murilolimaveloso/CRM.git
cd CRM
```

#### 2. Crie um Ambiente Virtual

**Linux/Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows:**
```batch
python -m venv venv
venv\Scripts\activate
```

Você saberá que está ativado quando ver `(venv)` no início da linha de comando.

#### 3. Instale as Dependências

```bash
pip install -r requirements.txt
```

Isso instalará:
- Flask (framework web)
- Flask-SQLAlchemy (banco de dados)
- Flask-Login (autenticação)
- scikit-learn (IA)
- pandas, numpy (análise de dados)
- E outras bibliotecas necessárias

#### 4. Configure as Variáveis de Ambiente

```bash
# Copie o arquivo de exemplo
cp .env.example .env

# Edite o arquivo .env com suas configurações
nano .env  # ou use seu editor preferido
```

**Configuração mínima para demo:**
```env
SECRET_KEY=minha-chave-secreta-super-segura
DATABASE_URL=sqlite:///crm.db
```

#### 5. Inicialize o Banco de Dados

```bash
python init_db.py
```

Isso criará:
- Tabelas do banco de dados
- Usuário admin (admin/admin123)
- Usuários agentes de teste
- Dados de exemplo (imóveis e leads)

#### 6. Inicie o Servidor

```bash
cd backend
python app.py
```

Você verá:
```
 * Running on http://127.0.0.1:5000
 * Running on http://0.0.0.0:5000
```

#### 7. Acesse a Aplicação

Abra seu navegador e acesse:
```
http://localhost:5000
```

Ou abra diretamente o frontend:
```
Abrir: frontend/index.html
```

---

## Primeiros Passos

### 1. Fazer Login

**Credenciais de Demo:**
- **Usuário:** admin
- **Senha:** admin123

**Outros usuários de teste:**
- joao / senha123 (agente)
- maria / senha123 (agente)

### 2. Explorar o Dashboard

Após o login, você verá:
- 📊 **Estatísticas** em tempo real
- 📈 **Gráficos** de desempenho
- 📝 **Atividades** recentes
- 💰 **Receita** do mês

### 3. Navegar pelo Sistema

Use o menu lateral para acessar:
- **Dashboard** - Visão geral
- **Imóveis** - Gerenciar propriedades
- **Leads** - Gerenciar clientes potenciais
- **Relatórios** - Análises e métricas
- **IA** - Sugestão de preços
- **Integrações** - WhatsApp e Pagamentos

---

## Usando o Sistema

### Gerenciar Imóveis

#### Adicionar um Novo Imóvel

1. Clique em **"Imóveis"** no menu
2. Clique em **"+ Adicionar Imóvel"**
3. Preencha os dados:
   - Título
   - Tipo (Apartamento, Casa, Terreno, Comercial)
   - Preço
   - Área (m²)
   - Quartos, Banheiros, Vagas
   - Endereço completo
4. A **IA calculará automaticamente** o preço sugerido
5. Salve o imóvel

#### Filtrar Imóveis

Use os filtros disponíveis:
- Por tipo
- Por faixa de preço
- Por cidade
- Por status

### Gerenciar Leads

#### Adicionar um Novo Lead

1. Clique em **"Leads"** no menu
2. Clique em **"+ Adicionar Lead"**
3. Preencha:
   - Nome
   - Email e Telefone
   - WhatsApp
   - Orçamento
   - Preferências
   - Fonte (Website, WhatsApp, Indicação, etc.)
4. Atribua a um agente
5. Salve o lead

#### Acompanhar Status do Lead

Status disponíveis:
- 🆕 **Novo** - Lead acabou de entrar
- 📞 **Contactado** - Já fizemos contato
- 💡 **Interessado** - Demonstrou interesse
- 🤝 **Negociando** - Em processo de negociação
- ✅ **Convertido** - Venda concluída
- ❌ **Perdido** - Não deu certo

### Usar a IA para Sugerir Preços

#### Calcular Preço de um Imóvel

1. Vá em **"IA - Sugestão de Preço"**
2. Preencha os dados do imóvel:
   - Tipo
   - Área
   - Quartos
   - Banheiros
   - Vagas
   - Cidade
3. Clique em **"Calcular Preço Sugerido"**
4. A IA mostrará:
   - Preço sugerido
   - Nível de confiança
   - Fatores considerados

#### Como funciona a IA

A IA considera:
- **Área total** - Maior área = maior preço
- **Localização** - Cidades grandes têm multiplicador maior
- **Tipo de imóvel** - Comercial > Apartamento > Casa > Terreno
- **Comodidades** - Quartos, banheiros, vagas aumentam o valor
- **Mercado** - Tendências atuais da região

### Enviar Mensagens WhatsApp

1. Vá em **"Integrações"**
2. Na seção **WhatsApp Business**:
   - Digite o número (com +55)
   - Escreva a mensagem
   - Clique em **"Enviar WhatsApp"**

**Exemplo de número:** `+5511987654321`

**Modo Demo:** No modo demonstração, as mensagens não são enviadas de verdade, apenas simuladas.

### Processar Pagamentos

#### Gerar Pix

1. Clique em **"Gerar Pix"**
2. O sistema gerará:
   - QR Code
   - Código copia-e-cola
   - ID de pagamento

#### Processar Cartão

1. Clique em **"Processar Cartão"**
2. Informe os dados do cartão
3. Escolha número de parcelas
4. Confirme o pagamento

---

## Configuração das Integrações

### WhatsApp Business API

Para usar WhatsApp em produção:

1. **Obtenha as credenciais:**
   - Acesse: https://developers.facebook.com/
   - Crie um app Business
   - Obtenha o Phone Number ID e Access Token

2. **Configure no .env:**
   ```env
   WHATSAPP_API_KEY=seu-token-de-acesso
   WHATSAPP_PHONE_ID=seu-phone-number-id
   ```

3. **Teste a integração:**
   ```bash
   python -c "from backend.services.whatsapp_service import WhatsAppService; ws = WhatsAppService(); print(ws.send_message('+5511999999999', 'Teste'))"
   ```

### Integração Pix

Para usar Pix em produção:

1. **Escolha um provedor:**
   - Mercado Pago
   - PagSeguro
   - Gerencianet
   - Asaas

2. **Configure no .env:**
   ```env
   PIX_API_KEY=sua-chave-api
   PIX_API_URL=https://api.provedor.com
   ```

3. **Adapte o código:**
   - Edite `backend/services/payment_service.py`
   - Implemente a API do seu provedor

### Integração Stripe (Cartão)

1. **Crie uma conta:**
   - Acesse: https://stripe.com/
   - Crie uma conta

2. **Obtenha as chaves:**
   - Dashboard > Developers > API Keys
   - Copie a Secret Key

3. **Configure no .env:**
   ```env
   STRIPE_API_KEY=sk_test_sua_chave_secreta
   ```

4. **Instale o SDK:**
   ```bash
   pip install stripe
   ```

---

## Solução de Problemas

### Erro: "ModuleNotFoundError"

**Problema:** Python não encontra um módulo.

**Solução:**
```bash
# Certifique-se de que o ambiente virtual está ativado
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate  # Windows

# Reinstale as dependências
pip install -r requirements.txt
```

### Erro: "Port already in use"

**Problema:** A porta 5000 já está sendo usada.

**Solução 1:** Pare o processo que está usando a porta:
```bash
# Linux/Mac
lsof -ti:5000 | xargs kill -9

# Windows
netstat -ano | findstr :5000
taskkill /PID <PID> /F
```

**Solução 2:** Use outra porta:
```bash
# No arquivo backend/app.py, altere a porta
app.run(debug=True, host='0.0.0.0', port=8000)
```

### Erro: "Database locked"

**Problema:** O banco SQLite está bloqueado.

**Solução:**
```bash
# Pare o servidor
Ctrl+C

# Delete o banco e recrie
rm crm.db
python init_db.py

# Reinicie o servidor
python backend/app.py
```

### Frontend não carrega os dados

**Problema:** API não está respondendo.

**Solução:**
1. Verifique se o backend está rodando:
   ```bash
   curl http://localhost:5000/api/auth/me
   ```

2. Verifique o console do navegador (F12) para erros

3. Verifique se a URL da API está correta em `frontend/app.js`:
   ```javascript
   const API_URL = 'http://localhost:5000/api';
   ```

### "Permission Denied" no Linux/Mac

**Problema:** Sem permissão para executar scripts.

**Solução:**
```bash
chmod +x start.sh
chmod +x init_db.py
```

### Dependências não instalam

**Problema:** Erro ao instalar scikit-learn ou numpy.

**Solução:**
```bash
# Atualize pip
pip install --upgrade pip setuptools wheel

# Instale dependências do sistema (Ubuntu/Debian)
sudo apt-get install python3-dev build-essential

# Tente novamente
pip install -r requirements.txt
```

---

## Usando com Docker

### Construir a Imagem

```bash
docker build -t crm-imobiliario .
```

### Executar o Container

```bash
docker run -p 5000:5000 crm-imobiliario
```

### Usar Docker Compose

```bash
docker-compose up
```

---

## Atualizações e Manutenção

### Atualizar o Sistema

```bash
# Puxe as últimas alterações
git pull origin main

# Reinstale dependências
pip install -r requirements.txt

# Atualize o banco de dados (se necessário)
python init_db.py
```

### Backup do Banco de Dados

```bash
# SQLite
cp crm.db crm.db.backup

# PostgreSQL
pg_dump dbname > backup.sql
```

### Logs e Debug

Para ver logs detalhados:
```bash
# No backend/app.py, ative o modo debug
app.run(debug=True)
```

---

## Próximos Passos

Após dominar o básico:

1. ✅ **Personalize** o sistema para seu negócio
2. ✅ **Configure** as integrações reais
3. ✅ **Importe** seus dados existentes
4. ✅ **Treine** sua equipe
5. ✅ **Deploy** em produção
6. ✅ **Monitore** o desempenho
7. ✅ **Ajuste** a IA com dados reais

---

## Suporte

- 📖 **Documentação:** README.md
- 🔌 **API:** API_DOCUMENTATION.md
- 💬 **Issues:** https://github.com/Murilolimaveloso/CRM/issues

---

**Bom uso do seu CRM Imobiliário! 🏠✨**
