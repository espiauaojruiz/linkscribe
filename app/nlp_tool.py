import spacy

class NLPTool:
  def clean_text(self, text: str):
    nlp_model = spacy.load("en_core_web_md")
    try:
      cleaned_text = nlp_model(text)
      tokens = []
      exclusion_list = ["nan"]
      for token in cleaned_text:
        if not (token.is_stop or token.is_punct or token.text.isnumeric() or (not token.text.isalnum()) or token.text in exclusion_list):
          token = str(token.lemma_.lower().strip())
          tokens.append(token)
      return ' '.join(tokens)
    except Exception as e:
      print("Excepción presentada en NLPTool:clean_text")
      raise
