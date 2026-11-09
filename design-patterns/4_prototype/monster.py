from abc import ABC, abstractmethod
from copy import deepcopy

"""
Prototype Design Pattern: This pattern is used to create new objects by copying an existing object, known as the prototype. It is useful when the cost of creating a new object is expensive or complex.

Example: If creating a new monster from scratch is costly, we can clone an existing monster prototype and modify it as needed.
"""


class MonsterPrototype(ABC):
    def __init__(self):
        self.name = ""
        self.color = ""
        self.weapon = ""
        self.skills = []

    @abstractmethod
    def clone(self) -> "MonsterPrototype":
        pass


class Orc(MonsterPrototype):
    def __init__(self, name, color, weapon, skills):
        super().__init__()
        self.name = name
        self.color = color
        self.weapon = weapon
        self.skills = skills

    def clone(self):
        return deepcopy(self)

    def __str__(self) -> str:
        return f"Monster: {self.name} | Color: {self.color} | Weapon: {self.weapon} | Skills: {self.skills}"


if __name__ == "__main__":
    orc_prototype = Orc(
        name="Orc Warrior",
        color="Green",
        weapon="Battleaxe",
        skills=["Charge", "Enrage"],
    )
    print(f"Original: {orc_prototype}\n")

    # Spawn Clone 1
    orc_clone_1 = orc_prototype.clone()
    orc_clone_1.color = "Red"

    # Spawn Clone 2
    orc_clone_2 = orc_prototype.clone()
    orc_clone_2.weapon = "Warhammer"
    orc_clone_2.skills.append("Shield Bash")  # Verifies deep copy works independently

    print("--- Spawning completed instantly via cloning ---")
    print(f"Original Prototype remains unchanged: \n -> {orc_prototype}")
    print(f"Spawned Clone 1: \n -> {orc_clone_1}")
    print(f"Spawned Clone 2: \n -> {orc_clone_2}")
