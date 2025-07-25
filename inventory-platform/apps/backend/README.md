# Inventory Management Backend

A FastAPI-based REST API for inventory management with PostgreSQL database integration, JWT authentication, and comprehensive resource management capabilities.

## Features

- 🔐 **JWT Authentication** - Secure user registration, login, and session management
- 📦 **Resource Management** - Full CRUD operations for inventory items
- 🔍 **Advanced Filtering** - Search, sort, and filter resources by multiple criteria
- 📊 **Auto Status Management** - Automatic status updates based on quantity levels
- 🚀 **FastAPI Framework** - Modern, fast, and auto-documented API
- 🐘 **PostgreSQL Integration** - Robust relational database with SQLAlchemy ORM
- 🔄 **Database Migrations** - Alembic-powered schema versioning
- 🐳 **Docker Ready** - Containerized development and deployment
- 📚 **Auto-Generated Documentation** - Swagger UI and ReDoc integration

## API Endpoints Overview

### Authentication
- `POST /api/v1/auth/register` - User registration
- `POST /api/v1/auth/login` - User login (returns JWT token)

### User Management
- `GET /api/v1/users/me` - Get current user profile

### Resource Management
- `POST /api/v1/resources/` - Create new resource
- `GET /api/v1/resources/` - List resources with filtering/sorting
- `GET /api/v1/resources/{id}` - Get specific resource
- `PUT /api/v1/resources/{id}` - Update resource
- `DELETE /api/v1/resources/{id}` - Delete resource
- `GET /api/v1/resources/categories/list` - Get available categories

## Quick Start

### Prerequisites
- Docker and Docker Compose
- Python 3.11+ (for local development)
- PostgreSQL (if running without Docker)

### 1. Project Setup
```bash
# From the root directory
./setup.sh
```

### 2. Start Development Environment
```bash
# Start all services (database + API)
./start-dev.sh
```

### 3. Access the API
- **API Base URL**: http://localhost:8000
- **Interactive Documentation**: http://localhost:8000/docs
- **Alternative Documentation**: http://localhost:8000/redoc
- **Database Admin**: http://localhost:5050 (admin@inventory.com / admin123)

## Development Workflow

### Local Development (Without Docker)
```bash
cd backend

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Start PostgreSQL (ensure it's running on localhost:5432)
# Then start the backend
./start-local.sh
```

### Database Migrations
```bash
# Create new migration
./migrate.sh create "Description of changes"

# Apply migrations
./migrate.sh upgrade

# Rollback last migration
./migrate.sh downgrade

# View migration history
./migrate.sh history
```

### Docker Development
```bash
# Start all services
docker-compose up -d

# View logs
docker-compose logs -f backend

# Access backend container
docker-compose exec backend bash

# Restart services
docker-compose restart backend
```

## Configuration

### Environment Variables
Key environment variables (set in root `.env` file):

```env
# Database
DATABASE_URL=postgresql://inventory_user:inventory_password@postgres:5432/inventory_db

# JWT Security
SECRET_KEY=your-secure-secret-key-32-characters-minimum
ACCESS_TOKEN_EXPIRE_MINUTES=30

# CORS Settings
BACKEND_CORS_ORIGINS=["http://localhost:3000", "http://localhost:3001"]
```

### Resource Status Logic
Resources automatically receive status updates based on quantity:
- **Available**: quantity > 10
- **Low Stock**: quantity 1-10
- **Out of Stock**: quantity = 0

## API Usage Examples

### User Registration
```bash
curl -X POST "http://localhost:8000/api/v1/auth/register" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "user@example.com",
    "password": "securepassword123"
  }'
```

### User Login
```bash
curl -X POST "http://localhost:8000/api/v1/auth/login" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "user@example.com",
    "password": "securepassword123"
  }'
```

### Create Resource (with JWT token)
```bash
curl -X POST "http://localhost:8000/api/v1/resources/" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_JWT_TOKEN" \
  -d '{
    "name": "Laptop Computer",
    "description": "Dell XPS 13 Developer Edition",
    "category": "Electronics",
    "quantity": 25
  }'
```

