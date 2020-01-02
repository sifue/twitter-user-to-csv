# TwitterのリストやフォローしているユーザーからAutoML向けラベル付きCSVを取得するスクリプト
AutoMLの単一ラベルの学習データに用いる用のデータCSVを作成する。
人間のユーザーが意図を持って集めているだろうリストとフォローしている人(friends)から名前、スクリーンネーム、説明、場所のデータを取得したPythonの辞書型をtoStringしたデータをラベル付きで作成する。
たぶん、フォローされている人のCSVもAPI名を変更するだけで作れれるが、ボットなどのノイズフォロワーが多いため扱わない。

## 必要なもの

```
python3 --version # Python 3.6.9
pip3 install twitter
```

## リストから取得する場合

```
env CONSUMER_KEY=xxxxxxxxxxxxxx CONSUMER_SECRET=xxxxxxxxxxxxxx TOKEN=xxxxxxxxxxxxxx TOKEN_SECRET=xxxxxxxxxxxxxx python3 twitter_list_fetcher.py sifue nnn ./n_sample_list.csv n_student
```

## フォローしている人から取得する場合

```
env CONSUMER_KEY=xxxxxxxxxxxxxx CONSUMER_SECRET=xxxxxxxxxxxxxx TOKEN=xxxxxxxxxxxxxx TOKEN_SECRET=xxxxxxxxxxxxxx python3 twitter_friend_fetcher.py sifue ./n_sample_friend.csv not_n_student
```

## 出力されるCSV

```
"{'name': 'ミンカ・リー', 'screen_name': 'minkalee', 'location': '', 'description': 'むかしむかしメイドで踊ってた'}",not_n_student
"{'name': 'ダルビッシュ有(Yu Darvish)', 'screen_name': 'faridyu', 'location': '', 'description': 'Chicago Cubs #11 「弱い者ほど相手を許すことができない。 許すということは、強さの証だ。」←なんでも許すって意味ちゃうし、議論してるだけで「許してないやん笑」って言ってくるやつおるけど理解力ないの晒してるだけやで。'}",not_n_student
"{'name': '伊藤賢治', 'screen_name': 'itoken0705', 'location': '( o ▽ n )o彡゜', 'description': '作曲家。\n12月は15日（日）に、""サガシリーズ30周年""を迎えます！皆さんありがとう(^o^)\nそして変わらず、制作の日々…。\n令和元年も終わる…。'}",not_n_student
"{'name': '小島秀夫', 'screen_name': 'Kojima_Hideo', 'location': '故郷は地球', 'description': 'ゲームデザイナー：僕の体の70%は映画でできている'}",not_n_student
"{'name': 'ヒャダイン こと 前山田健一(39)', 'screen_name': 'HyadainMaeyamad', 'location': 'Tokyo', 'description': '料理と猫と告知を主につぶやきます。インチキ音楽クリエイターです。よろしくお願いします。'}",not_n_student
"{'name': '宋\u3000文洲', 'screen_name': 'sohbunshu', 'location': '北京市海淀区', 'description': '中国に帰った中国人。日本で創業し東証1部上場を果たした最初の外国人。2005年に引退しその後に帰国'}",not_n_student
"{'name': '東国原英夫', 'screen_name': 'higashi_kokuba', 'location': '', 'description': '「てげ」･･･方言の意味としては、「とても」「非常に」「すごく」という意味の副詞であるが、私の場合は、これらの意味にプラスして、独自の解釈で、「がんばれ」「気合いだ」といった激励や励ましの意味で使っている。'}",not_n_student
```

