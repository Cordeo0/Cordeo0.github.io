from media import Media
import json
class Watchlist():
    def __init__(self):
        self.items = []

    def add(self,media):
        self.items.append(media)
    def remove(self, title):
        self.items= [m for m in self.items if m.title != title]


    def load(self, path):
        try:
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            return []
        except json.JSONDecodeError as e:
            print("Invalid JSON:", e)
            return []
    def save(self, path, data):
        try:
            with open(path, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
        except OSError as e:
            print("Could not save file:", e)
    def search(self, title):
        found = False
        for media in self.items:
            if media.title.lower() == title.lower():
                found = True

                print(f"{media.title}, {media.media_type}, {media.status}, {media.rating}, {media.notes} ")

                break
        if not found:
            print("No media with that title found.")    

    def list_by_type(self):
            if not self.items:
                print("\nWatchlist is empty")
                return
            for media in sorted(self.items, key=lambda x: x.media_type):
                print(f"{media.title}, {media.media_type}, {media.status}, {media.rating}, {media.notes} ")

    def list_by_title(self):
        if not self.items:
            print("\nWatchlist is empty")
            return
        for media in sorted(self.items, key=lambda x: x.title):
            print(f"{media.title}, {media.media_type}, {media.status}, {media.rating}, {media.notes} ")
    def list_by_status(self):
        if not self.items:
            print("\nWatchlist is empty")
            return
        for media in sorted(self.items, key=lambda x: x.status):
            print(f"{media.title}, {media.media_type}, {media.status}, {media.rating}, {media.notes} ")
    def list_by_rating(self):
        if not self.items:
            print("\nWatchlist is empty")
            return
        for media in sorted(self.items, key=lambda x: x.rating):
            print(f"{media.title}, {media.media_type}, {media.status}, {media.rating}, {media.notes} ")

    def edit(self, ):
        #ask which title, 
        title = input("Type in name of media you wish to edit. ")

        item = None
        for media in self.items:
            if media.title.lower() == title.lower():
                item = media
                break
        if item is None:
            print("No media with that title found.")
            return
        #then ask which field to modify
        print("The valid fields are title, media_type, status, rating, notes")
        field = input("Enter field you wish to edit. ")
        

        if not hasattr(item, field):
            print(f"'{field}' is not a valid field for this media. ")
            
        #then type in new value, 
        new = input("Enter new value. (Will erase previous) ")

        setattr(item, field, new)
        print(f"Updated {field} for '{item.title}' to: {new}")
        