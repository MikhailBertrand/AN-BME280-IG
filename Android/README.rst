========================================================================
artifactnoise-bme280　Androidライブラリの使い方
========================================================================

作成日:2020/03/18

現在再編集中です。

■ 概要
------------------------------------------------------------------------

Android端末で、AN-BME280-IGを利用するためのライブラリです。

AndroidのUSBホスト機能を使用します。

root権限は不要です。


■ ライブラリインストール
------------------------------------------------------------------------

Android Stadioのプロズエクトのlibsにxxx.aarファイルをコピーします。

build.gradleファイルに以下の一文を追加します。

::

    dependencies {
        implementation fileTree(dir: 'libs', include: ['*.jar'])
        // この行を追加
        implementation fileTree(dir: 'libs', include: ['*.aar'])

        implementation 'androidx.appcompat:appcompat:1.1.0'
        implementation 'androidx.constraintlayout:constraintlayout:1.1.3'
        testImplementation 'junit:junit:4.12'
        androidTestImplementation 'androidx.test.ext:junit:1.1.1'
        androidTestImplementation 'androidx.test.espresso:espresso-core:3.2.0'
    }




■ APIリスト
------------------------------------------------------------------------

JAVA (Android ネイティブ)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
- 参照するクラス
import com.example.artifactnoise_bme280.BME280;

- クラスの継承（MainActivityのthisActivityを継承させます)
BME280 bme280 = new BME280(this);

- BME280　バージョンの読み出し
String　VERSION()

- BME280　ライセンス情報の読み出し
String　LICENSE()

- BME280　初期化処理
void Init()

- BME280　センサー取得値　更新コマンド
void readData();

- BME280　室温の取得(セルシウス温度 ℃) 
double Temperature();

- BME280　湿度の取得(相対湿度 %) 
double Pressure();

- BME280　大気圧の取得(気圧値 Pa) 
double Humidity ();

- BME280　モジュールの状態取得（文字列）
String STATE_String()

    // 初期状態
    "INIT"
    // 接続完了、データ取得可能状態
    "SUCCESS"
    // USB機器接続権限未取得
    "NO_USB_PERMISSION"
    // USB機器接続失敗
    "CONNECTION_FAILED"
    // USB機器が切り離された
    "ACTION_USB_DEVICE_DETACHED"
    // USB機器が接続され権限を確認中
    "ACTION_USB_PERMISSION"
    // USB機器が接続された
    "ACTION_USB_DEVICE_ATTACHED"
    // 接続許可が追加で添付された
    "EXTRA_PERMISSION_GRANTED"

- 例：

.. highlight:: JAVA

    public class MainActivity extends AppCompatActivity {
        public static TextView textView;

        @Override
        protected void onCreate(Bundle savedInstanceState) {
            super.onCreate(savedInstanceState);
            setContentView(R.layout.activity_main);

            final BME280 bme280 = new BME280(this);
            final TextView textView = findViewById(R.id.textView);
            new Thread(new Runnable() {
                @Override
                public void run() {
                    while(true)
                    {
                        while(bme280.STATE_String().equals("SUCCESS"))
                        {
                            bme280.Init();
                            bme280.readData();
                            StringBuffer strbuf = new StringBuffer();
                            strbuf.append(String.format("temp : %-6.2f ℃ \n", bme280.Temperature()));
                            strbuf.append(String.format("hum : %6.2f ％ \n", bme280.Humidity()));
                            strbuf.append(String.format("pressure : %7.2f hPa \n", bme280.Pressure() / 100));
                            strbuf.append("OK. \n");
                            textView.setText(strbuf);
                            try {
                                Thread.sleep(500);
                            } catch (InterruptedException e) {
                            }
                        }
                    }
                }
            }).start();
        }
    }


::
    
    MIT License
    Copyright (c) 2018 ArtifactNoise,LLP/Yuta Kitagami   
