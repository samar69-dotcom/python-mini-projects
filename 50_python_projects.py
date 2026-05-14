# ============================================================
# 50 PYTHON PROJECTS FOR GITHUB PORTFOLIO
# Author: Samar | github.com/yourprofile
# Run any section individually or browse as a reference
# ============================================================

# ── PROJECT 1: Mood Journal ──────────────────────────────────
# Saves daily mood entries with timestamps to a text file.
def mood_journal():
    import datetime
    mood = input("How are you feeling today? ")
    note = input("Any thoughts? ")
    entry = f"[{datetime.date.today()}] Mood: {mood} | Note: {note}\n"
    with open("mood_log.txt", "a") as f:
        f.write(entry)
    print("Entry saved!")

# mood_journal()


# ── PROJECT 2: Random Quote of the Day ──────────────────────
def quote_of_the_day():
    import random
    quotes = [
        "Push yourself, because no one else is going to do it for you.",
        "Great things never come from comfort zones.",
        "Dream it. Wish it. Do it.",
        "Success doesn't just find you. You have to go out and get it.",
        "The harder you work, the luckier you get.",
    ]
    print("💬 Quote of the Day:", random.choice(quotes))

# quote_of_the_day()


# ── PROJECT 3: Countdown Timer ───────────────────────────────
def countdown_timer():
    import time
    seconds = int(input("Set timer for how many seconds? "))
    for i in range(seconds, 0, -1):
        print(f"\r⏳ {i} seconds remaining...", end="")
        time.sleep(1)
    print("\n🔔 Time's up!")

# countdown_timer()


# ── PROJECT 4: Word Frequency Counter ───────────────────────
def word_frequency():
    text = input("Paste your text: ")
    words = text.lower().split()
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    print("\nTop words:")
    for word, count in sorted_freq[:10]:
        print(f"  {word}: {count}")

# word_frequency()


# ── PROJECT 5: Expense Tracker ───────────────────────────────
def expense_tracker():
    expenses = []
    while True:
        item = input("Item (or 'done'): ")
        if item == "done":
            break
        amount = float(input(f"Cost of {item}: ₹"))
        expenses.append((item, amount))
    total = sum(a for _, a in expenses)
    print("\n📊 Expense Summary:")
    for item, amount in expenses:
        print(f"  {item}: ₹{amount:.2f}")
    print(f"  TOTAL: ₹{total:.2f}")

# expense_tracker()


# ── PROJECT 6: Password Generator ───────────────────────────
def password_generator():
    import random, string
    length = int(input("Password length (e.g. 12): "))
    chars = string.ascii_letters + string.digits + "!@#$%^&*()"
    password = "".join(random.choices(chars, k=length))
    print(f"🔐 Your password: {password}")

# password_generator()


# ── PROJECT 7: BMI Calculator ────────────────────────────────
def bmi_calculator():
    weight = float(input("Weight in kg: "))
    height = float(input("Height in meters (e.g. 1.75): "))
    bmi = weight / (height ** 2)
    category = (
        "Underweight" if bmi < 18.5 else
        "Normal" if bmi < 25 else
        "Overweight" if bmi < 30 else
        "Obese"
    )
    print(f"📏 BMI: {bmi:.2f} — {category}")

# bmi_calculator()


# ── PROJECT 8: Habit Streak Tracker ─────────────────────────
def habit_streak():
    import datetime
    habit = input("Habit name: ")
    with open(f"{habit}_streak.txt", "a") as f:
        f.write(str(datetime.date.today()) + "\n")
    with open(f"{habit}_streak.txt") as f:
        days = f.readlines()
    print(f"🔥 You've tracked '{habit}' for {len(days)} day(s)!")

# habit_streak()


# ── PROJECT 9: Coin Flip Simulator ───────────────────────────
def coin_flip():
    import random
    flips = int(input("How many times to flip? "))
    results = [random.choice(["Heads", "Tails"]) for _ in range(flips)]
    heads = results.count("Heads")
    print(f"🪙 Heads: {heads} | Tails: {flips - heads}")

# coin_flip()


