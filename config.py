# config.py

# Column Index (0-based)
HASHTAGS_TARGET_INDEX = 19

# ─── Control Sheet Names ────────────────────────────────────────────────────
# Name to assign to the final combined master sheet
FINAL_MASTER_SHEET_NAME = "Final MasterSheet"
# Name to assign to the consolidated food sheet

# ─── File Paths ───────────────────────────────────────────────────────────────
INPUT_FILE  = r"H:\My Drive\HireThen\Internal - Flyberg Content\Location Scrapping Info\Sudip Paul\Ready to create hashtags\ExtraHashtags\Cleaned Malapurram data.xlsx"
OUTPUT_FILE = r"H:\My Drive\HireThen\Internal - Flyberg Content\Location Scrapping Info\Subhojyoti\Hashtags Completed Data\FINAL Malappuram.xlsx"

# Map of “dominant” hashtags → a set of hashtags to remove when the dominant one is present
CONFLICT_HASHTAG_MAP = {
    "#HyperMarkets": {"#MarketStalls", "#StreetMarkets","#Vendors"},
    "#SuperMarkets":{"#MarketStalls","#StreetMarkets","#Vendors"},
    "#OutletMalls": {"#MarketStalls", "#StreetMarkets", "#Theaters"},
    "#ShoppingMalls": {"#MarketStalls", "#StreetMarkets", "#Theaters"},
    "#Churches":      {"#Church"},
    "#Monasteries":   {"#Monastery"},
    "#ArtGalleries":  {"#ArtGallery"},
    "#Beaches":       {"#Beach"},
    "#ChildrenSAmusementCenter": {"#AmusementParks","#Rides","#Entertainment"},
    "#ChildrensAmusementCenter": {"#AmusementParks","#Rides","#Entertainment"},
    "#AmusementParks": {"#Parks","#Sightseeing"},
    "#ArtCafe":         {"#Art","#Culture"},
    "#Billiards":         {"#Pools"},
    "#Pools":           {"#SwimmingPool"},
    "#LiveMusic":       {"#Music","#LiveMusicBar","LiveMusicVenue"},
    "#HistoricSites": {"#History"},
    "#Desserts":        {"#Sweet"},
    "#MarineLife":      {"#Exhibits"},
    "#WildLife":        {"#Exhibits"},
    "#Statues":         {"#WildLife"},
    "#Bakery":          {"#BakeryAndCakeShop"},
    "#CityHall":        {"#CityOrTownHall"},
    "#KiteSurfing":      {"#Surfing"},
    "#PerformingArts":   {"#Art"},
    # …add more rules here as needed
}

# ─── Keywords for Identifying Food Sheets ────────────────────────────────────
FOOD_SHEET_KEYWORDS = [
    "restaurants", "bars", "cafes", "nightlife", "deli", "bakery", "night life",
    "nightclubs", "breweries", "local food","beverages","drinks",
]

# ─── Words to Omit When Generating Word-by-Word Tags ──────────────────────────
OMIT_WORDS = {
    "restaurant","place", "lounge", "takeout", "health", "delivery","takeaway", "modern",
    "joint", "pub", "nightlife", "spot", "fine","dining", "eatery","grill", "delivery service",
    "fast food", "family", "vegan", "vegetarian", "vegan-friendly","Gluten-free","shop","new",
    }
