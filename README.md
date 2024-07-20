# GIT-DEMO

- maekdown語法
    - https://hackmd.io/@eMP9zQQ0Qt6I8Uqp2Vqy6w/SyiOheL5N/%2FBVqowKshRH246Q7UDyodFA?type=book
### 演練git 相關指令

重點指令
=
### 本地相關
- git init
    - 初始專案
- git add .
    - U/M/A/D (控管模式)
- git checkout .
    - 恢復修改 (反悔簡易恢復)
    - 任一個commit-object / branch
- git commit -m "xxx"
    - 暫存區 => 倉庫區
- git log / git status
- git checkout -b <新增分支跟切換>
- git merge <分支合併>
- git reset -- hard HEAD (commit-object)
- git reflog
- git push
- git push -f

### 雲端相關
- github 建立新的雲端倉庫位址
- git add remote origin http:/xxx/xxx.git
- git remote -v (檢視雲端倉庫狀態)
- git push -u origin master (與本地同名)
    - git push
- 複製專案到本地端
    - git clone http:/xxx/xxx.git
- 同步專案到本地端
    - git pull

