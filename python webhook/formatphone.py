def format_tel(tel):
    trans_table = {ord('-') : None, ord('(') : None, ord(')') : None}


    if tel[0] == '8' or tel[0] == '7':
        new_tel = '+7' + tel[1:]
        return new_tel.translate(trans_table)
    else:
        return tel.translate(trans_table)
    

print(format_tel("8(912)98-00-5-66"))