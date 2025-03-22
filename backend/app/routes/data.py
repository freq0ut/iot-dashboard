from fastapi import APIRouter, Depends, HTTPException
from datetime import datetime
from app.schemas import IoTData
from app.core.authentication import get_current_user
from app.core.dependencies import get_db_dependency
from app.database import iot_table
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.models import Device, User

router = APIRouter()

# ✅ Accept IoT sensor data and store in DynamoDB
@router.post("/")
async def submit_iot_data(
    data: IoTData,
    db: AsyncSession = Depends(get_db_dependency),
    current_user: User = Depends(get_current_user)
):
    # Validate that the device belongs to the current user
    result = await db.execute(select(Device).where(Device.id == data.device_id))
    device = result.scalars().first()

    if not device or device.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail="Device not found or access denied.")

    # Add a UTC timestamp and store in DynamoDB
    timestamp = int(datetime.utcnow().timestamp())

    iot_table.put_item(Item={
        "device_id": str(data.device_id),
        "timestamp": timestamp,
        "sensor_type": data.sensor_type,
        "value": data.value
    })

    return {"status": "Data stored successfully", "timestamp": timestamp}
