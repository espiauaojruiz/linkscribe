import requests
import pandas as pd
import bs4
from urllib.parse import urlparse
from bs4 import BeautifulSoup

class ScrapTool:
  def scrap(self, website_url: str):
    try:
      headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0'
      }
      response = requests.get(website_url, headers=headers, timeout=60)
      soup = BeautifulSoup(response.content, "lxml")
      if soup:
        result = {
          "title": self.get_title(soup),
          "description": self.get_decsription(soup),
          "preview": self.get_preview(soup),
          "content": self.get_content(soup)
        }
        return result
      else:
        return None
    except Exception as e:
      print("Excepción presentada en ScrapTool:scrap")
      raise

  def get_title(self, soup:BeautifulSoup):
    try:
      if soup.title:
        return soup.title.string
      else:
        return None
    except Exception as e:
      print("Excepción presentada en ScrapTool:get_title")
      raise

  def get_decsription(self, soup: BeautifulSoup):
    try:
      metatag = soup.find('meta', attrs={'name': 'description'})
      if metatag:
        return metatag.get('content')
      else:
        return None
    except Exception as e:
      print("Excepción presentada en ScrapTool:get_decsription")
      raise

  def get_preview(self, soup):
    try:
      metatag = soup.find('meta', property='og:image')
      if metatag:
        return metatag.get('content')
      else:
        return None
    except Exception as e:
      print("Excepción presentada en ScrapTool:get_preview")
      raise

  def get_content(self, soup:BeautifulSoup):
    try:
      ignored_tags = ['style', 'script', 'head', 'title', 'meta', '[document]',"a","noscript"]
      tags = soup.find_all(string=True)
      result = []
      for tag in tags:
          stripped_tag = tag.strip()
          if tag.parent.name not in ignored_tags \
            and isinstance(tag, bs4.element.Comment)==False \
            and not stripped_tag.isnumeric() \
            and len(stripped_tag)>0:
            result.append(stripped_tag)
      return ' '.join(result)
    except Exception as e:
      print("Excepción presentada en ScrapTool:get_content")
      raise
