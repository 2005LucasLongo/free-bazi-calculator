import tkinter as tk
from tkinter import messagebox
import methods.build_chart as bc
import methods.calc_elements as elements
import methods.shen_sha as shen
import datetime as dt
from datetime import timedelta

# --------------------------------------------------
# Dicionários de cores para os caracteres
# --------------------------------------------------
hs_colors = {
    "庚": "gray",
    "辛": "gray",
    "壬": "blue",
    "癸": "blue",
    "甲": "green",
    "乙": "green",
    "丙": "red",
    "丁": "red",
    "戊": "#a0522d",  # marrom amarelado
    "己": "#a0522d"
}

eb_colors = {
    "寅": "green",
    "卯": "green",
    "辰": "#a0522d",  # marrom amarelado
    "巳": "red",
    "午": "red",
    "未": "#a0522d",
    "申": "gray",
    "酉": "gray",
    "戌": "#a0522d",
    "亥": "blue",
    "子": "blue",
    "丑": "#a0522d"
}

# --------------------------------------------------
# Funções auxiliares para atualizar widgets com cores
# --------------------------------------------------
def update_heavenly_text(widget, text):
    widget.config(state="normal")
    widget.delete(0, tk.END)
    widget.insert(0, text)
    color = hs_colors.get(text, "black")
    widget.config(fg=color, state="readonly")

def update_earthly_text(widget, text):
    widget.config(state="normal")
    widget.delete(0, tk.END)
    widget.insert(0, text)
    color = eb_colors.get(text, "black")
    widget.config(fg=color, state="readonly")

