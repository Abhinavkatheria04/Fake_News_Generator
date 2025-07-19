import random

subjects=["Ankita Bansal","Rohit Mehra","The Monkeys","Justin Bieber","badshah"]

actions=["discovered a hidden tunnel",
         "danced",
         "fought a monkey over a sandwich",
         "grew a potato",
         "built a rocket using kitchen utensils"]

place_or_things=["at tea stall in Varanasi",
                 "at a haunted library in Rajasthan",
                 "and a secret cave near Manali",
                 "on the street",
                 "at taj mahal",]

while True:
    subject=random.choice(subjects)
    action=random.choice(actions)
    place=random.choice(place_or_things)

    headline=f"BREAKING NEWS : {subject} {action} {place} "
    print("\n"+ headline)

    user_input=input("\n Do you want another headline? (yes/no)").strip().lower()
    if user_input == "no":
        break

