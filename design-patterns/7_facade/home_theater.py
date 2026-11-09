"""
The Facade is a structural design pattern that provides a simplified interface to a complex system of classes, library, or framework. It wraps the complexities of the system and provides a simple interface to clients.

Example:
HomeTheaterFacade simplifies the process of watching a movie by coordinating the TV and SoundSystem.
"""


class TV:
    def turn_on(self):
        print("📺 TV is now ON.")

    def set_input(self, source: str):
        print(f"🔌 TV input set to {source}.")

    def turn_off(self):
        print("📺 TV is now OFF.")


class SoundSystem:
    def turn_on(self):
        print("🔊 Sound system is now ON.")

    def set_volume(self, level: int):
        print(f"🎛️ Volume set to {level}.")

    def turn_off(self):
        print("🔊 Sound system is now OFF.")


class HomeTheaterFacade:
    def __init__(self, tv: TV, sound_system: SoundSystem):
        self.tv = tv
        self.sound_system = sound_system

    def watch_movie(self, movie_name: str):
        self.tv.turn_on()
        self.tv.set_input("HDMI1")
        self.sound_system.turn_on()
        self.sound_system.set_volume(50)
        print(f"🎬 Now playing '{movie_name}'.")

    def end_movie(self):
        self.tv.turn_off()
        self.sound_system.turn_off()


if __name__ == "__main__":
    home_theater = HomeTheaterFacade(tv=TV(), sound_system=SoundSystem())
    home_theater.watch_movie("Inception")
    home_theater.end_movie()
