# My toys
## description
私のおもちゃを詰め込んだレポジトリ<br>
おそらく役に立つものはない<br>
### hitofude.py
とある入社試験で作ったやつ<br>
python hitofude.py N M<br>
でN*Mのマスを一筆ですべて埋める方法が何通りあるかを計算して標準出力に出す<br>
numpyが必要<br>
### new_calender.py
これも某社の入社試験で作ったやつ<br>
python new_calender.py y m w YYYY-MM-DD<br>
で1年がy日、ひと月m日、一週間w日のカレンダーで、YYYY年MM月DD日が何曜日(A-Z曜日)かを判定する。<br>
閏月の場合などで存在しない日にちを指定した場合は-1を返す。<br>
### brace_openner.py
某社入社試験で作った。<br>
シェルでできるブレース展開をわざわざpythonでやるやつ<br>
なお多重展開は不可能。気が向いたら作るかも<br>
標準入力で受け取って標準出力で展開
例 : a{b,c} -> ab ac
