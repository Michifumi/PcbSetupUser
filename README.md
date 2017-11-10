# "PcbSetupUser"について


## Ａ.概要
+ "PcbSetupUser.py"は、KiCADv4の基板設計ソフトPcbnewで動作するマクロプログラムであり、指定された基準ファイルのユーザー設定を、マクロを実行している基板ファイルへ追記するソフトです。


## Ｂ.ファイル内容
+ "PcbSetupUser.py" ... KiCAD用基板ファイルのユーザ設定をコピーするソフト

 
## Ｃ.動作確認環境
+ KiCAD Ver4.07 on Windows7-64bit / Ubuntu14.04LTS-64bit


## Ｄ.使用方法
1. ユーザー設定の基準基板ファイルを、これから追記したい基板ファイルと同じフォルダーへコピーし、そのファイル名を"Default.kicad_pcb"へ変更する。
2. 基板ファイルの新規作成直後は、設定情報が何も無い状態なので、ネットリストを予め読み込み、設定情報が出来た後、セーブした状態にしておいてください。
3. Pcbnewを起動し、Pythonコンソールを選択実行する。　
4. コンソール内で、「pwd」を実行し、出てきたフォルダ（普通は"C:\Program Files\KiCad")へ、本ソフト"PcbSetupUser.py"をコピーする。
5. コンソール内で、「execfile("PcbSetupUser.py")」と入力、実行する。


## Ｅ.その他
1. ユーザー設定の基準基板ファイルをコピーするのではなく、絶対パスで指定したい場合は、以下の内容にプログラムを変更する。

    txt = PcbSetup_Read(「ユーザ設定の基準ファイル名」 ,"PcbSetupUser.txt")

    尚、「ユーザ設定の基準入力ファイル名」内のパス名は、'\\'ではなく、'/'を使う事。

2. ユーザー設定内容は、デフォルトでは、"PcbSetupUser.txt"に書かれる。　又、変更前のファイルは、「"ファイル名" + "_bak"」になります。
3. 変更前の「"ファイル名" + "_bak"」が既にある場合や変更前から既にユーザー設定があった場合は、ユーザー設定を追記しないで処理を終了します。


## Ｆ.参考にさせて頂いたサイト
+ 「KiCad用のPythonスクリプト ～ ほぼ回路図の配置通りにフットプリントを予備配置する」
        <https://qiita.com/silvermoon/items/da4fcdba319f46570a60>


## Ｇ.変更履歴
---
2017/11/10   (3rd commit)  

+ README.mdの説明文について変更。  

---
2017/10/22   (2nd commit)  
  
1. プログラムを、終了時のファルダー位置が、起動した時の位置に戻すように変更した。  
2. 基板ファイルの新規作成直後は、設定情報が何も無い状態なので、このファイルの「Ｄ.使用方法」にネットリストを読み込んだ（設定情報が出来た）後に、実行するように説明を追加。  
3. 上記2を前提にLinuxでも動作を確認した所、問題なかった。 

---
2017/10/19   (1st commit)    

---
