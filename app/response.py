from .response_data import ResponseData

class Response:
  status:int
  message:str
  data:ResponseData

  def to_dict(self):
    return {
      'status': self.status,
      'message': self.message,
      'data': self.data.to_dict() if self.data else None
    }
