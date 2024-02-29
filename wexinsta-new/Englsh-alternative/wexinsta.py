# wexinsta.py

import instaloader
import os
from datetime import datetime

# ANSI Color Codes for Colorful Printing
class Colors:
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    END = "\033[0m"

def display_text_art(file_name):
    try:
        with open(file_name, 'r') as file:
            art = file.read()
            print(art)
    except FileNotFoundError:
        print("Text art file not found.")
        
def display_social_media(file_name):
    try:
        with open(file_name, 'r') as file:
            social_media_info = file.read()
            print(Colors.YELLOW + social_media_info + Colors.END)
    except FileNotFoundError:
        print("Social media file not found.")
        
def get_instagram_user_info(username, log_file, L):
    try:
        profile = instaloader.Profile.from_username(L.context, username)

        print(Colors.GREEN + "User Information:" + Colors.END)
        print("Username:", profile.username)
        print("Name:", profile.full_name)
        print("Number of Followers:", profile.followers)
        print("Number of Followees:", profile.followees)
        print("Number of Posts:", profile.mediacount)
        print("Biography:", profile.biography)
        print("Profile Picture URL:", profile.profile_pic_url)
        print("Is Private Account?:", profile.is_private)
        print("Is Verified Account?:", profile.is_verified)

        # Add information to the log file
        with open(log_file, 'a') as f:
            f.write(f"\n[{datetime.now()}] {Colors.GREEN}User Information Retrieved:{Colors.END}\n")
            f.write(f"Username: {profile.username}\n")
            f.write(f"Name: {profile.full_name}\n")
            f.write(f"Number of Followers: {profile.followers}\n")
            f.write(f"Number of Followees: {profile.followees}\n")
            f.write(f"Number of Posts: {profile.mediacount}\n")
            f.write(f"Biography: {profile.biography}\n")
            f.write(f"Profile Picture URL: {profile.profile_pic_url}\n")
            f.write(f"Is Private Account?: {profile.is_private}\n")
            f.write(f"Is Verified Account?: {profile.is_verified}\n")

    except instaloader.exceptions.ProfileNotExistsException:
        print(f"{Colors.RED}Error:{Colors.END} User {username} not found.")
        with open(log_file, 'a') as f:
            f.write(f"\n[{datetime.now()}] {Colors.RED}Error:{Colors.END} User {username} not found.\n")

def get_followers_and_followees(username, log_file, L):
    try:
        profile = instaloader.Profile.from_username(L.context, username)

        print("\n" + Colors.GREEN + "Followers:" + Colors.END)
        with open(log_file, 'a') as f:
            f.write(f"\n[{datetime.now()}] {Colors.GREEN}Followers:{Colors.END}\n")
            for follower in profile.get_followers():
                print(f" - {follower.username}")
                f.write(f" - {follower.username}\n")

        print("\n" + Colors.GREEN + "Following:" + Colors.END)
        with open(log_file, 'a') as f:
            f.write(f"\n[{datetime.now()}] {Colors.GREEN}Following:{Colors.END}\n")
            for followee in profile.get_followees():
                print(f" - {followee.username}")
                f.write(f" - {followee.username}\n")

    except instaloader.exceptions.ProfileNotExistsException:
        print(f"{Colors.RED}Error:{Colors.END} User {username} not found.")
        with open(log_file, 'a') as f:
            f.write(f"\n[{datetime.now()}] {Colors.RED}Error:{Colors.END} User {username} not found.\n")
    except instaloader.exceptions.LoginRequiredException:
        print(f"{Colors.RED}Error:{Colors.END} You need to log in to fetch followers and following.")
        with open(log_file, 'a') as f:
            f.write(f"\n[{datetime.now()}] {Colors.RED}Error:{Colors.END} You need to log in to fetch followers and following.\n")

def switch_user():
    return input("Enter new username: ")

