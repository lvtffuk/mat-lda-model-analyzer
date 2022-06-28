import json
import os
import pyLDAvis.gensim_models
import pickle 
import pyLDAvis 
import gensim
from http.server import BaseHTTPRequestHandler, HTTPServer

lda_model = gensim.models.LdaMulticore.load(os.getenv("MODEL_FILE_PATH"))
corpus = json.load(open(os.getenv("CORPUS_FILE_PATH")))
num_topics = lda_model.num_topics
id2word = lda_model.id2word
hostname = "0.0.0.0"
port = int(os.getenv("PORT", "8080"))

# pyLDAvis.enable_notebook()

LDAvis_data_filepath = os.path.join("./output/ldadavis_prepared_" + str(num_topics))
# # this is a bit time consuming - make the if statement True
# # if you want to execute visualization prep yourself
if 1 == 1:
    LDAvis_prepared = pyLDAvis.gensim_models.prepare(lda_model, corpus, id2word)
    with open(LDAvis_data_filepath, 'wb') as f:
        pickle.dump(LDAvis_prepared, f)
# load the pre-prepared pyLDAvis data from disk
with open(LDAvis_data_filepath, 'rb') as f:
    LDAvis_prepared = pickle.load(f)
pyLDAvis.save_html(LDAvis_prepared, "./output/ldadavis_prepared_" + str(num_topics) + ".html")
LDAvis_prepared

class MyServer(BaseHTTPRequestHandler):
	def do_GET(self):
		self.send_response(200)
		self.send_header("Content-type", "text/html")
		self.end_headers()
		self.wfile.write(bytes(open("./output/ldadavis_prepared_" + str(num_topics) + ".html").read(), "utf-8"))

if __name__ == "__main__":        
    webServer = HTTPServer((hostname, port), MyServer)
    print("Server started http://%s:%s" % (hostname, port))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")