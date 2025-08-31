# Deploy AI Agent 🤖

An intelligent email management system powered by LangGraph and OpenAI that combines research capabilities with automated email operations. This AI agent can research topics, compose emails, send them, and manage your inbox through a conversational chat interface.

## 🌟 Why This Project Matters

### The Future of Intelligent Automation
This project represents a significant step toward **truly intelligent automation** that goes beyond simple rule-based systems. By combining multiple AI agents with real-world integrations, it demonstrates how AI can seamlessly handle complex, multi-step workflows that traditionally require human intervention.

### Key Impact Areas

#### 🔬 **Research & Knowledge Management**
- **Automated Information Gathering**: Transform how we collect and synthesize information by having AI agents research topics and deliver comprehensive summaries directly to your inbox
- **Time Multiplication**: What typically takes hours of manual research, reading, and summarizing can now be completed in minutes with higher consistency and thoroughness
- **Continuous Learning**: The system can monitor trends, compile reports, and keep you informed about developments in your areas of interest

#### 📧 **Intelligent Communication**
- **Context-Aware Email Management**: Move beyond simple email filters to an AI that understands intent, context, and priority
- **Personalized Automation**: The AI learns your communication patterns and can draft emails that match your tone and style
- **Proactive Communication**: Schedule reminders, follow-ups, and periodic reports without manual intervention

#### 🏗️ **Scalable AI Architecture**
- **Multi-Agent Orchestration**: Demonstrates how specialized AI agents can work together under a supervisor, paving the way for more complex autonomous systems
- **Real-World Integration**: Shows practical implementation of AI agents with existing tools (Gmail, databases, APIs) that businesses actually use
- **Extensible Framework**: The architecture can be adapted for various domains beyond email - customer service, data analysis, content creation, and more

### 🚀 Innovation Highlights

#### **LangGraph Multi-Agent System**
This project showcases the cutting-edge **LangGraph framework** for building sophisticated AI workflows. Unlike simple chatbots, this system demonstrates:
- **Specialized Agent Coordination**: Different agents with specific expertise working together
- **Dynamic Workflow Management**: The supervisor agent intelligently routes tasks based on context and requirements
- **Stateful Conversations**: Maintains context across multiple interactions and tasks

#### **Practical AI Integration**
While many AI projects remain theoretical, this system provides:
- **Production-Ready Architecture**: Dockerized, scalable, and deployable in real environments
- **Secure Implementation**: Proper authentication, environment configuration, and security practices
- **Real Business Value**: Immediate productivity gains for professionals, researchers, and businesses

### 🌍 Broader Implications

#### **Democratizing AI Capabilities**
This project makes advanced AI workflows accessible to developers and organizations without requiring deep ML expertise. The clear documentation and setup guides lower the barrier to implementing intelligent automation.

#### **Template for AI-Driven Workflows**
The architecture serves as a blueprint for building other AI-powered systems:
- **Customer Support**: AI agents handling tickets, research, and responses
- **Content Creation**: Research, writing, and distribution pipelines
- **Data Analysis**: Automated reporting and insight generation
- **Project Management**: Task coordination and progress tracking

#### **Educational Value**
For developers and AI practitioners, this project demonstrates:
- How to structure multi-agent systems
- Best practices for AI tool integration
- Production deployment considerations
- Real-world application of modern AI frameworks

### 💡 Future Potential

This system is a foundation for even more sophisticated applications:
- **Enterprise Integration**: Scale to handle multiple users, teams, and complex workflows
- **Industry-Specific Agents**: Customize for healthcare, finance, legal, or other specialized domains
- **Advanced Orchestration**: Add scheduling, conditional logic, and complex decision trees
- **Cross-Platform Integration**: Extend beyond email to Slack, Teams, CRM systems, and more

By demonstrating how AI agents can work together to handle real-world tasks, this project contributes to the broader vision of **AI as a collaborative partner** rather than just a tool, showing the path toward more autonomous and intelligent systems that enhance human productivity and decision-making.

## 🚀 Features

- **Multi-Agent Architecture**: Supervisor agent coordinates between specialized research and email agents
- **Intelligent Email Management**: Send, receive, and process emails automatically
- **Research Capabilities**: AI-powered research with email delivery of results
- **Gmail Integration**: Full IMAP/SMTP integration for Gmail accounts
- **RESTful API**: FastAPI-based backend with chat endpoints
- **Database Integration**: PostgreSQL for persistent chat history
- **Docker Ready**: Containerized application with Docker Compose support
- **Real-time Processing**: Asynchronous email processing and AI responses

## 🏗️ Architecture

The system uses a multi-agent architecture built with LangGraph:

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Supervisor    │────│  Research Agent  │────│  Email Agent    │
│     Agent       │    │                  │    │                 │
│                 │    │ - Web research   │    │ - Send emails   │
│ - Coordinates   │    │ - Content gen    │    │ - Read inbox    │
│ - Manages flow  │    │ - Data analysis  │    │ - Process msgs  │
└─────────────────┘    └──────────────────┘    └─────────────────┘
         │                       │                       │
         └───────────────────────┼───────────────────────┘
                                 │
                    ┌─────────────────────┐
                    │    FastAPI Server   │
                    │                     │
                    │ - Chat endpoints    │
                    │ - Message history   │
                    │ - Health checks     │
                    └─────────────────────┘
                                 │
                    ┌─────────────────────┐
                    │   PostgreSQL DB     │
                    │                     │
                    │ - Chat messages     │
                    │ - User sessions     │
                    └─────────────────────┘
