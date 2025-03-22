from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.models import Device
from app.schemas import DeviceCreate, DeviceResponse
from app.core.dependencies import get_db_dependency
from app.core.authentication import get_current_user
from app.models.models import User

router = APIRouter()


# ✅ Register a new device for the authenticated user
@router.post("/", response_model=DeviceResponse)
async def register_device(
    device: DeviceCreate,
    db: AsyncSession = Depends(get_db_dependency),
    current_user: User = Depends(get_current_user)
):
    if device.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail="You can only register devices for yourself.")

    new_device = Device(name=device.name, owner_id=current_user.id)
    db.add(new_device)
    await db.commit()
    await db.refresh(new_device)
    return new_device


# ✅ List all devices for the authenticated user
@router.get("/", response_model=list[DeviceResponse])
async def list_devices(
    db: AsyncSession = Depends(get_db_dependency),
    current_user: User = Depends(get_current_user)
):
    result = await db.execute(select(Device).where(Device.owner_id == current_user.id))
    devices = result.scalars().all()
    return devices
