## About
Returns dynamically generated images in matplotlib for cloud functions HTTP requests

## Usage

```
$ brew cask install google-cloud-sdk
$ gcloud init
$ gcloud components update && gcloud components install beta
$ git clone https://github.com/tanabee/functions-matplotlib.git
$ cd functions-matplotlib
$ gcloud functions deploy graph --runtime python37 --trigger-http
```

## More information

https://qiita.com/tanabee/items/2bfee85f9659be097750