# ── PROJECT 10: Number Guessing Game ─────────────────────────
def number_guessing():
    import random
    secret = random.randint(1, 100)
    attempts = 0
    print("Guess a number between 1 and 100!")
    while True:
        guess = int(input("Your guess: "))
        attempts += 1
        if guess < secret:
            print("Too low!")
        elif guess > secret:
            print("Too high!")
        else:
            print(f"🎉 Correct in {attempts} attempts!")
            break

# number_guessing()


# ── PROJECT 11: To-Do List with File Save ────────────────────
def todo_list():
    tasks = []
    while True:
        action = input("add/done/list/quit: ").strip().lower()
        if action == "add":
            tasks.append(input("Task: "))
        elif action == "list":
            for i, t in enumerate(tasks, 1):
                print(f"  {i}. {t}")
        elif action == "done":
            idx = int(input("Task number done: ")) - 1
            print(f"✅ Completed: {tasks.pop(idx)}")
        elif action == "quit":
            with open("todos.txt", "w") as f:
                f.write("\n".join(tasks))
            print("Saved!")
            break

# todo_list()


# ── PROJECT 12: Text Encrypt/Decrypt (Caesar Cipher) ─────────
def caesar_cipher():
    text = input("Text: ")
    shift = int(input("Shift (e.g. 3): "))
    mode = input("Encrypt or Decrypt? (e/d): ")
    if mode == "d":
        shift = -shift
    result = ""
    for ch in text:
        if ch.isalpha():
            base = ord("A") if ch.isupper() else ord("a")
            result += chr((ord(ch) - base + shift) % 26 + base)
        else:
            result += ch
    print(f"Result: {result}")

# caesar_cipher()


# ── PROJECT 13: Daily Affirmation Sender ─────────────────────
def affirmations():
    import random
    lines = [
        "You are capable of amazing things.",
        "Every day is a fresh start.",
        "You are enough, always.",
        "Keep going. You're doing better than you think.",
        "Your potential is limitless.",
    ]
    print("✨ Affirmation:", random.choice(lines))

# affirmations()


# ── PROJECT 14: Age Calculator ───────────────────────────────
def age_calculator():
    import datetime
    dob = input("Date of birth (YYYY-MM-DD): ")
    born = datetime.datetime.strptime(dob, "%Y-%m-%d").date()
    today = datetime.date.today()
    age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
    print(f"🎂 You are {age} years old!")

# age_calculator()


# ── PROJECT 15: Simple Chatbot (Rule-based) ──────────────────
def simple_chatbot():
    responses = {
        "hi": "Hey! How are you?",
        "how are you": "I'm just code, but I'm doing great!",
        "bye": "Goodbye! Have a great day!",
        "help": "I can chat with you. Try: hi, how are you, bye",
    }
    print("ChatBot ready. Type 'bye' to exit.")
    while True:
        user = input("You: ").lower().strip()
        print("Bot:", responses.get(user, "I don't understand that yet!"))
        if user == "bye":
            break

# simple_chatbot()


# ── PROJECT 16: Dice Roller ──────────────────────────────────
def dice_roller():
    import random
    sides = int(input("Dice sides (e.g. 6): "))
    rolls = int(input("Number of dice: "))
    results = [random.randint(1, sides) for _ in range(rolls)]
    print(f"🎲 Rolls: {results} | Total: {sum(results)}")

# dice_roller()


# ── PROJECT 17: Instagram Caption Idea Generator ─────────────
def caption_generator():
    import random
    topic = input("What's your post about? (e.g. mindset): ")
    templates = [
        f"The secret to {topic}? Start before you're ready. 🔥",
        f"Every day is a chance to improve your {topic}. 💪",
        f"Small steps toward {topic} every day = massive results. 🚀",
        f"Your {topic} journey is yours alone. Own it. ✨",
        f"They said {topic} was hard. They were right. Do it anyway. 😤",
    ]
    print("\n📸 Caption Idea:\n" + random.choice(templates))

# caption_generator()


