import tkinter as tk
from tkinter import ttk
from tkcalendar import *
import datetime
from code_files.db_sql_alchemy import *
from code_files.weather_api import *
from code_files.constant_values import *



class HomeApp(tk.Tk):
    def __init__(self):
        # main setup
        super().__init__()
        self.title('SmartHome App')
        self.geometry('500x500')
        self.minsize(500,500)
        self.maxsize(500,500)

        # widgets
        self.menu = Menu(self)



class Menu(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.place(x=0,y=0,relheight=1,relwidth=1)

        options_frame = tk.Frame(self, bg='grey')
        options_frame.pack(side=tk.LEFT)
        options_frame.pack_propagate(False)
        options_frame.configure(width=100, height=500)

        main_frame = tk.Frame(self,bg=MAIN_FRM_CLR, highlightbackground='light blue',
                              highlightthickness=2)
        main_frame.pack(side=tk.LEFT)
        main_frame.pack_propagate(False)
        main_frame.configure(width=500, height=500)

        img = Image.open(CLOUD_PATH)
        img = img.resize((150, 150))
        IMG = ImageTk.PhotoImage(img)

        img2 = Image.open(CLOTH_PATH)
        img2 = img2.resize((150, 150))
        IMG2 = ImageTk.PhotoImage(img2)


        def home_page():
            def clock_time():
                clock = time.strftime('%H:%M:%S')
                lb_clock.config(text=clock)
                lb_clock.after(200, clock_time)

            home_frame = tk.Frame(main_frame, bg=HOME_CLR)
            home_frame.pack_propagate(False)
            home_frame.configure(width=500, height=500)

            lb_clock = tk.Label(home_frame, bg=HOME_CLR,
                                   font=('Bahnschrift Bold', 30),foreground=MAIN_FRM_CLR)
            lb_clock.pack()
            clock_time()

            my_calendar = Calendar(home_frame,setmode='day',date_pattern='d/m/yy',
                                   selectbackground='#00BE9E')
            my_calendar.pack()

            lb_location = tk.Label(home_frame, text=get_location(), bg=HOME_CLR,
                                   font=('Bauhaus 93', 20),foreground=MAIN_FRM_CLR)
            lb_location.pack()

            lb_temperature = tk.Label(home_frame, text=get_temp(), bg=HOME_CLR,
                                   font=('Bahnschrift Bold', 40), foreground=MAIN_FRM_CLR)
            lb_temperature.pack()


            home_frame.pack()

        def weather_page():
            weather_frame = tk.Frame(main_frame, bg=LABEL_CLR,highlightbackground='red')
            weather_frame.pack_propagate(False)
            weather_frame.configure(width=500, height=500)

            tk.Label(weather_frame, image=IMG, bg=LABEL_CLR,).pack()

            lb_temp = tk.Label(weather_frame, text='TEMPERATURE',bg=LABEL_CLR,font=('Bahnschrift Bold', 20),foreground=MAIN_FRM_CLR)
            lb_temp.pack()
            weather_frame.pack()

            temp_frame = tk.Frame(weather_frame, bg=LABEL_CLR)

            lb_temp = tk.Label(temp_frame, text=f'{get_temp()}',bg=LABEL_CLR,
                               font=('Bahnschrift', 40),foreground='light grey')
            lb_temp.grid(column=0,row=1,padx=20)

            lb_max_low = tk.Label(temp_frame, text=f'MAX / MIN:\n{get_max_low_temp()}',bg=LABEL_CLR,
                               font=('Bahnschrift', 20),foreground='#FF6B61')
            lb_max_low.grid(column=1, row=1)

            temp_frame.pack()

            air_hum_frame = tk.Label(weather_frame, bg=LABEL_CLR)
            lb_humy = tk.Label(air_hum_frame, text=f'HUMIDITY: {get_humidity()}', bg=LABEL_CLR,
                                  font=('Bahnschrift', 20),foreground='#99FF9F')
            lb_humy.pack()

            lb_air_press = tk.Label(air_hum_frame, text=f'AIR PRESSURE: {get_air_press()}', bg=LABEL_CLR,
                                   font=('Bahnschrift', 20),foreground='#99FF9F')
            lb_air_press.pack()
            lb_home = tk.Label(air_hum_frame, text='HOME VALUES',  bg=LABEL_CLR,
                                   font=('Bahnschrift', 20),foreground=MAIN_FRM_CLR)
            lb_home.pack(pady=10)
            lb_home_temp = tk.Label(air_hum_frame, text=f'Tmp: {house_temp()} & Hum: {house_humidty()}',bg=LABEL_CLR,
                                   font=('Bahnschrift', 20),foreground=MAIN_FRM_CLR)
            lb_home_temp.pack()
            air_hum_frame.pack()

        def clothing_page():
            cloth_frame = tk.Frame(main_frame,bg=HOME_CLR)
            cloth_frame.pack_propagate(False)
            cloth_frame.configure(width=500, height=500)

            tk.Label(cloth_frame, image=IMG2, bg=HOME_CLR).pack()
            lb = tk.Label(cloth_frame, text="Please wear this:",bg=HOME_CLR ,font=('Bauhaus 93', 20),foreground=MAIN_FRM_CLR)
            lb.pack()
            lb = tk.Label(cloth_frame, text=clothing_wear(), bg=HOME_CLR,font=('Bahnschrift', 20),foreground=CLOTH_CLR)
            lb.pack()
            lb = tk.Label(cloth_frame, text='Accessories to take:', bg=HOME_CLR,font=('Bauhaus 93', 20),foreground=MAIN_FRM_CLR)
            lb.pack()
            lb = tk.Label(cloth_frame, text=accessories(), bg=HOME_CLR,font=('Bahnschrift', 20),foreground=CLOTH_CLR)
            lb.pack()

            cloth_frame.pack()

        def about_page():
            about_frame = tk.Frame(main_frame,bg=HOME_CLR)
            about_frame.pack_propagate(False)
            about_frame.configure(width=500, height=500)

            lb = tk.Label(about_frame, text="Settings page\n\nBeta version",bg=HOME_CLR, font=("Bold", 30))
            lb.pack()

            about_frame.pack()

            clock = time.strftime('%H:%M:%S')
            date = datetime.today()

            db_user = WeatherData(date,clock,get_temp(),get_humidity(),get_air_press())
            session.add(db_user)
            session.commit()


        def hide_indicators():
            home_indicate.config(bg='grey')
            menu_indicate.config(bg='grey')
            cloth_indicate.config(bg='grey')
            about_indicate.config(bg='grey')

        def delete_pages():
            for frame in main_frame.winfo_children():
                frame.destroy()

        def indicate(lb, page):
            hide_indicators()
            lb.config(bg='light blue')
            delete_pages()
            page()

        home_page()

        home_btn = tk.Button(options_frame, text='Home',
                             font=OPT_FONT,
                             fg='light blue',
                             bg='grey', bd=0,
                             command=lambda: indicate(home_indicate, home_page))
        home_btn.place(x=10, y=50)

        home_indicate = tk.Label(options_frame, text="", bg='grey')
        home_indicate.place(x=3, y=50, width=5, height=40)

        menu_btn = tk.Button(options_frame, text='Weather',
                             font=OPT_FONT,
                             fg='light blue',
                             bg='grey', bd=0,
                             command=lambda: indicate(menu_indicate, weather_page))
        menu_btn.place(x=10, y=100)

        menu_indicate = tk.Label(options_frame, text="", bg='grey')
        menu_indicate.place(x=3, y=100, width=5, height=40)

        cloth_btn = tk.Button(options_frame, text='Clothing',
                                font=OPT_FONT,
                                fg='light blue',
                                bg='grey', bd=0,
                                command=lambda: indicate(cloth_indicate, clothing_page))
        cloth_btn.place(x=10, y=150)

        cloth_indicate = tk.Label(options_frame, text="", bg='grey')
        cloth_indicate.place(x=3, y=150, width=5, height=40)

        about_btn = tk.Button(options_frame, text='Settings',
                              font=OPT_FONT,
                              fg='light blue',
                              bg='grey', bd=0,
                              command=lambda: indicate(about_indicate, about_page))
        about_btn.place(x=10, y=200)

        about_indicate = tk.Label(options_frame, text="", bg='grey')
        about_indicate.place(x=3, y=200, width=5, height=40)



