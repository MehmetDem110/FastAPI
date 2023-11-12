from pydantic import BaseModel



class SnackBase(BaseModel):
    name: str
    description: str | None = None


class SnackCreate(SnackBase):
    pass


class Snack(SnackBase):
    id: int

    class Config:
        orm_mode = True


class SodaBase(BaseModel):
    name: str
    flavor: str


class SodaCreate(SodaBase):
    pass


class Soda(SodaBase):
    id: int

    class Config:
        orm_mode = True