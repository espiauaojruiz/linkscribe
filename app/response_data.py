class ResponseData:
  title:str
  description:str
  preview_link:str
  category_int:int
  category_str:str

  def to_dict(self):
    return {
      'title': self.title,
      'description': self.description,
      'previewLink': self.preview_link,
      'categoryIndex': self.category_int,
      'category': self.category_str
    }
