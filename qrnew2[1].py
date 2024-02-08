import tkinter as tk
from tkinter import Entry, Label, Button, StringVar
import qrcode

class QRCodeGeneratorApp:
    def __init__(self, master):
        self.master = master
        master.title("QR Code Generator")
        master.geometry("500x300")  

        self.master.configure(bg='#F0F0F0')
        self.label = Label(master, text="Enter the link here :", font=("Arial", 14), bg='#F0F0F0')
        self.label.pack(pady=10)

        self.entry = Entry(master, width=40, font=("Arial", 12))
        self.entry.pack(pady=10)

        self.filename_label = Label(master, text="Enter QR code filename:", font=("Arial", 14), bg='#F0F0F0')
        self.filename_label.pack(pady=10)

        self.filename_entry = Entry(master, width=40, font=("Arial", 12))
        self.filename_entry.pack(pady=10)

        self.generate_button = Button(master, text="Generate QR Code", command=self.generate_qr_code, font=("Arial", 14), bg='#4CAF50', fg='white')
        self.generate_button.pack(pady=20)

    def generate_qr_code(self):
        data_to_encode = self.entry.get()
        filename = self.filename_entry.get() or "generated_qrcode"  

        if data_to_encode:
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(data_to_encode)
            qr.make(fit=True)

            img = qr.make_image(fill_color="#4CAF50", back_color="white")

            # Save the image of qr
            img.save(f"{filename}.png")

            result_label = Label(self.master, text=f"QR code generated and saved as '{filename}.png'", font=("Arial", 12), bg='#F0F0F0')
            result_label.pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = QRCodeGeneratorApp(root)
    root.mainloop()
