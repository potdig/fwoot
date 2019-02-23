# fwoot

## 機能
foobar2000のタイトルバーの情報を用いたテキストが入力された状態で、Twitterのシェアページを表示します。
今のところはフォーマット固定です: `Now Playing: {曲情報}`

## 使用法
### foobar2000での設定
初めに、本ツール向けにfoobar2000のタイトルバーの表記設定を変更してください。
+ メニューから[File]-[Preferences]を選ぶ
+ 設定画面のツリーから[Display]-[Default User Interface]を選ぶ
+ "Window title"の設定をこんな感じで変更する: `[%title%] [/ %artist%] ['['%album% [Tr. %tracknumber%]']'] - foobar2000` (重要: ` - foobar2000`の文字列を必ず含むようにしてください。この文字列でウィンドウを検索する仕組みになってます。)

### ツールの使用
+ fwoot.exeを実行する
+ Webブラウザでシェアページが出るのでツイートする

## 入れたい機能
- テキストのフォーマットくらいは変えれるようにしたい