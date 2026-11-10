/**
 * The YouTubeChannel class represents a YouTube channel with a name and provides a method to upload videos.
 * It follows the Observer pattern where users can subscribe to channels and get notified when a new video is uploaded.
 */

import { fileURLToPath } from "url";

abstract class Observer {
  public username: string;
  public subscribed_channels: string[];

  constructor(username: string) {
    this.username = username;
    this.subscribed_channels = [];
  }

  abstract notify(subject_name: string, subject_title: string): void;
}

abstract class Subject {
  abstract subscribe(observer: Observer): void;
  abstract unsubscribe(observer: Observer): void;
  abstract notify(subject_title: string): void;
}

class User extends Observer {
  notify(subject_name: string, subject_title: string): void {
    console.log(
      `🔔 ${this.username} has been notified about a new video '${subject_title}' on ${subject_name}.`,
    );
  }
}

class YouTubeChannel extends Subject {
  private name: string = "";
  private subscribers: Observer[] = [];

  constructor(name: string) {
    super();
    this.name = name;
  }

  upload_video(video_title: string) {
    console.log(`📹 '${video_title}' has been uploaded to ${this.name}.`);
    this.notify(video_title);
  }

  subscribe(observer: Observer): void {
    this.subscribers.push(observer);
    observer.subscribed_channels.push(this.name);
    console.log(`👤 ${observer.username} has subscribed to ${this.name}.`);
  }

  unsubscribe(observer: Observer): void {
    let subscribed = false;
    this.subscribers = this.subscribers.filter((subscriber) => {
      if (subscriber === observer) {
        subscribed = true;
        console.log(
          `👤 ${observer.username} has unsubscribed from ${this.name}.`,
        );
      }
    });

    if (subscribed === false) {
      console.log(`👤 ${observer.username} is not subscribed to ${this.name}.`);
    }
  }

  notify(subject_title: string): void {
    for (let subscriber of this.subscribers) {
      subscriber.notify(this.name, subject_title);
    }
  }
}

if (process.argv[1] === fileURLToPath(import.meta.url)) {
  const user1 = new User("Alice");
  const user2 = new User("Bob");

  const channel = new YouTubeChannel("TechTalks");
  channel.subscribe(user1);
  channel.subscribe(user2);
  channel.upload_video("Understanding Design Patterns");

  channel.unsubscribe(user1);
  channel.upload_video("Observer Pattern Explained");
}
