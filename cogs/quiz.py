active_quiz = {}

questions = [

    {
        "question": "What is the largest planet in our Solar System?",
        "options": "A - Earth\nB - Mars\nC - Jupiter\nD - Saturn",
        "answer": "C"
    },
    {
        "question": "Who won the 2018 FIFA World Cup?",
        "options": "A - Germany\nB - France\nC - Brazil\nD - Argentina",
        "answer": "B"
    },
    {
        "question": "What is the capital of Japan?",
        "options": "A - Seoul\nB - Beijing\nC - Tokyo\nD - Bangkok",
        "answer": "C"
    },
    {
        "question": "Which game features the character Master Chief?",
        "options": "A - Halo\nB - Doom\nC - Destiny\nD - Mass Effect",
        "answer": "A"
    },
    {
        "question": "How many players are on the field for one football team at the start of a match?",
        "options": "A - 9\nB - 10\nC - 11\nD - 12",
        "answer": "C"
    },
    {
        "question": "Which animal is known as the fastest land animal?",
        "options": "A - Lion\nB - Cheetah\nC - Horse\nD - Leopard",
        "answer": "B"
    },
    {
        "question": "Who painted the Mona Lisa?",
        "options": "A - Vincent van Gogh\nB - Pablo Picasso\nC - Leonardo da Vinci\nD - Michelangelo",
        "answer": "C"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": "A - Venus\nB - Mars\nC - Mercury\nD - Neptune",
        "answer": "B"
    },
    {
        "question": "What is the main currency of the United Kingdom?",
        "options": "A - Euro\nB - Dollar\nC - Pound Sterling\nD - Franc",
        "answer": "C"
    },
    {
        "question": "Which company created the PlayStation?",
        "options": "A - Microsoft\nB - Nintendo\nC - Sega\nD - Sony",
        "answer": "D"
    },

    {
        "question": "What is the smallest prime number?",
        "options": "A - 0\nB - 1\nC - 2\nD - 3",
        "answer": "C"
    },
    {
        "question": "Which country is famous for the Great Wall?",
        "options": "A - Japan\nB - China\nC - India\nD - Thailand",
        "answer": "B"
    },
    {
        "question": "What is the chemical symbol for gold?",
        "options": "A - Ag\nB - Go\nC - Gd\nD - Au",
        "answer": "D"
    },
    {
        "question": "Which football club is known as 'The Red Devils'?",
        "options": "A - Liverpool\nB - Arsenal\nC - Manchester United\nD - Chelsea",
        "answer": "C"
    },
    {
        "question": "How many sides does a hexagon have?",
        "options": "A - 5\nB - 6\nC - 7\nD - 8",
        "answer": "B"
    },
    {
        "question": "Which ocean is the largest?",
        "options": "A - Atlantic Ocean\nB - Indian Ocean\nC - Arctic Ocean\nD - Pacific Ocean",
        "answer": "D"
    },
    {
        "question": "What is the name of Mario's brother?",
        "options": "A - Luigi\nB - Wario\nC - Yoshi\nD - Toad",
        "answer": "A"
    },
    {
        "question": "Which gas do humans need to breathe?",
        "options": "A - Carbon dioxide\nB - Oxygen\nC - Hydrogen\nD - Helium",
        "answer": "B"
    },
    {
        "question": "Who was the first person to walk on the Moon?",
        "options": "A - Buzz Aldrin\nB - Yuri Gagarin\nC - Neil Armstrong\nD - Michael Collins",
        "answer": "C"
    },
    {
        "question": "Which country invented pizza as we know it today?",
        "options": "A - Spain\nB - Italy\nC - France\nD - Greece",
        "answer": "B"
    },

    {
        "question": "What is the hardest natural substance on Earth?",
        "options": "A - Iron\nB - Diamond\nC - Quartz\nD - Titanium",
        "answer": "B"
    },
    {
        "question": "Which animal can sleep while standing up?",
        "options": "A - Horse\nB - Dog\nC - Penguin\nD - Dolphin",
        "answer": "A"
    },
    {
        "question": "Which movie features the character Jack Sparrow?",
        "options": "A - The Mummy\nB - Pirates of the Caribbean\nC - Indiana Jones\nD - Gladiator",
        "answer": "B"
    },
    {
        "question": "What is the capital of Australia?",
        "options": "A - Sydney\nB - Melbourne\nC - Canberra\nD - Brisbane",
        "answer": "C"
    },
    {
        "question": "Which instrument has black and white keys?",
        "options": "A - Guitar\nB - Piano\nC - Violin\nD - Trumpet",
        "answer": "B"
    },
    {
        "question": "How many continents are there?",
        "options": "A - 5\nB - 6\nC - 7\nD - 8",
        "answer": "C"
    },
    {
        "question": "Which company developed Minecraft?",
        "options": "A - Valve\nB - Mojang\nC - Blizzard\nD - Ubisoft",
        "answer": "B"
    },
    {
        "question": "What is the largest mammal in the world?",
        "options": "A - African Elephant\nB - Giraffe\nC - Blue Whale\nD - Orca",
        "answer": "C"
    },
    {
        "question": "Which country has the most islands in the world?",
        "options": "A - Indonesia\nB - Sweden\nC - Philippines\nD - Japan",
        "answer": "B"
    },
    {
        "question": "What does CPU stand for?",
        "options": "A - Central Processing Unit\nB - Computer Personal Unit\nC - Central Power Utility\nD - Computer Processing Utility",
        "answer": "A"
    },

    {
        "question": "Which football player is famous for the 'Siuuu' celebration?",
        "options": "A - Lionel Messi\nB - Neymar\nC - Cristiano Ronaldo\nD - Kylian Mbappé",
        "answer": "C"
    },
    {
        "question": "What is the boiling point of water at sea level?",
        "options": "A - 50°C\nB - 75°C\nC - 100°C\nD - 125°C",
        "answer": "C"
    },
    {
        "question": "Which planet has the most prominent ring system?",
        "options": "A - Mars\nB - Saturn\nC - Venus\nD - Earth",
        "answer": "B"
    },
    {
        "question": "Which superhero is also known as Bruce Wayne?",
        "options": "A - Superman\nB - Iron Man\nC - Batman\nD - Spider-Man",
        "answer": "C"
    },
    {
        "question": "Which country is shaped like a boot?",
        "options": "A - Italy\nB - Portugal\nC - Chile\nD - Greece",
        "answer": "A"
    },
    {
        "question": "What is the largest organ of the human body?",
        "options": "A - Heart\nB - Liver\nC - Skin\nD - Brain",
        "answer": "C"
    },
    {
        "question": "Which game series features the character Link?",
        "options": "A - Final Fantasy\nB - The Legend of Zelda\nC - Pokémon\nD - Metroid",
        "answer": "B"
    },
    {
        "question": "Which metal is liquid at room temperature?",
        "options": "A - Mercury\nB - Copper\nC - Silver\nD - Aluminum",
        "answer": "A"
    },
    {
        "question": "What is the capital of Canada?",
        "options": "A - Toronto\nB - Vancouver\nC - Montreal\nD - Ottawa",
        "answer": "D"
    },
    {
        "question": "Which singer released the album 'Thriller'?",
        "options": "A - Elvis Presley\nB - Michael Jackson\nC - Prince\nD - David Bowie",
        "answer": "B"
    },

    {
        "question": "What is the largest desert in the world?",
        "options": "A - Sahara\nB - Gobi\nC - Antarctic Desert\nD - Arabian Desert",
        "answer": "C"
    },
    {
        "question": "Which animal is known for changing its color?",
        "options": "A - Chameleon\nB - Tiger\nC - Elephant\nD - Kangaroo",
        "answer": "A"
    },
    {
        "question": "Which company created Windows?",
        "options": "A - Apple\nB - Google\nC - Microsoft\nD - IBM",
        "answer": "C"
    },
    {
        "question": "What is the name of Earth's natural satellite?",
        "options": "A - Mars\nB - Luna\nC - Moon\nD - Titan",
        "answer": "C"
    },
    {
        "question": "Which sport uses a shuttlecock?",
        "options": "A - Tennis\nB - Badminton\nC - Squash\nD - Volleyball",
        "answer": "B"
    },
    {
        "question": "How many colors are traditionally found in a rainbow?",
        "options": "A - 5\nB - 6\nC - 7\nD - 8",
        "answer": "C"
    },
    {
        "question": "Which Pokémon is number 25 in the original Pokédex?",
        "options": "A - Pikachu\nB - Charmander\nC - Bulbasaur\nD - Squirtle",
        "answer": "A"
    },
    {
        "question": "Which country is home to the pyramids of Giza?",
        "options": "A - Mexico\nB - Egypt\nC - Peru\nD - Jordan",
        "answer": "B"
    },
    {
        "question": "What is the freezing point of water?",
        "options": "A - 0°C\nB - 10°C\nC - -10°C\nD - 5°C",
        "answer": "A"
    },
    {
        "question": "Which bird is often associated with delivering messages in history?",
        "options": "A - Eagle\nB - Raven\nC - Pigeon\nD - Falcon",
        "answer": "C"
    },

    {
        "question": "Which football club plays at Anfield?",
        "options": "A - Everton\nB - Liverpool\nC - Manchester City\nD - Arsenal",
        "answer": "B"
    },
    {
        "question": "What is the capital of Portugal?",
        "options": "A - Porto\nB - Coimbra\nC - Faro\nD - Lisbon",
        "answer": "D"
    },
    {
        "question": "Which famous detective lives at 221B Baker Street?",
        "options": "A - Hercule Poirot\nB - Sherlock Holmes\nC - Batman\nD - Inspector Gadget",
        "answer": "B"
    },
    {
        "question": "Which element has the chemical symbol O?",
        "options": "A - Gold\nB - Oxygen\nC - Osmium\nD - Iron",
        "answer": "B"
    },
    {
        "question": "Which game company created the Mario franchise?",
        "options": "A - Sega\nB - Nintendo\nC - Sony\nD - Capcom",
        "answer": "B"
    },
    {
        "question": "Which country is famous for the Eiffel Tower?",
        "options": "A - Italy\nB - Germany\nC - France\nD - Belgium",
        "answer": "C"
    },
    {
        "question": "What is the fastest bird in the world when diving?",
        "options": "A - Eagle\nB - Peregrine Falcon\nC - Hawk\nD - Owl",
        "answer": "B"
    },
    {
        "question": "Which movie features a character named Darth Vader?",
        "options": "A - Star Wars\nB - Star Trek\nC - Avatar\nD - Dune",
        "answer": "A"
    },
    {
        "question": "What is 12 × 12?",
        "options": "A - 124\nB - 132\nC - 144\nD - 154",
        "answer": "C"
    },
    {
        "question": "Which planet is closest to the Sun?",
        "options": "A - Venus\nB - Mercury\nC - Earth\nD - Mars",
        "answer": "B"
    },

    {
        "question": "Which country won the first FIFA World Cup in 1930?",
        "options": "A - Brazil\nB - Argentina\nC - Uruguay\nD - Italy",
        "answer": "C"
    },
    {
        "question": "What is the tallest animal in the world?",
        "options": "A - Elephant\nB - Giraffe\nC - Camel\nD - Horse",
        "answer": "B"
    },
    {
        "question": "Which programming language is commonly represented by the snake logo?",
        "options": "A - Java\nB - C++\nC - Python\nD - Ruby",
        "answer": "C"
    },
    {
        "question": "Which country is home to the city of Barcelona?",
        "options": "A - Portugal\nB - Spain\nC - Italy\nD - France",
        "answer": "B"
    },
    {
        "question": "Which superhero uses a hammer called Mjölnir?",
        "options": "A - Thor\nB - Hulk\nC - Captain America\nD - Wolverine",
        "answer": "A"
    },
    {
        "question": "What is the smallest country in the world?",
        "options": "A - Monaco\nB - Vatican City\nC - San Marino\nD - Liechtenstein",
        "answer": "B"
    },
    {
        "question": "Which sport is associated with Wimbledon?",
        "options": "A - Golf\nB - Tennis\nC - Cricket\nD - Rugby",
        "answer": "B"
    },
    {
        "question": "What type of animal is a Komodo dragon?",
        "options": "A - Snake\nB - Lizard\nC - Crocodile\nD - Turtle",
        "answer": "B"
    },
    {
        "question": "Which company owns Instagram?",
        "options": "A - Google\nB - Apple\nC - Meta\nD - Amazon",
        "answer": "C"
    },
    {
        "question": "Which ancient civilization built Machu Picchu?",
        "options": "A - Romans\nB - Greeks\nC - Incas\nD - Vikings",
        "answer": "C"
    },

    {
        "question": "Which is the longest river in South America?",
        "options": "A - Amazon River\nB - Nile River\nC - Mississippi River\nD - Yangtze River",
        "answer": "A"
    },
    {
        "question": "What is the name of the cowboy character in Toy Story?",
        "options": "A - Buzz\nB - Woody\nC - Andy\nD - Rex",
        "answer": "B"
    },
    {
        "question": "Which country is famous for the Taj Mahal?",
        "options": "A - India\nB - Pakistan\nC - Nepal\nD - Bangladesh",
        "answer": "A"
    },
    {
        "question": "How many hearts does an octopus have?",
        "options": "A - 1\nB - 2\nC - 3\nD - 4",
        "answer": "C"
    },
    {
        "question": "Which football player is nicknamed 'The King'?",
        "options": "A - Pelé\nB - Maradona\nC - Zidane\nD - Ronaldinho",
        "answer": "A"
    },
    {
        "question": "Which game features the map 'Summoner's Rift'?",
        "options": "A - Valorant\nB - League of Legends\nC - Overwatch\nD - Dota 2",
        "answer": "B"
    },
    {
        "question": "What is the largest bone in the human body?",
        "options": "A - Skull\nB - Femur\nC - Humerus\nD - Tibia",
        "answer": "B"
    },
    {
        "question": "Which country gave the Statue of Liberty to the United States?",
        "options": "A - Spain\nB - France\nC - Germany\nD - Italy",
        "answer": "B"
    },
    {
        "question": "What does 'www' stand for in a website address?",
        "options": "A - World Wide Web\nB - World Web Window\nC - Web World Wide\nD - Wide World Website",
        "answer": "A"
    },
    {
        "question": "Which animal is the largest land animal?",
        "options": "A - Rhino\nB - Hippopotamus\nC - African Elephant\nD - Giraffe",
        "answer": "C"
    },

    {
        "question": "Which country has the city of New York?",
        "options": "A - Canada\nB - United States\nC - United Kingdom\nD - Australia",
        "answer": "B"
    },
    {
        "question": "Which instrument does a drummer play?",
        "options": "A - Drums\nB - Piano\nC - Guitar\nD - Saxophone",
        "answer": "A"
    },
    {
        "question": "Which planet is famous for its Great Red Spot?",
        "options": "A - Jupiter\nB - Saturn\nC - Neptune\nD - Uranus",
        "answer": "A"
    },
    {
        "question": "What is the currency of Japan?",
        "options": "A - Won\nB - Yuan\nC - Yen\nD - Ringgit",
        "answer": "C"
    },
    {
        "question": "Which movie franchise features the character John Wick?",
        "options": "A - Mission Impossible\nB - John Wick\nC - Die Hard\nD - Taken",
        "answer": "B"
    },
    {
        "question": "How many legs does a spider have?",
        "options": "A - 6\nB - 8\nC - 10\nD - 12",
        "answer": "B"
    },
    {
        "question": "Which country is famous for the ancient city of Rome?",
        "options": "A - Greece\nB - Spain\nC - Italy\nD - Turkey",
        "answer": "C"
    },
    {
        "question": "What is the largest ocean animal?",
        "options": "A - Great White Shark\nB - Blue Whale\nC - Giant Squid\nD - Orca",
        "answer": "B"
    },
    {
        "question": "Which video game series features Geralt of Rivia?",
        "options": "A - Skyrim\nB - The Witcher\nC - Dark Souls\nD - Dragon Age",
        "answer": "B"
    },
    {
        "question": "Which famous scientist developed the theory of relativity?",
        "options": "A - Isaac Newton\nB - Albert Einstein\nC - Galileo Galilei\nD - Nikola Tesla",
        "answer": "B"
    },

    {
        "question": "Which country is known as the Land of the Rising Sun?",
        "options": "A - China\nB - South Korea\nC - Japan\nD - Thailand",
        "answer": "C"
    },
    {
        "question": "What is the main ingredient in guacamole?",
        "options": "A - Tomato\nB - Avocado\nC - Potato\nD - Cucumber",
        "answer": "B"
    },
    {
        "question": "Which football competition is played between European national teams?",
        "options": "A - Copa América\nB - UEFA European Championship\nC - AFC Asian Cup\nD - Africa Cup of Nations",
        "answer": "B"
    },
    {
        "question": "Which animal is famous for having a pouch for its young?",
        "options": "A - Kangaroo\nB - Tiger\nC - Panda\nD - Gorilla",
        "answer": "A"
    },
    {
        "question": "Which company developed the Xbox?",
        "options": "A - Sony\nB - Nintendo\nC - Microsoft\nD - Sega",
        "answer": "C"
    },
    {
        "question": "Which is the largest country by land area?",
        "options": "A - Canada\nB - China\nC - United States\nD - Russia",
        "answer": "D"
    },
    {
        "question": "How many minutes are there in one hour?",
        "options": "A - 30\nB - 45\nC - 60\nD - 90",
        "answer": "C"
    },
    {
        "question": "Which animal is known for its black and white stripes?",
        "options": "A - Zebra\nB - Panda\nC - Skunk\nD - Penguin",
        "answer": "A"
    },
    {
        "question": "Which fictional character lives in a pineapple under the sea?",
        "options": "A - Patrick Star\nB - SpongeBob SquarePants\nC - Nemo\nD - Aquaman",
        "answer": "B"
    },
    {
        "question": "What is the name of the galaxy containing our Solar System?",
        "options": "A - Andromeda\nB - Milky Way\nC - Whirlpool\nD - Sombrero",
        "answer": "B"
    }
]