### List Resources with Filtering
```bash
# Get all resources
curl -X GET "http://localhost:8000/api/v1/resources/" \
  -H "Authorization: Bearer YOUR_JWT_TOKEN"

# Filter by category and status
curl -X GET "http://localhost:8000/api/v1/resources/?category=Electronics&status=Available&sort_by=name&sort_order=asc" \
  -H "Authorization: Bearer YOUR_JWT_TOKEN"

# Search resources
curl -X GET "http://localhost:8000/api/v1/resources/?search=laptop" \
  -H "Authorization: Bearer YOUR_JWT_TOKEN"
```

## Database Schema

### Users Table
- `id` (Primary Key)
- `email` (Unique)
- `hashed_password`
- `is_active`
- `created_at`
- `updated_at`

### Resources Table
- `id` (Primary Key)
- `name`
- `description`
- `category`
- `quantity`
- `status` (Available/Low Stock/Out of Stock)
- `date_added`
- `last_updated`
- `owner_id` (Foreign Key to Users)

## Security Features

- **Password Hashing**: BCrypt with salt
- **JWT Tokens**: Secure token-based authentication
- **User Isolation**: Users can only access their own resources
- **CORS Protection**: Configurable cross-origin request handling
- **Input Validation**: Pydantic schema validation
- **SQL Injection Protection**: SQLAlchemy ORM parameterized queries

## Production Deployment

### Using Docker Compose
```bash
# Create production environment file
cp .env.prod.example .env.prod
# Edit .env.prod with secure production values

# Deploy to production
./deploy.sh
```

### Manual Deployment
1. Set up PostgreSQL database
2. Configure environment variables
3. Build Docker image: `docker build -t inventory-backend .`
4. Run migrations: `alembic upgrade head`
5. Start container with proper environment variables

## Monitoring and Maintenance

### Health Checks
- **API Health**: `GET /health`
- **Database Connection**: Included in health endpoint
- **Service Status**: `./monitor.sh`

### Database Backup
```bash
# Create backup
./backup-db.sh

# Backups are stored in ./backups/YYYYMMDD/
```

### Logs
```bash
# View all logs
make logs

# Backend specific logs
make logs-backend

# Database logs
make logs-db
```

## Development Tools

### Database Management
- **PgAdmin**: http://localhost:5050 (development only)
- **Direct Connection**: `make db-shell`

### Code Quality
```bash
# Format code
black app/
isort app/

# Lint code
flake8 app/
```

## Troubleshooting

### Common Issues

**Database Connection Failed**
```bash
# Check if PostgreSQL is running
docker-compose ps postgres

# Restart database
docker-compose restart postgres
```

**Migration Errors**
```bash
# Reset database (⚠️ This will delete all data)
make db-reset
```

**Port Already in Use**
```bash
# Check what's using port 8000
lsof -i :8000

# Stop conflicting services
docker-compose down
```

**JWT Token Expired**
- Login again to get a new token
- Tokens expire after 30 minutes by default

### Debug Mode
Set `ENVIRONMENT=development` in your `.env` file to enable debug mode with detailed error messages.

## Contributing

1. Follow the existing code structure
2. Add appropriate error handling
3. Update documentation for new endpoints
4. Ensure database migrations are properly versioned
5. Test API endpoints manually using `/docs`

## Architecture Notes

- **Layered Architecture**: Models → Schemas → API Endpoints
- **Dependency Injection**: FastAPI's dependency system for database sessions and authentication
- **ORM Pattern**: SQLAlchemy for database interactions
- **Schema Validation**: Pydantic for request/response validation
- **Migration Management**: Alembic for database schema versioning

## Future Enhancements

- [ ] Redis caching for improved performance
- [ ] Rate limiting implementation
- [ ] File upload support for resource images
- [ ] Audit logging for resource changes
- [ ] Bulk operations for resources
- [ ] Advanced reporting endpoints
- [ ] WebSocket support for real-time updates