# WexInsta - Instagram Bilgi Çekme Aracı

Bu araç, Instagram kullanıcıları hakkında bilgi çekmek için kullanılan bir Python uygulamasıdır. 

## Kurulum

1. Python'u indirin ve yükleyin: [Python İndirme Sayfası](https://www.python.org/downloads/)

2. Proje dizinine gidin:

    ```bash
    cd /path/to/wexinsta
    ```

3. Virtual environment oluşturun (isteğe bağlı):

    ```bash
    python -m venv venv
    ```

4. Virtual environment'ı etkinleştirin:

    - **Linux/Mac:**
    
        ```bash
        source venv/bin/activate
        ```

    - **Windows:**
    
        ```bash
        .\venv\Scripts\activate
        ```

5. Gerekli bağımlılıkları yükleyin:

    ```bash
    pip install -r requirements.txt
    ```

6. Uygulamayı çalıştırın:

    ```bash
    python wexinsta.py
    ```

## Kullanım

1. Uygulamayı çalıştırdığınızda, Instagram kullanıcı adınızı girin.

2. Menüden istediğiniz seçeneği seçin.

    - Seçenekler:
        - 1: Kullanıcı Bilgileri Göster
        - 2: Takipçileri ve Takip Edilenleri Göster
        - 3: Beğenilen Gönderileri Göster
        - 4: IGTV Videoları ve Hikayeleri Göster
        - 5: Profil Fotoğrafları ve Medyayı İndir
        - 6: Çıkış

3. Seçiminize göre talimatları takip edin.

## Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Daha fazla bilgi için [LICENSE](LICENSE) dosyasına göz atın.
