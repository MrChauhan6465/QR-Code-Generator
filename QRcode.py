"""we can genarate qrcode using two approches """

#1 ) generating simple qrcode without customizing 
def qrcode1():
    import qrcode as qr 
    image = qr.make("https://profile.w3schools.com/refresh-session?redirect_url=https%3A%2F%2Fmy-learning.w3schools.com%2F")
    image.save("w3schools.jpg")

qrcode1()



#2 ) generating qrcode with customizing 

def qrcode2():
    import qrcode as qr
    from PIL import Image 

    new_qr  = qr.QRCode(version=1,
                        error_correction=qr.constants.ERROR_CORRECT_H,
                        box_size=20,border=4,)
                    
    new_qr.add_data("https://zty.pe/")
    new_qr.make(fit=True)
    img = new_qr.make_image(fillcolor ="red",back_color ="blue")
    img.save("ztype.jpg")
qrcode2()