# ── PROJECT 18: Typing Speed Test ────────────────────────────
def typing_speed():
    import time
    sentence = "The quick brown fox jumps over the lazy dog"
    print(f"Type this:\n{sentence}")
    input("Press Enter to start...")
    start = time.time()
    typed = input()
    elapsed = time.time() - start
    words = len(sentence.split())
    wpm = (words / elapsed) * 60
    accuracy = sum(a == b for a, b in zip(typed, sentence)) / len(sentence) * 100
    print(f"⌨️  Speed: {wpm:.1f} WPM | Accuracy: {accuracy:.1f}%")

# typing_speed()


# ── PROJECT 19: Bill Splitter ────────────────────────────────
def bill_splitter():
    total = float(input("Total bill amount: ₹"))
    people = int(input("Number of people: "))
    tip_pct = float(input("Tip %: "))
    tip = total * tip_pct / 100
    grand = total + tip
    per_person = grand / people
    print(f"💰 Each person pays: ₹{per_person:.2f} (includes tip)")

# bill_splitter()


# ── PROJECT 20: Palindrome Checker ───────────────────────────
def palindrome_checker():
    word = input("Enter a word or phrase: ").replace(" ", "").lower()
    if word == word[::-1]:
        print("✅ It's a palindrome!")
    else:
        print("❌ Not a palindrome.")

# palindrome_checker()


# ── PROJECT 21: Rock Paper Scissors ──────────────────────────
def rock_paper_scissors():
    import random
    choices = ["rock", "paper", "scissors"]
    wins = {"rock": "scissors", "paper": "rock", "scissors": "paper"}
    user = input("rock / paper / scissors: ").lower()
    comp = random.choice(choices)
    print(f"Computer chose: {comp}")
    if user == comp:
        print("It's a tie!")
    elif wins[user] == comp:
        print("🏆 You win!")
    else:
        print("💀 You lose!")

# rock_paper_scissors()


# ── PROJECT 22: Anagram Checker ──────────────────────────────
def anagram_checker():
    w1 = input("Word 1: ").lower().replace(" ", "")
    w2 = input("Word 2: ").lower().replace(" ", "")
    if sorted(w1) == sorted(w2):
        print("✅ They are anagrams!")
    else:
        print("❌ Not anagrams.")

# anagram_checker()


# ── PROJECT 23: Temperature Converter ────────────────────────
def temp_converter():
    temp = float(input("Temperature value: "))
    unit = input("Convert from (C/F/K): ").upper()
    if unit == "C":
        print(f"→ {temp * 9/5 + 32:.2f}°F | {temp + 273.15:.2f}K")
    elif unit == "F":
        c = (temp - 32) * 5/9
        print(f"→ {c:.2f}°C | {c + 273.15:.2f}K")
    elif unit == "K":
        c = temp - 273.15
        print(f"→ {c:.2f}°C | {c * 9/5 + 32:.2f}°F")

# temp_converter()


# ── PROJECT 24: Story Generator ──────────────────────────────
def story_generator():
    import random
    name = input("Hero's name: ")
    place = input("A place: ")
    item = input("A magical item: ")
    villain = input("A villain: ")
    endings = ["won the battle and became a legend.",
               "outsmarted the enemy using wit alone.",
               "discovered the true power was within all along."]
    story = (
        f"Once upon a time, {name} traveled to {place}. "
        f"Armed with a {item}, {name} faced the fearsome {villain}. "
        f"In the end, {name} {random.choice(endings)}"
    )
    print("\n📖 Your Story:\n" + story)

# story_generator()


# ── PROJECT 25: Currency Converter (Offline rates) ───────────
def currency_converter():
    rates = {"USD": 1, "INR": 83.5, "EUR": 0.92, "GBP": 0.79}
    amount = float(input("Amount: "))
    from_curr = input("From currency (USD/INR/EUR/GBP): ").upper()
    to_curr = input("To currency: ").upper()
    result = amount / rates[from_curr] * rates[to_curr]
    print(f"💱 {amount} {from_curr} = {result:.2f} {to_curr}")

# currency_converter()


# ── PROJECT 26: Fibonacci Generator ──────────────────────────
def fibonacci():
    n = int(input("How many Fibonacci numbers? "))
    a, b = 0, 1
    seq = []
    for _ in range(n):
        seq.append(a)
        a, b = b, a + b
    print("🔢 Fibonacci:", seq)