# --------------------------------------------------
# Função que será chamada ao clicar em "CALCULATE"
# --------------------------------------------------
def montar_mapa_bazi():
    # Primeiro, tentamos obter dia, mês e ano (obrigatórios)
    try:
        d = int(entry_dia.get())
        m = int(entry_mes.get())
        a = int(entry_ano.get())
    except ValueError:
        messagebox.showerror("Erro", "Please insert valid numbers for day, month and year.")
        return

    # Lê se o DST está marcado (True/False)
    dst = dst_var.get()

    # Calcula pilares do dia, mês e ano
    hs_d = bc.get_day_heavenly_stem(a, m, d)
    eb_d = bc.get_day_earthly_branch(a, m, d)
    hs_m = bc.get_month_heavenly_stem(a, m, d)
    eb_m = bc.get_month_earthly_branch(a, m, d)
    hs_a = bc.get_year_heavenly_stem(a, m, d)
    eb_a = bc.get_year_earthly_branch(a, m, d)

    # Exibe pilares do dia, mês e ano com cores
    update_heavenly_text(entry_hs_dia, hs_d)
    update_earthly_text(entry_eb_dia, eb_d)
    update_heavenly_text(entry_hs_mes, hs_m)
    update_earthly_text(entry_eb_mes, eb_m)
    update_heavenly_text(entry_hs_ano, hs_a)
    update_earthly_text(entry_eb_ano, eb_a)

    # Lógica para hora
    hour_str = entry_hora.get().strip()
    has_hour = (hour_str != "")  # Para sabermos se existe pilar de hora

    if not has_hour:
        # Limpa o pilar da hora
        update_heavenly_text(entry_hs_hora, "")
        update_earthly_text(entry_eb_hora, "")

        # Calcula elementos SEM hora
        result_elements = elements.calc_element_percentage_unknown_hour(
            hs_a, eb_a, hs_m, eb_m, hs_d, eb_d
        )

        # Calcula shen sha SEM hora
        result_shen = shen.check_all_no_hour_chart(
            year_heavenly_stem=hs_a,
            year_earthly_branch=eb_a,
            month_heavenly_stem=hs_m,
            month_earthly_branch=eb_m,
            day_heavenly_stem=hs_d,
            day_earthly_branch=eb_d
        )
        # result_shen: {'year': [...], 'month': [...], 'day': [...]}
        hs_h = None  # Para uso posterior no texto
        eb_h = None

    else:
        # Verifica se a hora é válida
        try:
            h = int(hour_str)
            if not (0 <= h <= 23):
                messagebox.showerror("Erro", "Hour must be between 0 and 23.")
                return
            else:
                if dst and h == 0:
                    # if DST is checked and the person was born at midnight, we assume they were born at 23h the previous day
                    h = 23
                    previous_day = dt.datetime(a, m, d) - timedelta(days=1)
                    a = previous_day.year
                    m = previous_day.month
                    d = previous_day.day
                    print(f"Day changed to {d}/{m}/{a} due to DST.")
                    dst = False
                    
                    # Atualiza os pilares do dia, mês e ano
                    hs_d = bc.get_day_heavenly_stem(a, m, d)
                    eb_d = bc.get_day_earthly_branch(a, m, d)
                    hs_m = bc.get_month_heavenly_stem(a, m, d)
                    eb_m = bc.get_month_earthly_branch(a, m, d)
                    hs_a = bc.get_year_heavenly_stem(a, m, d)
                    eb_a = bc.get_year_earthly_branch(a, m, d)
                    
                    update_heavenly_text(entry_hs_dia, hs_d)
                    update_earthly_text(entry_eb_dia, eb_d)
                    update_heavenly_text(entry_hs_mes, hs_m)
                    update_earthly_text(entry_eb_mes, eb_m)
                    update_heavenly_text(entry_hs_ano, hs_a)
                    update_earthly_text(entry_eb_ano, eb_a)
                    
        except ValueError:
            messagebox.showerror("Erro", "Hour must be a numeric value or be empty.")
            return

        # Gera pilar da hora
        hs_h = bc.get_hour_heavenly_stem(a, m, d, h, dst)
        eb_h = bc.get_hour_earthly_branch(h, dst)

        # Exibe pilares da hora com cores
        update_heavenly_text(entry_hs_hora, hs_h)
        update_earthly_text(entry_eb_hora, eb_h)

        # Calcula elementos COM hora
        result_elements = elements.calc_element_percentage_fullchart(
            hs_a, eb_a,
            hs_m, eb_m,
            hs_d, eb_d,
            hs_h, eb_h
        )

        # Calcula shen sha COM hora
        result_shen = shen.check_all_full_chart(
            year_heavenly_stem=hs_a,
            year_earthly_branch=eb_a,
            month_heavenly_stem=hs_m,
            month_earthly_branch=eb_m,
            day_heavenly_stem=hs_d,
            day_earthly_branch=eb_d,
            hour_heavenly_stem=hs_h,
            hour_earthly_branch=eb_h
        )
        # result_shen: {'year': [...], 'month': [...], 'day': [...], 'hour': [...]}

    # Exibe os percentuais dos elementos
    text_elements.config(state="normal")
    text_elements.delete("1.0", tk.END)

    text_elements.insert(tk.END, "Elements:\n")
    for element_name, percent_value in result_elements.items():
        status = elements.get_element_status(percent_value)  # "deficient", "normal", "excessive", etc.
        line = f"{element_name.capitalize()}: {percent_value:.2f}% ({status})\n"
        text_elements.insert(tk.END, line)

    text_elements.config(state="disabled")

    # Exibe as Shen Sha
    text_shen_sha.config(state="normal")
    text_shen_sha.delete("1.0", tk.END)

    # Monta o texto semelhante ao que era exibido no terminal
    # YEAR
    text_shen_sha.insert(tk.END, f"Year pillar ({hs_a}{eb_a}):\n")
    year_stars = result_shen.get('year', [])
    if year_stars:
        for star in year_stars:
            text_shen_sha.insert(tk.END, f"- {star}\n")
    else:
        text_shen_sha.insert(tk.END, "No stars found.\n")

    text_shen_sha.insert(tk.END, "\n")  # Linha em branco

    # MONTH
    text_shen_sha.insert(tk.END, f"Month pillar ({hs_m}{eb_m}):\n")
    month_stars = result_shen.get('month', [])
    if month_stars:
        for star in month_stars:
            text_shen_sha.insert(tk.END, f"- {star}\n")
    else:
        text_shen_sha.insert(tk.END, "No stars found.\n")

    text_shen_sha.insert(tk.END, "\n")

    # DAY
    text_shen_sha.insert(tk.END, f"Day pillar ({hs_d}{eb_d}):\n")
    day_stars = result_shen.get('day', [])
    if day_stars:
        for star in day_stars:
            text_shen_sha.insert(tk.END, f"- {star}\n")
    else:
        text_shen_sha.insert(tk.END, "No stars found.\n")

    # Se a hora existe, mostramos as estrelas do pilar da hora
    if has_hour and hs_h is not None and eb_h is not None:
        text_shen_sha.insert(tk.END, "\n")
        text_shen_sha.insert(tk.END, f"Hour pillar ({hs_h}{eb_h}):\n")
        hour_stars = result_shen.get('hour', [])
        if hour_stars:
            for star in hour_stars:
                text_shen_sha.insert(tk.END, f"- {star}\n")
        else:
            text_shen_sha.insert(tk.END, "No stars found.\n")

    text_shen_sha.config(state="disabled")


