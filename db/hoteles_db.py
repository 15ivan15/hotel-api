from typing import  Dict
from pydantic import BaseModel

class HotelsInDB(BaseModel):
    hotelname: str
    estrellas: str
    tipo_habitacion: str
    tarifa_inicial:float
    tarifa_alta:float
    tarifa_baja:float
    ciudad:str
    zona: str

# class HotelsInDB_alta(BaseModel):
#     hotelname: str
#     estrellas: str
#     tipo_habitacion: str
#     tarifa_alta:float
#     ciudad: str
#     zona: str
    
database_hotels = Dict[str, HotelsInDB]

database_hotels = {
    "Bogotá": HotelsInDB(**{"hotelname":"Casa Gabriela", 
                            "estrellas":"2",
                            "tarifa_inicial": 40.340,
                            "tarifa_alta": 55.000,
                            "tarifa_baja":38.500,
                            "tipo_habitacion":"Individual",
                            "ciudad":"Bogotá", 
                            "zona":"Centro"}),
    "Bogotá1": HotelsInDB(**{"hotelname":"Bogotá DC", 
                            "estrellas":"3",
                            "tarifa_inicial": 58.600,
                            "tarifa_alta": 75.600,
                            "tarifa_baja":50.600,
                            "tipo_habitacion":"Doble",
                            "ciudad":"Bogotá", 
                            "zona":"Centro"}),
    "Bogotá2": HotelsInDB(**{"hotelname":"DoubleTree by Hilton Bogotá AR", 
                            "estrellas":"5",
                            "tarifa_inicial": 186.140,
                            "tarifa_alta": 174.800,
                            "tarifa_baja": 225.850,
                            "tipo_habitacion":"sencilla",
                            "ciudad":"Bogotá", 
                            "zona":"Centro"}),
    "Bogotá3": HotelsInDB(**{"hotelname":"Santa Bárbara Boutique", 
                            "estrellas":"3",
                            "tarifa_inicial": 155.820,
                            "tarifa_alta":187.600,
                            "tarifa_baja":150.200,
                            "tipo_habitacion": "Doble",
                            "ciudad":"Bogotá", 
                            "zona":"Norte"}),
    "Bogotá4": HotelsInDB(**{"hotelname":"101 Park House", 
                            "estrellas":"5",
                            "tarifa_inicial":353.380,
                            "tarifa_alta":399.700,
                            "tarifa_baja":343.000,
                            "tipo_habitacion":"Suite Business",
                            "ciudad":"Bogotá", 
                            "zona":"Norte"}),
    "Bogotá5": HotelsInDB(**{"hotelname":"Loft Aparment in south location", 
                            "estrellas":"4",
                            "tarifa_inicial":89.900,
                            "tarifa_alta":115.200,
                            "tarifa_baja":75.000,
                            "tipo_habitacion":"Individual",
                            "ciudad":"Bogotá", 
                            "zona":"Sur"}),
    "Bogotá6": HotelsInDB(**{"hotelname":"Expo Suites Parque Bavaria", 
                            "estrellas":"3",
                            "tarifa_inicial": 119.000,
                            "tarifa_alta": 135.000,
                            "tarifa_baja": 105.500,
                            "tipo_habitacion":"Doble",
                            "ciudad":"Bogotá", 
                            "zona":"Oriente"}),
    "Bogotá7": HotelsInDB(**{"hotelname":"Hotel Grand Park", 
                            "estrellas":"4",
                            "tarifa_inicial": 156.000,
                            "tarifa_alta": 186.700,
                            "tarifa_baja": 134.200,
                            "tipo_habitacion":"Cama en Habitación compartida",
                            "ciudad":"Bogotá", 
                            "zona":"Oriente"}),
    "Bogotá8": HotelsInDB(**{"hotelname":"GHL Hotel Capital", 
                            "estrellas":"5",
                            "tarifa_inicial": 195.500,
                            "tarifa_alta": 239.900,
                            "tarifa_baja": 187.000,
                            "tipo_habitacion":"Doble 2 camas",
                            "ciudad":"Bogotá", 
                            "zona":"Occidente"}),
}

def get_hotel(hotelname: str):
    if hotelname in database_hotels.keys():
        return database_hotels[hotelname]
    else: 
        return None
    
    
def update_hotel(hotel_in_db: HotelsInDB):
    for clave in database_hotels.keys():
        if get_hotel(clave).ciudad == hotel_in_db.ciudad:
            if get_hotel(clave).hotelname == hotel_in_db.hotelname:
                get_hotel(clave).tarifa_inicial=hotel_in_db.tarifa_inicial
                database_hotels[clave] = get_hotel(clave)
                return hotel_in_db
