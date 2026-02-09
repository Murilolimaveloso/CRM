// API Configuration
const API_URL = 'http://localhost:5000/api';

// Simple state management
const state = {
    user: null,
    properties: [],
    leads: [],
    currentView: 'dashboard'
};

// Initialize app
document.addEventListener('DOMContentLoaded', () => {
    // Check if user is logged in
    const savedUser = localStorage.getItem('user');
    if (savedUser) {
        state.user = JSON.parse(savedUser);
        showDashboard();
    } else {
        showLogin();
    }
    
    // Setup event listeners
    setupEventListeners();
});

function setupEventListeners() {
    // Login form
    const loginForm = document.getElementById('login-form');
    if (loginForm) {
        loginForm.addEventListener('submit', handleLogin);
    }
    
    // Logout button
    const logoutBtn = document.getElementById('logout-btn');
    if (logoutBtn) {
        logoutBtn.addEventListener('click', handleLogout);
    }
    
    // Navigation
    document.querySelectorAll('.sidebar a[data-view]').forEach(link => {
        link.addEventListener('click', (e) => {
            e.preventDefault();
            const view = e.target.getAttribute('data-view');
            switchView(view);
        });
    });
    
    // AI Price Form
    const aiPriceForm = document.getElementById('ai-price-form');
    if (aiPriceForm) {
        aiPriceForm.addEventListener('submit', handleAIPriceCalculation);
    }
    
    // WhatsApp Form
    const whatsappForm = document.getElementById('whatsapp-form');
    if (whatsappForm) {
        whatsappForm.addEventListener('submit', handleWhatsAppSend);
    }
}

// Authentication
async function handleLogin(e) {
    e.preventDefault();
    
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    
    // Demo mode - accept any credentials for demonstration
    // In production, this would call the actual API
    if (username && password) {
        const demoUser = {
            id: 1,
            username: username,
            email: `${username}@example.com`,
            role: 'admin'
        };
        
        state.user = demoUser;
        localStorage.setItem('user', JSON.stringify(demoUser));
        showDashboard();
    }
}

function handleLogout() {
    state.user = null;
    localStorage.removeItem('user');
    showLogin();
}

function showLogin() {
    document.getElementById('login-screen').style.display = 'block';
    document.getElementById('dashboard-screen').style.display = 'none';
}

function showDashboard() {
    document.getElementById('login-screen').style.display = 'none';
    document.getElementById('dashboard-screen').style.display = 'flex';
    
    if (state.user) {
        document.getElementById('user-name').textContent = state.user.username;
    }
    
    // Load initial view
    switchView('dashboard');
}

// View Management
function switchView(viewName) {
    // Hide all views
    document.querySelectorAll('.view').forEach(view => {
        view.style.display = 'none';
    });
    
    // Show selected view
    const selectedView = document.getElementById(`view-${viewName}`);
    if (selectedView) {
        selectedView.style.display = 'block';
    }
    
    // Update active menu item
    document.querySelectorAll('.sidebar a').forEach(link => {
        link.classList.remove('active');
    });
    const activeLink = document.querySelector(`.sidebar a[data-view="${viewName}"]`);
    if (activeLink) {
        activeLink.classList.add('active');
    }
    
    // Update page title
    const titles = {
        'dashboard': 'Dashboard',
        'properties': 'Imóveis',
        'leads': 'Leads',
        'reports': 'Relatórios',
        'ai': 'IA - Sugestão de Preço',
        'integrations': 'Integrações'
    };
    document.getElementById('page-title').textContent = titles[viewName] || viewName;
    
    state.currentView = viewName;
    
    // Load view data
    loadViewData(viewName);
}

function loadViewData(viewName) {
    switch(viewName) {
        case 'dashboard':
            loadDashboardData();
            break;
        case 'properties':
            loadProperties();
            break;
        case 'leads':
            loadLeads();
            break;
        case 'reports':
            loadReports();
            break;
    }
}

