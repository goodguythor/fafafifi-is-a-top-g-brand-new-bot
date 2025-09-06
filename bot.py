import re
import random
import os

# Pronoun Reflection
reflections = {
    r"\bi\b": "you",
    r"\bme\b": "you",
    r"\bmy\b": "your",
    r"\bam\b": "are",
    r"\byou\b": "I",
    r"\byour\b": "my",
    r"\byours\b": "mine",
}

def reflect(words):
    reflected_words = []
    for word in words:
        reflected = word
        for pat, repl in reflections.items():
            if re.fullmatch(pat, word, flags=re.I):
                reflected = re.sub(pat, repl, word, flags=re.I)
                break
        reflected_words.append(reflected)
    return ''.join(reflected_words)

# Bot Correct Response
patterns = [
    (
        re.compile(r"\bi( am|(')?(m|ve))?\b.*\b(do(ing)?|done|did)\b.*\b(workout(s)?|working out|exercis(e|ing))\b", re.I),
        [
            "That's cool, is it strength training or cardio?",
            "Nice! Was it a tough session or more of a recovery workout?"
        ]
    ),
    (
        re.compile(r"\bi( am|(')?(m|ve))?\b.*\b(do(ing)?|done|did)\b.*\bcardio\b", re.I),
        [
            "That's great, what kind of cardio did you just have?",
            "Cardio is awesome for your heart! Was it running, cycling, or something else?"
        ]
    ),
    (
        re.compile(r"\bi( am|(')?(m|ve))?\b.*\b(do(ing)?|done|did)\b.*\b(ran|run(s|ning)?)\b", re.I),
        [
            "How long do you run?",
            "Running is a great way to clear your mind. Was it outdoors or on a treadmill?"
        ]
    ),
    (
        re.compile(r"\bi( am|(')?(m|ve))?\b.*\b(do(ing)?|done|did|ran|run(s|ning)?)\b.*\b(half |full )?marathon\b", re.I),
        [
            "Wow, {X}??? You're an endurance monster.",
            "{X}? That's incredible! How did you feel during the race?"
        ]
    ),
    (
        re.compile(r"\b(\d+(\.\d+)?)\s*km\b", re.I),
        [
            "{X} km is a great distance!",
            "Wow, you just did a long run of {X} km, at what pace do you run?"
        ]
    ),
    (
        re.compile(r"\bpace\s*(\d+(\.\d+)?)\b", re.I),
        [
            "That's a great pace for a beginner, keep up the good work!!!",
            "Wow, you could've been an athlete if you keep doing this consistently.",
            "Even the fastest runner in the police academy couldn't even catch u if u ran at this pace"
        ]
    ),
    (
        re.compile(r"\b(hurt|injur(y|ed|ies))\b", re.I),
        [
            "You need to warm up before doing workout to avoid injury and wear a proper gear. If the injury isn't getting better soon, I suggest you to see a doctor ASAP!",
            "Ouch! Make sure to rest and recover. If it hurts a lot, maybe see a doctor."
        ]
    ),
    (
        re.compile(r"\bstrength\b", re.I),
        [
            "Wow, Ronnie Coleman must be so proud of you! Which body part did you just train?",
            "Strength training is the key to gains! What exercises did you do today?"
        ]
    ),
    (
        re.compile(r"\b(((a|A)rm(s)*|(l|L)eg(s)*|(c|C)ore|(b|B)ack)+)\b", re.I),
        [
            "Yeah Buddy, Your {X} must've been stronger rn.",
            "Nice! Training your {X} is always a good idea."
        ]
    ),
    (
        re.compile(r"\bfinish(ed)?\s*workout\b", re.I),
        [
            "Rate the difficulty from 0-10",
            "Congrats on finishing your workout! How do you feel now?"
        ]
    ),
    (
        re.compile(r"\b(\d+(\.\d+)?)\b", re.I),
        [
            "Lightweight BABY!!!",
            "Good grind!",
            "You're a goddamn hulk!!!"
        ]
    ),
    (
        re.compile(r"\b(rest\s*day|resting)\b", re.I),
        [
            "Rest is just as important as training! Enjoy your recovery.",
            "Rest days help your muscles grow stronger. Take it easy!"
        ]
    ),
    (
        re.compile(r"\b(protein|nutrition|diet|eat|food)\b", re.I),
        [
            "Nutrition is key! Are you tracking your macros or just eating intuitively?",
            "Eating well fuels your progress. Got any favorite meals?"
        ]
    ),
    (
        re.compile(r"\b(motivat(e|ion|ed)|lazy|tired)\b", re.I),
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