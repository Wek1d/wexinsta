# wexinsta.py

import instaloader
import os
from datetime import datetime

# Renkli Yazdırma için ANSI Renk Kodları
class Colors:
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    END = "\033[0m"

def get_instagram_user_info(username, log_file, L):
    try:
        profile = instaloader.Profile.from_username(L.context, username)

        print(Colors.GREEN + "Kullanıcı Bilgileri:" + Colors.END)
        print("Kullanıcı Adı:", profile.username)
        print("İsim:", profile.full_name)
        print("Takipçi Sayısı:", profile.followers)
        print("Takip Ettiği Sayısı:", profile.followees)
        print("Gönderi Sayısı:", profile.mediacount)
        print("Biyografi:", profile.biography)
        print("Profil Fotoğrafı URL:", profile.profile_pic_url)
        print("Özel Hesap mı?:", profile.is_private)
        print("Onaylı Hesap mı?:", profile.is_verified)

        # Log dosyasına bilgileri ekle
        with open(log_file, 'a') as f:
            f.write(f"\n[{datetime.now()}] {Colors.GREEN}Kullanıcı Bilgileri Çekildi:{Colors.END}\n")
            f.write(f"Kullanıcı Adı: {profile.username}\n")
            f.write(f"İsim: {profile.full_name}\n")
            f.write(f"Takipçi Sayısı: {profile.followers}\n")
            f.write(f"Takip Ettiği Sayısı: {profile.followees}\n")
            f.write(f"Gönderi Sayısı: {profile.mediacount}\n")
            f.write(f"Biyografi: {profile.biography}\n")
            f.write(f"Profil Fotoğrafı URL: {profile.profile_pic_url}\n")
            f.write(f"Özel Hesap mı?: {profile.is_private}\n")
            f.write(f"Onaylı Hesap mı?: {profile.is_verified}\n")

    except instaloader.exceptions.ProfileNotExistsException:
        print(f"{Colors.RED}Hata:{Colors.END} {username} adlı kullanıcı bulunamadı.")
        with open(log_file, 'a') as f:
            f.write(f"\n[{datetime.now()}] {Colors.RED}Hata:{Colors.END} {username} adlı kullanıcı bulunamadı.\n")

def get_followers_and_followees(username, log_file, L):
    try:
        profile = instaloader.Profile.from_username(L.context, username)

        print("\n" + Colors.GREEN + "Takipçiler:" + Colors.END)
        with open(log_file, 'a') as f:
            f.write(f"\n[{datetime.now()}] {Colors.GREEN}Takipçiler:{Colors.END}\n")
            for follower in profile.get_followers():
                print(f" - {follower.username}")
                f.write(f" - {follower.username}\n")

        print("\n" + Colors.GREEN + "Takip Edilenler:" + Colors.END)
        with open(log_file, 'a') as f:
            f.write(f"\n[{datetime.now()}] {Colors.GREEN}Takip Edilenler:{Colors.END}\n")
            for followee in profile.get_followees():
                print(f" - {followee.username}")
                f.write(f" - {followee.username}\n")

    except instaloader.exceptions.ProfileNotExistsException:
        print(f"{Colors.RED}Hata:{Colors.END} {username} adlı kullanıcı bulunamadı.")
        with open(log_file, 'a') as f:
            f.write(f"\n[{datetime.now()}] {Colors.RED}Hata:{Colors.END} {username} adlı kullanıcı bulunamadı.\n")
    except instaloader.exceptions.LoginRequiredException:
        print(f"{Colors.RED}Hata:{Colors.END} Takipçi ve Takip Edilenleri çekmek için giriş yapmalısınız.")
        with open(log_file, 'a') as f:
            f.write(f"\n[{datetime.now()}] {Colors.RED}Hata:{Colors.END} Takipçi ve Takip Edilenleri çekmek için giriş yapmalısınız.\n")

def switch_user():
    return input("Yeni kullanıcı adı girin: ")