# fibonacci()


# ── PROJECT 27: Flashcard Quiz ───────────────────────────────
def flashcard_quiz():
    cards = {
        "Capital of France?": "Paris",
        "Largest planet?": "Jupiter",
        "Speed of light?": "299,792,458 m/s",
    }
    score = 0
    for q, a in cards.items():
        answer = input(f"❓ {q} ")
        if answer.strip().lower() == a.lower():
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Answer: {a}")
    print(f"\n🏆 Score: {score}/{len(cards)}")

# flashcard_quiz()


# ── PROJECT 28: Motivational Alarm ───────────────────────────
def motivational_alarm():
    import time, random
    seconds = int(input("Remind me in how many seconds? "))
    msgs = [
        "🔥 Get up and grind!",
        "💪 Time to move. No excuses.",
        "🚀 Every second counts. GO.",
    ]
    time.sleep(seconds)
    print(random.choice(msgs))

# motivational_alarm()


# ── PROJECT 29: Text to Morse Code ───────────────────────────
def morse_code():
    morse = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
        'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
        'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
        'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
        'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
        'Z': '--..', ' ': '/'
    }
    text = input("Text to Morse: ").upper()
    result = " ".join(morse.get(c, "?") for c in text)
    print("📡 Morse:", result)

# morse_code()


# ── PROJECT 30: Name Numerology ──────────────────────────────
def numerology():
    name = input("Enter your full name: ").upper()
    total = sum(ord(c) - 64 for c in name if c.isalpha())
    while total > 9:
        total = sum(int(d) for d in str(total))
    meanings = {
        1: "Leader & Pioneer", 2: "Diplomat & Peacemaker",
        3: "Creative & Expressive", 4: "Stable & Hardworking",
        5: "Adventurous & Free", 6: "Caring & Responsible",
        7: "Spiritual & Analytical", 8: "Ambitious & Powerful",
        9: "Compassionate & Wise"
    }
    print(f"🔮 Your number: {total} — {meanings.get(total, 'Mysterious')}")

# numerology()


# ── PROJECT 31: Daily Water Intake Tracker ───────────────────
def water_tracker():
    goal = 8
    count = 0
    print("💧 Water Tracker (goal: 8 glasses). Type 'drink' or 'quit'.")
    while True:
        cmd = input("> ").lower()
        if cmd == "drink":
            count += 1
            print(f"  {count}/{goal} glasses 💧")
            if count >= goal:
                print("🎉 Goal reached!")
                break
        elif cmd == "quit":
            print(f"Today's count: {count} glasses.")
            break

# water_tracker()


# ── PROJECT 32: Screen Time Log ──────────────────────────────
def screen_time_log():
    import datetime
    app = input("App/Activity name: ")
    minutes = int(input("Minutes spent: "))
    with open("screen_time.txt", "a") as f:
        f.write(f"{datetime.date.today()} | {app} | {minutes} min\n")
    print(f"📱 Logged {minutes} min on {app}.")

# screen_time_log()


# ── PROJECT 33: Random Name Picker ───────────────────────────
def name_picker():
    import random
    raw = input("Enter names separated by commas: ")
    names = [n.strip() for n in raw.split(",")]
    winner = random.choice(names)
    print(f"🎉 Selected: {winner}")

# name_picker()


