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

def reflect(text):
    for pat, repl in reflections.items():
        text = re.sub(pat, repl, text, flags=re.I)
    return text

# Bot Correct Response
patterns = [
    (
        re.compile(r"\b(workout)\b", re.I),
        lambda m: "That's cool, is it strength training or cardio?"
    ),
    (
        re.compile(r"\b(cardio)\b", re.I),
        lambda m: "That's great, what kind of cardio did you just had?"
    ),
    (
        re.compile(r"\b(run)\b", re.I),
        lambda m: "How long do you run?"
    ),
    (
        re.compile(r"\b(half\s*)?marathon\b", re.I),
        lambda m: f"Wow, you just did a {m.group(0).strip()}??? You're an endurance monster."
    ),
    (
        re.compile(r"\b(\d+(\.\d+)?)\s*km\b", re.I),
        lambda m: (
            f"{m.group(1)} km is a great distance!" if float(m.group(1)) <= 5
            else f"Wow, you just did a long run of {m.group(1)} km, at what pace do you run?"
        )
    ),
    (
        re.compile(r"\bpace\s*(\d+(\.\d+)?)\b", re.I),
        lambda m: (
            "That's a great pace for a beginner, keep up the good work!!!" if float(m.group(1)) > 7
            else "Wow, you could've been an athlete if you keep doing this consistently." if float(m.group(1)) > 4
            else "Even the fastest runner in the police academy couldn't even catch u if u ran at this pace"
        )
    ),
    (
        re.compile(r"\b(hurt|injur(y|ed|ies))\b", re.I),
        lambda m: "You need to warm up before doing workout to avoid injury and wear a proper gear. If the injury isn't getting better soon, I suggest you to see a doctor ASAP!"
    ),
    (
        re.compile(r"\bstrength\b", re.I),
        lambda m: "Wow, Ronnie Coleman must be so proud of you! Which body part did you just train?"
    ),
    (
        re.compile(r"\b(((a|A)rm(s)*|(l|L)eg(s)*|(c|C)ore|(b|B)ack)+)\b", re.I),
        lambda m: f"Yeah Buddy, Your {m.group(1)} must've been stronger rn."
    ),
    (
        re.compile(r"\bfinish(ed)?\s*workout\b", re.I),
        lambda m: "Rate the difficulty from 0-10"
    ),
    (
        re.compile(r"\b(\d+(\.\d+)?)\b", re.I),
        lambda m: (
            "Lightweight BABY!!!" if float(m.group(1)) < 5
            else "Good grind!" if float(m.group(1)) < 7
            else "You're a goddamn hulk!!!"
        )
    ),
    (
        re.compile(r"\b(rest\s*day|resting)\b", re.I),
        lambda m: "Rest is just as important as training! Enjoy your recovery."
    ),
    (
        re.compile(r"\b(protein|nutrition|diet|eat|food)\b", re.I),
        lambda m: "Nutrition is key! Are you tracking your macros or just eating intuitively?"
    ),
    (
        re.compile(r"\b(motivat(e|ion|ed)|lazy|tired)\b", re.I),
        lambda m: "Remember, progress is made one step at a time. You got this!"
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
    for pat, response in patterns:
        m = pat.match(user)
        if m:
            return response(m)
    return random.choice(defaults)


log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)
log_file = os.path.join(log_dir, "conversation.txt")

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