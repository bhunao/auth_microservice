from fastapi import APIRouter, HTTPException, status

from src.models import CreateUser, UpdateUser, User

router = APIRouter(prefix="/users")


fake_db: list[User] = []


class UserDatabase:
    def create(self, record: CreateUser) -> User:
        user = User(username=record.username, password=record.password)
        fake_db.append(user)
        return user

    def read(self, _id: int) -> User | None:
        for user in fake_db:
            if user.id == _id:
                return user
        return None

    def update(self, record: UpdateUser) -> User | None:
        db_record = get_user(record.id)
        if db_record:
            if record.username:
                db_record.username = record.username
            if record.password:
                db_record.password = record.password
            return db_record
        return

    def delete(self, _id: int) -> User | None:
        db_user = get_user(_id)
        if db_user:
            fake_db.remove(db_user)
            return db_user
        return


def get_user(id: int) -> User | None:
    global fake_db
    for user in fake_db:
        if user.id == id:
            return user
    return None


@router.post("/")
def create_user(record: CreateUser):
    user = User(username=record.username, password=record.password)
    fake_db.append(user)
    return user


@router.get("/{id}")
def read_users(_id: int):
    for user in fake_db:
        if user.id == _id:
            return user
    raise HTTPException(status.HTTP_404_NOT_FOUND, f"No user with id: '{_id}' found.")


@router.put("/")
def update_user(record: UpdateUser):
    db_record = get_user(record.id)
    if db_record:
        if record.username:
            db_record.username = record.username
        if record.password:
            db_record.password = record.password
        return db_record
    else:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND, f"No user with id: '{record.id}' found."
        )


@router.delete("/")
def delete_user(_id: int):
    db_user = get_user(_id)
    if db_user:
        fake_db.remove(db_user)
    raise HTTPException(status.HTTP_404_NOT_FOUND, f"No user with id: '{_id}' found.")
