def download_word2vec_model(model_name, filename):
    filehandler = open(filename, 'wb')
    model = api.load(model_name)
    pickle.dump(model, filehandler)

def retrieve_word2vec_model(filename):
    filehandler = open(filename, 'rb')
    model = pickle.load(filehandler)
    return model