# --------------------------------------------------
# Criação da janela principal (root)
# --------------------------------------------------
root = tk.Tk()
root.title("BaZi Calculator")

# Frame para as entradas de data/hora
frame_inputs = tk.Frame(root, padx=10, pady=10)
frame_inputs.pack()

# Rótulos e caixas de entrada
label_dia = tk.Label(frame_inputs, text="Day:")
label_dia.grid(row=0, column=0, sticky="e")
entry_dia = tk.Entry(frame_inputs, width=5)
entry_dia.grid(row=0, column=1, padx=5)

label_mes = tk.Label(frame_inputs, text="Month:")
label_mes.grid(row=0, column=2, sticky="e")
entry_mes = tk.Entry(frame_inputs, width=5)
entry_mes.grid(row=0, column=3, padx=5)

label_ano = tk.Label(frame_inputs, text="Year:")
label_ano.grid(row=0, column=4, sticky="e")
entry_ano = tk.Entry(frame_inputs, width=5)
entry_ano.grid(row=0, column=5, padx=5)

label_hora = tk.Label(frame_inputs, text="Hour (0-23):")
label_hora.grid(row=0, column=6, sticky="e")
entry_hora = tk.Entry(frame_inputs, width=5)
entry_hora.grid(row=0, column=7, padx=5)

# Checkbox para DST
dst_var = tk.BooleanVar()
check_dst = tk.Checkbutton(frame_inputs, text="DST", variable=dst_var)
check_dst.grid(row=0, column=8, padx=5)

# Botão para gerar o mapa
btn_gerar = tk.Button(frame_inputs, text="CALCULATE", command=montar_mapa_bazi)
btn_gerar.grid(row=0, column=9, padx=10)

# Frame para exibir o mapa
frame_mapa = tk.Frame(root, padx=10, pady=10)
frame_mapa.pack()

# Linha de títulos (H, D, M, Y)
label_titulo_h = tk.Label(frame_mapa, text="H")
label_titulo_h.grid(row=0, column=0, padx=10)
label_titulo_d = tk.Label(frame_mapa, text="D")
label_titulo_d.grid(row=0, column=1, padx=10)
label_titulo_m = tk.Label(frame_mapa, text="M")
label_titulo_m.grid(row=0, column=2, padx=10)
label_titulo_y = tk.Label(frame_mapa, text="Y")
label_titulo_y.grid(row=0, column=3, padx=10)

# Linha de Heavenly Stems (usando Entry para texto copiável)
entry_hs_hora = tk.Entry(frame_mapa, width=12, state="readonly")
entry_hs_hora.grid(row=1, column=0, padx=5, pady=5)
entry_hs_dia = tk.Entry(frame_mapa, width=12, state="readonly")
entry_hs_dia.grid(row=1, column=1, padx=5, pady=5)
entry_hs_mes = tk.Entry(frame_mapa, width=12, state="readonly")
entry_hs_mes.grid(row=1, column=2, padx=5, pady=5)
entry_hs_ano = tk.Entry(frame_mapa, width=12, state="readonly")
entry_hs_ano.grid(row=1, column=3, padx=5, pady=5)

# Linha de Earthly Branches (também com Entry)
entry_eb_hora = tk.Entry(frame_mapa, width=12, state="readonly")
entry_eb_hora.grid(row=2, column=0, padx=5, pady=5)
entry_eb_dia = tk.Entry(frame_mapa, width=12, state="readonly")
entry_eb_dia.grid(row=2, column=1, padx=5, pady=5)
entry_eb_mes = tk.Entry(frame_mapa, width=12, state="readonly")
entry_eb_mes.grid(row=2, column=2, padx=5, pady=5)
entry_eb_ano = tk.Entry(frame_mapa, width=12, state="readonly")
entry_eb_ano.grid(row=2, column=3, padx=5, pady=5)

# Frame para exibir os elementos
frame_elements = tk.Frame(root, padx=10, pady=10)
frame_elements.pack()

# Texto (read-only) para mostrar os percentuais
text_elements = tk.Text(frame_elements, width=50, height=8, state="disabled")
text_elements.pack()

# Frame para exibir as Shen Sha
frame_shen_sha = tk.Frame(root, padx=10, pady=10)
frame_shen_sha.pack()

# Texto (read-only) para mostrar as Shen Sha
text_shen_sha = tk.Text(frame_shen_sha, width=50, height=12, state="disabled")
text_shen_sha.pack()

# Inicia o loop principal da aplicação
root.mainloop()