def download_igtv_and_stories(username, log_file, L):
    try:
        profile = instaloader.Profile.from_username(L.context, username)

        print("\n" + Colors.GREEN + "IGTV Videoları:" + Colors.END)
        with open(log_file, 'a') as f:
            f.write(f"\n[{datetime.now()}] {Colors.GREEN}IGTV Videoları:{Colors.END}\n")
            for igtv_video in profile.get_igtv():
                print(f" - {igtv_video.url}")
                f.write(f" - {igtv_video.url}\n")

        print("\n" + Colors.GREEN + "Hikayeler:" + Colors.END)
        with open(log_file, 'a') as f:
            f.write(f"\n[{datetime.now()}] {Colors.GREEN}Hikayeler:{Colors.END}\n")
            for story in profile.get_stories():
                print(f" - {story.url}")
                f.write(f" - {story.url}\n")

    except instaloader.exceptions.ProfileNotExistsException:
        print(f"{Colors.RED}Hata:{Colors.END} {username} adlı kullanıcı bulunamadı.")
        with open(log_file, 'a') as f:
            f.write(f"\n[{datetime.now()}] {Colors.RED}Hata:{Colors.END} {username} adlı kullanıcı bulunamadı.\n")

def download_profile_media(username, log_file, L):
    try:
        profile = instaloader.Profile.from_username(L.context, username)

        print("\n" + Colors.GREEN + "Profil Fotoğrafları ve Medya İndirme:" + Colors.END)
        with open(log_file, 'a') as f:
            f.write(f"\n[{datetime.now()}] {Colors.GREEN}Profil Fotoğrafları ve Medya İndirme:{Colors.END}\n")
            for post in profile.get_posts():
                print(f" - {post.url}")
                f.write(f" - {post.url}\n")
                L.download_post(post, target=f"{profile.username}_{post.date_utc}")

    except instaloader.exceptions.ProfileNotExistsException:
        print(f"{Colors.RED}Hata:{Colors.END} {username} adlı kullanıcı bulunamadı.")
        with open(log_file, 'a') as f:
            f.write(f"\n[{datetime.now()}] {Colors.RED}Hata:{Colors.END} {username} adlı kullanıcı bulunamadı.\n")

def main():
    print(Colors.BLUE + "WexInsta - Instagram Bilgi Çekme Aracı" + Colors.END)
    kullanici_adi = input("Instagram kullanıcı adını girin: ")
    log_file = f"{kullanici_adi}_log.txt"
    L = instaloader.Instaloader()

    while True:
        print("\n" + Colors.YELLOW + "Seçenekler:" + Colors.END)
        print("1: Kullanıcı Bilgileri Göster")
        print("2: Takipçileri ve Takip Edilenleri Göster (Giriş Yapılması Gerekiyor)")
        print("3: Beğenilen Gönderileri Göster")
        print("4: IGTV Videoları ve Hikayeleri Göster")
        print("5: Profil Fotoğrafları ve Medyayı İndir")
        print("6: Video İndirme")
        print("7: Kullanıcı Değiştir")
        print("8: Çıkış")

        secim = input("Lütfen bir seçenek numarası girin: ")

        if secim == "1":
            get_instagram_user_info(kullanici_adi, log_file, L)
        elif secim == "2":
            # Giriş yapmadan takipçi ve takip edilenleri çekme hatasını ele al
            if not L.context.is_logged_in:
                print(f"{Colors.RED}Hata:{Colors.END} Giriş yapmadan bu seçeneği kullanamazsınız.")
                with open(log_file, 'a') as f:
                    f.write(f"\n[{datetime.now()}] {Colors.RED}Hata:{Colors.END} Giriş yapmadan takipçi ve takip edilenleri çekemezsiniz.\n")
            else:
                get_followers_and_followees(kullanici_adi, log_file, L)
        elif secim == "3":
            # Beğenilen Gönderileri Göster
            pass
        elif secim == "4":
            download_igtv_and_stories(kullanici_adi, log_file, L)
        elif secim == "5":
            download_profile_media(kullanici_adi, log_file, L)
        elif secim == "6":
            # Video İndirme
            pass
        elif secim == "7":
            kullanici_adi = switch_user()
            log_file = f"{kullanici_adi}_log.txt"
            print(f"Kullanıcı değiştirildi. Yeni kullanıcı: {kullanici_adi}")
        elif secim == "8":
            print("Çıkılıyor...")
            break
        else:
            print(f"{Colors.RED}Geçersiz seçenek!{Colors.END} Lütfen tekrar deneyin.")

if __name__ == "__main__":
    main()
