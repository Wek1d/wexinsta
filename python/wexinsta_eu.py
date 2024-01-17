# wexinsta_eu.py

import instaloader
import os
from datetime import datetime

# ANSI Color Codes for Colored Printing
class Colors:
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    END = "\033[0m"

def get_instagram_user_info(username, log_file, L):
    try:
        profile = instaloader.Profile.from_username(L.context, username)

        print(Colors.GREEN + "User Information:" + Colors.END)
        print("Username:", profile.username)
        print("Full Name:", profile.full_name)
        print("Followers:", profile.followers)
        print("Following:", profile.followees)
        print("Post Count:", profile.mediacount)
        print("Biography:", profile.biography)
        print("Profile Picture URL:", profile.profile_pic_url)
        print("Private Account?:", profile.is_private)
        print("Verified Account?:", profile.is_verified)

        # Add information to the log file
        with open(log_file, 'a') as f:
            f.write(f"\n[{datetime.now()}] {Colors.GREEN}User Information Retrieved:{Colors.END}\n")
            f.write(f"Username: {profile.username}\n")
            f.write(f"Full Name: {profile.full_name}\n")
            f.write(f"Followers: {profile.followers}\n")
            f.write(f"Following: {profile.followees}\n")
            f.write(f"Post Count: {profile.mediacount}\n")
            f.write(f"Biography: {profile.biography}\n")
            f.write(f"Profile Picture URL: {profile.profile_pic_url}\n")
            f.write(f"Private Account?: {profile.is_private}\n")
            f.write(f"Verified Account?: {profile.is_verified}\n")

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
        print(f"{Colors.RED}Error:{Colors.END} You need to be logged in to retrieve followers and followees.")
        with open(log_file, 'a') as f:
            f.write(f"\n[{datetime.now()}] {Colors.RED}Error:{Colors.END} You need to be logged in to retrieve followers and followees.\n")

def switch_user():
    return input("Enter the new username: ")

def download_igtv_and_stories(username, log_file, L):
    try:
        profile = instaloader.Profile.from_username(L.context, username)

        print("\n" + Colors.GREEN + "IGTV Videos:" + Colors.END)
        with open(log_file, 'a') as f:
            f.write(f"\n[{datetime.now()}] {Colors.GREEN}IGTV Videos:{Colors.END}\n")
            for igtv_video in profile.get_igtv():
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

        print("\n" + Colors.GREEN + "Profile Photos and Media Download:" + Colors.END)
        with open(log_file, 'a') as f:
            f.write(f"\n[{datetime.now()}] {Colors.GREEN}Profile Photos and Media Download:{Colors.END}\n")
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
    username = input("Enter the Instagram username: ")
    log_file = f"{username}_log.txt"
    L = instaloader.Instaloader()

    while True:
        print("\n" + Colors.YELLOW + "Options:" + Colors.END)
        print("1: Show User Information")
        print("2: Show Followers and Following (Login Required)")
        print("3: Show Liked Posts")
        print("4: Show IGTV Videos and Stories")
        print("5: Download Profile Photos and Media")
        print("6: Video Download")
        print("7: Switch User")
        print("8: Exit")

        choice = input("Please enter an option number: ")

        if choice == "1":
            get_instagram_user_info(username, log_file, L)
        elif choice == "2":
            # Handle error of fetching followers and followees without logging in
            if not L.context.is_logged_in:
                print(f"{Colors.RED}Error:{Colors.END} You cannot use this option without logging in.")
                with open(log_file, 'a') as f:
                    f.write(f"\n[{datetime.now()}] {Colors.RED}Error:{Colors.END} You cannot fetch followers and followees without logging in.\n")
            else:
                get_followers_and_followees(username, log_file, L)
        elif choice == "3":
            # Show Liked Posts
            pass
        elif choice == "4":
            download_igtv_and_stories(username, log_file, L)
        elif choice == "5":
            download_profile_media(username, log_file, L)
        elif choice == "6":
            # Video Download
            pass
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