```

## 📋 Prerequisites

- **Docker & Docker Compose** (recommended)
- **Python 3.13+** (for local development)
- **Gmail Account** with App Password enabled
- **OpenAI API Key**
- **PostgreSQL** (handled by Docker Compose)

## ⚙️ Environment Setup

Create a `.env` file in the project root:

```bash
# OpenAI Configuration
OPENAI_API_KEY=your_openai_api_key_here

# Database Configuration
DATABASE_URL=postgresql+psycopg://admin:password@localhost:5432/my_database

# Gmail/Email Configuration
EMAIL_SERVER=smtp.gmail.com
EMAIL_PORT=465
EMAIL_USERNAME=your_email@gmail.com
EMAIL_PASSWORD=your_gmail_app_password
EMAIL_FROM=your_email@gmail.com
EMAIL_TO=your_email@gmail.com

# API Configuration (optional)
API_KEY=your_api_key_here
PORT=8000
```

### 🔐 Gmail App Password Setup

1. Enable 2-Factor Authentication on your Gmail account
2. Go to Google Account settings → Security → App passwords
3. Generate a new app password for "Mail"
4. Use this 16-character password as `EMAIL_PASSWORD`

## 🐳 Quick Start with Docker (Recommended)

1. **Clone the repository**
   ```bash
   git clone https://github.com/henryantwi/docker-ai-agent-python.git
   cd docker-ai-agent-python
   ```

2. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your actual values
   ```

3. **Start the application**
   ```bash
   docker compose up --build
   ```

4. **Verify the installation**
   ```bash
   curl http://localhost:8080/health/
   ```

The application will be available at:
- **API**: http://localhost:8080
- **Database**: localhost:5432 (PostgreSQL)

## 🛠️ Local Development Setup

### 1. Install Dependencies

```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Database Setup

```bash
# Start PostgreSQL with Docker
docker run -d \
  --name postgres-dev \
  -e POSTGRES_USER=admin \
  -e POSTGRES_PASSWORD=password \
  -e POSTGRES_DB=my_database \
  -p 5432:5432 \
  postgres:17.5
```

### 3. Run the Application

```bash
cd backend/src
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

## 📚 API Usage

### Chat Endpoint

Send a message to the AI agent:

```bash
POST http://localhost:8080/api/chat/
Content-Type: application/json

{
    "message": "Research the benefits of meditation and email me the results"
}
```

### Get Recent Messages

Retrieve chat history:

```bash
GET http://localhost:8080/api/chat/recent/
```

### Example Interactions

1. **Research and Email**:
   ```json
   {
     "message": "Research why it is good to go outside and email me the results"
   }
   ```

2. **Direct Email**:
   ```json
   {
     "message": "Send me an email with the subject 'Daily Reminder' and body 'Don't forget to exercise today!'"
   }
   ```

3. **Inbox Management**:
   ```json
   {
     "message": "Check my emails from the last 24 hours and summarize them"
   }
   ```

## 🔧 Available Tools

The AI agents have access to these tools:

- **`send_me_email`**: Send emails with custom subject and body
- **`get_unread_emails`**: Retrieve unread emails from specified time period
- **`research_email`**: Perform research and generate email content

## 🚀 Deployment

### Docker Hub Deployment

1. **Build and tag the image**:
   ```bash
   docker build -f backend/Dockerfile -t your-username/docker-ai-agent-python:v1 ./backend
   ```

2. **Push to Docker Hub**:
   ```bash
   docker push your-username/docker-ai-agent-python:v1
   ```

### DigitalOcean App Platform

The project includes configuration for DigitalOcean deployment. Update the environment variables in your DigitalOcean app settings.

## 🧪 Testing

Test the API using the included `api.http` file with your favorite HTTP client or use cURL:

```bash
# Health check
curl http://localhost:8080/health/

# Send a chat message
curl -X POST http://localhost:8080/api/chat/ \
  -H "Content-Type: application/json" \
  -d '{"message": "Hello, can you help me with my emails?"}'
```

## 🛡️ Security

- Non-root user in Docker container
- Environment-based configuration
- Gmail App Password authentication
- SSL/TLS email encryption

## 📁 Project Structure

```
docker-ai-agent-python/
├── backend/
│   ├── src/
│   │   ├── api/
│   │   │   ├── ai/          # AI agents and tools
│   │   │   ├── chat/        # Chat endpoints and models
│   │   │   ├── myemailer/   # Email functionality
│   │   │   └── db.py        # Database configuration
│   │   └── main.py          # FastAPI application
│   ├── Dockerfile
│   └── requirements.txt
├── docker-compose.yml
├── api.http                 # API testing examples
├── docker-commands.md       # Docker reference
└── README.md
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Troubleshooting

### Common Issues

1. **Gmail Authentication Error**:
   - Ensure 2FA is enabled
   - Use App Password, not regular password
   - Check EMAIL_USERNAME and EMAIL_PASSWORD in .env

2. **Database Connection Error**:
   - Verify PostgreSQL is running
   - Check DATABASE_URL format
   - Ensure database exists

3. **OpenAI API Error**:
   - Verify OPENAI_API_KEY is correct
   - Check API quota and billing

### Logs

View application logs:
```bash
docker compose logs -f backend
```

### Database Access

Connect to the database:
```bash
docker exec -it <postgres_container_name> psql -U admin -d my_database
```

## 🔮 Future Enhancements

- [ ] Web frontend interface
- [ ] Multiple email provider support
- [ ] Advanced scheduling capabilities
- [ ] Email templates and automation
- [ ] Analytics and reporting
- [ ] Multi-user support

---

For more information or support, please open an issue in the repository.
