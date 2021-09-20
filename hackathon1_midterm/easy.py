from datetime import datetime

# 1
# Viết hàm day_diff() nhận vào ngày phải release sản phẩm và ngày đội dev viết xong code. 
# Tính số ngày mà team test có để test sản phẩm (= release_date - code_complete_day). 
# Lưu ý, ngày release sản phẩm sẽ ở định dạng 19/12/2021 còn ngày code_complete có định dạng 2021-17-05

def day_diff(release_date, code_complete_day):
    d1 = datetime.strptime(release_date, "%d/%m/%Y")
    d2 = datetime.strptime(code_complete_day, "%Y-%d-%m")
    return abs((d2 - d1).days)


# 2
# Viết hàm alpha_num() tìm tất cả những từ trong một câu có chứa cả chữ cái và số. Trả ra danh sách các từ như vậy trong một câu.
# Vd:
# str1 = "Emma25 is Data scientist50 and AI Expert"
# alpha_num(str1) == ["Emma25", "scientist50"]

def alpha_num(sentence):
    splited = sentence.split(" ")
    result = []
    for word in splited:
        hasLetter = False
        hasDigit = False
        for char in word:
            number = ord(char)
            if number >= 48 and number <= 57:
                hasDigit = True
            elif number >= 65 and number <= 90:
                hasLetter = True
            elif number >= 97 and number <= 122:
                hasLetter = True
        if hasDigit and hasLetter:
            result.append(word)
    return result

# print(day_diff("10/05/2021","2021-01-03"))
# print(alpha_num("Emma25 is Data scientist50 and AI Expert"))