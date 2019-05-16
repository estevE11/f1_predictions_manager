from gspread_formatting import *

color_right = Color(0, 1, 0)
color_wrong = Color(1, .5, 0)

constructors_color = {"mercedes":Color(.2, .6, 1),
                    "ferrari":Color(1, 0, 0),
                    "redbull":Color(0, 0, 1),
                    "mclaren":Color(1, .7, 0),
                    "renault":Color(1, 1, 0),
                    "alfa":Color(.7, .3, .3),
                    "racing_point":Color(1, 0, 1),
                    "toro_rosso":Color(0, .5, .5),
                    "williams":Color(1, 1, 1),
                    "haas":Color(.6, .6, .6),
                }


constructors_name = {"mercedes":"Mercedes",
                    "ferrari":"Ferrari",
                    "redbull":"RedBull",
                    "mclaren":"McLaren",
                    "renault":"Renault",
                    "alfa":"Alfa Romeo",
                    "racing_point":"Racing Point",
                    "toro_rosso":"Toro Rosso",
                    "williams":"Williams",
                    "haas":"Haas",
                }

drivers_color = {
                    "bottas":[Color(.7, .8, .8), Color(0, 0, 0)],
                    "hamilton":[Color(.7, .8, .8), Color(0, 0, 0)],
                    "max_verstappen":[Color(0, 0, 1), Color(1, 1, 1)],
                    "gasly":[Color(0, 0, 1), Color(1, 1, 1)],
                    "vettel":[Color(1, 0, 0), Color(1, 1, 1)],
                    "leclerc":[Color(1, 0, 0), Color(1, 1, 1)],
                    "sainz":[Color(1, .7, 0), Color(0, 0, 0)],
                    "norris":[Color(1, .7, 0), Color(0, 0, 0)],
                    "hulkenberg":[Color(1, 1, 0), Color(0, 0, 0)],
                    "ricciardo":[Color(1, 1, 0), Color(0, 0, 0)],
                    "raikkonen":[Color(.7, .3, .3), Color(1, 1, 1)],
                    "giovinazzi":[Color(.7, .3, .3), Color(1, 1, 1)],
                    "perez":[Color(1, 0, 1), Color(0, 0, 0)],
                    "stroll":[Color(1, 0, 1), Color(0, 0, 0)],
                    "kvyat":[Color(0, .5, .5), Color(1, 1, 1)],
                    "albon":[Color(0, .5, .5), Color(1, 1, 1)],
                    "russell":[Color(1, 1, 1), Color(0, 0, 0)],
                    "kubica":[Color(1, 1, 1), Color(0, 0, 0)],
                    "grosjean":[Color(.6, .6, .6), Color(0, 0, 0)],
                    "kevin_magnussen":[Color(.6, .6, .6), Color(0, 0, 0)]
                }

drivers_name = {
                    "bottas":"Bottas",
                    "hamilton":"Hamilton",
                    "max_verstappen":"Verstappen",
                    "gasly":"Gasly",
                    "vettel":"Vettel",
                    "leclerc":"Leclerc",
                    "sainz":"Sainz",
                    "norris":"Norris",
                    "hulkenberg":"Hulkenberg",
                    "ricciardo":"Ricciardo",
                    "raikkonen":"Raikkonen",
                    "giovinazzi":"Giovinazzi",
                    "perez":"Perez",
                    "stroll":"Stroll",
                    "kvyat":"Kvyat",
                    "albon":"Albon",
                    "russell":"Russell",
                    "kubica":"Kubica",
                    "grosjean":"Grosjean",
                    "kevin_magnussen":"Magnussen",
                }
