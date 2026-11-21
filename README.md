# niwanowa-samples

色々検証したものをここにまとめる

検証用・学習用のリポジトリを、履歴ごとこのリポジトリのサブフォルダにまとめた。取り込みは `git subtree` で行い、各フォルダの履歴はマージコミットの親として残っている。ルートの `.github` は元のまま。

## もともとこのリポジトリにあるもの

| folder | original repo URL | description |
| --- | --- | --- |
| [Mermaid](Mermaid) | https://github.com/niwanowa/niwanowa-samples/tree/main/Mermaid | GitHub の Mermaid 図サンプル |
| [azure-terraform](azure-terraform) | https://github.com/niwanowa/niwanowa-samples/tree/main/azure-terraform | Azure のリソースグループ、仮想ネットワーク、Static Web Apps 用 Terraform |
| [cp_test](cp_test) | https://github.com/niwanowa/niwanowa-samples/tree/main/cp_test | コピー動作の確認用ファイル |
| [google-reverse-geocoding](google-reverse-geocoding) | https://github.com/niwanowa/niwanowa-samples/tree/main/google-reverse-geocoding | Google Maps の逆ジオコーディング試行 |
| [youtube-data-api](youtube-data-api) | https://github.com/niwanowa/niwanowa-samples/tree/main/youtube-data-api | YouTube Data API の検索と LiveFans のスクレイピング |

## experiments

| folder | original repo URL | description |
| --- | --- | --- |
| [experiments/hello-world-pages](experiments/hello-world-pages) | https://github.com/niwanowa/hello-world-pages | Hello World の GitHub Pages デモ |
| [experiments/chattest](experiments/chattest) | https://github.com/niwanowa/chattest | チャット試行。中身は README のみ |
| [experiments/niwa-test-azSWA](experiments/niwa-test-azSWA) | https://github.com/niwanowa/niwa-test-azSWA | Azure Static Web Apps のワークフローのみ |
| [experiments/my-first-static-web-app-](experiments/my-first-static-web-app-) | https://github.com/niwanowa/my-first-static-web-app- | Azure Static Web Apps の Vanilla JavaScript アプリ |
| [experiments/testSnapStart](experiments/testSnapStart) | https://github.com/niwanowa/testSnapStart | API Gateway と Lambda SnapStart のサーバーレス検証 |
| [experiments/aws_sam_hello_world](experiments/aws_sam_hello_world) | https://github.com/niwanowa/aws_sam_hello_world | AWS SAM の Hello World |
| [experiments/tryOpenAIAPI](experiments/tryOpenAIAPI) | https://github.com/niwanowa/tryOpenAIAPI | OpenAI API（GPT-4、画像、音声）の試行。キーは環境変数 |
| [experiments/first_cc](experiments/first_cc) | https://github.com/niwanowa/first_cc | React + TypeScript + Vite の TODO アプリ |
| [experiments/niwanowa-sTemplate](experiments/niwanowa-sTemplate) | https://github.com/niwanowa/niwanowa-sTemplate | git hooks 付きのリポジトリテンプレート |

## learning

| folder | original repo URL | description |
| --- | --- | --- |
| [learning/learnNextjs](learning/learnNextjs) | https://github.com/niwanowa/learnNextjs | Next.js ダッシュボードチュートリアル |
| [learning/amplifyNextjsHandsOn](learning/amplifyNextjsHandsOn) | https://github.com/niwanowa/amplifyNextjsHandsOn | create-next-app で作った Next.js ハンズオン |
| [learning/niwanowa-learning-react](learning/niwanowa-learning-react) | https://github.com/niwanowa/niwanowa-learning-react | Reactハンズオンラーニング 第2版 学習用リポジトリ |
| [learning/udemy_python](learning/udemy_python) | https://github.com/niwanowa/udemy_python | Udemy の Python 講座の演習 |
| [learning/DenoAdventBar](learning/DenoAdventBar) | https://github.com/niwanowa/DenoAdventBar | Deno のアドベントカレンダー進捗バー |

## atcoder

| folder | original repo URL | description |
| --- | --- | --- |
| [atcoder/AtCoder](atcoder/AtCoder) | https://github.com/niwanowa/AtCoder | AtCoder ABC などの Python 解答 |
| [atcoder/ABC115](atcoder/ABC115) | https://github.com/niwanowa/ABC115 | AtCoder ABC115 の Python 解答 |
| [atcoder/AtCoder_Beginners_Selection](atcoder/AtCoder_Beginners_Selection) | https://github.com/niwanowa/AtCoder_Beginners_Selection | AtCoder Beginners Selection の Python 解答 |

## misc

| folder | original repo URL | description |
| --- | --- | --- |
| [misc/makeRSSfromConnpass2](misc/makeRSSfromConnpass2) | https://github.com/niwanowa/makeRSSfromConnpass2 | Connpass から RSS を作る試行。README と LICENSE のみ |
| [misc/LLMComparison_backend](misc/LLMComparison_backend) | https://github.com/niwanowa/LLMComparison_backend | LLM 比較のバックエンド用置き場。LICENSE と .gitignore のみ |
| [misc/site-diff-checker](misc/site-diff-checker) | https://github.com/niwanowa/site-diff-checker | Web ページの差分を検知して Discord に通知するボット |

## empty / not imported

コミットが無いため中身を作れず、フォルダも追加していない。

| original repo | original repo URL | reason |
| --- | --- | --- |
| mdn_learn_get_start | https://github.com/niwanowa/mdn_learn_get_start | コミットが 0 件 |
| VC_Client_Model_Adder | https://github.com/niwanowa/VC_Client_Model_Adder | コミットが 0 件 |

## skipped files

認証情報ファイル、秘密の入った `.env`、秘密鍵、トークン、100MB を超えるファイルは見つからなかった。取り込み時に省いたファイルはない。
