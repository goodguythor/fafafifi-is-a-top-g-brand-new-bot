import re
import random
import os

# Pronoun Reflection
reflections = {
    r"\bi(\s+am|(')?(?:m|ve))?\b": "you",
    r"\bmy\b": "your",
}

def reflect(sentence):
    words = sentence.split()
    i = 0
    while i < len(words) - 1:
        if words[i].lower() == "i" and words[i + 1].lower() == "am":
            words[i] = "i am"
            del words[i + 1]
        else:
            i += 1
    reflected_words = []
    for word in words:
        reflected = word
        for pat, repl in reflections.items():
            if re.fullmatch(pat, word, flags=re.I):
                reflected = re.sub(pat, repl, word, flags=re.I)
                break
        reflected_words.append(reflected)
    return ' '.join(reflected_words)

# Bot Correct Response
patterns = [
    ( # Banned Words
        re.compile(r".*(fuck|shit|stupid|bitch|retard)", re.I),
        [
            "My mom said that you can't use bad words if you want to go to the heaven 🥺",
            "Mom, I'm scared 🥺"
        ]
    ), 
    ( # Negation 
        re.compile(r".*\b(i(?:\s+am|(')?(?:m|ve))?|my)\b.*\b(not|don(')?t|do not|didn(')?t|did not|ain(')?t)\b", re.I),
        [
            "It's ok to not doing anything in a day, just take your time to recover and relax"
        ]
    ),
    ( # Rest
        re.compile(r".*\b(i(?:\s+am|(')?(?:m|ve))?|my)\b.*\brest(\s*day|ing)?\b", re.I),
        [
            "Rest is just as important as training! Enjoy your recovery.",
            "Rest days help your muscles grow stronger. Take it easy!"
        ]
    ),
    ( # Injury
        re.compile(r".*\b(i(?:\s+am|(')?(?:m|ve))?|my)\b.*\b(hurt(ing|s)?|injur(y|ed|ies))\b", re.I),
        [
            "You need to warm up before doing workout to avoid injury and wear a proper gear. If the injury isn't getting better soon, I suggest you to see a doctor ASAP!",
            "Ouch! Make sure to rest and recover. If it hurts a lot, maybe see a doctor."
        ]
    ),
    ( # Strength
        re.compile(r".*\bi(?:\s+am|(')?(?:m|ve))?\b.*\b(train|workout|exercise)(s|ing)?\b\s\bmy\s(streng(th|ht)|muscle)(s)?\b\s*", re.I),
        [
            "Wow, Ronnie Coleman must be so proud of you! Which body part did you just train?",
            "Strength training is the key to gains! What exercises did you do today?"
        ]
    ),
    ( # Body Part Exercise
        re.compile(r".*\bi(?:\s+am|(')?(?:m|ve))?\b.*(\b(train(s|ing)?|workout|exercis(e|ing))\b)\s*\bmy\s(arm|leg|core|back)(s)?\b", re.I),
        [
            "Yeah Buddy {X}, You must've been stronger rn.",
        ]
    ),
    ( # Simple Workout
        re.compile(r".*\bi(?:\s+am|(')?(?:m|ve))?\b.*\b(workout(s)?|working out|exercis(e|ing))\b", re.I),
        [
            "That's cool, is it strength training or cardio?"
        ]
    ),
    ( # Cardio
        re.compile(r".*\bi(?:\s+am|(')?(?:m|ve))?\b.*\bcardio\b", re.I),
        [
            "That's great, what kind of cardio did you just have?",
            "Cardio is awesome for your heart! Was it running, cycling, or something else?"
        ]
    ),
    ( # Distance
        re.compile(r".*\bi(\s+am|(')?(m|ve))?\b.*\b(r(u|a)n(s|ning)?|walk(s|ed)?|cycl(e(s)?|ing))\b.*\b(\d+(\.\d+)?)\s*(k(m|ilo(\s*meter)?)?|mile)(s)?\b", re.I),
        [
            "{X}? That's a great distance!",
            "Wow, {X}, at what pace do you run?"
        ]
    ),
    ( # Marathon
        re.compile(r".*\bi(?:\s+am|(')?(?:m|ve))?\b.*\b(r(u|a)n(s)?|walk(s)?|cycl(e(s)?|ing))\b.*\b(half|full)?\s*marathon\b", re.I),
        [
            "Wow, {X}??? You're an endurance monster.",
            "{X}? That's incredible! How did you feel during the race?"
        ]
    ),
    ( # Pace
        re.compile(r".*\b(i(?:\s+am|(')?(?:m|ve))?|my)\b.*\b(r(u|a)n(s)?|walk(s)?|cycl(e(s)?|ing))\b.*\bpace(s)?\b.*\b(\d+(\.\d+)?)\b", re.I),
        [
            "That's a great pace, keep up the good work!!!",
            "Wow, you could've been an athlete if you keep doing this consistently."
        ]
    ),
    ( # Simple Run
        re.compile(r".*\bi(?:\s+am|(')?(?:m|ve))?\b.*\b(?:ran|run(?:s|ning)?)\b", re.I),
        [
            "How long do you run?",
            "Running is a great way to clear your mind."
        ]
    ),
    ( # Great
        re.compile(r".*\b(i(?:\s+am|(')?(?:m|ve))?|my)\b.*\b(good|great|happy)\b", re.I),
        [
            "That's nice, hope that feelings stay with you for a long time"
        ]
    ),
    ( # Tired
        re.compile(r".*\b(i(?:\s+am|(')?(?:m|ve))?|my)\b.*\b(lazy|tired)\b", re.I),
        [
            "Remember, progress is made one step at a time. You got this!",
            "Everyone feels tired sometimes. Just keep moving forward!"
        ]
    ),
]

# Bot Default Response
defaults = [
    "Hah?",
    "Just ask AI bro.",
    "Just google bro.",
    "YNTKTS",
    "Ehmm, downstreaming?",
    "Ehmm, 19 millions jobs opportunities?",
    "Ehmm, AI?",
    "Ehmm, free lunch?",
    "Ehmm, Greenflation?",
]

# Bot Reply Function
def reply(user):
    for pat, responses in patterns:
        m = pat.match(user)
        if m:
            user_reflected = reflect(user.strip())
            return random.choice(responses).format(X=user_reflected)
    return random.choice(defaults)

if __name__ == "__main__":
    log_dir = "logs"
    os.makedirs(log_dir, exist_ok=True)
    log_file = os.path.join(log_dir, "logs.txt")
    with open(log_file, "a", encoding="utf-8") as f:
        while True:
            try:
                user = input("YOU: ").strip()
                if not user:
                    print("Goodbye.")
                    break
                bot_reply = reply(user)
                print("fAfAfIfI:", bot_reply)
                f.write(f"YOU: {user}\n")
                f.write(f"fAfAfIfI: {bot_reply}\n")
            except KeyboardInterrupt:
                print("\nGoodbye.")
                break