# Coffee Brewing Timer

## 概要
このプロジェクトは、様々なコーヒー抽出メソッドに対応したタイマーアプリです。
現在、4:6メソッドに対応しており、今後スイートスポット、1分ドリップなどのメソッドも追加予定です。
コーヒー豆の量に合わせて推奨湯量を自動計算し、抽出タイミングを表示で知らせてくれます。
https://screencast.apps.chrome/1-h4-s-Q3JzpJ7p0EDf19u7oC4mU73QBN?createdTime=2025-02-02T07%3A11%3A24.860Z

## 使い方
1. アプリケーションを起動すると、Webブラウザでタイマーが表示されます。
2. サイドバーで抽出方法を選択します。（現在は4:6メソッドのみ利用可能です。）
3. コーヒー粉の量をグラム単位で入力します。
4. 「タイマー開始」ボタンをクリックすると、タイマーが開始されます。
5. タイマーの指示に従って、コーヒーを抽出してください。
6. 各抽出タイミングで音声が鳴り、画面に次のアクションが表示されます。

## その他
このアプリは、美味しいコーヒーを淹れる手助けをすることを目的としています。
抽出方法や湯量、時間などはあくまで推奨値です。ご自身の好みに合わせて調整してください。

## 今後の予定
- スイートスポット抽出法の実装
- 1分ドリップ抽出法の実装
- 抽出時間のカスタマイズ機能
- 音声ファイルの機能
- UI/UXの改善

## 謝辞
このアプリの開発にあたり、以下の情報を参考にさせていただきました。
- 4:6メソッド: [Philocoffea](https://philocoffea.com/?mode=f3) - 開発者: Tetsu Kasuya (2016 World Brewers Cup Champion)
- スイートスポット: [COFFEE BREWING SCHOOL](https://www.coffeebrewinginstitute.com/)
- 1分ドリップ: [TRUNK COFFEE](https://trunk-coffee.com/)

## インストール方法
ローカル環境で実行するには、以下の手順に従ってください。

1. Python 3.7以降がインストールされていることを確認してください。
2. 必要なライブラリをインストールします。
   ```bash
   pip install streamlit numpy
   ```
3. このリポジトリをクローンまたはダウンロードします。
4. アプリケーションを実行します。
   ```bash
   streamlit run your_app_name.py  # your_app_name.py はこのファイルのファイル名
   ```
