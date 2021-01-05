def date_to_text(date):
    date = date.split("/")
    result = date[0] + " de "

    if date[1] == "01":
        result = result + "janeiro de " + date[2]
    elif date[1] == "02":
        result = result + "fevereiro de " + date[2]
    elif date[1] == "03":
        result = result + "março de " + date[2]
    elif date[1] == "04":
        result = result + "abril de " + date[2]
    elif date[1] == "05":
        result = result + "maio de " + date[2]
    elif date[1] == "06":
        result = result + "junho de " + date[2]
    elif date[1] == "07":
        result = result + "julho de " + date[2]
    elif date[1] == "08":
        result = result + "agosto de " + date[2]
    elif date[1] == "09":
        result = result + "setembro de " + date[2]
    elif date[1] == "10":
        result = result + "outubro de " + date[2]
    elif date[1] == "11":
        result = result + "novembro de " + date[2]
    elif date[1] == "12":
        result = result + "dezembro de " + date[2]
    print(result)


date_to_text("22/07/1999")
