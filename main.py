import qrcode
import sys

file_path = "qrcode.png"


def main():

    url = "https://www.hemkop.se/recept/asia_tofu?gclsrc=aw.ds&gad_source=1&gad_campaignid=12258323741&gbraid=0AAAAADQyiMC-GmfUGQtpPlfoaJaMwb_Le&gclid=CjwKCAiA-__MBhAKEiwASBmsBNjFVeXRWnLjBeKaJt0t2s3Uu89Duc6uwNzwckCnsY7-5BYNbDMtEBoCCCQQAvD_BwE"

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
