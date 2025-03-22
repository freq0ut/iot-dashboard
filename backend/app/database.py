from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
import boto3
from app.config import Config

Base = declarative_base()

# ✅ Async engine & session
engine = create_async_engine(Config.DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine, expire_on_commit=False, class_=AsyncSession)

# ✅ Safe FastAPI dependency
async def get_db():
    session = SessionLocal()
    try:
        yield session
    finally:
        # Don't manually close it here — FastAPI handles cleanup
        pass

# ✅ DynamoDB setup
dynamodb = boto3.resource(
    "dynamodb",
    region_name=Config.AWS_REGION,
    aws_access_key_id=Config.AWS_ACCESS_KEY_ID,
    aws_secret_access_key=Config.AWS_SECRET_ACCESS_KEY
)

iot_table = dynamodb.Table("IoT_Data")
