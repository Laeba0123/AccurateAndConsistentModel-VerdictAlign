# deploy.sh
#!/bin/bash

echo "🚀 Starting VerdictAlign Deployment..."

# Check Docker
if ! command -v docker &> /dev/null; then
    echo "❌ Docker not found. Please install Docker first."
    exit 1
fi

# Build and deploy
echo "📦 Building Docker images..."
docker-compose build

echo "🚢 Starting services..."
docker-compose up -d

echo "✅ Deployment complete!"
echo "🌐 Frontend: http://localhost"
echo "🔧 Backend API: http://localhost:8000/api/docs"
echo "📊 Health Check: http://localhost:8000/health"

# Show logs
docker-compose logs -f