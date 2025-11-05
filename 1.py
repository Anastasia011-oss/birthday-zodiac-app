import tkinter as tk

root = tk.Tk()
root.title("Знак зодиака")
root.geometry("450x550")
root.configure(bg="#f2f2f2")

label_title = tk.Label(root, text="Введите дату рождения:", font=("Arial", 14, "bold"), bg="#f2f2f2")
label_title.pack(pady=(20, 10))

frame = tk.Frame(root, bg="#f2f2f2")
frame.pack(pady=10)

tk.Label(frame, text="День:", font=("Arial", 12), bg="#f2f2f2").grid(row=0, column=0, padx=5)
entry_day = tk.Entry(frame, font=("Arial", 12), width=5, justify="center")
entry_day.grid(row=0, column=1, padx=5)

tk.Label(frame, text="Месяц:", font=("Arial", 12), bg="#f2f2f2").grid(row=0, column=2, padx=5)
entry_month = tk.Entry(frame, font=("Arial", 12), width=5, justify="center")
entry_month.grid(row=0, column=3, padx=5)

tk.Label(frame, text="Год:", font=("Arial", 12), bg="#f2f2f2").grid(row=0, column=4, padx=5)
entry_year = tk.Entry(frame, font=("Arial", 12), width=7, justify="center")
entry_year.grid(row=0, column=5, padx=5)

label_res = tk.Label(root, text="", font=("Arial", 18, "bold"), bg="#f2f2f2", wraplength=400)
label_res.pack(pady=20)

label_desc = tk.Label(root, text="", font=("Arial", 12), bg="#f2f2f2", wraplength=400, justify="center")
label_desc.pack(pady=10)

zodiac_info = {
    "Овен": {"color": "#FF5733", "desc": "Активный, смелый и решительный. Любит быть лидером и идти вперёд."},
    "Телец": {"color": "#27AE60", "desc": "Надёжный, терпеливый и любит комфорт. Ценит стабильность и красоту."},
    "Близнецы": {"color": "#00B0F0", "desc": "Любопытный, разговорчивый и энергичный. Всегда в движении и поиске нового."},
    "Рак": {"color": "#2E86C1", "desc": "Чуткий, заботливый и семейный. Ценит уют и эмоциональную связь."},
    "Лев": {"color": "#F1C40F", "desc": "Щедрый, уверенный и творческий. Любит внимание и быть в центре событий."},
    "Дева": {"color": "#45B39D", "desc": "Умная, внимательная к деталям и практичная. Любит порядок и помогает другим."},
    "Весы": {"color": "#BB8FCE", "desc": "Дипломатичный, справедливый и дружелюбный. Стремится к гармонии во всём."},
    "Скорпион": {"color": "#8E44AD", "desc": "Страстный, сильный и загадочный. Имеет глубокие эмоции и мощную интуицию."},
    "Стрелец": {"color": "#E67E22", "desc": "Оптимистичный, свободолюбивый и честный. Любит приключения и знания."},
    "Козерог": {"color": "#616A6B", "desc": "Трудолюбивый, целеустремлённый и ответственный. Ценит дисциплину и успех."},
    "Водолей": {"color": "#5DADE2", "desc": "Оригинальный, независимый и доброжелательный. Думает нестандартно и любит перемены."},
    "Рыбы": {"color": "#48C9B0", "desc": "Мечтательный, добрый и интуитивный. Часто живёт в мире фантазий и чувств."}
}

def get_zodiac_sign(day, month):
    if (month == 3 and day >= 21) or (month == 4 and day <= 20):
        return "Овен"
    elif (month == 4 and day >= 21) or (month == 5 and day <= 21):
        return "Телец"
    elif (month == 5 and day >= 22) or (month == 6 and day <= 21):
        return "Близнецы"
    elif (month == 6 and day >= 22) or (month == 7 and day <= 22):
        return "Рак"
    elif (month == 7 and day >= 23) or (month == 8 and day <= 21):
        return "Лев"
    elif (month == 8 and day >= 22) or (month == 9 and day <= 23):
        return "Дева"
    elif (month == 9 and day >= 24) or (month == 10 and day <= 23):
        return "Весы"
    elif (month == 10 and day >= 24) or (month == 11 and day <= 22):
        return "Скорпион"
    elif (month == 11 and day >= 23) or (month == 12 and day <= 22):
        return "Стрелец"
    elif (month == 12 and day >= 23) or (month == 1 and day <= 20):
        return "Козерог"
    elif (month == 1 and day >= 21) or (month == 2 and day <= 19):
        return "Водолей"
    elif (month == 2 and day >= 20) or (month == 3 and day <= 20):
        return "Рыбы"

def show_zodiac():
    try:
        day = int(entry_day.get())
        month = int(entry_month.get())
        year = int(entry_year.get())
        sign = get_zodiac_sign(day, month)

        if not sign:
            raise ValueError

        info = zodiac_info[sign]
        color = info["color"]
        desc = info["desc"]

        label_res.config(text=f"Поздравляю! Ваш знак зодиака: {sign}", fg=color)
        label_desc.config(text=desc, fg=color)

    except:
        label_res.config(text="Ошибка: введите корректную дату!", fg="red")
        label_desc.config(text="", fg="black")

btn = tk.Button(root, text="Узнать знак зодиака", command=show_zodiac,
                font=("Arial", 13, "bold"), bg="#4CAF50", fg="white", width=25)
btn.pack(pady=10)

root.mainloop()
