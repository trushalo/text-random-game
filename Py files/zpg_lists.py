import random

# Character creation lists
first_names = ["John", "Jane", "David", "Mary", "James", "Robert", "Michael", "William", "Charles", "Joseph", "Thomas",
               "Christopher", "Daniel", "Paul", "Richard", "Mark", "Donald", "George", "Kenneth", "Steven", "Edward",
               "Brian", "Ronald", "Anthony", "Kevin", "Jason", "Jeffrey", "Frank", "Scott", "Eric", "Stephen", "Andrew",
               "Raymond", "Gregory", "Joshua", "Peter", "Dennis", "Walter", "Patrick", "Charles", "Eugene", "Roy",
               "Ralph", "Carl", "Noah", "Elijah", "Oliver", "William", "James", "Logan", "Benjamin", "Ethan", "Jacob",
               "Mason", "Michael", "Alexander", "David", "Daniel", "Matthew", "Aiden", "Anthony", "Joseph", "Joshua",
               "Christopher", "Andrew", "Christian", "Ethan", "Connor", "Liam", "Isaac", "Dylan", "Jackson", "Caleb",
               "Hunter", "Ryan", "Luke", "Aaron", "Landon", "Jayden", "Owen", "Gabriel", "Nathan", "Isaac", "Emma",
               "Olivia", "Sophia", "Isabella", "Ava", "Mia", "Emily", "Chloe", "Madison", "Charlotte", "Abigail",
               "Elizabeth", "Samantha", "Sofia", "Amelia", "Lily", "Grace", "Evelyn", "Chloe", "Ella", "Addison",
               "Aubrey", "Natalie", "Zoe", "Hannah", "Hailey", "Skylar", "Alyssa", "Victoria", "Ashley", "Brooklyn",
               "Avery", "Claire", "Kayla", "Sarah", "Madeline", "Allison", "Savannah", "Alexis", "Lauren", "Taylor",
               "Peyton", "Kennedy", "Allegri", "Gammi", "Stud", "Dash"]
last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez",
              "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson", "Thomas", "Taylor", "Moore", "Jackson", "Martin",
              "Lee", "Perez", "Thompson", "White", "Harris", "Sanchez", "Clark", "Lewis", "Robinson", "Walker", "Young",
              "Allen", "King", "Wright", "Scott", "Torres", "Nguyen", "Hill", "Flores", "Green", "Adams", "Nelson",
              "Baker", "Hall", "Hart", "Clark", "Lewis", "Robinson", "Walker", "Wright", "Scott", "Torres", "Hill",
              "Flores", "Green", "Adams", "Nelson", "Baker", "Hall", "Hart", "Beefpile", "Riprock"]
ship_names = ["The Wanderer", "The Zephyr", "The Valkyrie", "The Peregrine", "The Serpent's Fang", "The Crimson Dawn",
              "The Iron Hammer", "The Ghost Ship", "The Shadow Dancer", "The Celestial Hawk", "The Leviathan",
              "The Tempest", "The Aurora", "The Banshee", "The Kraken", "The Voidwalker", "The Nebula", "The Colossus",
              "The Endeavor", "The Pathfinder", "The Voyager", "The Intrepid", "The Excelsior", "The Phoenix",
              "The Raven", "The Seraph"]
job_list = [
    'Pilot', 'Engineer', 'Navigator', 'Cleaner', 'Wormhole specialist', 'Life support specialist', 'Systems engineer',
    'Electrician'
]

