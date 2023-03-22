import json
# from keybert import KeyBERT

f_videos = open('videos.json')
f_articles = open('articles.json')

videos_data = json.load(f_videos)
articles_data = json.load(f_articles)

def video(videos_json):
	for video_id, video_data in videos_json.items():
		yield {video_id: video_data}

def article(articles_json):
	for article_id, article_data in articles_json.items():
		yield {article_id: article_data}

video_ids = list(video_id for video_id in videos_data.keys())
article_ids = list(article_id for article_id in articles_data.keys())

# iter(article(articles_data))
# iter(video(videos_data))

# print(video_ids)
# print()
# print(article_ids)

# print()
# print(next(video(videos_data))[video_ids[0]])
# print()
# print(next(article(articles_data))[article_ids[0]])

def video_text(id):
	return videos_data[id]["text"]

def article_text(id):
	return articles_data[id]["text"]

def video_categories(id):
	categories = list()
	for i in range(0, len(videos_data[id]["categoriaIAB"])):
		categories.append(videos_data[id]["categoriaIAB"][i]["class"])
	return categories

def article_categories(id):
	categories = list()
	for i in range(0, len(articles_data[id]["categoriaIAB"])):
		categories.append(articles_data[id]["categoriaIAB"][i]["class"])
	return categories

def video_keywords(id):
	return videos_data[id]["keywords"]

def article_keywords(id):
	return articles_data[id]["keywords"]

def article_title(id):
	return articles_data[id]["title"]

# for id in video_ids:
# 	print(video_keywords(id))

# for id in article_ids:
# 	print(article_title(id))

# kw_model = KeyBERT()
# def keybert_keywords(text):
# 	return kw_model.extract_keywords(text)

# print(video_text(video_ids[0]), end='\n\n')
print(' '.join(article_keywords(article_ids[0])), end='\n\n')
print(' '.join(video_keywords(video_ids[5])), end='\n\n')
print(' '.join(video_keywords(video_ids[8])), end='\n\n')
print(' '.join(video_keywords(video_ids[25])), end='\n\n')


# print(' '.join(video_keywords("pre-b42video32")))
# print(keybert_keywords(video_text(video_ids[0])))

f_videos.close()
f_articles.close()
