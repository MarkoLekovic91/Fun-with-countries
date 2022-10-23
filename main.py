from tkinter import *
from playsound import playsound
import csv

THEME_COLOR ="sandybrown"


def display():
    global img_flag, img_flags,territory_img,territory_img1

    country_label1.grid(row=1, column=1,pady=10,padx=20)
    capital_city1.grid(row=4, column=1,pady=10,padx=20)
    continent_label1.grid(row=5, column=1,pady=10,padx=20)
    population_label1.grid(row=2, column=1,pady=10,padx=20)
    land_area_label1.grid(row=3, column=1,pady=10,padx=20)
    border_label1.grid(row=6,column=1,columnspan=2,pady=10,padx=20)
    ccp.grid(row=4,column=2,padx=20)
    anthem.grid(row=7,column=1,pady=10,padx=20)


    entered_country = input_country.get()






    with open("data.csv", mode="r") as data1:


        for line in data1:
            data_list = data1.readlines()
            for i in range(0, 195):

                    if data_list[i].split(",")[0] == entered_country:
                        if entered_country == "CAR":
                            img_flag = PhotoImage(file=f'Drzave/{data_list[i].split(",")[0]}.png')
                            img_flags = canvas.create_image(50, 50, image=img_flag)
                            territory_img = PhotoImage(file=f'Drzave/{data_list[i].split(",")[0]}.png')
                            territory_img1 = canvas1.create_image(50,50,image=territory_img)
                            country_label1.config(text='Central African Republic', font=("Arial", 15, "italic"),
                                                  bg=THEME_COLOR)
                            continent_label1.config(text=f' {data_list[i].split(",")[3]}', font=("Arial", 15, "italic"),
                                                    bg=THEME_COLOR)
                            population_label1.config(text=f'{data_list[i].split(",")[1]}', font=("Arial", 15, "italic"),
                                                     bg=THEME_COLOR)
                            land_area_label1.config(text=f'{data_list[i].split(",")[2]} km²',
                                                    font=("Arial", 15, "italic"), bg=THEME_COLOR)
                            capital_city1.config(text=f'{data_list[i].split(",")[5]}', font=("Arial", 15, "italic"),
                                                 bg=THEME_COLOR)
                            ccp.config(text=f'{data_list[i].split(",")[7]}', font=("Arial", 15, "italic"),
                                                 bg=THEME_COLOR)
                            border_label1.config(text=f'{data_list[i].split(",")[6]}', font=("Arial", 15, "italic"),
                                                 bg=THEME_COLOR)

                        elif entered_country == "UK":
                            img_flag = PhotoImage(file=f'Drzave/{data_list[i].split(",")[0]}.png')
                            img_flags = canvas.create_image(50, 50, image=img_flag)
                            territory_img = PhotoImage(file=f'Teritorije/{data_list[i].split(",")[0]}.png')
                            territory_img1 = canvas1.create_image(50,50,image=territory_img)
                            country_label1.config(text='United Kingdom', font=("Arial", 15, "italic"),
                                                  bg=THEME_COLOR)
                            continent_label1.config(text=f' {data_list[i].split(",")[3]}', font=("Arial", 15, "italic"),
                                                    bg=THEME_COLOR)
                            population_label1.config(text=f'{data_list[i].split(",")[1]}', font=("Arial", 15, "italic"),
                                                     bg=THEME_COLOR)
                            land_area_label1.config(text=f'{data_list[i].split(",")[2]} km²',
                                                    font=("Arial", 15, "italic"), bg=THEME_COLOR)
                            capital_city1.config(text=f'{data_list[i].split(",")[5]}',
                                                 font=("Arial", 15, "italic"),
                                                 bg=THEME_COLOR)
                            ccp.config(text=f'{data_list[i].split(",")[7]}', font=("Arial", 15, "italic"),
                                       bg=THEME_COLOR)
                            border_label1.config(text=f'{data_list[i].split(",")[6]}', font=("Arial", 15, "italic"),
                                                 bg=THEME_COLOR)
                        elif entered_country == "USA":
                            img_flag = PhotoImage(file=f'Drzave/{data_list[i].split(",")[0]}.png')
                            img_flags = canvas.create_image(50, 50, image=img_flag)
                            territory_img = PhotoImage(file=f'Teritorije/{data_list[i].split(",")[0]}.png')
                            territory_img1 = canvas1.create_image(50,50,image=territory_img)
                            country_label1.config(text='United States of America', font=("Arial", 15, "italic"),
                                                  bg=THEME_COLOR)
                            continent_label1.config(text=f' {data_list[i].split(",")[3]}', font=("Arial", 15, "italic"),
                                                    bg=THEME_COLOR)
                            population_label1.config(text=f'{data_list[i].split(",")[1]}', font=("Arial", 15, "italic"),
                                                     bg=THEME_COLOR)
                            land_area_label1.config(text=f'{data_list[i].split(",")[2]} km²',
                                                    font=("Arial", 15, "italic"), bg=THEME_COLOR)
                            capital_city1.config(text=f'{data_list[i].split(",")[5]}',
                                                 font=("Arial", 15, "italic"),
                                                 bg=THEME_COLOR)
                            ccp.config(text=f'{data_list[i].split(",")[7]}', font=("Arial", 15, "italic"),
                                       bg=THEME_COLOR)
                            border_label1.config(text=f'{data_list[i].split(",")[6]}', font=("Arial", 15, "italic"),
                                                 bg=THEME_COLOR)

                        elif entered_country == "UAE":
                            img_flag = PhotoImage(file=f'Drzave/{data_list[i].split(",")[0]}.png')
                            img_flags = canvas.create_image(50, 50, image=img_flag)
                            territory_img = PhotoImage(file=f'Teritorije/{data_list[i].split(",")[0]}.png')
                            territory_img1 = canvas1.create_image(50,50,image=territory_img)
                            country_label1.config(text='United Arab Emirates', font=("Arial", 15, "italic"),
                                                  bg=THEME_COLOR)
                            continent_label1.config(text=f' {data_list[i].split(",")[3]}', font=("Arial", 15, "italic"),
                                                    bg=THEME_COLOR)
                            population_label1.config(text=f'{data_list[i].split(",")[1]}', font=("Arial", 15, "italic"),
                                                     bg=THEME_COLOR)
                            land_area_label1.config(text=f'{data_list[i].split(",")[2]} km²',
                                                    font=("Arial", 15, "italic"), bg=THEME_COLOR)
                            capital_city1.config(text=f'{data_list[i].split(",")[5]}',
                                                 font=("Arial", 15, "italic"),
                                                 bg=THEME_COLOR)
                            ccp.config(text=f'{data_list[i].split(",")[7]}', font=("Arial", 15, "italic"),
                                       bg=THEME_COLOR)
                            border_label1.config(text=f'{data_list[i].split(",")[6]}', font=("Arial", 15, "italic"),
                                                 bg=THEME_COLOR)

                        elif entered_country == "DRC":
                            img_flag = PhotoImage(file=f'Drzave/{data_list[i].split(",")[0]}.png')
                            img_flags = canvas.create_image(50, 50, image=img_flag)
                            territory_img = PhotoImage(file=f'Teritorije/{data_list[i].split(",")[0]}.png')
                            territory_img1 = canvas1.create_image(50,50,image=territory_img)
                            country_label1.config(text='Democratic Republic of the Congo', font=("Arial", 15, "italic"),
                                                  bg=THEME_COLOR)
                            continent_label1.config(text=f' {data_list[i].split(",")[3]}', font=("Arial", 15, "italic"),
                                                    bg=THEME_COLOR)
                            population_label1.config(text=f'{data_list[i].split(",")[1]}', font=("Arial", 15, "italic"),
                                                     bg=THEME_COLOR)
                            land_area_label1.config(text=f'{data_list[i].split(",")[2]} km²',
                                                    font=("Arial", 15, "italic"), bg=THEME_COLOR)
                            capital_city1.config(text=f'{data_list[i].split(",")[5]}',
                                                 font=("Arial", 15, "italic"),
                                                 bg=THEME_COLOR)
                            ccp.config(text=f'{data_list[i].split(",")[7]}', font=("Arial", 15, "italic"),
                                       bg=THEME_COLOR)
                            border_label1.config(text=f'{data_list[i].split(",")[6]}', font=("Arial", 15, "italic"),
                                                 bg=THEME_COLOR)

                        else:

                            img_flag = PhotoImage(file=f'Drzave/{data_list[i].split(",")[0]}.png')
                            img_flags = canvas.create_image(50, 50, image=img_flag)
                            territory_img = PhotoImage(file=f'Teritorije/{data_list[i].split(",")[0]}.png')
                            territory_img1 = canvas1.create_image(50,50,image=territory_img)
                            country_label1.config(text=f'{data_list[i].split(",")[0]}', font=("Arial", 15, "italic"),
                                              bg=THEME_COLOR)
                            continent_label1.config(text=f' {data_list[i].split(",")[3]}', font=("Arial", 15, "italic"),bg=THEME_COLOR)
                            population_label1.config(text=f'{data_list[i].split(",")[1]}', font=("Arial", 15, "italic"),bg=THEME_COLOR)
                            land_area_label1.config(text=f'{data_list[i].split(",")[2]} km²', font=("Arial", 15, "italic"),bg=THEME_COLOR)
                            capital_city1.config(text=f'{data_list[i].split(",")[5]}',
                                                 font=("Arial", 15, "italic"),
                                                 bg=THEME_COLOR)
                            ccp.config(text=f'{data_list[i].split(",")[7]}', font=("Arial", 15, "italic"),
                                       bg=THEME_COLOR)
                            border_label1.config(text=f'{data_list[i].split(",")[6]}', font=("Arial", 15, "italic"),
                                             bg=THEME_COLOR)
                            anthem.config(text=f'{data_list[i].split(",")[9]}', font=("Arial", 15, "italic"),
                                             bg=THEME_COLOR)
                            playsound(f'himne/{data_list[i].split(",")[0]}.mp3')

                            button_play = Button(text="PLAY", fg="white", bg="green", width=10,
                                                 font=("Arial", 10, "bold"))
                            button_play.grid(row=7, column=2)




                    input_country.delete(0,END)