gender = ['he', 'she', 'they', 'ee', 'zir', 'en', 'ne']
gender_is = ['he', 'she', 'en', 'ne']
gender_are = ['they', 'ee', 'zir']
# set initial comment_list variable.
'''
1. Comment to display.
2. Mood effected.
3. Amount mood effected.'''
comment_list = [("Debating the merits of tinned food versus freeze-dried rations.", "sad", 1),
                ("Threaten the ship's AI to stop it from singing opera.", "angry", 1),
                ("Patching up a hole in the hull with something from the back of the fridge.", "sad", 1),
                ("Contemplating the existential crisis of being a glorified space janitor.", "sad", 1),
                ("Yell at pilot for being unreasonable.", "angry", +1),
                ("Go to the gym to burn some energy.", "angry", -2),
                ("Drunkenly sing an ode to tachyonic quantum wormhole instabilities.", "sad", -2),
                (f"Take NPC out drinking.", "sad", -3), ("Duct tape and hope.", "sad", 1),
                ("Convince the ship's AI to sing opera.", "reckless", -1),
                ("Replace a busted thruster with a potato.", "sad", -1),
                ("Meditate on the futility of existence.", "sad", 2),
                ("Hack the ship's vending machine for extra snacks.", "greedy", 1),
                ("Yell at the ship's AI for being slow.", "angry", 1),
                ("Write a heartfelt poem about the ship's rust.", "sad", 1),
                ("Share your lunch with the slime-molds inhabiting the galley.", "greedy", -1),
                ("Attempt a daring spacewalk to replace a faulty antenna.", "reckless", 2),
                (f"Start a karaoke competition with X and the AI; cheat by planting a Trojan.", "reckless", 2),
                (f"Perfecting maintenance by the proud tradition of shit built by the lowest bidder.", "reckless", -1)

                ]

quest_list = [

]
# mood lists index 0 comment, 1 emote, 2 emote int, 3 health, 4 wealth
chill_list = [("Read a classic novel in the ship's library", "angry", -2, 2, 0),
              ("Play a virtual reality game", "angry", random.randint(-3, 3), 0, 20),
              ("Take a zero-gravity yoga class", "angry", -2, 1, 15),
              ("Listen to ambient music in the observation deck", "angry", -1, 0, 0),
              ("Watch a movie in the private theater", "angry", 0, -1, 25),
              ("Play a strategy game on the ship's computer", "angry", 2, -2, 10),
              ("Engage in a philosophical debate with the ship's AI", "angry", 2, 1, 0),
              ("Train in the ship's gym", "angry", 3, 2, 15), (
              "Pilot the ship through a nebula because it's pretty. Spend 3 hours fixing the ship.", "angry", 5, -3,
              500)]
angry_list = [("Hack the enemy mainframe", "angry", 4, -2, 10),  # Focus and problem-solving can be cathartic
              ("Pilot the ship at dangerous speeds", "angry", 3, -3, 20),  # A risky thrill can relieve stress
              ("Overclock the engines", "angry", 2, -4, 30),  # Dangerous, but the adrenaline rush might help
              ("Engage in a heated debate with the AI", "angry", 1, -1, 0),
              # Arguing can be cathartic, but it's mentally taxing
              ("Try to meditate on the vastness of space", "angry", -2, 3, 0),  # A peaceful activity to calm the mind
              ("Tend to the ship's garden", "angry", -3, 5, 0),  # A grounding and nurturing activity
              ("Write poetry about the stars", "angry", -4, 4, 0),  # A creative outlet to express emotions
              ("Analyze alien artifacts", "angry", -5, 2, 0),  # A focused, intellectual pursuit can be calming
              ]
sad_list = [("Blast some questionable 2480s hair metal!", "sad", -2, -1, 0),  # A bit of headbanging might help, right?
            ("Meditate... in the engine room. It's *very* calming.", "sad", -1, 1, 0),  # Not exactly zen...
            ("Write a heartfelt poem about the ship's leaky hull.", "sad", 1, -1, 0),
            # Cathartic, but might worsen the mood.
            ("Attempt to bake a cake using emergency rations. Results may vary.", "sad", -3, random.randint(-3, 2), -5),
            # A sweet distraction, but costly.
            ("Have a philosophical debate with the ship's AI about the meaning of existence. /n Lose", "sad", 2, 0, 0),
            # Might spiral into existential dread.
            (
            "Engage in a high-stakes game of space poker. Winner takes all!", "sad", 5, 2, random.randint(-1000, 1000)),
            # A risky gamble, but could be fun.
            ("Build a tiny spaceship out of spare parts. It's surprisingly therapeutic!", "sad", -4, 1, -2),
            # A creative outlet, but requires resources.
            ("Scream into the void of space. Let it all out!", "sad", 3, -1, 0)
            # Cathartic, but might attract unwanted attention.
            ]
