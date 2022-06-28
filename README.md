# mat-lda-model-analyzer
Visualizations for LDA models from (mat-analyzer)[https://github.com/zabkwak/mat-analyzer].

## Development
### Requirements
- Python 3
- `gcc` and `g++` libraries
### Installation & test run
```bash
git clone git@github.com:zabkwak/mat-lda-model-analyzer.git
cd mat-lda-model-analyzer
pip install -r requirements.txt
python ./
```

## Settings
The settings are set with environment variables. 
Variable | Description | Required | Default value
:------------ | :------------- | :-------------| :-------------
`MODEL_INPUT_FILE_PATH` | The filepath of the LDA model. | :heavy_check_mark: | 
`CORPUS_FILE_PATH` | The filepath of the `json` file with corpus data. | :heavy_check_mark: | 

## Input
The input directory should contain 4 files with the `LDA` model and the corpus file.
- `lda.model`
- `lda.model.expElogbeta.npy`
- `lda.model.id2word`
- `lda.model.state`

## Docker
The [image](https://github.com/zabkwak/mat-lda-model-analyzer/pkgs/container/mat-lda-model-analyzer) is stored in GitHub packages registry and the app can be run in the docker environment.
```bash
docker pull ghcr.io/zabkwak/mat-lda-model-analyzer:latest
```

```bash
docker run \
-p 8080:8080 \
-d \
--restart=unless-stopped \
--name=mat-lda-model-analyzer \
-v '/absolute/path/to/input/dir:/usr/src/app/input' \
ghcr.io/zabkwak/mat-lda-model-analyzer:latest  
```
The app will be accessible on `http://localhost:8080`.