window = Tk()
window.title("Fun With Countries")
window.config(width=1000,height=1000,bg=THEME_COLOR,pady=20,padx=20)

country_label = Label(text="Country: ", font=("Arial", 15, "bold"), bg=THEME_COLOR)
country_label.grid(row=1, column=0)

capital_city = Label(text="Capital City/Population: ", font=("Arial", 15, "bold"), bg=THEME_COLOR)
capital_city.grid(row=4, column=0)

# empty_label = Label()
# empty_label.grid(row=7,column=0)
# empty_label1 = Label()
# empty_label1.grid(row=7,column=1)

land_area_label1 = Label()
capital_city1 = Label()
continent_label1 = Label()
population_label1 = Label()
country_label1 = Label()
border_label1 = Label()
ccp = Label()
anthem = Label()

population_label = Label(text="Population: ", font=("Arial", 15, "bold"), bg=THEME_COLOR)
population_label.grid(row=2,column=0)

land_area_label = Label(text="Land Area: ", font=("Arial", 15, "bold"), bg=THEME_COLOR)
land_area_label.grid(row=3,column=0)

border_label = Label(text="Borders: ", font=("Arial", 15, "bold"), bg=THEME_COLOR)
border_label.grid(row=6,column=0)

flag_label = Label(text="Flag/Territory: ", font=("Arial", 15, "bold"), bg=THEME_COLOR)
flag_label.grid(row=0,column=0)

