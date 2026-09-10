from fastapi import APIRouter
import json

router = APIRouter()

@router.delete("/delete_user")
async def delete_user(id: str):
    return
    # for user in fake_db:
    #     if int(user["user_id"]) == int(id):
    #         fake_db.remove(user)
    #         with open(document, "w") as file:
    #             json.dump(fake_db, file, indent=4)
    #         return f"user deleted successfully"