# ─── Exclusions & Plural-Priority ─────────────────────────────────────────────
EXCLUDED_TYPE_HASHTAGS = {
    "#GlutenFree",
    "#Vegan",  
    "#ParkRide", 
    "#Vegetarian",
    "#Gastropub",
    "#GokartingVenue",
    "#AdultEntertainment",
    "#AdultEntertainmentStore",
    "#AdultEntertainmentClub",
    "#HistoricalPlaceMuseum",
    "#HistoryMuseum",
    "#LocalHistoryMuseum",
    "#HistoricalLandmark",
    "#HistoricalPlace",
    "#ExhibitionAndTradeCentre",
    "#PerformingArtsTheater",
    "#Shop",
    "#FastFoodRestaurant",
    "#Restaurant",
    "#Cafe",
    "#Vegan",
    "#Vegetarian",
    "#Nan",
    "#Non",
    "#HikingArea",
    "#EventVenue",
    "#EventPlanner",
    "#Bar",
    "#Food",
    "#Grill",
    "#EscapeRoomCenter",
    "#FastFood",
    "#IceCreamShop",
    "#BakeryAndCake",
    "#Diner",
    "#ThaiMassageShop",
    "#ThaiMassageTherapist",
    "#VideoGameStore",
    "#CityPark",
    "#SyokudoAndTeishokuRestaurant",
    "#LiveMusicVenue",
    "#WineBar",
    "#Cafeteria",
    "#CoffeeShop",
    "#PoolHall",
    "#WildlifeAndSafariPark",
}

# ─── Content-Based Hashtag Rules ──────────────────────────────────────────────
# The hashtag to add when any animal is mentioned
WILDLIFE_TAG = "#Wildlife"
MARINE_LIFE_TAG = "#MarineLife"