happy_list = [("Meditate in the ship's quiet room", "sad", 3, 5, 0),  # Calming and restorative.
              ("Argue with the AI about the best Star Trek series", "sad", -5, -2, 0),
              # A bit of fun, but can be frustrating.
              ("Conduct repairs while dancing a jig, curse that inconvenient bulkhead thoroughly", "sad", 4, -3, 10),
              # Frustrating but can be rewarding.
              ("Overanalyze the ship's sensor readings", "sad", 2, -2, 0),  # Can be tedious and anxiety-inducing.
              ("Attempt to grow plants in the hydroponics bay", "sad", -2, 3, 20),  # Calming and productive.
              ("Debate philosophical questions with the ship's AI", "sad", 1, -1, 0),
              # Stimulating but can lead to existential dread.
              ("Try to learn a new language using the ship's language learning program", "sad", 3, -1, 0),
              # Challenging but rewarding.
              ("Spend hours trying to figure out a complex puzzle in the ship's library", "sad", 4, -2, 0),
              # Engaging but can be frustrating.
              ("Watch old Earth movies with the crew", "sad", -1, 2, 0),  # Nostalgic and bonding.
              ("Try to write a poem or short story", "sad", 2, -1, 0),  # Creative but can be self-critical.
              ("Clean the ship's hydroponics bay", "sad", 1, 1, 0),  # Productive but mundane.
              ("Attempt to repair a damaged part of the ship's hull", "sad", 5, -4, 50),  # Dangerous and stressful.
              ("Hack into the ship's systems to see what secrets it's hiding", "sad", 5, -3, 0),  # Exciting but risky.
              ("Try to contact other civilizations using the ship's long-range communication system", "sad", 3, -2, 0),
              # Hopeful but uncertain.
              ("Spend hours staring out the viewport, pondering the meaning of existence", "sad", 2, -2, 0),
              # Philosophical but can be depressing.
              ]
# Adds ship's health at index[4]
reckless_list = [("Attempt a risky hyperspace jump to a nearby star system.", "reckless", 5, -10, 250, 100),
                 # High risk, high reward, potentially damaging to the ship
                 ("Modify the ship's AI without a backup.", "reckless", 3, -5, 100, 50),
                 # Could lead to unintended consequences
                 ("Experiment with alien technology without understanding it.", "reckless", 4, -8, 150, 75),
                 # High risk, potentially dangerous
                 ("Engage in an unauthorized space battle with a much larger ship.", "reckless", 5, -15, 0, 150),
                 # Suicidal and destructive
                 ("Ignore a distress signal from a known pirate faction.", "reckless", -2, 5, 0, 0),
                 # Could lead to future trouble
                 ("Disregard safety protocols during a repair mission.", "reckless", 3, -3, 50, 25),
                 # Risky, but necessary
                 ("Hack into a heavily fortified alien database.", "reckless", 4, -7, 200, 0),  # Illegal and dangerous
                 ("Attempt to steal valuable alien artifacts from a heavily guarded facility.", "reckless", 5, -10, 0,
                  100),  # High-risk theft
                 ("Ignore a warning from the ship's sensors about a potential hazard.", "reckless", 2, -2, 0, 50),
                 # Could lead to accidents
                 ("Overcharge the ship's engines to reach a distant destination faster.", "reckless", 3, -5, 100, 75),
                 #  Risky, but potentially rewarding
                 ("Use experimental weaponry on a live target.", "reckless", 4, -8, 200, 100),
                 #  Dangerous and unpredictable
                 ("Disobey direct orders from the captain during a crisis.", "reckless", 2, -3, 0, 25),
                 # Could lead to chaos and disaster
                 ("Attempt to bypass the ship's security system to access restricted areas.", "reckless", 3, -4, 50, 0),
                 # Could lead to accidents or data breaches
                 ]