// Dashboard Data
function loadDashboardData() {
    // Demo data
    document.getElementById('stat-properties').textContent = '45';
    document.getElementById('stat-leads-today').textContent = '12';
    document.getElementById('stat-revenue').textContent = 'R$ 125.000';
    document.getElementById('stat-leads-negotiating').textContent = '8';
    
    // Leads by status chart (simple text display)
    const leadsStatusChart = document.getElementById('leads-status-chart');
    leadsStatusChart.innerHTML = `
        <div class="report-item">
            <span>Novos</span>
            <strong>23</strong>
        </div>
        <div class="report-item">
            <span>Contactados</span>
            <strong>15</strong>
        </div>
        <div class="report-item">
            <span>Interessados</span>
            <strong>12</strong>
        </div>
        <div class="report-item">
            <span>Em Negociação</span>
            <strong>8</strong>
        </div>
        <div class="report-item">
            <span>Convertidos</span>
            <strong>5</strong>
        </div>
    `;
    
    // Recent activity
    const recentActivity = document.getElementById('recent-activity');
    recentActivity.innerHTML = `
        <div class="activity-item">
            <strong>Novo lead cadastrado</strong><br>
            <small>João Silva - Interessado em apartamento - Há 5 minutos</small>
        </div>
        <div class="activity-item">
            <strong>Imóvel adicionado</strong><br>
            <small>Apartamento 3 quartos - Centro - Há 1 hora</small>
        </div>
        <div class="activity-item">
            <strong>Lead convertido</strong><br>
            <small>Maria Santos - Venda finalizada - Há 2 horas</small>
        </div>
        <div class="activity-item">
            <strong>WhatsApp enviado</strong><br>
            <small>Mensagem automática para 5 leads - Há 3 horas</small>
        </div>
    `;
}

// Properties
function loadProperties() {
    const propertiesList = document.getElementById('properties-list');
    
    // Demo properties
    const demoProperties = [
        { id: 1, title: 'Apartamento Luxo 3 Quartos', type: 'Apartamento', price: 450000, city: 'São Paulo', status: 'Disponível' },
        { id: 2, title: 'Casa Condomínio Fechado', type: 'Casa', price: 650000, city: 'São Paulo', status: 'Disponível' },
        { id: 3, title: 'Cobertura Vista Mar', type: 'Apartamento', price: 1200000, city: 'Rio de Janeiro', status: 'Disponível' },
        { id: 4, title: 'Loja Comercial Centro', type: 'Comercial', price: 350000, city: 'Belo Horizonte', status: 'Vendido' },
        { id: 5, title: 'Terreno 500m²', type: 'Terreno', price: 200000, city: 'Curitiba', status: 'Disponível' }
    ];
    
    propertiesList.innerHTML = demoProperties.map(prop => `
        <div class="data-item">
            <div><strong>${prop.title}</strong></div>
            <div>${prop.type}</div>
            <div>R$ ${prop.price.toLocaleString('pt-BR')}</div>
            <div>${prop.city}</div>
            <div><span class="badge">${prop.status}</span></div>
        </div>
    `).join('');
}

// Leads
function loadLeads() {
    const leadsList = document.getElementById('leads-list');
    
    // Demo leads
    const demoLeads = [
        { id: 1, name: 'João Silva', phone: '(11) 98765-4321', status: 'Novo', source: 'Website', budget: 400000 },
        { id: 2, name: 'Maria Santos', phone: '(11) 97654-3210', status: 'Contactado', source: 'WhatsApp', budget: 600000 },
        { id: 3, name: 'Pedro Oliveira', phone: '(11) 96543-2109', status: 'Interessado', source: 'Indicação', budget: 350000 },
        { id: 4, name: 'Ana Costa', phone: '(11) 95432-1098', status: 'Negociando', source: 'Redes Sociais', budget: 800000 },
        { id: 5, name: 'Carlos Pereira', phone: '(11) 94321-0987', status: 'Convertido', source: 'Website', budget: 450000 }
    ];
    
    leadsList.innerHTML = demoLeads.map(lead => `
        <div class="data-item">
            <div><strong>${lead.name}</strong></div>
            <div>${lead.phone}</div>
            <div>${lead.status}</div>
            <div>${lead.source}</div>
            <div>R$ ${lead.budget.toLocaleString('pt-BR')}</div>
        </div>
    `).join('');
}

