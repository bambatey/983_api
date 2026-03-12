from datetime import datetime, timezone
import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import auth_routes

app = FastAPI(
    title="Personal Knowledge Server with Swagger",
    description="A production-ready FastAPI application with comprehensive Swagger documentation",
    version="1.0.0",
    contact={
        "name": "API Support Team",
        "url": "https://yourcompany.com/contact",
        "email": "support@yourcompany.com",
    },
    openapi_url="/openapi.json",
    docs_url="/docs",
    redoc_url="/redoc",
)

app.include_router(auth_routes.router)

if __name__ == "__main__":
    print(f"🚀 Server başlatılıyor...")
    print("📝 Loglar hem console'da hem de app.log dosyasında görünecek")
    print("🔧 Debug: Current working directory:", __import__("os").getcwd())
    print("🔧 Debug: __file__:", __file__)
    print("=" * 50)

    import uvicorn
    
    uvicorn.run(
        "app:app",  # ---! Import string olarak geçir - reload için gerekli
        host="0.0.0.0",
        port=8000,
        log_level="info",
        reload=True,
    )
