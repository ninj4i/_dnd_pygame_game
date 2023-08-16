class dnd_Race:
    def __init__ (self, name):
        self.Name = name
        self.Ability_score_increase = { "STR" : 0,
                                        "DEX" : 0,
                                        "CON" : 0,
                                        "INT" : 0,
                                        "WIS" : 0,
                                        "CHA" : 0}
        self.Age = {"adulthood" : 30,
                    "lifespan"  : 70}
        #self.Alignment = {}
        self.Size = "Medium"
        self.Speed = 30
        self.Languages = {"Common"}



dnd_races = {
    'Humans' : {}

}