// Reports
function loadReports() {
    // Overview
    const reportOverview = document.getElementById('report-overview');
    reportOverview.innerHTML = `
        <div class="report-item">
            <span>Total de Imóveis</span>
            <strong>45</strong>
        </div>
        <div class="report-item">
            <span>Total de Leads</span>
            <strong>63</strong>
        </div>
        <div class="report-item">
            <span>Vendas no Mês</span>
            <strong>5</strong>
        </div>
        <div class="report-item">
            <span>Receita Total</span>
            <strong>R$ 2.250.000</strong>
        </div>
    `;
    
    // Properties by type
    const reportProperties = document.getElementById('report-properties');
    reportProperties.innerHTML = `
        <div class="report-item">
            <span>Apartamentos</span>
            <strong>25</strong>
        </div>
        <div class="report-item">
            <span>Casas</span>
            <strong>12</strong>
        </div>
        <div class="report-item">
            <span>Terrenos</span>
            <strong>5</strong>
        </div>
        <div class="report-item">
            <span>Comercial</span>
            <strong>3</strong>
        </div>
    `;
    
    // Leads by source
    const reportLeads = document.getElementById('report-leads');
    reportLeads.innerHTML = `
        <div class="report-item">
            <span>Website</span>
            <strong>28</strong>
        </div>
        <div class="report-item">
            <span>WhatsApp</span>
            <strong>18</strong>
        </div>
        <div class="report-item">
            <span>Indicação</span>
            <strong>10</strong>
        </div>
        <div class="report-item">
            <span>Redes Sociais</span>
            <strong>7</strong>
        </div>
    `;
    
    // Sales
    const reportSales = document.getElementById('report-sales');
    reportSales.innerHTML = `
        <div class="report-item">
            <span>Vendas por Pix</span>
            <strong>2</strong>
        </div>
        <div class="report-item">
            <span>Vendas por Cartão</span>
            <strong>3</strong>
        </div>
        <div class="report-item">
            <span>Taxa de Conversão</span>
            <strong>7.9%</strong>
        </div>
        <div class="report-item">
            <span>Ticket Médio</span>
            <strong>R$ 450.000</strong>
        </div>
    `;
}

// AI Price Calculation
async function handleAIPriceCalculation(e) {
    e.preventDefault();
    
    const propertyType = document.getElementById('ai-property-type').value;
    const area = parseFloat(document.getElementById('ai-area').value);
    const bedrooms = parseInt(document.getElementById('ai-bedrooms').value);
    const bathrooms = parseInt(document.getElementById('ai-bathrooms').value);
    const parking = parseInt(document.getElementById('ai-parking').value);
    const city = document.getElementById('ai-city').value;
    
    // Simple price calculation algorithm
    const basePrice = {
        'apartamento': 4000,
        'casa': 3000,
        'terreno': 1500,
        'comercial': 5000
    };
    
    const cityMultiplier = {
        'São Paulo': 1.5,
        'Rio de Janeiro': 1.4,
        'Brasília': 1.3,
        'Belo Horizonte': 1.2,
        'Curitiba': 1.15,
        'Porto Alegre': 1.15
    };
    
    let price = area * (basePrice[propertyType] || 3500);
    price *= (1 + (bedrooms - 2) * 0.1);
    price *= (1 + (bathrooms - 1) * 0.05);
    price *= (1 + parking * 0.08);
    price *= (cityMultiplier[city] || 1.0);
    
    // Display result
    document.getElementById('ai-suggested-price').textContent = 
        `R$ ${Math.round(price).toLocaleString('pt-BR')}`;
    document.getElementById('ai-confidence').textContent = '85%';
    document.getElementById('ai-result').style.display = 'block';
}

// WhatsApp Integration
async function handleWhatsAppSend(e) {
    e.preventDefault();
    
    const number = document.getElementById('whatsapp-number').value;
    const message = document.getElementById('whatsapp-message').value;
    
    // Demo mode - just show success
    alert(`WhatsApp enviado para ${number}\n\nMensagem: ${message}\n\n(Modo demonstração)`);
    
    // Clear form
    document.getElementById('whatsapp-form').reset();
}

// Utility functions
function formatCurrency(value) {
    return new Intl.NumberFormat('pt-BR', {
        style: 'currency',
        currency: 'BRL'
    }).format(value);
}

function formatDate(date) {
    return new Date(date).toLocaleDateString('pt-BR');
}
