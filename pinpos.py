from playwright.sync_api import sync_playwright
import json

email = "louisewall@broccoli.eu.org"
passw = "Simplest1#"

with sync_playwright() as p:
    browser = p.firefox.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    #login pinterest
    page.goto("https://www.pinterest.com")
    page.locator("//div[@class='B1n tg7 tBJ dyH iFc sAJ H2s'][contains(text(),'Log in')]").click()
    page.locator("//input[@id='email']").fill(email)
    page.locator("//input[@id='password']").fill(passw)
    page.locator("//button[@type='submit']//div[@class='KS5 hs0 mQ8 un8 tkf TB_']").click()

    #get cookies
    all_cookies = context.cookies()
    for cookie in all_cookies:
        print(cookie)
    #page.pause()
    #browser.close()