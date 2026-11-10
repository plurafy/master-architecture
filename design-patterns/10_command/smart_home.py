"""
The Command Design Pattern is a behavioral software design pattern that turns a request or operation into a stand-alone object. This object contains all the information needed to execute the action later, including the method name, the target object, and any arguments.
"""

from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass

    @abstractmethod
    def undo(self) -> None:
        pass


class Light:
    def turn_on(self):
        print("💡 The light is ON.")

    def turn_off(self):
        print("🌑 The light is OFF.")


class LightOnCommand(Command):
    def __init__(self, light: Light) -> None:
        super()
        self.light = light

    def execute(self) -> None:
        self.light.turn_on()

    def undo(self) -> None:
        self.light.turn_off()


class LightOffCommand(Command):
    def __init__(self, light: Light) -> None:
        super()
        self.light = light

    def execute(self) -> None:
        self.light.turn_off()

    def undo(self) -> None:
        self.light.turn_on()


class RemoteControl:
    def __init__(self) -> None:
        self.history = []

    def press_button(self, command: Command) -> None:
        print("# Running a command...")
        command.execute()
        self.history.append(command)

    def press_undo(self) -> None:
        if self.history:
            print("# Undoing last command...")
            command = self.history.pop()
            command.undo()
        else:
            print("❌ Nothing to undo...")


if __name__ == "__main__":
    # Create the receiver
    living_room_light = Light()

    # Create the commands and bind them to the receiver
    light_on = LightOnCommand(living_room_light)
    light_off = LightOffCommand(living_room_light)

    # Initialize the invoker
    remote = RemoteControl()

    # Execute operations
    remote.press_button(light_on)  # Output: 💡 The light is ON.
    remote.press_button(light_off)  # Output: 🌑 The light is OFF.

    # Undo operations
    remote.press_undo()  # Output: 💡 The light is ON.
