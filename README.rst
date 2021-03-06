========================================================================
温度／湿度／気圧を計測する　室内環境計測モジュール
========================================================================

作成日:2018/05/01

現在再編集中です。

■ 概要
------------------------------------------------------------------------

USBで手軽に大気中の温度／湿度／気圧　を計測します。




.. image:: ./img/2018_05_07.png








■ 取説
------------------------------------------------------------------------

.. image:: ./img/取説.png




■ ライブラリインストール
------------------------------------------------------------------------

・モジュールのType-C端子にケーブルを接続します。

・LEDの点灯を確認します。

・ソースを以下のコマンドでダウンロードします。

git clone https://github.com/ArtifactNoise/AN-BME280-IG.git

・ライブラリをインストールします。

pip3 install PyMCP2221A

・サンプルプログラムを実行します。

cd ./AN-BME280-IG/Python/example

python3 BME280_test.py

■ サンプルプログラム
------------------------------------------------------------------------

コマンドライン
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    https://github.com/ArtifactNoise/AN-BME280-IG/blob/master/Python/example/BME280_test.py

-   初期化
    
    from PyMCP2221A import BME280
    
    device = BME280.BME280()

-   全てのデータ読出し

    device.readData()

-   温度値の関数 [℃]

    device.temperature

-   湿度値の関数 [%]

    device.humidity

    ※ device.var_h　は古い関数で使用しない方向でおねがいします。 

-   気圧値の関数　[pa]

    device.pressure

※ヘクトパスカル(hPa)に変換する際は　device.pressure/100 をします。

GUIアプリ
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


.. image:: ./img/GUI_sample.jpg
    :width: 480px


https://github.com/ArtifactNoise/AN-BME280-IG/blob/master/Python/example/BME280_GUI.py


KivyによるGUIアプリ
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
okajun35様より、Kivyで動くサンプルプログラムを頂きました！　有難うございます！！

https://github.com/okajun35/AN-USB-BME280

.. raw:: html

    <blockquote class="twitter-video" data-lang="ja"><p lang="ja" dir="ltr">技術書典４で買った<a href="https://twitter.com/nonNoise?ref_src=twsrc%5Etfw">@nonNoise</a>の温度センサー。これはすごい！！<br>ドライバーのインストールも簡単でなによりPythonで値が取得できる。<br>ラズパイよりも全然簡単なのでおすすめ。<a href="https://twitter.com/hashtag/%E6%8A%80%E8%A1%93%E6%9B%B8%E5%85%B8?src=hash&amp;ref_src=twsrc%5Etfw">#技術書典</a>　<a href="https://twitter.com/hashtag/%E6%8A%80%E8%A1%93%E6%9B%B8%E5%85%B84?src=hash&amp;ref_src=twsrc%5Etfw">#技術書典4</a> <a href="https://t.co/A5dq0sgeG1">pic.twitter.com/A5dq0sgeG1</a></p>&mdash; okazaki jun (@dario_okazaki) <a href="https://twitter.com/dario_okazaki/status/988445093907415041?ref_src=twsrc%5Etfw">2018年4月23日</a></blockquote>
    <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>



■ 参考資料
------------------------------------------------------------------------


::
    
    MIT License
    Copyright (c) 2018 ArtifactNoise,LLP/Yuta Kitagami   
