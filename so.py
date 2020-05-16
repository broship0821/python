import requests
from bs4 import BeautifulSoup


URL = f"https://stackoverflow.com/jobs?q=python"

def get_last_page():
  result = requests.get(URL)
  soup = BeautifulSoup(result.text, 'html.parser')
  pages = soup.find("div", class_="s-pagination").find_all("span")
  last_page = pages[-2].string
  return int(last_page)

def extract_job(html):
  title = html.find("a", class_="s-link").get("title")
  company = html.find("h3").find("span").get_text(strip=True)
  location = html.find("h3").find("span", class_="fc-black-500").get_text(strip=True)
  job_id = html.find("a", class_="js-undismiss-job").get("data-id")
  return {
    "title": title,
    "company": company,
    "location": location,
    "link": f"https://stackoverflow.com/jobs/{job_id}"
  }

def extract_jobs(last_page):
  jobs = []
  for page in range(last_page):
    print(f"Scrapping SO page {page}")
    result = requests.get(f"{URL}&pg={page+1}")
    soup = BeautifulSoup(result.text, 'html.parser')
    results = soup.find_all("div", class_="-job")
    for result in results:
      job = extract_job(result)
      jobs.append(job)
  return jobs
      


def get_jobs():
  last_page = get_last_page()
  jobs = extract_jobs(last_page)
  return jobs