continent_label = Label(text="Continent: ", font=("Arial", 15, "bold"), bg=THEME_COLOR)
continent_label.grid(row=5,column=0)

anthem_label = Label(text="Anthem: ", font=("Arial", 15, "bold"), bg=THEME_COLOR)
anthem_label.grid(row=7,column=0)



# territory_label = Label(text="Territory: ", font=("Arial", 15, "bold"), bg=THEME_COLOR)
# territory_label.grid(row=7,column=0)


canvas = Canvas(width=100,height=100,bg=THEME_COLOR,highlightthickness=0)
img_flag = PhotoImage(file="Drzave/allflags.png")
img_flags = canvas.create_image(50,50,image=img_flag)
canvas.grid(row=0,column=1)

canvas1 = Canvas(width=100,height=100,highlightthickness=0,bg=THEME_COLOR)
territory_img = PhotoImage(file="Teritorije/worldmap.png")
territory_img1 = canvas1.create_image(50,50,image=territory_img)


canvas1.grid(row=0,column=2)

input_country = Entry(width=30,font=("Arial",15,"bold"))
input_country.grid(row=9,column=0,columnspan=2,pady=20)


button_next = Button(text="→",fg="white",bg="green",width= 10,font=("Arial",10,"bold"),command=display)
button_next.grid(row=9,column=2)














window.mainloop()
