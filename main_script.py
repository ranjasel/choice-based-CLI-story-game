# import
import time
import re

# allowed chars
pattern = '^[a-zA-Z ]+$'

# story script
story = {

    "start": {
        "text": "You wake up in a dark forest. A cold wind blows. Two paths lie ahead.",
        "choices": {"1": "Enter the forest", "2": "Walk toward distant lights"},
        "next": {"1": "forest_entry", "2": "village_entry"},
        "end": False
    },

    # --- FOREST BRANCH ---

    "forest_entry": {
        "text": "The forest is dense. You hear something moving.",
        "choices": {"1": "Follow the sound", "2": "Climb a tree"},
        "next": {"1": "wolf_encounter", "2": "tree_view"},
        "end": False
    },

    "wolf_encounter": {
        "text": "A wolf appears, growling at you.",
        "choices": {"1": "Fight", "2": "Run"},
        "next": {"1": "death_wolf", "2": "deep_forest"},
        "end": False
    },

    "tree_view": {
        "text": "From the tree, you spot a cave nearby.",
        "choices": {"1": "Go to cave", "2": "Stay in tree"},
        "next": {"1": "cave_entrance", "2": "fall_end"},
        "end": False
    },

    "deep_forest": {
        "text": "You reach a glowing clearing with a sword in stone.",
        "choices": {"1": "Take sword", "2": "Ignore it"},
        "next": {"1": "sword_power", "2": "lost_end"},
        "end": False
    },

    "cave_entrance": {
        "text": "The cave is dark but something glows inside.",
        "choices": {"1": "Enter cave", "2": "Leave"},
        "next": {"1": "cave_inside", "2": "deep_forest"},
        "end": False
    },

    "cave_inside": {
        "text": "A strange creature sleeps beside treasure.",
        "choices": {"1": "Take treasure", "2": "Wake creature"},
        "next": {"1": "greed_end", "2": "spirit_test"},
        "end": False
    },

    "spirit_test": {
        "text": "The creature tests your intentions.",
        "choices": {"1": "Speak truthfully", "2": "Lie"},
        "next": {"1": "blessing_end", "2": "death_creature"},
        "end": False
    },

    # --- VILLAGE BRANCH ---

    "village_entry": {
        "text": "You reach a quiet village. One house has light.",
        "choices": {"1": "Enter house", "2": "Explore outside"},
        "next": {"1": "old_man", "2": "watch_tower"},
        "end": False
    },

    "old_man": {
        "text": "An old man offers you help.",
        "choices": {"1": "Trust him", "2": "Refuse"},
        "next": {"1": "safe_escape", "2": "village_dark"},
        "end": False
    },

    "watch_tower": {
        "text": "A tall watch tower stands nearby.",
        "choices": {"1": "Climb tower", "2": "Search ground"},
        "next": {"1": "tower_top", "2": "trap_trigger"},
        "end": False
    },

    "tower_top": {
        "text": "You see a clear path out of the forest.",
        "choices": {"1": "Follow path", "2": "Wait longer"},
        "next": {"1": "escape_end", "2": "tower_collapse"},
        "end": False
    },

    "trap_trigger": {
        "text": "You activate a hidden trap.",
        "choices": {"1": "Escape quickly", "2": "Freeze"},
        "next": {"1": "injured_escape", "2": "trap_end"},
        "end": False
    },

    "village_dark": {
        "text": "The village suddenly becomes dark and silent.",
        "choices": {"1": "Run away", "2": "Stay"},
        "next": {"1": "escape_end", "2": "void_end"},
        "end": False
    },

    # --- ENDINGS ---

    "death_wolf": {
        "text": "The wolf overpowers you. You died.",
        "choices": {},
        "next": {},
        "end": True
    },

    "fall_end": {
        "text": "You slip from the tree and fall to your death.",
        "choices": {},
        "next": {},
        "end": True
    },

    "lost_end": {
        "text": "You wander endlessly and are never seen again.",
        "choices": {},
        "next": {},
        "end": True
    },

    "sword_power": {
        "text": "You gain immense power and become the forest guardian.",
        "choices": {},
        "next": {},
        "end": True
    },

    "greed_end": {
        "text": "The cave collapses as you grab treasure. You are trapped.",
        "choices": {},
        "next": {},
        "end": True
    },

    "death_creature": {
        "text": "The creature destroys you instantly.",
        "choices": {},
        "next": {},
        "end": True
    },

    "blessing_end": {
        "text": "You are blessed and safely leave the forest.",
        "choices": {},
        "next": {},
        "end": True
    },

    "safe_escape": {
        "text": "The old man guides you out safely.",
        "choices": {},
        "next": {},
        "end": True
    },

    "escape_end": {
        "text": "You find your way out of the forest.",
        "choices": {},
        "next": {},
        "end": True
    },

    "tower_collapse": {
        "text": "The tower collapses. You fall and die.",
        "choices": {},
        "next": {},
        "end": True
    },

    "trap_end": {
        "text": "The trap activates fully. You couldn’t escape.",
        "choices": {},
        "next": {},
        "end": True
    },

    "injured_escape": {
        "text": "You escape injured but alive.",
        "choices": {},
        "next": {},
        "end": True
    },

    "void_end": {
        "text": "The darkness consumes everything. You fade away.",
        "choices": {},
        "next": {},
        "end": True
    }
}

class Game:
    def __init__(self, story, name):
        self.story = story
        self.current_scene = "start"
        self.name = name

    def display_scene(self):
        # current scene
        print("\n" + "-"*40)
        print(f"» {self.story[self.current_scene]['text']}")
        print("-"*40)
        for key, val in self.story[self.current_scene]["choices"].items():
            print(f"▶ Choice {key} - {val}")

    def get_choice(self):
        print("\nWhat is your choice (enter choice number!)")
        while True:
            choice = str(input("► ").strip())
            if choice in self.story[self.current_scene]["choices"]:
                break
            else: 
                time.sleep(0.3)
                print("Invalid choice, retry.")
                continue
        return choice
    
    def advance_scene(self, choice):
        self.current_scene = self.story[self.current_scene]["next"][choice]

    def run(self):
        print(f"Welcome, {self.name}! Your adventure begins...")
        while True:
            while True:
                self.display_scene()

                if self.story[self.current_scene]["end"]:
                    break
                choice = self.get_choice()
                self.advance_scene(choice)
            print(f"\nGame Over. Thanks for playing {self.name}!")

            print("\nWould you like to replay the game? (y/n)")
            replay = input().strip().lower()
            if replay in ['y', 'yes']:
                self.current_scene = "start"
                continue
            elif replay in ['n', 'no']:
                break
        print("\nGame Exit.")

print("Welcome to choice-driven story game.")
print("What is your name, adventurer?")
while True:
    game_name = str(input("► ").strip())
    if re.match(pattern, game_name):
        break
    else:
        print("Name can only contain letters and spaces, retry.")
        continue

game_run = Game(story, game_name)
game_run.run()