# ─────────────────────────────────────────────────────────────────────────────
# CONTENT_RULES (now includes all original content rules + the moved TYPE_RULES)
# ─────────────────────────────────────────────────────────────────────────────
CONTENT_RULES = {
    # ─── Food Rule Map ────────────────────────────────────────────────────────────
    "adult entertainment":   ["#StripClub"],
    "adult entertainment club": ["#StripClub"],
    "bakery":  ["#Bakery"],
    "cake":             ["#Bakery"],
    "south indian":          ["#SouthIndian", "#Indian"],
    "north indian":          ["#NorthIndian", "#Indian"],
    "latin american":        ["#LatinAmerican", "#American"],
    "sweet":                 ["#Desserts"],
    "art cafe":            ["#ArtCafe"],
    "dog cafe":             ["#DogCafe"],
    "ice cream shop":        ["#IceCream"],
    "live music bar":       ["#LiveMusic"],
    "live concert":         ["#LiveMusic"],
    "syokudo and teishoku restaurant": ["#Syokudo","#Teishoku"],

    # ─── Nature & Parks ───────────────────────────────────────────────
    "park":                ["#Parks", "#Sightseeing"],
    "arboretum":           ["#Gardens","#Nature"],
    "garden":              ["#Gardens", "#Nature"],
    "picnic":              ["#PicnicSpots"],
    "safari park":         ["#SafariPark"],
    "aquarium":            ["#Aquariums", "#MarineLife"],
    "zoo":                 ["#Zoos", "#Wildlife"],
    "forest":              ["#Wildlife"],

    # ─── Hiking Trails & Tranportation ───────────────────────────────────────────────
    "hiking":              ["#HikingTrails"],
    "walking paths":      ["#HikingTrails"],
    "camping":              ["#Camping"],
    "campground":           ["#Camping"],
    "camp":                  ["#Camping"],   
    "tram":                ["#Trams"],
    "bus station":         ["#BusStops"],
    "bus stop":           ["#BusStops"],
    "train station":      ["#TrainStations"],
    "railway station":    ["#TrainStations"],
    "subway station":     ["#SubwayStations"],
    "metro station":      ["#MetroStations"],
    "ferry":              ["#Ferries"],
    "cruise":             ["#Cruises"],
    "toy train":          ["#ToyTrains"],

    # ─── Water Activities & Pools ───────────────────────────────────────
    "boat":                ["#Boating"],
    "surfing":             ["#Surfing"],
    "kite surfing":        ["#KiteSurfing"],
    "swimming":            ["#Swimming"],
    "boating":             ["#Boating"],
    "canoeing":            ["#Canoeing"],
    "fishing":             ["#Fishing"],
    "kayak":               ["#Kayaking"],
    "kayaking":            ["#Kayaking"],
    "rafting":             ["#Rafting"],
    "pool":                ["#Pools"],
    "water park":          ["#WaterParks", "#Pools", "#Swimming", "#WaterSlides"],
    "water slides":        ["#WaterSlides"],
    "beach":               ["#Beaches", "#Swimming"],
    "beaches":             ["#Beaches", "#Swimming"],
    "thermal bath":        ["#ThermalBaths"],
    "spa":                 ["#Spas"],
    "healthspa":           ["#HealthSpa","#Spas"],
    "massage":             ["#Massage"],
    "thai massage":        ["ThaiMassage","#Massage"],
    "thai massage shop":   ["ThaiMassage","Massage"],
    "hot spring":          ["#HotSprings"],  

    # ─── Entertainment & Amusements ────────────────────────────────────
    "amusement park":      ["#AmusementParks", "#Rides", "#Entertainment"],
    "amusement center":     ["#AmusementParks","#Rides","#Entertainment"],
    "casino":              ["#Casinos", "#Gambling"],
    "rides":                 ["#Rides"],
    "bumper car":         ["#BumperCars"],
    "cable car":        ["#CableCars"],
    "skii":             ["#Skiing"],
    "axe throwing":     ["#AxeThrowing"],
    "zip line":             ["#ZipLine"],
    "billiard":             ["#Billiards"],
    "billard":              ["#Billiards"],
    "pool hall":            ["#Billiards"],
    "gaming":              ["#Gaming"],
    "night club":           ["#NightClubs"],
    "adult entertainment": ["#StripClub"],
    "theme park":          ["#ThemeParks", "#AmusementParks", "#Rides", "#Entertainment"],
    "skate park":            ["#Skating","#Parks","#Sightseeing"],
    "skatepark":            ["#Skating","#Parks","#Sightseeing"],
    "arcade":              ["#Arcades", "#VideoGames"],
    "board game club":    ["#BoardGames", "#GameClub"],
    "video arcades":       ["#Arcades", "#VideoGames"],
    "game store":          ["#GameStore", "#VideoGames"],
    "video gameshop":      ["#GameStore", "#VideoGames"],
    "video game shop":     ["#GameStore", "#VideoGames"],
    "video game store":    ["#GameStore", "#VideoGames"],
    "escape room":         ["#EscapeRooms", "#Puzzles"],
    "escape games":        ["#EscapeRooms","#Puzzles"],
    "concert hall":        ["#ConcertHalls", "#Music"],
    "concert":              ["#Concerts", "#Music"],
    "performing arts":     ["#PerformingArts", "#Culture"],
    "performing arts center": ["#PerformingArts", "#Culture"],
    "performing arts theater": ["#PerformingArts", "#Theaters"],
    "ice rink":            ["#IceSkating"],
    "ballet":               ["#Ballet"],
    "ice skating":         ["#IceSkating"],
    "laser tag":           ["#LaserTag"],
    "go kart":             ["#GoKart"],
    "go karting":          ["#GoKart"],
    "go karting venue":    ["#GoKart"],
    "rides":               ["#Rides"],
    "skate":               ["#Skating"],
    "bowling":            ["#Bowling"],
    "amphitheater":         ["#Amphitheaters", "#Theaters"],
    "movie theater":       ["#MovieTheaters", "#Theaters"],
    "multiplex":           ["#MovieTheaters"],
    "cinema":              ["#MovieTheaters"],
    "theater":             ["#Theaters"],
    "stadium":              ["#Stadiums"],
    "arena":                ["#Arenas"],


    # ─── Museums & Exhibitions ─────────────────────────────────────────
    "museum":              ["#Museums", "#History"],
    "art museum":          ["#ArtMuseum", "#Art", "#Culture"],
    "science museum":      ["#Museums", "#Science"],
    "army museum":         ["#Museums", "#History", "#Military"],
    "heritage museums":    ["#Museums", "#Heritage"],
    "interactive exhibit": ["#InteractiveExhibits"],
    "interactive exhibition": ["#InteractiveExhibits"],
    "rotating exhibit":   ["#RotatingExhibits"],
    "rotating exhibition": ["#RotatingExhibits"],
    "interactive exhibitions": ["#InteractiveExhibitions"],
    "exhibition and trade centre": ["#Exhibitions","#TradeCenter"],
    "exhibition":          ["#Exhibitions"],
    "exhibits":            ["#Exhibits"],

    # ─── Arts & Culture ────────────────────────────────────────────────
    "art":                 ["#Art", "#Culture"],
    "History": ["#History"],
    "Historical":  ["#History"],
    "art gallery":         ["#ArtGalleries", "#Art", "#Culture"],
    "art galleries":       ["#ArtGalleries", "#Art", "#Culture"],
    "art center":          ["#ArtCenters", "#Art", "#Culture"],
    "cultural":            ["#Culture"],
    "culture":             ["#Culture"],
    "music":               ["#Music"],
    "live music":          ["#LiveMusic"],
    "sculpture":           ["#Sculptures"],
    "fountain":            ["#Fountains"],

    # ─── Landmarks & Scenic ────────────────────────────────────────────
    "bridge":              ["#Bridges"],
    "water fall":          ["#WaterFalls","#Sightseeing"],
    "waterfall":           ["#WaterFalls","#Sightseeing"],
    "cave":                ["#Caves"],
    "fortress":            ["#Fortresses","#History"],
    "castle":              ["#Castles","#History"],
    "palace":              ["#Palaces","#History"],
    "island":               ["#Islands"],
    "city or town hall":    ["#CityHall","#TownHall"],
    "city hall":            ["#CityHall"],
    "town hall":            ["#TownHall"],
    "mansion":              ["#Mansions"],
    "villa":                ["#Villas"],
    "statue":              ["#Statues"],
    "altar":                ["#Altars", "#Religion","#Praying"],
    "memorial":            ["#Memorials", "#History"],
    "sunset":             ["#Sunsets", "#Sightseeing"],
    "sunrise":             ["#Sunrises", "#Sightseeing"],
    "panoramic views":      ["#Sightseeing"],
    "viewpoint":           ["#Sightseeing"],
    "monument":            ["#Monuments", "#History"],
    "observation deck":    ["#ObservationDecks", "#Sightseeing"],
    "landscape":           ["#Sightseeing"],
    "picturesque":         ["#Sightseeing"],
    "scenic":              ["#Sightseeing"],
    "sightseeing":         ["#Sightseeing"],

    # ─── Markets & Shopping ─────────────────────────────────────────────
    "market":              ["#Markets", "#MarketStalls", "#Vendors", "#StreetMarkets"],
    "supermarket":         ["#Markets","#RetailStores","#Supermarkets"],
    "shopping center":      ["#ShoppingCenters","#Markets","#RetailStores","#Fashion","#FoodCourt"],
    "shopping complex":     ["#ShoppingComplex","#Markets","#RetailStores","#Fashion","#FoodCourt"],
    "department store":    ["#DepartmentStores", "#RetailStores", "#Markets"],
    "shopping mall":       ["#ShoppingMalls", "#RetailStores", "#Fashion", "#FoodCourt", "#Markets"],
    "outlet mall":         ["#OutletMalls", "#RetailStores", "#Fashion", "#FoodCourt", "#Markets"],
    "hypermarket":         ["#Hypermarkets", "#RetailStores", "#Markets"],

    # ─── Sports & Leisure ──────────────────────────────────────────────
    "golf":                ["#Golf"],
    "minigolf":             ["#Minigolf"],

    # ─── Events & Venues ────────────────────────────────────────────────
    "event":               ["#Events"],
    "festival":            ["#Festivals"],
    "tour operator":       ["#TourOperators"],

    # ─── Family & Kids ──────────────────────────────────────────────────
    "playground":          ["#Playgrounds"],
    "children":            ["#ChildrensActivities"],
    "child":               ["#ChildrensActivities"],
    "kid":                ["#ChildrensActivities"],
    "toddler":             ["#ChildrensActivities"],

    # ─── Religion & Spiritual ──────────────────────────────────────────
    "religion":            ["#Religion", "#Praying"],
    "religious":           ["#Religion", "#Praying"],
    "church":              ["#Churches", "#Praying", "#Religion"],
    "parish":              ["#Churches","#Praying","#Religion"],
    "jehovahs witness kingdom hall":["#Religion","#Praying"],
    "buddhist temple":      ["#BuddhistTemple","#Temples","#Praying","#Religion"],
    "gurudwara":            ["#Gurudwara","#Religion","#Praying"],
    "cathedral":           ["#Cathedrals","#Churches","#Praying","#Religion"],
    "shrine":              ["#Shrines", "#Praying", "#Religion"],
    "monastery":           ["#Monasteries", "#Religion", "#Praying"],
    "temple":              ["#Temples", "#Praying", "#Religion"],
    "ashram":              ["#Ashrams","#Religion","#Praying"],
    "mosque":              ["#Mosques", "#Praying", "#Religion"],
    "synagogue":           ["#Synagogues", "#Praying", "#Religion"],
    "basilica":            ["#Basilicas", "#Churches", "#Religion", "#Praying"],
    "chapel":              ["#Chapels", "#Religion", "#Praying"],
    "place of worship":    ["#Religion","#Praying"],

    # ─── Tea Experiences ────────────────────────────────────────────────
    "tea ceremony":        ["#TeaCeremony"],
    "tea house":           ["#TeaHouse"],
    "tea shop":            ["#Tea"],

    # ─── VR & Virtual ───────────────────────────────────────────────────
    "vr":                  ["#VR"],
    "virtual reality":     ["#VR"],

    # ─── Misc (unique finds) ────────────────────────────────────────────
    "science":             ["#Science"],

    # ─── Historic & Heritage ──────────────────────────────────────────────
    "historic site":       ["#HistoricSites", "#Heritage"],
    "historical site":     ["#HistoricSites", "#Heritage"],
    "historic landmark":   ["#HistoricSites", "#Heritage"],
    "historical landmark": ["#HistoricSites", "#Heritage"],
    "historical place":    ["#HistoricSites", "#Heritage"],
    "heritage":             ["#Heritage"],
    "heritage museum":     ["#Museums", "#Heritage"],
    "archaeological":       ["#Archaeology"],
}


