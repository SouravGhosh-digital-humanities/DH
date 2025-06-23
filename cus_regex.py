text = text.lower() # Convert all characters to lowercase for uniformity
text = re.sub(r'[^a-z\s]', ' ', text) # Replace any character that is not a lowercase alphabet or whitespace with a space
text = re.sub(r'\s+', ' ', text).strip() # Replace multiple whitespace characters with a single space and remove leading/trailing spaces
text = re.sub(r'\b\w{1,2}\b', '', text) # Remove words with 1 or 2 characters (commonly stopwords or irrelevant)
text = re.sub(r'\d+', '', text) # Remove all numeric digits
text = re.sub(r'http\S+', '', text) # Remove URLs starting with http or https
text = re.sub(r'www\S+', '', text) # Remove URLs starting with www
text = re.sub(r'\S*@\S*\s?', '', text) # Remove email addresses
