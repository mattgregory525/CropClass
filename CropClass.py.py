class Crop:
    #Doc string
    """ A simulation of a generic food crop"""

    #Constructor
    def __init__(self,growth_rate,light_need,water_need):

        #Set attributes
        self._growth = 0
        self._days_growing = 0
        self._growth_rate = growth_rate
        self._light_need = light_need
        self._water_need = water_need
        self._status = "Seed"
        self._type = "Generic"

    def needs(self):
        #Returns a dictionary containing light/water need
        return{"Light need": self._light_need,"Water need": self._water_need,}


    def report(self):
        #Returns a disctionary containing type, status, days growing
        return {"Type": self._type, "Status": self._status, "Growth": self._growth, "Days growing": self._days_growing}
        








def main():
    #Instaniate class
    new_crop = Crop(1,4,3)
    print (new_crop.needs())
    print (new_crop.report())


if __name__ == "__main__":
    main()
    
