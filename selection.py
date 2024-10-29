from getServerInfo import getServerInf


class Selection():
    def __init__(self):
        self.info = getServerInf()
        self.facciones_squad = {
                                "VDV": ("🇷🇺", 
                                        {"name":"Russian Airborne Forces", "biomes":
                                                                                    {"desert": "https://steamuserimages-a.akamaihd.net/ugc/2482127496596627806/049046D8FB03AAB413CF7E3514B274174D8263F1/",
                                                                                     "forest": "https://steamuserimages-a.akamaihd.net/ugc/2482127496596632932/D5CDC3834E94640812D80F38AF4AB99EE691594C/"}
                                        
                                        }),  # Rusian Airborne Forces
                               
                               "RGF": ("🇷🇺", 
                                        {"name":"Russian Ground Forces", "biomes":
                                                                                    {"desert": "https://steamuserimages-a.akamaihd.net/ugc/2482127496596627806/049046D8FB03AAB413CF7E3514B274174D8263F1/",
                                                                                     "forest": "https://steamuserimages-a.akamaihd.net/ugc/2482127496596632955/43FA7C40197D0D82E6460791DBC59219DD6C8FC1/"}
                                        
                                        }),  # Russian Ground Forces

                               "USA": ("🇺🇸", 
                                        {"name":"United States Army", "biomes":
                                                                    {"default": "https://steamuserimages-a.akamaihd.net/ugc/2482127496596634099/F87A2E8D75C48E506EC71018A1EFA406DDAD79E2/"}
                                        
                                        }),  # United States Army
                              
                               "USMC": ("🇺🇸", 
                                        {"name":"United States Marine Corps", "biomes":
                                                                                    {"desert": "https://steamuserimages-a.akamaihd.net/ugc/2482127496596634121/2BB65F2436C00FAD7913870F5CE6AC26E3ACB491/",
                                                                                     "forest": "https://steamuserimages-a.akamaihd.net/ugc/2482127496596634106/50F4D86454CC2F776D7331C77B6D9E58092352E1/"}
                                        
                                        }),  # United States Marine Corps

                               "BAF": ("🇬🇧", 
                                        {"name":"British Armed Forces", "biomes":
                                                                        {"default": "https://steamuserimages-a.akamaihd.net/ugc/2482127496596623438/127E98BD8F081B2B890E7EFF11B86774DBDB2A3A/"}
                                        
                                        }),  # British Armed Forces

                                "IMF": ("🏴‍☠️", 
                                        {"name":"Irregular Militia Forces", "biomes":
                                                                        {"default": "https://steamuserimages-a.akamaihd.net/ugc/2482127496596621949/C37FFB957ED5958DA8D81D2E7C62D519CE98C0CF/"}
                                        
                                        }),  # Irregular Militia Forces
                                
                                "CAF": ("🇨🇦", 
                                        {"name":"Canadian Armed Forces", "biomes":
                                                                                    {"desert": "https://steamuserimages-a.akamaihd.net/ugc/2482127496596623448/D8D19FDCC136ED9B3D9D017D70D133AF269A233E/",
                                                                                     "forest": "https://steamuserimages-a.akamaihd.net/ugc/2482127496596623460/8266D99385698B561FAC948272B9D605B0E72F40/"}
                                        
                                        }),  # Canadian Armed Forces
                                
                                "ADF": ("🇦🇺", 
                                        {"name":"Australian Defence Force", "biomes":
                                                                        {"default": "https://steamuserimages-a.akamaihd.net/ugc/2482127496596623424/6E542EA0D05C15B2491E84E8B32892BC24E88371/"}
                                        
                                        }),  # Australian Defence Force
                                
                                "INS": ("💣", 
                                        {"name":"Insurgent", "biomes":
                                                                        {"default": "https://steamuserimages-a.akamaihd.net/ugc/2482127496596621941/38EAEB3EBA08274CACCADB87E64F3BA99AAE2FE9/"}
                                        
                                        }),  # Insurgent

                              "WPMC": ("💰", 
                                        {"name":"Western Private Military Contractors", "biomes":
                                                                        {"default": "https://steamuserimages-a.akamaihd.net/ugc/2462995990959160355/6C9491F7235C5845210F6FFD932E3DFE4A8ADC27/"}
                                        
                                        }),  # Western Private Military Contractors

                                }

        self.maps = {
                        "AlBasrah": "desert",           
                        "Fallujah": "desert",      
                        "Yehorivka": "forest",   
                        "Narva": "forest",             
                        "Gorodok": "forest",   
                        "Mutaha": "desert",              
                        "Kamdesh": "forest",    
                        "Tallil_Outskirts": "desert",  
                        "JensenRange": "training",      
                        "Belaya": "snow",        
                        "FoolsRoad": "forest",     
                        "GooseBay": "forest",  
                        "KohatToi": "desert",   
                        "KamdeshHighlands": "forest",  
                        "LashkarValley": "desert", 
                        "LogarValley": "desert",
                        "Skorpo": "forest",
                        "Sanxian_Islands": "forest", 
                        "Fulda": "forest",         
                        "Anvil": "desert",
                        "Manicouagan": "forest",   
                        "Sumari": "desert",        
                        "Chora": "desert",       
                        "Mestia": "forest"      
                    }

        self.map = self.info["Map"]
        self.Team1 = self.info["Team1"]
        self.Team2 = self.info["Team2"]
        self.biome = self.maps[self.getMapName()]


    def getFactionsEmoji(self):
        return 
    
    def getMapName(self):
        return self.map[:self.map.find("_")]
    
    def getMapType(self):
        return self.maps[self.mapas_squad[self.info["Map"]][:self.mapas_squad[self.info["Map"]].find("-")-1]]
    
    def getTeams(self):
        return [self.info["Team1"], self.facciones_squad["Team2"]]

    def getEnemyTeam(self, selFac):
        if selFac == self.Team1:
            return self.Team2
        elif selFac == self.Team2:
            return self.Team1
        else:
            return "No se ha podido especificar la faccion" + selFac
    
    def getEnemyTeamReal(self, selFac):
        selFac = self.getEnemyTeam(selFac)
        return self.facciones_squad[selFac[:selFac.find("_")]][1]["name"]
    
    def getEnemyUniform(self, selFac):
        team = self.getEnemyTeam(selFac)
        mapName = self.getMapName()
        dispo = self.facciones_squad[team[:team.find("_")]][1]["biomes"].keys()
        if self.maps[mapName] in dispo:
            return self.facciones_squad[team[:team.find("_")]][1]["biomes"][self.maps[mapName]]
        else:
            return self.facciones_squad[team[:team.find("_")]][1]["biomes"]["default"]
        
    def selectTeam(self):
        return 

#sel = Selection()
#print(sel.getMapImage())