def download_igtv_and_post(username, log_file, L):
    try:
        profile = instaloader.Profile.from_username(L.context, username)

        print("\n" + Colors.GREEN + "IGTV Videos:" + Colors.END)
        with open(log_file, 'a') as f:
            f.write(f"\n[{datetime.now()}] {Colors.GREEN}IGTV Videos:{Colors.END}\n")
            for igtv_video in profile.get_igtv_posts():
                print(f" - {igtv_video.url}")
                f.write(f" - {igtv_video.url}\n")

        print("\n" + Colors.GREEN + "Stories:" + Colors.END)
        with open(log_file, 'a') as f:
            f.write(f"\n[{datetime.now()}] {Colors.GREEN}Stories:{Colors.END}\n")
            for story in profile.get_stories():
                print(f" - {story.url}")
                f.write(f" - {story.url}\n")

    except instaloader.exceptions.ProfileNotExistsException:
        print(f"{Colors.RED}Error:{Colors.END} User {username} not found.")
        with open(log_file, 'a') as f:
            f.write(f"\n[{datetime.now()}] {Colors.RED}Error:{Colors.END} User {username} not found.\n")

def download_profile_media(username, log_file, L):
    try:
        profile = instaloader.Profile.from_username(L.context, username)

        print("\n" + Colors.GREEN + "Downloading Profile Pictures and Media:" + Colors.END)
        with open(log_file, 'a') as f:
            f.write(f"\n[{datetime.now()}] {Colors.GREEN}Downloading Profile Pictures and Media:{Colors.END}\n")
            for post in profile.get_posts():
                print(f" - {post.url}")
                f.write(f" - {post.url}\n")
                L.download_post(post, target=f"{profile.username}_{post.date_utc}")

    except instaloader.exceptions.ProfileNotExistsException:
        print(f"{Colors.RED}Error:{Colors.END} User {username} not found.")
        with open(log_file, 'a') as f:
            f.write(f"\n[{datetime.now()}] {Colors.RED}Error:{Colors.END} User {username} not found.\n")

def main():
    print(Colors.BLUE + "WexInsta - Instagram Information Retrieval Tool" + Colors.END)
    username = input("Enter Instagram username: ")
    log_file = f"{username}_log.txt"
    L = instaloader.Instaloader()
    
    # Displaying Text Art
    display_text_art("textart.txt")
    
    # Displaying Social Media Info
    display_social_media("social_media.txt")

    while True:
        print("\n" + Colors.RED + "Options:" + Colors.END)
        print("1: Show User Information")
        print("2: Show Followers and Following (Login Required)")
        print("3: Show Liked Posts")
        print("4: Show IGTV Videos and Posts")
        print("5: Download Profile Pictures and Media")
        print("6: Download Videos")
        print("7: Switch User")
        print("8: Exit")

        choice = input("Please enter an option number: ")

        if choice == "1":
            get_instagram_user_info(username, log_file, L)
        elif choice == "2":
            if not L.context.is_logged_in:
                print(f"{Colors.RED}Error:{Colors.END} You can't use this option without logging in.")
                with open(log_file, 'a') as f:
                    f.write(f"\n[{datetime.now()}] {Colors.RED}Error:{Colors.END} You can't fetch followers and following without logging in.\n")
            else:
                get_followers_and_followees(username, log_file, L)
        elif choice == "3":
            print("Option to show liked posts has not been implemented yet.")
        elif choice == "4":
            download_igtv_and_post(username, log_file, L)
        elif choice == "5":
            download_profile_media(username, log_file, L)
        elif choice == "6":
            print("Option for video downloading has not been implemented yet.")
        elif choice == "7":
            username = switch_user()
            log_file = f"{username}_log.txt"
            print(f"User switched. New user: {username}")
        elif choice == "8":
            print("Exiting...")
            break
        else:
            print(f"{Colors.RED}Invalid option!{Colors.END} Please try again.")

if __name__ == "__main__":
    main()

