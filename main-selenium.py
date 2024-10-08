import time

from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys

from selenium.common.exceptions import WebDriverException

def main():

    # Set up the Selenium WebDriver

    driver = webdriver.Chrome()  # Make sure ChromeDriver is in your PATH

    # driver.get('chrome://dino')  # Navigate to the Dino game
    # driver.get('chrome://network-error/-106')
    # driver.get('https://chromedino.com')

    try:
        driver.get('chrome://dino')
    except WebDriverException:
        pass


    # Wait for the game to load

    time.sleep(2)

 

    # Start the game by pressing the spacebar

    body = driver.find_element(By.TAG_NAME, 'body')

    body.send_keys(Keys.SPACE) 



    # Main game loop

    try:

        while True:

            # Get the current height of the dinosaur

            dino = driver.find_element(By.CSS_SELECTOR, '.dino')

            dino_rect = dino.rect

           

            # Check for obstacles

            try:

                obstacle = driver.find_element(By.CSS_SELECTOR, '.obstacle')

                obstacle_rect = obstacle.rect



                # Jump over the obstacle if it is close

                if obstacle_rect['x'] < dino_rect['x'] + dino_rect['width'] + 50:  # Adjust the threshold as needed

                    body.send_keys(Keys.SPACE)

            except:

                pass  # No obstacles, continue running



            time.sleep(0.1)  # Adjust the speed of the loop



    except KeyboardInterrupt:

        print("Game stopped.")

    finally:

        driver.quit()  # Close the browser



if __name__ == "__main__":

    main()

