# -*- coding: utf-8 -*-
import os
import pcbnew

def PcbSetup_Read(rfname, wfname = '') :

    setuptxt = []
    n = 0; lock = 0
    for line in open(rfname, 'r'):
        n += 1
        if n == 1 :                        #ヘッダーチェック
            if line[0:10] != '(kicad_pcb' :
                break
            else :
                continue
    
        if lock == 0 :                    #「(setup」まで読み飛ばし処理
            if line[2:8] == '(setup' : 
                lock = 1
            continue
        elif lock == 1 :                  #「(setup」の後の「)」から読み飛ばし
            if line[2] == ')' :
                lock = 2
                continue
        else :
            continue
            
        if line[4:10] == '(user_' :       #「(user_」の行を記録する
            setuptxt.append(line)

            
    if wfname != '' :                    #設定の書き込み
        f = open(wfname, 'w')
        for w in setuptxt : 
            f.write(w)      
        f.close()
                  
    return setuptxt



def PcbSetup_Append(setuptxt, afname, check = False) :

    if check :
        if len(PcbSetup_Read(afname)) != 0 :   #ユーザ設定が既にある場合、処理を終了
            return False

    tfname = afname.replace('.kicad_pcb', '.@kicad_pcb')
    f = open(tfname, 'w')

    n = 0; lock = 0
    for line in open(afname, 'r'):
        n += 1
        f.write(line)
        if n == 1 :                        #ヘッダーチェック
            if line[0:10] != '(kicad_pcb' :
                break
            else :
                continue
    
        if lock == 0 :                    #「(setup」まで読み飛ばし処理
            if line[2:8] == '(setup' : 
                lock = 1
                for w in setuptxt :       #設定の書き込み
                    f.write(w)  
            continue
        elif lock == 1 :                  #「(setup」の後の「)」から読み飛ばし
            if line[2] == ')' :
                lock = 2
                continue
        else :
            continue

    f.close()

    if lock >= 2 :  
        bfname = afname.replace('.kicad_pcb', '.kicad_pcb_bak', 1)
        if not os.path.isfile(bfname) :
            os.rename(afname, bfname) 
            os.rename(tfname, afname)
            return True

    return False


#今実行している基板ファイル名を取得
pcb = pcbnew.GetBoard()
pcb_file = pcb.GetFileName()
pcb_dir = os.path.dirname(pcb_file)
pcb_name =  os.path.basename(pcb_file)
#print("Dir:{0:s}   Name:{1:s}\n").format(pcb_dir, pcb_name)

#作業ディレクトリを記憶
now_dir = os.getcwd() 
#作業ディレクトリを今実行しているディレクトリへ移動
os.chdir(pcb_dir)



#指定ファイルからユーザ設定を読み取る
#PcbSetup_Read(「ユーザ設定の基準入力ファイル名」 [,「読み取ったユーザー設定情報出力」])：返送値はユーザ設定のタプル値
#絶対パスで基準ファイル指定する場合
#txt = PcbSetup_Read('C:/Users/admin/Documents/KiCad_Data/Nucleo-EXT/Nucleo_EXT.kicad_pcb', 'PcbSetupUser.txt')
#
#マクロを実行しているディレクトリに基準ファイルがある場合
txt = PcbSetup_Read('Default.kicad_pcb', 'PcbSetupUser.txt')


#実行している基板設計ファイルへユーザ設定を書き込む
#PcbSetup_Append(「ユーザ設定リスト値」, 「ユーザ設定を追記したい基板設計ファイル名」,「ファイルが既にユーザ設定しているかチェック」)
#第三引数が'True'の場合は、ファイルに既にユーザ設定が書かれている場合は、追記せずに処理終了。
PcbSetup_Append(txt, pcb_file, True)
#
#第三引数が'False'の場合は、ファイルに既にユーザ設定が書かれていても、追記処理。
#PcbSetup_Append(txt, pcb_file, False)

#作業ディレクトリを元に戻す
os.chdir(now_dir)

