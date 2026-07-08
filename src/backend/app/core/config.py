from pydantic_settings import BaseSettings
from typing import Optional
import os


class Settings(BaseSettings):
    # App
    APP_NAME: str = "Zero-Trust RBAC Platform"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = False
    ENVIRONMENT: str = "development"
    
    # Database
    DATABASE_URL: str = "postgresql+asyncpg://postgres:postgres@localhost:5432/zerotrust"
    DATABASE_POOL_SIZE: int = 10
    DATABASE_MAX_OVERFLOW: int = 20
    
    # Security
    SECRET_KEY: str = "change-me-in-production-use-strong-random-key"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7
    
    # Azure AD / OIDC
    AZURE_AD_TENANT_ID: Optional[str] = None
    AZURE_AD_CLIENT_ID: Optional[str] = None
    AZURE_AD_CLIENT_SECRET: Optional[str] = None
    OIDC_ISSUER_URL: Optional[str] = None
    
    # GitHub Integration
    GITHUB_APP_ID: Optional[str] = None
    GITHUB_APP_PRIVATE_KEY: Optional[str] = None
    GITHUB_APP_INSTALLATION_ID: Optional[str] = None
    GITHUB_WEBHOOK_SECRET: Optional[str] = None
    GITHUB_API_URL: str = "https://api.github.com"
    
    # Redis
    REDIS_URL: str = "redis://localhost:6379/0"
    
    # ML Services
    ML_ANOMALY_MODEL_PATH: str = os.path.expanduser("~/.cache/zt-models/anomaly-detector")
    ML_POLICY_MODEL_PATH: str = os.path.expanduser("~/.cache/zt-models/policy-generator")
    ML_EMBEDDING_MODEL: str = "sentence-transformers/all-MiniLM-L6-v2"
    HF_TOKEN: Optional[str] = None
    
    # Monitoring
    PROMETHEUS_METRICS_PORT: int = 9090
    GRAFANA_URL: Optional[str] = None
    
    # Audit
    AUDIT_LOG_RETENTION_DAYS: int = 2555  # 7 years
    AUDIT_BATCH_SIZE: int = 100
    
    # Rate Limiting
    RATE_LIMIT_REQUESTS: int = 100
    RATE_LIMIT_WINDOW: int = 60
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True


settings = Settings()