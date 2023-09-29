import os
import tkinter as tk
import urllib.request
from tkinter.font import Font

if not os.path.exists("fon.png"):
    urllib.request.urlretrieve("https://province-helper.ru/fon.png", "fon.png")

def dismiss(win_t):
    win_t.grab_release()
    win_t.destroy()
def show_info(text0, button0):
    info = tk.Toplevel(window)
    info.title("Информация")
    screen_width = info.winfo_screenwidth()
    screen_height = info.winfo_screenheight()
    x = (screen_width // 2) - (500 // 2)
    y = (screen_height // 2) - (200 // 2)
    info.geometry(f'500x200+{x}+{y}')
    info.minsize(width=500, height=200)
    info.maxsize(width=500, height=200)
    info.protocol("WM_DELETE_WINDOW", lambda: dismiss(info))
    bold_font = Font(family="Arial", size=12, weight="bold")
    label = tk.Label(info, text=text0, font=bold_font)
    label.pack()
    label.place(relx=0.5, rely=0.2, anchor=tk.CENTER)
    but = tk.Button(info, text=button0, command=lambda: dismiss(info))
    but.place(x=200, y=125)
    info.grab_set()

def register():
    getlogin = login.get()
    getpass = password.get()
    if (len(getpass) == 0 or len(getlogin) == 0):
        show_info('Вы оставили пустым поле "Логин" и/или "Пароль"', "Повторить ввод")
    else:
        f_reg = False
        file_path = 'accounts.txt'
        if os.path.exists(file_path):
            file = open(file_path, "r+")
            text = file.read().split("\n")
            for j in range(len(text)-1):
                if (text[j] == ""):
                    continue
                str = text[j].split();
                if str[0] == getlogin and str[1] == getpass:
                    f_reg = True
                    break
                elif str[0] == getlogin and str[1] != getpass:
                    f_reg = "nopass"
            file.close()
        else:
            with open(file_path, 'w') as file:
                file.write('')
        if (f_reg == "nopass"):
            show_info(getlogin + ", Вы указали неверный пароль.", "Повторить попытку")
        else:
            if not f_reg:
                file = open(file_path, "r+")
                file.seek(0, os.SEEK_END)
                file.write(getlogin+' '+getpass+'\n')
                file.close()
                show_info("Добро пожаловать, " + getlogin + ". Вы успешно зарегистрировались.", "Начать игру!")
            else:
                show_info("С возвращением, "+getlogin+". Вы успешно авторизовались.", "Начать игру!")
            #label_username.place_forget()
            #label_password.place_forget()
            canvas.delete(image_id)
            login.place_forget()
            password.place_forget()
            button_register.place_forget()

window = tk.Tk()
window.title("Авторизация и регистрация")

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = (screen_width // 2) - (900 // 2)
y = (screen_height // 2) - (750 // 2)
window.geometry(f'900x750+{x}+{y}')

canvas = tk.Canvas(window, width=screen_width, height=screen_height)
image = tk.PhotoImage(file="fon.png")
image_id = canvas.create_image(0, 0, anchor=tk.NW, image=image)
canvas.pack()

#label_username = tk.Label(window, text="Имя пользователя:")
#label_password = tk.Label(window, text="Пароль:")
login = tk.Entry(window, width=30)
password = tk.Entry(window, width=30, show="•")
button_register = tk.Button(window, text="Регистрация/авторизация", command=register)

login.place(x=450, y=300)
password.place(x=450, y=350)
#label_username.place(x=300, y=300)
#label_password.place(x=300, y=350)
button_register.place(x=375, y=400)

window.mainloop()