from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random

# https://www.facebook.com/groups/miaigroup/posts/1775605586544039/?__cft__[0]=AZX-yfAZRvXIcCbVpQpgOGUWyOeZhH-elrXC-q9K7J32bbHCzu8p4wAkTAyAWCjRRrsxDkmb7ECRXKvv9y3TC-ioTajWpqs6SbJVh56WY7L-trsbQ6o0912-doL9AVwhQVEvuazKrrjjnZXHDpWuSARPRHeb2E5hB0MrrV8TFkxzRLHb7jVDQrz2IL0dgEOwFppCYvwm80oDIlXEg4sVWyGhpUaOzURUegVHDZVdELuS0g&__tn__=%2CO%2CP-R

# /html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[4]/div/div/div/div/div/div/div[2]/div/div/div/div/div/div/div/div/div/div/div[13]/div/div/div[4]/div/div/div[1]/div/div[1]/div/div[2]/div[2]/span/div/span/span

browser = webdriver.Chrome()

#browser.get("https://www.facebook.com/groups/miaigroup/posts/1773869206717677/?__cft__[0]=AZUZZG8LPqrh5QasMIbx5g3mM7fdoqNo7RDSqWT1I6pSUXMTV6ZZM2gXA51gC9GQ6Z5gztwkgSgwOxupKUg6EPZCMhsR9NBofo6mF3cjK-O4E8XpGKu6ytAkD1FA9bkIuuu3f9Xio5lzLL1WgxVqYolUAvBZbRZ3sjukW38IL4r7bkcH1VWDuLbmlcy3uYvj9453YQj1TjgqXwV1X4BvdZ1S&__tn__=%2CO%2CP-R")

browser.get("https://www.facebook.com/thongtinchinhphu/posts/pfbid02NsPvTWpCEzvcY8VuPbmwx1eYGVKJyXK7tJTY5mD1ScoWR3AHc2YNJztvc2xp9hvhl?__cft__[0]=AZXSMr2YVk6o_G5BTbHAsHpO0gQPq79QTsS8Qjl9QXEpeRkbwuqSRtkdTEVErzAXW0E5U886MiojeiuDwgadXvYKpOjf0H19FhfgffrZEXBWywOUKU6AIxuJz5ZnQywH7ifMW6As2nPImcF0pigkH0H3-sbZNCMpWDf8szruvv9Daa7aQIPqKrBD3FYJnOJhRvM&__tn__=%2CP-R")
#browser.get("https://www.facebook.com/irecapcomics/posts/pfbid0289GCfykdnLNoEqZ5cXemshKr29Hf8Ka5uMdgm9epT3VveW9jH73XQmfxCk6J7dFxl?__cft__[0]=AZUtpx6ARA9X87dfbTBXZeEqq24As2sKpyg7TL3j4RC0tboTkHvcHNJPbPYeBLzksEO3afNc31ydnmpwXxJ8iUOtONFirh9obCRfsAfXoHaEPyysP5b-K6X8aowTuUIyw2w86SAmLZg7BNsVC4HSuojd9kaZ-WMXBx5vznpi3i1tZdVGNcaIL0kcLsXjJaEyx_U&__tn__=%2CO%2CP-R")




sleep(random.randint(5,8))

try:


    showcomment_link = browser.find_element(By.XPATH, "//span[text()='Most relevant']")
    showcomment_link.click()
    print("Nhấn vào 'Xem thêm bình luận' thành công")
    
    # Thêm thời gian chờ sau khi nhấn
    sleep(5)
except Exception as e:
    print("Lỗi:", e)


# try:
#     # comment_links = browser.find_elements(
#     #     By.XPATH,
#     #     "//div[contains(@class, 'xv55zj0') and contains(@class, 'x1vvkbs') and contains(@class, 'x1rg5ohu') and contains(@class, 'xxymvpz')]"
#     # )
# #     comment_links = browser.find_elements(
# #     By.XPATH,
# #     "//div[contains(@class,'xdj266r') and contains(@class,'x11i5rnm') and contains(@class,'xat24cr') and contains(@class,'x1mh8g0r') and contains(@class,'x1vvkbs') and contains(@class,'x126k92a')]"
# # )
    
#     comment_links = browser.find_elements(
#     By.XPATH,
#     "//div[contains(@class, 'x78zum5')]"
# )







#     # In ra nội dung của từng comment
#     for comment in comment_links:
#         if comment.text.strip() == "":
#             continue
#         else:
#             print(comment.text)
#             print("-----------------------")
#         #break




#     # Thêm thời gian chờ sau khi nhấn
#     sleep(5)
#     print("OK", len(comment_links))
# except Exception as e:
#     print("Lỗi:", e)


sleep(8)

