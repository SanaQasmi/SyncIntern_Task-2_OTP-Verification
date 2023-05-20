import random
import tkinter as tk
from tkinter import messagebox

def generate_otp():
    otp = ""
    for _ in range(6):
        otp += str(random.randint(0, 9))
    return otp

def send_otp(phone_number, otp):
    
    print(f"OTP sent to {phone_number}: {otp}")

def verify_otp():
    user_otp = otp_entry.get()


    if user_otp == generated_otp:
        messagebox.showinfo("OTP Verification", "OTP Verification Successful!")
    else:
        messagebox.showerror("OTP Verification", "OTP Verification Failed!")


window = tk.Tk()
window.title("OTP Verification")
window.geometry("400x300")

phone_number = "+5207089244"
generated_otp = generate_otp()
send_otp(phone_number, generated_otp)


otp_label = tk.Label(window, text="ENTER THE OTP:",width=20, height=2,fg="red",font=("Wide Latin", 12, "bold"))
otp_label.pack()

otp_entry = tk.Entry(window, show="*")
otp_entry.pack()

verify_button = tk.Button(window, text="VERIFY", command=verify_otp,fg="blue",font=("Times New Roman", 12, "bold"))
verify_button.pack()


window.mainloop()


#Python3 OTP Verification_Sana Qasmi