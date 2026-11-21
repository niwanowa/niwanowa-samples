# 1章　Reactの世界へようこそ
1.3.1 githubリポジトリ
　将来のためにリンクをここに残しておく
・日本語版 : https://github.com/oreilly-japan/learning-react-2e-ja
・原版 : https://github.com/MoonHighway/learning-react

1.3.2 React Developer Toolsのインストール
　これを追加
React Developer Tools - Chrome ウェブストア
https://chrome.google.com/webstore/detail/react-developer-tools/fmkadmapgofadopljbjfkapdkoienihi/related?hl=ja

動作確認、よし（https://www.instagram.com）
![インスタで動作確認](image.png)

さらに、よし(よくわからんけど表示されてるな、程度の認識)
![動作確認](image-1.png)

1.3.3 Node.jsのインストール
```zsh
node -v
zsh: correct node to _node [nyae]? n
zsh: command not found: node
```
だったので
```
brew install node 
```

 よし(動作確認)
 ```
 node -v
v20.7.0
 ```

 1.3.3.1 npm
 なんか今後に支障をきたしたら嫌なので適当なディレクトリを作ってnpm initしてみる
 ```
 ~/D/niwanowa-learning-react ❯❯❯ cd chapter-01/1.3.3.1
~/D/n/c/1.3.3.1 ❯❯❯ npkm init -y
zsh: correct npkm to npm [nyae]? y
Wrote to /Users/niwa/Dev/niwanowa-learning-react/chapter-01/1.3.3.1/package.json:

{
  "name": "1.3.3.1",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "keywords": [],
  "author": "",
  "license": "ISC"
}
 ```

 1.3.3.2 Yarn
 Yarnをnpmでインストールする。
 yって大文字なんすね
 ```
 npm install -g yarn

added 1 package in 4s
 ```

 npm installとyarn installって何が違うの？
 pip installとconda install?

 1章読了
2023/09/21