from watchlist import Watchlist
from media import Media
import json
from pathlib import Path

def main():
    watchlist = Watchlist()
    data = watchlist.load("watchlist.json")
    if data:
        for item in data:
            media = Media(item["title"],item["type"],item["status"],item["rating"],item["notes"])
            watchlist.add(media)

    while True:

        menu()

        choice = input("Choose an option: ")

        if choice == "1":
            # Add Item
            title = input("Title: ")
            media_type = input("Media Type: ")
            status = input("Status: ")
            rating = input("Rating: ")
            notes = input("Notes: ") 
            media = Media(title, media_type, status, rating, notes) 
            watchlist.add(media)
        elif choice == "2":
            # Remove Item
            watchlist.list_by_type()
            title_to_remove = input("Enter Title to remove: ")
            watchlist.remove(title_to_remove)
        elif choice == "3":
            # List Items sorted by media
            print(f"\n")
            watchlist.list_by_type()
            # Ask user if they want to sort
            
            print("\nIf you wish to sort type the number next to it")
            print("1. Sort by title")
            print("2. Sort by status")
            print("3. Sort by rating")
            print("4. Edit a field")
            option = input("\nEnter the number you wish to execute, or enter to return ")
            if option == "1":
                print(f"\n")
                watchlist.list_by_title()
            elif option ==  "2":
                print(f"\n")
                watchlist.list_by_status()
            elif option == "3":
                print(f"\n")
                watchlist.list_by_rating()
            elif option == "4":
                watchlist.edit()        #Working
        elif choice == "4":
            title = input("Enter title to search your watchlist for it. ")
            watchlist.search(title)

        elif choice == "5":
            # Save and Quit
            data =[]
            for media in watchlist.items:
                data.append({
                    "title": media.title,
                    "type": media.media_type,
                    "status": media.status,
                    "rating": media.rating,
                    "notes": media.notes
                })

            watchlist.save("watchlist.json", data)
            
            break

        else:
            print("Invalid option")    


def menu():
    print("\n--- Watchlist ---")
    print("1. Add Item")
    print("2. Remove Media")
    print("3. View and Edit Watchlist")
    print("4. Search Watchlist")
    print("5. Save and Quit")

if __name__ == "__main__":
    main()
