# Análise e Visualização de Vendas com Dashboard Web

## Funcionalidades

* Dashboard interativo de vendas por mês, vendedor e produto
* Filtragem por anos e  meses
* Gráficos dinâmicos: barras e pizza

## Tecnologias Utilizadas

**Frontend:**

* JavaScript
* React
* Axios
* Recharts
* CSS

**Backend:**

* Python
* Flask
* flask-cors
* Pandas

---

## Como rodar o Projeto localmente?

### Backend

1. Clone o repositório:

```
git clone https://github.com/Guilherme-Software/Lotus.git
```

2. Certifique-se de estar na pasta do projeto:

```
cd Lotus
```

3. Crie e ative o ambiente virtual:

* Windows:

```
python -m venv venv
venv\Scripts\activate
```

* Linux/macOS:

```
python3 -m venv venv
source venv/bin/activate
```

4. Instale as dependências:

```
pip install -r requirements.txt
```

5. Rode o backend Flask:

```
flask --app backend run
```

---

### Frontend

1. Abra um novo terminal e certifique-se de estar na pasta do projeto:

```
cd Lotus
```

2. Entre na pasta frontend:

```
cd frontend
```

3. Instale as dependências do frontend:

```
npm install
```

4. Rode o frontend:

```
npm run dev
```

---

### Acesso

* Backend: [http://127.0.0.1:5000](http://127.0.0.1:5000)
* Frontend: [http://localhost:5173](http://localhost:5173)

---

## Capturas de tela:

**1. Gráfico de barras com vendas por mês**
![Screenshot 2025-06-19 153556](https://github.com/user-attachments/assets/5bcc9a7d-273d-42cb-aa71-6a90dadc1e94)

**2. Gráfico de pizza com total por vendedor**
![Screenshot 2025-06-19 153625](https://github.com/user-attachments/assets/903c5a2d-a3d3-4257-93c3-a5e847e8a045)

**3. Quantas vezes cada produto foi vendido.**
![Screenshot 2025-06-19 153655](https://github.com/user-attachments/assets/a8295357-1cdd-45e1-bfda-6527ce23d6a7)

**4. Filtragem de vendas em 2025 nos meses de Jan, Fev e Mar.**
![Screenshot 2025-06-19 153928](https://github.com/user-attachments/assets/50288534-4cae-4685-a62b-efa32299bb8a)
