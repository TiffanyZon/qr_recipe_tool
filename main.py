import qrcode
import sys

file_path = "qrcode.png"


def main():

    url = input("Enter the URL: ").strip()
    if not url or not url.startswith("https://"):
        print("URL cannot be empty and has to start with 'https://'")
        return 1

    qr_code = qrcode.QRCode()

    qr_code.add_data(url)

    qr_img = qr_code.make_image()

    qr_img.save(file_path)

    print("QR Code was generated")


if __name__ == "__main__":
    main()
