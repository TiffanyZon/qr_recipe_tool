import qrcode
import sys

file_path = "qrcode.png"


def main():

    url = input("Enter the URL: ").strip()

    if not url:
        print("URL cannot be empty")
        return 1
    if not url.startswith("https://"):
        print("URL must start with 'http://' or 'https://'")
        return 1

    try:
        qr_code = qrcode.QRCode()
        qr_code.add_data(url)
        qr_img = qr_code.make_image()
        qr_img.save(file_path)

        print("QR Code was generated")
        return 0
    except Exception as e:
        print(f"Failed to generate QR code: {e}")
        return 1


if __name__ == "__main__":
    main()