# ─── Animal Keywords for Wildlife Detection ────────────────────────────────────
ANIMAL_KEYWORDS = [
    "lion", "tiger", "elephant", "zebra", "giraffe", "bear", "wolf", "fox",
    "bird", "eagle", "penguin", "cobra", "python",
    "antelope", "monkey", "kangaroo", "panda", "hippopotamus", "rhinoceros",
    "buffalo", "deer", "elk", "moose", "bison", "peacock",
    "flamingo", "parrot", "crow", "pigeon", "sparrow", "owl", "bat", "leopard",
    "cheetah", "snake", "alligator", "crocodile", "frog", "toad", "lizard",
    "gecko", "chameleon", "turtle", "butterfly", "bee", "ant", "spider",
    "scorpion", "cricket", "grasshopper", "duck", "goose", "swan", "turkey", "cow", "bull", "horse",
    "donkey", "mule", "sheep", "goat", "pig", "boar", "camel", "llama",
    "alpaca", "yak", "reindeer", "zebu","wildlife"
]   

# ─── Marine‐Life Keywords for Marine Detection ─────────────────────────────────
MARINE_KEYWORDS = [
    "whale", "dolphin", "shark", "octopus", "jellyfish", "crab", "lobster", "shrimp", "seal", "otter", "turtle",
    "fish", "stingray", "manta ray", "eel", "seaweed", "sea lion", "walrus", "porpoise", "narwhal", "manatee", "dugong",
    "marlin", "tuna", "salmon", "cod", "trout", "seahorse", "starfish", "sea urchin", "urchin",
    "squid", "cuttlefish", "krill", "plankton", "coral", "anemone", "barnacle",
    "oyster", "clam", "mussel", "scallop",
    "pufferfish", "lionfish",
    "penguin", "albatross", "pelican", "seagull", "cormorant",
    "sea cucumber","marinelife"
]

