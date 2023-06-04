# import statements

import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd

# Selectors

CLOSE_BTN = "div.crossIcon"
ARTICLE_CSS = ".jobTuple"
JOB_TITLE = ".info a.title"
COMPANY_NAME = ".companyInfo a.subTitle"
EXPERIENCE = "li.experience span"
SALARY = "li.salary span"
LOCATION = "li.location span.ellipsis"

# Variables/Lists
chrome_driver_path = "C:\Development\chromedriver.exe"

form_url = "https://docs.google.com/forms/d/e/1FAIpQLSecro95YDNWQSbCLxaPDStv5pyxJAEb4qREeQMTdR5Z7PIp6g/viewform?usp=sf_link"
website_url = "https://www.naukri.com/python-developer-jobs-in-new-delhi?k=python%20developer&l=new%20delhi&ctcFilter=6to10"

job_links = []
job_skills_required = []

# Initialising chrome driver

chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(website_url)

element = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CSS_SELECTOR, CLOSE_BTN)))
try:
    element.click()
except selenium.common.exceptions.ElementNotInteractableException:
    print(f"Element is visible: {str(element.is_displayed())}")
else:
    # scraping job data

    soup = BeautifulSoup(driver.page_source, "html.parser")

    all_articles = soup.select(ARTICLE_CSS)

    for article in all_articles:
        URL = article.find("a", "title").get("href")
        job_links.append(URL)

    all_titles = soup.select(JOB_TITLE)
    all_company_names = soup.select(COMPANY_NAME)
    all_experience = soup.select(EXPERIENCE)
    all_salaries = soup.select(SALARY)
    all_locations = soup.select(LOCATION)

    job_titles = [title.get_text() for title in all_titles]
    company_names = [company_name.get_text() for company_name in all_company_names]
    experiences = [exp.get_text() for exp in all_experience]
    salaries = [salary.get_text() for salary in all_salaries]
    locations = [location.get_text() for location in all_locations]

    for i in range(len(all_articles)):
        skills = all_articles[i].find_all("li", "dot")
        skill_set = [skill.get_text() for skill in skills]
        skill_set = ", ".join(skill_set)
        job_skills_required.append(skill_set)

    # Creating dataframe and converting to excel sheet

    job_data = {
        "JobTitle": job_titles,
        "CompanyName": company_names,
        "Experience": experiences,
        "SkillSet": job_skills_required,
        "Salary": salaries,
        "JobLocation": locations,
        "JobLink": job_links
    }

    df = pd.DataFrame(data=job_data)
    df.to_excel(excel_writer="JobListings.xlsx", sheet_name="Sheet 1")

finally:
    driver.close()
