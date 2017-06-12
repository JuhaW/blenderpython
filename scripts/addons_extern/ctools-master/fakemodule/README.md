# blender fake python module


pycharmでの使用を前提としたコード補完用の擬似pythonモジュール。  
blender-2.78最新版のものをbpymodules278xとして同梱しているが、py_module_gen.pyで自分の環境に合ったものを生成出来る。


![img.01](_images/img.01.jpg)

![img.02](_images/img.02.jpg)

![img.03](_images/img.03.jpg)

## py_module_gen.pyの使い方

* py_module_gen.pyとbgl_functions.pyは同一ディレクトリーに置く

* Sphinxをインストールする <http://sphinx-doc.org/index.html>  
  pipを使ってインストールなら以下のコマンド

  ```
  # pip3 install sphinx
  ```

* blenderのソースを取得する

  ```
  % git clone http://git.blender.org/blender.git
  % cd blender
  % git submodule update --init --recursive
  % git submodule foreach git checkout master
  % git submodule foreach git pull --rebase origin master
  ```

* ソースのバージョンをblenderの実行ファイルのものに合わせる  
  例) 2.78cの場合

  ```
  % git checkout v2.78c
  ```

* rstファイルの生成

  ```
  % blender --background --factory-startup -noaudio --python doc/python_api/sphinx_doc_gen.py
  ```

* rst -> xml  

  ```
  % sphinx-build -b xml doc/python_api/sphinx-in doc/python_api/sphinx-out
  ```

* xml -> py  
  py_module_gen.pyを実行する。パスは各自修正すること  
  --outputで指定したディレクトリーの下にbpy,bgl,mathutils等のpythonモジュールが生成される

  ```
  
  % blender --background -noaudio --python ctools/fakemodule/py_module_gen.py -- --input ./sphinx-out --output ./bpymodules
  ```

* pycharmでの設定  
  File -> Settings... -> Project -> Project Structure -> +Add Content Root を押して先程作ったディレクトリー(任意の場所に移動しておく)を指定する  
  ![img.04](_images/img.04.jpg)

License: GPL version 2 or any later version
