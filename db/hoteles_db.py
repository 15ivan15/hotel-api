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
                            "tarifa_inicial": 40340,
                            "tarifa_alta": 55000,
                            "tarifa_baja":38500,
                            "tipo_habitacion":"Individual",
                            "ciudad":"Bogotá", 
                            "zona":"Centro"}),
    "Bogotá1": HotelsInDB(**{"hotelname":"Bogotá DC", 
                            "estrellas":"3",
                            "tarifa_inicial": 58600,
                            "tarifa_alta": 75600,
                            "tarifa_baja":50600,
                            "tipo_habitacion":"Doble",
                            "ciudad":"Bogotá", 
                            "zona":"Centro"}),
    "Bogotá2": HotelsInDB(**{"hotelname":"DoubleTree by Hilton Bogotá AR", 
                            "estrellas":"5",
                            "tarifa_inicial": 186140,
                            "tarifa_alta": 174800,
                            "tarifa_baja": 225850,
                            "tipo_habitacion":"sencilla",
                            "ciudad":"Bogotá", 
                            "zona":"Centro"}),
    "Bogotá3": HotelsInDB(**{"hotelname":"Santa Bárbara Boutique", 
                            "estrellas":"3",
                            "tarifa_inicial": 155820,
                            "tarifa_alta":187600,
                            "tarifa_baja":150200,
                            "tipo_habitacion": "Doble",
                            "ciudad":"Bogotá", 
                            "zona":"Norte"}),
    "Bogotá4": HotelsInDB(**{"hotelname":"101 Park House", 
                            "estrellas":"5",
                            "tarifa_inicial":353380,
                            "tarifa_alta":399700,
                            "tarifa_baja":343000,
                            "tipo_habitacion":"Suite Business",
                            "ciudad":"Bogotá", 
                            "zona":"Norte"}),
    "Bogotá5": HotelsInDB(**{"hotelname":"Loft Aparment in south location", 
                            "estrellas":"4",
                            "tarifa_inicial":89900,
                            "tarifa_alta":115200,
                            "tarifa_baja":75000,
                            "tipo_habitacion":"Individual",
                            "ciudad":"Bogotá", 
                            "zona":"Sur"}),
    "Bogotá6": HotelsInDB(**{"hotelname":"Expo Suites Parque Bavaria", 
                            "estrellas":"3",
                            "tarifa_inicial": 119000,
                            "tarifa_alta": 135000,
                            "tarifa_baja": 105500,
                            "tipo_habitacion":"Doble",
                            "ciudad":"Bogotá", 
                            "zona":"Oriente"}),
    "Bogotá7": HotelsInDB(**{"hotelname":"Hotel Grand Park", 
                            "estrellas":"4",
                            "tarifa_inicial": 156000,
                            "tarifa_alta": 186700,
                            "tarifa_baja": 134200,
                            "tipo_habitacion":"Cama en Habitación compartida",
                            "ciudad":"Bogotá", 
                            "zona":"Oriente"}),
    "Bogotá8": HotelsInDB(**{"hotelname":"GHL Hotel Capital", 
                            "estrellas":"5",
                            "tarifa_inicial": 195500,
                            "tarifa_alta": 239900,
                            "tarifa_baja": 187000,
                            "tipo_habitacion":"Doble 2 camas",
                            "ciudad":"Bogotá", 
                            "zona":"Occidente"}),
    "Bogotá": HotelsInDB(**{"hotelname":"Casa Gabriela", 
                            "estrellas":"2",
                            "tarifa_inicial": 40340,
                            "tarifa_alta": 55000,
                            "tarifa_baja":38500,
                            "tipo_habitacion":"Individual",
                            "ciudad":"Bogotá", 
                            "zona":"Centro"}),
    "Bogotá1": HotelsInDB(**{"hotelname":"Bogotá DC", 
                            "estrellas":"3",
                            "tarifa_inicial": 58600,
                            "tarifa_alta": 75600,
                            "tarifa_baja":50600,
                            "tipo_habitacion":"Doble",
                            "ciudad":"Bogotá", 
                            "zona":"Centro"}),
    "Bogotá2": HotelsInDB(**{"hotelname":"DoubleTree by Hilton Bogotá AR", 
                            "estrellas":"5",
                            "tarifa_inicial": 186140,
                            "tarifa_alta": 174800,
                            "tarifa_baja": 225850,
                            "tipo_habitacion":"sencilla",
                            "ciudad":"Bogotá", 
                            "zona":"Centro"}),
    "Bogotá3": HotelsInDB(**{"hotelname":"Santa Bárbara Boutique", 
                            "estrellas":"3",
                            "tarifa_inicial": 155820,
                            "tarifa_alta":187600,
                            "tarifa_baja":150200,
                            "tipo_habitacion": "Doble",
                            "ciudad":"Bogotá", 
                            "zona":"Norte"}),
    "Bogotá4": HotelsInDB(**{"hotelname":"101 Park House", 
                            "estrellas":"5",
                            "tarifa_inicial":353380,
                            "tarifa_alta":399700,
                            "tarifa_baja":343000,
                            "tipo_habitacion":"Suite Business",
                            "ciudad":"Bogotá", 
                            "zona":"Norte"}),
    "Bogotá5": HotelsInDB(**{"hotelname":"Loft Aparment in south location", 
                            "estrellas":"4",
                            "tarifa_inicial":89900,
                            "tarifa_alta":115200,
                            "tarifa_baja":75000,
                            "tipo_habitacion":"Individual",
                            "ciudad":"Bogotá", 
                            "zona":"Sur"}),
    "Bogotá6": HotelsInDB(**{"hotelname":"Expo Suites Parque Bavaria", 
                            "estrellas":"3",
                            "tarifa_inicial": 119000,
                            "tarifa_alta": 135000,
                            "tarifa_baja": 105500,
                            "tipo_habitacion":"Doble",
                            "ciudad":"Bogotá", 
                            "zona":"Oriente"}),
    "Bogotá7": HotelsInDB(**{"hotelname":"Hotel Grand Park", 
                            "estrellas":"4",
                            "tarifa_inicial": 156000,
                            "tarifa_alta": 186700,
                            "tarifa_baja": 134200,
                            "tipo_habitacion":"Cama en Habitación compartida",
                            "ciudad":"Bogotá", 
                            "zona":"Oriente"}),
    "Bogotá8": HotelsInDB(**{"hotelname":"GHL Hotel Capital", 
                            "estrellas":"5",
                            "tarifa_inicial": 195500,
                            "tarifa_alta": 239900,
                            "tarifa_baja": 187000,
                            "tipo_habitacion":"Doble 2 camas",
                            "ciudad":"Bogotá", 
                            "zona":"Occidente"}),
    "Medellín": HotelsInDB(**{"hotelname":"Ayenda 1248 Conquistadores", 
                            "estrellas":"1",
                            "tarifa_inicial": 42660,
                            "tarifa_alta": 53000,
                            "tarifa_baja":36400,
                            "tipo_habitacion":"Doble",
                            "ciudad":"Medellín", 
                            "zona":"Centro"}),
    "Medellín9": HotelsInDB(**{"hotelname":"Hotel Med Estadio", 
                            "estrellas":"3",
                            "tarifa_inicial": 149000,
                            "tarifa_alta": 160000,
                            "tarifa_baja":135000,
                            "tipo_habitacion":"Triple",
                            "ciudad":"Medellín", 
                            "zona":"Centro"}),
    "Medellín10": HotelsInDB(**{"hotelname":"Rivière Boutique Hotel", 
                            "estrellas":"4",
                            "tarifa_inicial": 105000,
                            "tarifa_alta": 119000,
                            "tarifa_baja": 97000,
                            "tipo_habitacion":"Sencilla",
                            "ciudad":"Medellín", 
                            "zona":"Centro"}),
    "Medellín11": HotelsInDB(**{"hotelname":"Hotel Estadio Real", 
                            "estrellas":"3",
                            "tarifa_inicial": 140000,
                            "tarifa_alta":155000,
                            "tarifa_baja":131000,
                            "tipo_habitacion": "Doble",
                            "ciudad":"Medellín", 
                            "zona":"Norte"}),
    "Medellín12": HotelsInDB(**{"hotelname":"Hotel Cristal", 
                            "estrellas":"2",
                            "tarifa_inicial":70000,
                            "tarifa_alta":85000,
                            "tarifa_baja":62000,
                            "tipo_habitacion":"Individual",
                            "ciudad":"Medellín", 
                            "zona":"Norte"}),
    "Medellín13": HotelsInDB(**{"hotelname":"Hotel Intercontinental Medellín", 
                            "estrellas":"5",
                            "tarifa_inicial":555740,
                            "tarifa_alta":630000,
                            "tarifa_baja":430000,
                            "tipo_habitacion":"Suite Junior",
                            "ciudad":"Medellín", 
                            "zona":"Sur"}),
    "Medellín14": HotelsInDB(**{"hotelname":"Hotel San Antonio Guarne", 
                            "estrellas":"4",
                            "tarifa_inicial": 110000,
                            "tarifa_alta": 135000,
                            "tarifa_baja": 99000,
                            "tipo_habitacion":"Individual",
                            "ciudad":"Medellín", 
                            "zona":"Oriente"}),
    "Medellín15": HotelsInDB(**{"hotelname":"Hotel Suite del Parque", 
                            "estrellas":"2",
                            "tarifa_inicial": 133200,
                            "tarifa_alta": 155000,
                            "tarifa_baja": 115000,
                            "tipo_habitacion":"Doble",
                            "ciudad":"Medellín", 
                            "zona":"Occidente"}),
    "Medellín16": HotelsInDB(**{"hotelname":"Sites Hotel", 
                            "estrellas":"5",
                            "tarifa_inicial": 379900,
                            "tarifa_alta": 490000,
                            "tarifa_baja": 255000,
                            "tipo_habitacion":"Habitacion Deluxe",
                            "ciudad":"Medellín", 
                            "zona":"Occidente"}),

    "Neiva": HotelsInDB(**{"hotelname":"Hotel Paradisus", 
                            "estrellas":"3",
                            "tarifa_inicial": 59000,
                            "tarifa_alta": 79200,
                            "tarifa_baja":39500,
                            "tipo_habitacion":"Doble",
                            "ciudad":"Neiva", 
                            "zona":"Centro"}),
    "Neiva17": HotelsInDB(**{"hotelname":"HOTEL KHALIFA", 
                            "estrellas":"4",
                            "tarifa_inicial": 100840,
                            "tarifa_alta": 125000,
                            "tarifa_baja":99800,
                            "tipo_habitacion":"Individual",
                            "ciudad":"Neiva", 
                            "zona":"Centro"}),
    "Neiva18": HotelsInDB(**{"hotelname":"Hotel Neiva Plaza", 
                            "estrellas":"4",
                            "tarifa_inicial": 180000,
                            "tarifa_alta": 250000,
                            "tarifa_baja": 149000,
                            "tipo_habitacion":"Doble",
                            "ciudad":"Neiva", 
                            "zona":"Centro"}),
    "Neiva19": HotelsInDB(**{"hotelname":" La Providencia Hotel", 
                            "estrellas":"1",
                            "tarifa_inicial": 60000,
                            "tarifa_alta":79000,
                            "tarifa_baja":49000,
                            "tipo_habitacion": "Individual",
                            "ciudad":"Neiva", 
                            "zona":"Norte"}),
    "Neiva20": HotelsInDB(**{"hotelname":"Hotel Jesmar", 
                            "estrellas":"3",
                            "tarifa_inicial":70000,
                            "tarifa_alta":89000,
                            "tarifa_baja":57000,
                            "tipo_habitacion":"Habitacion Deluxe",
                            "ciudad":"Neiva", 
                            "zona":"Norte"}),
    "Neiva21": HotelsInDB(**{"hotelname":"Hotel Septima Avenida", 
                            "estrellas":"3",
                            "tarifa_inicial":80000,
                            "tarifa_alta":102000,
                            "tarifa_baja":65000,
                            "tipo_habitacion":"Doble",
                            "ciudad":"Neiva", 
                            "zona":"Sur"}),
    "Neiva22": HotelsInDB(**{"hotelname":"The Ancestral Magic of Huila", 
                            "estrellas":"4",
                            "tarifa_inicial": 203740,
                            "tarifa_alta": 250000,
                            "tarifa_baja": 185000,
                            "tipo_habitacion":"Apartamento",
                            "ciudad":"Neiva", 
                            "zona":"Oriente"}),
    "Neiva23": HotelsInDB(**{"hotelname":"Vesta Hotel Boutique", 
                            "estrellas":"5",
                            "tarifa_inicial": 250000,
                            "tarifa_alta": 302000,
                            "tarifa_baja": 199000,
                            "tipo_habitacion":"Suite",
                            "ciudad":"Neiva", 
                            "zona":"Oriente"}),
    "Neiva24": HotelsInDB(**{"hotelname":"Hotel Abadia", 
                            "estrellas":"2",
                            "tarifa_inicial": 75000,
                            "tarifa_alta": 99000,
                            "tarifa_baja": 64000,
                            "tipo_habitacion":"Individual",
                            "ciudad":"Neiva", 
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
