# Google Recorder Enabler

Googleレコーダーの互換性改善を目的として、Androidに `com.google.android.feature.PIXEL_2017_EXPERIENCE` を追加する非公式のroot用モジュールです。Googleレコーダー本体は含みません。

## 仕組みと影響

`system/etc/sysconfig/google_recorder_enabler.xml` をマウントし、機能フラグを1つ追加します。このフラグは端末全体から参照されます。APKの改変や端末モデル名の変更は行いません。本モジュールには通信処理や起動時スクリプトはありません。

## 必要環境

- root取得済み端末とモジュール管理アプリ。
- モジュールの `system` ディレクトリをマウントできる環境。
- KernelSU/SukiSUでは、構成に応じてMagic Mount-rsなどのマウント用メタモジュールが必要です。
- 本モジュール自体はZygisk/LSPosedを使用しません。

## 動作確認環境

OnePlus 13 / Android 16 / SukiSU Ultra（マウント用メタモジュールにMagic Mount-rsを使用）の環境で、フラグの反映とGoogleレコーダーの導入・起動を確認しています。

## インストール

1. Releasesから最新の `google-recorder-enabler-v*.zip` を取得します。Source code (zip)はインストール用ではありません。
2. SukiSUなどのモジュール管理アプリからZIPをインストールします。
3. 端末を再起動します。
4. 下記コマンドで反映を確認します。
5. Googleレコーダー本体は別途用意してください。

リカバリーからのインストールには対応していません。

```sh
su -c 'cat /system/etc/sysconfig/google_recorder_enabler.xml'
su -c '/system/bin/pm list features' | grep -Fx 'feature:com.google.android.feature.PIXEL_2017_EXPERIENCE'
```

## 制限とトラブル対応

- Play Storeでは引き続き非対応と表示される場合があります。
- アプリのインストール条件すべてを解除するものではありません。
- 録音、文字起こし、要約、アカウント連携など全機能の動作を保証しません。
- フラグが出ない場合は、再起動、有効状態、マウント用メタモジュールを確認してください。
- フラグがあるのに起動しない場合は、アプリのバージョンとエラーを確認してください。
- 他アプリもこのフラグを参照できます。全端末で起動障害が起こらないという保証はありません。

## 解除

通常起動できる場合は管理アプリで本モジュールを無効化または削除し、再起動してください。他のモジュールも同じフラグを追加している場合、フラグは残ります。起動不能時は利用しているroot環境の公式復旧手順を参照してください。

## ソースとビルド

`module.prop`、`customize.sh`、`system/` がモジュール本体です。Python 3で `python3 build.py` を実行すると `dist/` に配布ZIPとSHA-256ファイルを作成します。ZIPには作成元のUID/GIDを保存せず、日時を1980-01-01に固定します。同一Python/zlib環境では同じZIPを再生成できます。

## 参考

- https://github.com/Xmader/google-recorder （Pixel判定に関する参考。こちらはAPK改変方式であり、本モジュールとは実装が異なります）
- https://kernelsu.org/guide/module.html
- https://topjohnwu.github.io/Magisk/guides.html
- https://github.com/Tools-cx-app/meta-magic_mount-rs

## ライセンス

NYSL Version 0.9982（煮るなり焼くなり好きにしろライセンス）です。詳細は `LICENSE` を参照してください。Googleとの提携・承認を示すものではありません。

---

<sub>Published with the help of Muse — このリポジトリの整備と公開作業には Muse を利用しました。</sub>
