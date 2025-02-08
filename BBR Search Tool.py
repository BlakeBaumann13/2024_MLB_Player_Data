from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


def main():

    # Set up headless Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")

    player_name_input = input("Please enter a player to search for: ")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
   

    url = 'https://www.baseball-reference.com/leagues/majors/2024-standard-batting.shtml'

    driver.get(url)

    time.sleep(3)

    avg_table = driver.find_element(By.ID, 'players_standard_batting')

    rows = avg_table.find_elements(By.TAG_NAME, 'tr')

    found_player = False
    for row in rows:
        cells = row.find_elements(By.TAG_NAME, 'td')
        if cells:
            player_name = cells[0].text.strip()
            if not player_name[-1].isalpha():
                player_name = player_name[:-1]
            if player_name.lower() == player_name_input.lower():
               
                for printlist in cells:
                    print(printlist.text, end=" | ")
                found_player = True
                break


    if not found_player:
        print(f"Player {player_name_input} not found on the page.")

if __name__ == "__main__":
    main()