careful_list = [("He/she/they carefully labeled all their food in the fridge", "reckless", 2, 0, 0),
                # This activity is very cautious with little to no risk but also unhealthy.
                ("He/she/they double-checked all the ship's systems before setting off", "reckless", 2, 0, 0),
                # Another cautious activity, ensuring safety.
                ("He/she/they spent an hour cleaning the bridge", "reckless", 1, 0, 0),
                # A relatively minor act of caution.
                ("He/she/they argued with the engineer about a minor repair", "reckless", -1, -5, 0),
                # A risky argument, potentially damaging relationships.
                ("He/she/they tried to hotwire a damaged reactor", "reckless", -3, -20, -100),
                # A very risky and potentially damaging action.
                ("He/she/they took a shortcut through an asteroid field", "reckless", -2, -10, -50),
                # A risky maneuver to save time.
                ("He/she/they ignored a warning sign and entered a restricted area", "reckless", -2, -5, 0),
                # A reckless disregard for safety.
                ("He/she/they stole supplies from the cargo bay", "reckless", -1, -5, 0),
                # A risky and unethical action.
                ("He/she/they experimented with a new, untested propulsion system", "reckless", -3, -20, -150),
                # A highly risky and potentially destructive action.
                ("He/she/they challenged the captain to a duel", "reckless", -2, -10, 0),
                # A reckless and impulsive action.
                ]
greedy_list = [("He/she/they hoarded all the rations for himself/herself/themselves.", "greedy", 5, -1, 100),
               # Extremely selfish, improves mood, gains resources
               ("He/she/they sabotaged the ship's engine for personal gain.", "greedy", 4, -5, -100),
               # Very selfish, damages ship, hurts self
               ("He/she/they stole supplies from the cargo hold.", "greedy", 3, -2, 50),
               # Moderately selfish, gains resources, slight self-harm
               ("He/she/they refused to help with repairs, citing personal reasons.", "greedy", 2, -1, 0),
               # Slightly selfish, no direct gain or loss
               ("He/she/they shared a personal item with a crewmate.", "greedy", -1, 2, -5),
               # Generous, improves relationships, small cost
               ("He/she/they risked their life to save a crewmate.", "greedy", -3, 5, -100),
               # Very generous, greatly improves relationships, high risk
               ("He/she/they gave up their favorite snack to a hungry crewmate.", "greedy", -2, 1, -5),
               # Generous, improves relationships, small cost
               ("He/she/they volunteered for a dangerous mission.", "greedy", -2, 3, -150),
               # Generous, greatly improves reputation, high risk
               ("He/she/they spent personal time comforting a distressed crewmate.", "greedy", -1, 2, 0),
               # Generous, improves relationships, no cost
               ("He/she/they offered a kind word of encouragement to a fellow crewmate.", "greedy", -1, 1, 0)
               # Slightly generous, improves morale, no cost

               ]
# Greedy and philanthropy are currently the same.
philanthropy_list = [("He/she/they hoarded all the rations for himself/herself/themselves.", "greedy", 5, -1, 100),
                     # Extremely selfish, improves mood, gains resources
                     ("He/she/they sabotaged the ship's engine for personal gain.", "greedy", 4, -5, -100),
                     # Very selfish, damages ship, hurts self
                     ("He/she/they stole supplies from the cargo hold.", "greedy", 3, -2, 50),
                     # Moderately selfish, gains resources, slight self-harm
                     ("He/she/they refused to help with repairs, citing personal reasons.", "greedy", 2, -1, 0),
                     # Slightly selfish, no direct gain or loss
                     ("He/she/they shared a personal item with a crewmate.", "greedy", -1, 2, -5),
                     # Generous, improves relationships, small cost
                     ("He/she/they risked their life to save a crewmate.", "greedy", -3, 5, -100),
                     # Very generous, greatly improves relationships, high risk
                     ("He/she/they gave up their favorite snack to a hungry crewmate.", "greedy", -2, 1, -5),
                     # Generous, improves relationships, small cost
                     ("He/she/they volunteered for a dangerous mission.", "greedy", -2, 3, -150),
                     # Generous, greatly improves reputation, high risk
                     ("He/she/they spent personal time comforting a distressed crewmate.", "greedy", -1, 2, 0),
                     # Generous, improves relationships, no cost
                     ("He/she/they offered a kind word of encouragement to a fellow crewmate.", "greedy", -1, 1, 0)
                     # Slightly generous, improves morale, no cost
                     ]
