from pydantic import BaseModel


class Plant(BaseModel):

    name:str

    scientificName:str

    family:str

    description:str

    image:str | None = None

    diseases:list[str]=[]

    varieties:list[str]=[]