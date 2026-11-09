"""
The YouTubeChannel class represents a YouTube channel with a name and provides a method to upload videos.
It follows the Observer pattern where users can subscribe to channels and get notified when a new video is uploaded.
"""

from abc import ABC, abstractmethod


class Observer(ABC):
    def __init__(self, username: str):
        self.username = username
        self.subscribed_channels = []

    @abstractmethod
    def notify(self, channel_name: str, video_title: str):
        pass


class Subject(ABC):
    @abstractmethod
    def subscribe(self, observer: Observer):
        pass

    @abstractmethod
    def unsubscribe(self, observer: Observer):
        pass

    @abstractmethod
    def notify(self, video_title: str):
        pass


class User(Observer):
    def notify(self, channel_name: str, video_title: str):
        print(
            f"🔔 {self.username} has been notified about a new video '{video_title}' on {channel_name}."
        )


class YouTubeChannel(Subject):
    def __init__(self, name: str):
        self.name = name
        self.subscribers = []

    def upload_video(self, title: str):
        print(f"📹 '{title}' has been uploaded to {self.name}.")
        self.notify(title)

    def subscribe(self, observer: Observer):
        self.subscribers.append(observer)
        observer.subscribed_channels.append(self)
        print(f"👤 {observer.username} has subscribed to {self.name}.")

    def unsubscribe(self, observer: Observer):
        if observer in self.subscribers:
            self.subscribers.remove(observer)
            observer.subscribed_channels.remove(self)
            print(f"👤 {observer.username} has unsubscribed from {self.name}.")
        else:
            print(f"👤 {observer.username} is not subscribed to {self.name}.")

    def notify(self, video_title: str):
        for subscriber in self.subscribers:
            subscriber.notify(self.name, video_title)


if __name__ == "__main__":
    user1 = User("Alice")
    user2 = User("Bob")

    channel = YouTubeChannel("TechTalks")
    channel.subscribe(user1)
    channel.subscribe(user2)
    channel.upload_video("Understanding Design Patterns")
    channel.unsubscribe(user1)

    channel.upload_video("Observer Pattern Explained")