# ── PROJECT 34: Savings Goal Tracker ─────────────────────────
def savings_goal():
    goal = float(input("Savings goal (₹): "))
    saved = float(input("Amount saved so far (₹): "))
    monthly = float(input("Monthly saving amount (₹): "))
    remaining = goal - saved
    months = -(-remaining // monthly)  # ceiling division
    print(f"💰 Remaining: ₹{remaining:.2f}")
    print(f"📅 At ₹{monthly}/month → done in {int(months)} month(s)")

# savings_goal()


# ── PROJECT 35: Workout Rep Counter ──────────────────────────
def rep_counter():
    exercise = input("Exercise name: ")
    sets = int(input("Number of sets: "))
    reps = int(input("Reps per set: "))
    total = sets * reps
    print(f"💪 {exercise}: {sets} sets × {reps} reps = {total} total reps")

# rep_counter()


# ── PROJECT 36: Riddle Game ──────────────────────────────────
def riddle_game():
    riddles = [
        ("I speak without a mouth and hear without ears. What am I?", "echo"),
        ("The more you take, the more you leave behind. What am I?", "footsteps"),
        ("I have cities, but no houses live there. What am I?", "map"),
    ]
    import random
    q, a = random.choice(riddles)
    print(f"🧩 Riddle: {q}")
    guess = input("Your answer: ").lower()
    if guess == a:
        print("🎉 Correct!")
    else:
        print(f"❌ Answer: {a.capitalize()}")

# riddle_game()


# ── PROJECT 37: Time Zone Converter ──────────────────────────
def timezone_converter():
    offsets = {"IST": 5.5, "UTC": 0, "EST": -5, "PST": -8, "CET": 1}
    hour = int(input("Current hour (0-23): "))
    from_tz = input("From timezone (IST/UTC/EST/PST/CET): ").upper()
    to_tz = input("To timezone: ").upper()
    utc_hour = (hour - offsets[from_tz]) % 24
    target = (utc_hour + offsets[to_tz]) % 24
    print(f"🕐 {hour}:00 {from_tz} = {int(target)}:00 {to_tz}")

# timezone_converter()


# ── PROJECT 38: Fake Invoice Generator ───────────────────────
def invoice_generator():
    client = input("Client name: ")
    items = []
    while True:
        item = input("Item (or 'done'): ")
        if item == "done":
            break
        price = float(input(f"Price for {item}: ₹"))
        items.append((item, price))
    total = sum(p for _, p in items)
    print(f"\n{'='*30}")
    print(f"INVOICE — {client}")
    print(f"{'='*30}")
    for item, price in items:
        print(f"  {item:<20} ₹{price:.2f}")
    print(f"{'='*30}")
    print(f"  {'TOTAL':<20} ₹{total:.2f}")

# invoice_generator()


# ── PROJECT 39: Random Meal Idea ─────────────────────────────
def meal_idea():
    import random
    proteins = ["Chicken", "Paneer", "Eggs", "Tofu", "Lentils"]
    carbs = ["Rice", "Roti", "Pasta", "Quinoa", "Bread"]
    veggies = ["Spinach", "Capsicum", "Mushroom", "Broccoli", "Carrot"]
    print(f"🍽️  Meal Idea: {random.choice(proteins)} + "
          f"{random.choice(carbs)} + {random.choice(veggies)}")

# meal_idea()


# ── PROJECT 40: Email Subject Line Generator ──────────────────
def email_subject_generator():
    import random
    topic = input("Email topic (e.g. collaboration): ")
    templates = [
        f"Quick question about {topic}",
        f"Exciting opportunity: {topic}",
        f"Let's talk {topic}",
        f"Re: {topic} — worth a look?",
        f"One idea for {topic} you'll love",
    ]
    print("📧 Subject:", random.choice(templates))

# email_subject_generator()


# ── PROJECT 41: ASCII Art Generator ──────────────────────────
def ascii_art():
    import pyfiglet  # pip install pyfiglet
    text = input("Text to convert: ")
    print(pyfiglet.figlet_format(text))

# ascii_art()  # Requires: pip install pyfiglet


# ── PROJECT 42: Prime Number Checker ─────────────────────────
def prime_checker():
    n = int(input("Enter a number: "))
    if n < 2:
        print("Not prime.")
    elif all(n % i != 0 for i in range(2, int(n**0.5) + 1)):
        print(f"✅ {n} is a prime number!")
    else:
        print(f"❌ {n} is not a prime number.")

# prime_checker()


# ── PROJECT 43: Reading Time Estimator ───────────────────────
def reading_time():
    text = input("Paste your article/text:\n")
    words = len(text.split())
    minutes = words / 200  # avg reading speed
    print(f"📚 {words} words → ~{minutes:.1f} min read")

# reading_time()


# ── PROJECT 44: Username Generator ───────────────────────────
def username_generator():
    import random
    adjectives = ["Shadow", "Rise", "Dark", "Gold", "Silent", "Neon"]
    nouns = ["Wolf", "Phoenix", "Trader", "King", "Storm", "Falcon"]
    nums = random.randint(10, 99)
    username = f"{random.choice(adjectives)}{random.choice(nouns)}{nums}"
    print(f"👤 Username: {username}")

# username_generator()


# ── PROJECT 45: Color Mood Board (Hex Generator) ─────────────
def mood_color():
    import random
    moods = {
        "happy": ["#FFD700", "#FFA500", "#FF69B4"],
        "calm": ["#87CEEB", "#6495ED", "#4682B4"],
        "dark": ["#1a1a2e", "#16213e", "#0f3460"],
        "energy": ["#FF4500", "#FF6347", "#FF7F50"],
    }
    mood = input("Mood (happy/calm/dark/energy): ").lower()
    colors = moods.get(mood, ["#FFFFFF"])
    print(f"🎨 Color palette for '{mood}':", " | ".join(colors))

# mood_color()


# ── PROJECT 46: Bucket List Maker ────────────────────────────
def bucket_list():
    items = []
    print("📝 Bucket List Builder. Type items (empty line to finish):")
    while True:
        item = input(f"  {len(items)+1}. ")
        if not item:
            break
        items.append(item)
    print("\n🌟 Your Bucket List:")
    for i, item in enumerate(items, 1):
        print(f"  ☐ {item}")
    with open("bucket_list.txt", "w") as f:
        f.write("\n".join(f"☐ {item}" for item in items))
    print("Saved to bucket_list.txt!")

# bucket_list()


# ── PROJECT 47: Sleep Debt Calculator ────────────────────────
def sleep_debt():
    ideal = 8
    days = int(input("How many days to track? "))
    total = 0
    for i in range(1, days + 1):
        slept = float(input(f"  Hours slept on day {i}: "))
        total += slept
    ideal_total = ideal * days
    debt = ideal_total - total
    if debt > 0:
        print(f"😴 You owe yourself {debt:.1f} hours of sleep.")
    else:
        print(f"✅ You slept {abs(debt):.1f} extra hours. Well rested!")

# sleep_debt()


# ── PROJECT 48: Crypto Slang Dictionary ──────────────────────
def crypto_dictionary():
    glossary = {
        "hodl": "Hold On for Dear Life — don't sell!",
        "fud": "Fear, Uncertainty, Doubt — negative news",
        "moon": "Price going extremely high",
        "rug pull": "Devs abandon a project and take funds",
        "whale": "An investor with very large holdings",
        "degen": "High-risk speculative trader",
        "ath": "All-Time High price",
    }
    word = input("Look up term: ").lower()
    print(f"📖 {word.upper()}: {glossary.get(word, 'Term not found.')}")

# crypto_dictionary()


# ── PROJECT 49: Daily Challenge Generator ────────────────────
def daily_challenge():
    import random, datetime
    challenges = [
        "Do 50 push-ups today.",
        "Read for 30 minutes without your phone.",
        "Write 3 things you're grateful for.",
        "No social media for 12 hours.",
        "Drink 3 litres of water today.",
        "Reach out to someone you haven't spoken to in a while.",
        "Wake up 1 hour earlier tomorrow.",
        "Spend 20 minutes learning something new.",
    ]
    random.seed(datetime.date.today().toordinal())
    print("🎯 Today's Challenge:", random.choice(challenges))

# daily_challenge()


# ── PROJECT 50: Life Stats Summary ───────────────────────────
def life_stats():
    name = input("Your name: ")
    age = int(input("Your age: "))
    days_lived = age * 365
    hours_slept = days_lived * 8
    heartbeats = days_lived * 24 * 60 * 70  # avg 70 bpm
    print(f"\n📊 Life Stats for {name}:")
    print(f"  🗓  Days lived:        {days_lived:,}")
    print(f"  💤 Hours slept:       {hours_slept:,}")
    print(f"  ❤️  Heartbeats so far: {heartbeats:,}")
    print(f"  🚀 And counting...")

# life_stats()


# ============================================================
# HOW TO USE:
# 1. Uncomment any function call at the bottom of each block
# 2. Run: python 50_python_projects.py
# 3. Or copy individual projects into their own files
# ============================================================
